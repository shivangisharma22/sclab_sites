import wtforms as wtf
from flask_wtf import Form
from config import databases, promoter_options
from config import quad_stem_options, quad_loop_options, quad_strand_options


class GeneForm(Form):
    gene = wtf.StringField(u'Official Gene symbol')
    database = wtf.SelectField(u'Choose organism', choices=databases)


class G4Config(Form):
    promoter_up = wtf.SelectField(u'Promoter Upstream Offset', choices=promoter_options)
    promoter_down = wtf.SelectField(u'Promoter Downstream Offset', choices=promoter_options)
    stem = wtf.SelectField(u'Stem length', choices=quad_stem_options)
    loop_min = wtf.SelectField(u'Min loop length', choices=quad_loop_options)
    loop_max = wtf.SelectField(u'Max loop length', choices=quad_loop_options)
    strand = wtf.SelectField(u'Strand to search?', choices=quad_strand_options)

    overlapping_quads = wtf.fields.BooleanField(u'Search Overlapping  G4 motifs?')
    maximize_quads = wtf.fields.BooleanField(u'Maximize motif length?')


class SelectTx(Form):
    transcripts = wtf.RadioField()
