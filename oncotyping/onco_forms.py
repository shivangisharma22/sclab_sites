from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, DateField, IntegerField, RadioField
from wtforms.validators import DataRequired


class OncoLoginForm(Form):
    username = StringField(label='Oncotyping Username', validators=[DataRequired('Please enter username')])
    password = PasswordField(label='Password', validators=[DataRequired('You forgot to enter password')])
    remember_me = BooleanField(label='Remember me', default=False)


class OncoEntryForm(Form):
    code = StringField(label='Patient code', validators=[DataRequired()])
    age = IntegerField(label='Patient age', validators=[DataRequired()])
    date_of_entry = DateField(label='Date of data entry', validators=[DataRequired()], format='%d-%m-%Y')
    place_of_collection = StringField(label='Place of sample collection', validators=[DataRequired()])

    menopause = BooleanField(label='Menopause ?')
    familial_history = StringField(label='History of cancer in patient family')
    weight = IntegerField(label='Patient weight')
    hiv_status = BooleanField(label='Is patient HIV positive ?')

    date_of_death = DateField(label='Date of death')
    date_of_last_contact = DateField(label='Date of last contact')

    tnm_staging = StringField(label='TNM staging', validators=[DataRequired()])
    tumour_resection_date = DateField(label='Tumour resection date', validators=[DataRequired()])
    tumour_type = StringField(label='Tumour type', validators=[DataRequired()])
    tumour_site = StringField(label='Tumour site', validators=[DataRequired()])
    remission_history = StringField(label='Remission history')

    procurement_method = StringField(label='Procurement method', validators=[DataRequired()])
    pathology_report_id = StringField(label='Pathology report id', validators=[DataRequired()])
    normal_sample_collected = BooleanField(label='Normal sample collected?', validators=[DataRequired()])
    normal_tissue_proximity = StringField(label='Normal tissue proximity', validators=[DataRequired()])
    diagnosis = StringField(label="Pathologist's Diagnosis", validators=[DataRequired()])

    adjuvant_radiotherapy = StringField(label='Adjuvant radiotherapy')
    neo_adjuvant_radiotherapy = StringField(label='Neoadjuvant radiotherapy')
    adjuvant_chemotherapy = StringField(label='Adjuvant chemotherapy')
    neo_adjuvant_chemotherapy = StringField(label='Neo adjuvant chemotherapy')
    targeted_molecular_therapy = StringField(label='Targeted molecular therapy')

    er_status = BooleanField(label='ER positive ?', validators=[DataRequired()])
    pr_status = BooleanField(label='PR positive ?', validators=[DataRequired()])
    her2_status = BooleanField(label='HER2 positive ?', validators=[DataRequired()])

    #percent_lymphocyte_infiltration = db.PositiveIntegerField(null=True, blank=True)
    #percent_monocyte_infiltration = db.PositiveIntegerField(null=True, blank=True)
    #percent_necrosis = db.PositiveIntegerField(null=True, blank=True)
    #percent_neutrophil_infiltration = db.PositiveIntegerField(null=True, blank=True)
    #percent_normal_cells = db.PositiveIntegerField(null=True, blank=True)
    #percent_stromal_cells = db.PositiveIntegerField(null=True, blank=True)
    #percent_tumor_cells = db.PositiveIntegerField(null=True, blank=True)
