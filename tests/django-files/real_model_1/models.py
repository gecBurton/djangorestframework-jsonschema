import uuid
from django.core import validators
from django.db import models
from jsonschema2dj.valdiators import JSONSchemaValidator
try:
    from django.contrib.postgres.fields import JSONField
except ImportError:
    pass


class Manifest(models.Model):

    sample_id = models.IntegerField(validators=[validators.MinValueValidator(1000000000), validators.MaxValueValidator(2147483647)])
    well = models.CharField(help_text="""physical location of the well on the plate""", max_length=255, validators=[validators.RegexValidator("^[A-H](0[1-9]|1[1-2])$")])
    volume_ul = models.IntegerField(validators=[validators.MinValueValidator(10), validators.MaxValueValidator(700)])
    concentration_ng_ul = models.DecimalField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(9999.99)], max_digits=10, decimal_places=5)
    od_260_280 = models.DecimalField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)], max_digits=10, decimal_places=5)
    cancer_sample_y_n = models.CharField(max_length=3, choices=[('yes', 'yes'), ('no', 'no')])
    sample_type = models.CharField(max_length=44, choices=[('dna_blood_germline', 'dna_blood_germline'), ('dna_saliva', 'dna_saliva'), ('dna_fibroblast', 'dna_fibroblast'), ('dna_ff_germline', 'dna_ff_germline'), ('dna_ffpe_tumour', 'dna_ffpe_tumour'), ('dna_ff_tumour', 'dna_ff_tumour'), ('dna_blood_tumour', 'dna_blood_tumour'), ('dna_bone_marrow_aspirate_tumour_sorted_cells', 'dna_bone_marrow_aspirate_tumour_sorted_cells'), ('dna_bone_marrow_aspirate_tumour_cells', 'dna_bone_marrow_aspirate_tumour_cells'), ('tumour_tissue_ffpe', 'tumour_tissue_ffpe'), ('lysate_ffpe', 'lysate_ffpe'), ('lysate_ff', 'lysate_ff'), ('lysed_tumour_cells', 'lysed_tumour_cells'), ('streck_plasma', 'streck_plasma'), ('edta_plasma', 'edta_plasma'), ('lihep_plasma', 'lihep_plasma'), ('serum', 'serum'), ('rna_blood', 'rna_blood'), ('tumour_tissue_ff', 'tumour_tissue_ff'), ('bone_marrow_rna_gtc', 'bone_marrow_rna_gtc'), ('blood_rna_gtc', 'blood_rna_gtc')])
    plate = models.ForeignKey("Plate", on_delete=models.CASCADE)
    redcap = models.ManyToManyField("Redcap")


class Redcap(models.Model):

    GenOMICC = models.CharField(primary_key=True, max_length=255, validators=[validators.RegexValidator("^.{4,32}$")])
    sex = models.CharField(max_length=1, choices=[('m', 'm'), ('f', 'f'), ('u', 'u')])
    nhs_number = models.CharField(max_length=255, validators=[validators.RegexValidator("^\d{3} \d{3} \d{4}$")])
    date_of_birth = models.DateField()
    consent_taken_assertion = models.BooleanField()
    hospital_trust = models.CharField(max_length=255)
    date_of_identifying_eligibility_for_the_study = models.DateField()
    responsible_clinician = models.ForeignKey("ResponsibleClinician", on_delete=models.CASCADE)


class ResponsibleClinician(models.Model):

    name = models.CharField(null=True, max_length=255)
    email = models.EmailField(null=True)
    address = JSONField(validators=[JSONSchemaValidator({'type': 'object', 'properties': {'lines': {'type': 'array', 'items': {'type': 'string'}}, 'postcode': {'type': 'string', 'pattern': '^[A-Z]{2}\\d \\d[A-Z]{2}$'}}})])


class Plate(models.Model):

    barcode = models.CharField(primary_key=True, max_length=255, validators=[validators.RegexValidator("^LP\d{7}-DNA$")])
    priority = models.CharField(max_length=7, choices=[('routine', 'routine'), ('urgent', 'urgent')])
