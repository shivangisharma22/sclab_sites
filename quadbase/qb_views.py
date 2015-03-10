from flask import render_template, redirect, url_for, request
from utilities import pretty_seq_display, get_seq_from_das, shift_cords_to_tss
from quad_finder import quad_finder
from qb_forms import GeneForm, G4Config, SelectTx
from config import variable_stems
from sclab_sites import app
from operator import itemgetter
from ucsc_gene import UcscGene
import ast


@app.route("/quadbase", methods=('GET', 'POST'))
def qb_index():
    form = GeneForm()
    if form.validate_on_submit():
        gene = UcscGene(form.gene.data, form.database.data)
        if len(gene.transcript_ids) > 1:
            select_info = {}
            for i in gene.transcript_ids:
                select_info[i] = [gene.get_chromosome(i), gene.get_tss(i), gene.get_tes(i),
                                  gene.get_cds_start(i), gene.get_cds_stop(i), gene.get_strand(i)]
            return redirect(url_for('qb_select_transcript', select_info=select_info,
                                    database=form.database.data, gene_name=form.gene.data))
        else:
            return redirect(url_for('qb_quad_search', gene_name=form.gene.data,
                                    database=form.database.data, tx_id=gene.transcript_ids[0]))
    return render_template('qb_index.html', form=form)


@app.route("/quadbase/SelectTranscript", methods=('GET', 'POST'))
def qb_select_transcript():
    form = SelectTx()
    form.transcripts.choices = []
    for tx, value in ast.literal_eval(request.args.items()[0][1]).iteritems():
        choice_value = "<td>%s</td>" % tx
        for i in value:
            choice_value += "<td>" + str(i) + "</td>"
        form.transcripts.choices.append((tx, choice_value))
    if request.method == 'POST':
        return redirect(url_for('qb_quad_search', gene_name=request.args['gene_name'],
                                database=request.args['database'], tx_id=form.transcripts.data))
    return render_template('qb_select_transcript.html', gene_name=request.args['gene_name'], form=form)


@app.route("/quadbase/QuadSearch", methods=('GET', 'POST'))
def qb_quad_search():
    form = G4Config(stem=3, loop_min=1, loop_max=7)
    if form.validate_on_submit():
        gene_name = request.args['gene_name']
        database = request.args['database']
        tx_id = request.args['tx_id']
        gene = UcscGene(gene_name, database)
        up_coord, down_coord = gene.get_tss_offsets(tx_id, form.promoter_up.data, form.promoter_down.data)
        sequence = get_seq_from_das(database, gene.get_chromosome(tx_id), up_coord, down_coord)
        if form.stem.data in variable_stems:
            variable_stem = True
        else:
            variable_stem = False
        quads = quad_finder(gene_name, sequence, form.stem.data, int(form.loop_min.data),
                            int(form.loop_max.data), form.strand.data, variable_stem,
                            form.overlapping_quads.data, form.maximize_quads.data)
        quads = sorted(quads, key=itemgetter(1))
        tss_quads = shift_cords_to_tss(quads, form.promoter_up.data,
                                       form.promoter_down.data, gene.get_strand(tx_id))
        sequence = pretty_seq_display(sequence, quads, tss_quads, form.promoter_up.data,
                                      form.promoter_down.data, gene.get_strand(tx_id))
        return render_template('qb_result.html', sequence=sequence, quads=tss_quads)
    return render_template('qb_quad_config.html', form=form)

