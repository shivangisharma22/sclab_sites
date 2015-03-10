from sclab_sites import oncotypingdb as db


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True, index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.username


class Patient(db.Model):

    code = db.Column(db.String(200), primary_key=True)
    age = db.Column(db.Integer)
    date_of_entry = db.Column(db.DateTime)
    place_of_collection = db.Column(db.String(200))

    menopause = db.Column(db.Boolean)
    familial_history = db.Column(db.String(200))
    weight = db.Column(db.Integer)
    hiv_status = db.Column(db.Boolean)

    date_of_death = db.Column(db.DateTime)
    date_of_last_contact = db.Column(db.DateTime)

    tnm_staging = db.Column(db.String(200))
    tumour_resection_date = db.Column(db.String(200))
    tumour_type = db.Column(db.String(200))
    tumour_site = db.Column(db.String(200))
    remission_history = db.Column(db.String(200))

    procurement_method = db.Column(db.String(200))
    pathology_report_id = db.Column(db.String(200))
    normal_sample_collected = db.Column(db.Boolean)
    normal_tissue_proximity = db.Column(db.String(200))
    diagnosis = db.Column(db.String(200))

    adjuvant_radiotherapy = db.Column(db.String(200))
    neo_adjuvant_radiotherapy = db.Column(db.String(200))
    adjuvant_chemotherapy = db.Column(db.String(200))
    neo_adjuvant_chemotherapy = db.Column(db.String(200))
    targeted_molecular_therapy = db.Column(db.String(200))

    #percent_lymphocyte_infiltration = db.PositiveIntegerField(null=True, blank=True)
    #percent_monocyte_infiltration = db.PositiveIntegerField(null=True, blank=True)
    #percent_necrosis = db.PositiveIntegerField(null=True, blank=True)
    #percent_neutrophil_infiltration = db.PositiveIntegerField(null=True, blank=True)
    #percent_normal_cells = db.PositiveIntegerField(null=True, blank=True)
    #percent_stromal_cells = db.PositiveIntegerField(null=True, blank=True)
    #percent_tumor_cells = db.PositiveIntegerField(null=True, blank=True)

    er_status = db.Column(db.Boolean)
    pr_status = db.Column(db.Boolean)
    her2_status = db.Column(db.Boolean)

    #rin_value = db.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return '<Patient code %r>' % self.code
