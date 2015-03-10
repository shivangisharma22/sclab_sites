from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, DateField, IntegerField, RadioField
from wtforms.validators import DataRequired


class OncoLoginForm(Form):
    username = StringField(label='Oncotyping Username', validators=[DataRequired('Please enter username')])
    password = PasswordField(label='Password', validators=[DataRequired('You forgot to enter password')])
    remember_me = BooleanField(label='Remember me', default=False)


class OncoEntryForm(Form):
    code = StringField(label='Patient code', validators=[DataRequired()])
    pathology_report_id = StringField(label='Histopathology number', validators=[DataRequired()])
    date_of_collection = DateField(label='Date of Sample collection', validators=[DataRequired()], format='%d-%m-%Y')
    date_of_resection = DateField(label='Date of Tumour resection', validators=[DataRequired()], format='%d-%m-%Y')
    place_of_collection = StringField(label='Place of sample collection', validators=[DataRequired()])
    age = IntegerField(label='Patient age', validators=[DataRequired()])
    weight = IntegerField(label='Patient weight')
    menopause = BooleanField(label='Menopause ?')
    hiv_status = BooleanField(label='Is patient HIV positive ?')
    familial_history = StringField(label='History of cancer in patient family')
    normal_sample_collected = BooleanField(label='Normal sample collected?', validators=[DataRequired()])
    normal_tissue_proximity = StringField(label='Normal tissue proximity', validators=[DataRequired()])
    excision_method = StringField(label='Tumour excision methodology', validators=[DataRequired()])
    tumour_type = StringField(label='Tumour type', validators=[DataRequired()])
    tumour_site = StringField(label='Tumour site', validators=[DataRequired()])
    tnm_staging = StringField(label='TNM staging', validators=[DataRequired()])
    er_status = BooleanField(label='ER positive ?', validators=[DataRequired()])
    pr_status = BooleanField(label='PR positive ?', validators=[DataRequired()])
    her2_status = BooleanField(label='HER2 positive ?', validators=[DataRequired()])
    neo_adjuvant_chemotherapy = StringField(label='Neo adjuvant chemotherapy')
    neo_adjuvant_radiotherapy = StringField(label='Neoadjuvant radiotherapy')
    adjuvant_chemotherapy = StringField(label='Adjuvant chemotherapy')
    adjuvant_radiotherapy = StringField(label='Adjuvant radiotherapy')
    targeted_molecular_therapy = StringField(label='Hormonal therapy?')
    patient_alive = BooleanField(label='Patient alive?', validators=[DataRequired()])
    date_of_death = DateField(label='Date of death')
    date_of_last_contact = DateField(label='Date of last contact')
    remission_history = StringField(label='Remission history')
    comments = StringField(label="Other comments", validators=[DataRequired()])