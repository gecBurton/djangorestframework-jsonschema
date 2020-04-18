
import uuid
from django.core import validators
from django.db import models
try:
    from extra_fields import JSONSchemaField
except ImportError:
    pass


class manifest(models.Model):
    sample_id = models.IntegerField(null=False, validators=[validators.MinValueValidator(1000000000), validators.MaxValueValidator(2147483647)], primary_key=False, )
    well = models.CharField(null=False, primary_key=False, max_length=255, validators=[('RegexValidator', 'r"^[A-H](0[1-9]|1[1-2])$"')], )
    volume_ul = models.IntegerField(null=False, validators=[validators.MinValueValidator(10), validators.MaxValueValidator(700)], primary_key=False, )
    concentration_ng_ul = models.DecimalField(null=False, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(9999.99)], max_digits=10, decimal_places=5, primary_key=False, )
    od_260_280 = models.DecimalField(null=False, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)], max_digits=10, decimal_places=5, primary_key=False, )
    cancer_sample_y_n = models.CharField(null=False, primary_key=False, max_length=3, choices=[('yes', 'yes'), ('no', 'no')], )
    sample_type = models.CharField(null=False, primary_key=False, max_length=44, choices=[('dna_blood_germline', 'dna_blood_germline'), ('dna_saliva', 'dna_saliva'), ('dna_fibroblast', 'dna_fibroblast'), ('dna_ff_germline', 'dna_ff_germline'), ('dna_ffpe_tumour', 'dna_ffpe_tumour'), ('dna_ff_tumour', 'dna_ff_tumour'), ('dna_blood_tumour', 'dna_blood_tumour'), ('dna_bone_marrow_aspirate_tumour_sorted_cells', 'dna_bone_marrow_aspirate_tumour_sorted_cells'), ('dna_bone_marrow_aspirate_tumour_cells', 'dna_bone_marrow_aspirate_tumour_cells'), ('tumour_tissue_ffpe', 'tumour_tissue_ffpe'), ('lysate_ffpe', 'lysate_ffpe'), ('lysate_ff', 'lysate_ff'), ('lysed_tumour_cells', 'lysed_tumour_cells'), ('streck_plasma', 'streck_plasma'), ('edta_plasma', 'edta_plasma'), ('lihep_plasma', 'lihep_plasma'), ('serum', 'serum'), ('rna_blood', 'rna_blood'), ('tumour_tissue_ff', 'tumour_tissue_ff'), ('bone_marrow_rna_gtc', 'bone_marrow_rna_gtc'), ('blood_rna_gtc', 'blood_rna_gtc')], )

    plate = models.ForeignKey("plate", null=True, on_delete=models.CASCADE, )
    redcap = models.ManyToManyField("redcap", null=True, on_delete=models.CASCADE, )


class redcap(models.Model):
    GenOMICC = models.CharField(null=False, primary_key=True, max_length=255, validators=[('RegexValidator', 'r"^.{4,32}$"')], )
    sex = models.CharField(null=False, primary_key=False, max_length=1, choices=[('m', 'm'), ('f', 'f'), ('u', 'u')], )
    nhs_number = models.CharField(null=False, primary_key=False, max_length=255, validators=[('RegexValidator', 'r"^\\d{3} \\d{3} \\d{4}$"')], )
    date_of_birth = models.DateField(null=False, primary_key=False, )
    consent_taken_assertion = models.BooleanField(null=False, primary_key=False, )
    hospital_trust = models.CharField(null=False, primary_key=False, max_length=255, )
    date_of_identifying_eligibility_for_the_study = models.DateField(null=False, primary_key=False, )

    responsible_clinician = models.ForeignKey("ResponsibleClinician", null=True, on_delete=models.CASCADE, )


class ResponsibleClinician(models.Model):
    name = models.CharField(null=False, primary_key=False, max_length=255, )
    email = models.EmailField(null=False, primary_key=False, )
    address = models.JSONSchemaField(schema={'type': 'object', 'properties': {'lines': {'type': 'array', 'items': {'type': 'string'}}, 'postcode': {'type': 'string', 'pattern': '^[A-Z]{2}\\d \\d[A-Z]{2}$'}}}, )



class plate(models.Model):
    barcode = models.CharField(null=False, primary_key=True, max_length=255, validators=[('RegexValidator', 'r"^LP\\d{7}-DNA$"')], )
    priority = models.CharField(null=False, primary_key=False, max_length=7, choices=[('routine', 'routine'), ('urgent', 'urgent')], )

