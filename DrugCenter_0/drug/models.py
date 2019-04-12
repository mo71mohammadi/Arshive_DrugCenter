import datetime
from django.db import models
from djongo import models
from django.contrib.auth.models import User
from django import forms


class DosageForm(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    DosageFormName = models.CharField(max_length=300, null=True)
    DosageFormShortName = models.CharField(max_length=300, null=True)
    Class = models.CharField(max_length=300, null=True)
    Status = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.DosageFormName


class Molecule(models.Model):
    id = models.IntegerField('MoleculeID', primary_key=True)
    MoleculeName = models.CharField(max_length=300, null=True, unique=True)
    # Description = models.TextField(null=True, blank=True)
    # Structure = models.URLField(null=True, blank=True)
    # CASNumber = models.CharField(max_length=100, default=0, null=True, blank=True)
    # Weight = models.CharField(max_length=300, default=0, null=True, blank=True)
    # ChemicalFormula = models.CharField(max_length=300, null=True, blank=True)

    #


class Generic(models.Model):
    molecule = models.ForeignKey(Molecule, null=True, on_delete=models.SET_NULL, blank=True)
    id = models.IntegerField('GenericCode', default=0, primary_key=True)
    EnGenericName = models.CharField(max_length=300, null=True)
    # dosageForm = models.ForeignKey(DosageForm, on_delete=models.SET_NULL, null=True, blank=True)
    # Strength = models.CharField(max_length=10, null=True)
    ATCCode = models.IntegerField(default=0)
    ATCName = models.CharField(max_length=300, null=True)
    EssentialType = ((0, 'No'), (1, 'YES'))
    Essential = models.IntegerField(choices=EssentialType)

    def __str__(self):
        return f'{self.id:05d} '

    def Gid(self):
        return f'{self.id:05d}'


class Product(models.Model):
    eRx = models.CharField(max_length=50, unique=True)
    GenericCode = models.ForeignKey(Generic, on_delete=models.SET_NULL, null=True)
    BrandName = models.CharField(max_length=300, null=True)
    FaBrandName = models.CharField(max_length=300, null=True)
    BrandOwner = models.CharField(max_length=300, null=True)
    CoBrandOwner = models.CharField(max_length=300, null=True)
    Provider = models.CharField(max_length=300, null=True)
    Owner = models.CharField(max_length=300, null=True)
    Ptype = ((1, 'Drug'), (2, 'Supplement'), (3, 'Cosmetic'),)
    ProductType = models.IntegerField(choices=Ptype)
    ActivePackaging = models.IntegerField('eRx', default=0)
    # ProductType = models.CharField(max_length=1, choices=Product_Type, null=True)
    # PriceProvider = models.IntegerField(default=0)
    # DistributorPrice = models.IntegerField(default=0)
    # DrugstorePrice = models.IntegerField(default=0)
    # ManufactureDate = models.DateField('Manufacture', null=True)
    # ExpirationDate = models.DateField('Expiration', null=True)
    # DateChange = models.DateField(null=True)
    # ProductPic = models.ImageField(upload_to = 'pic_folder/', null=True)
    GTIN = models.BigIntegerField('ProductBarcod', default=0)
    IRC = models.BigIntegerField(default=0)
    IRC_N = models.BigIntegerField(default=0)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class Bime(models.Model):
    GenericCode = models.OneToOneField(Generic, on_delete=models.SET_NULL, null=True)
    EnGenericName = models.CharField(max_length=300, null=True)
    BrandName = models.CharField(max_length=300, null=True, blank=True)
    DosageForm = models.CharField(max_length=300, null=True)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    InfluencedDate = models.DateField(null=True)
    Insurance = models.CharField(max_length=50, null=True)
    Hospital = models.CharField(max_length=50, null=True)
    HospitalSazman = models.CharField(max_length=50, null=True)
    Approve = models.CharField(max_length=50, null=True)
    Receiver = models.CharField(max_length=50, null=True, blank=True)
    OrganizationPercent = models.CharField(max_length=300, null=True)
    MamaPermit = models.CharField(max_length=50, null=True)
    MDPermit = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Price


class Doc_inter(models.Model):
    id = models.IntegerField(primary_key=True)
    Severity = models.PositiveSmallIntegerField(default=0)
    Evidence = models.PositiveSmallIntegerField(default=0)
    Onset = models.PositiveSmallIntegerField(default=0)
    Monograph_1 = models.CharField(max_length=300, null=True)
    Monograph_2 = models.TextField(max_length=500, null=True)


class Interaction(models.Model):
    Doc = models.ForeignKey(Doc_inter, on_delete=models.SET_NULL, null=True)
    Drug_1 = models.PositiveSmallIntegerField(null=True)
    Drug_2 = models.PositiveSmallIntegerField(null=True)
    TitleDrug_1 = models.CharField(max_length=300, null=True)
    TitleDrug_2 = models.CharField(max_length=300, null=True)


class Interact_med(models.Model):
    object = models.CharField(max_length=300, null=True)
    subject = models.CharField(max_length=300, null=True)
    text = models.TextField(max_length=2000, null=True)
    severityId = models.PositiveSmallIntegerField(null=True)
    severity = models.CharField(max_length=200, null=True)


class Patient(models.Model):
    NationalCode = models.IntegerField(default=0)
    FirstName = models.CharField(max_length=100, null=True)
    LasttName = models.CharField(max_length=100, null=True)
    PhoneNumber = models.IntegerField(default=0)
    Birthdate = models.DateField(auto_now=True)


class Physician(models.Model):
    MedicalCode = models.IntegerField(default=0)
    Name = models.CharField(max_length=100, null=True)


class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, )
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, )
    physician = models.ForeignKey(Physician, on_delete=models.SET_NULL, null=True, )
    # tarikh = models.ArrayModelField(model_container=Product, model_form_class=ProductForm, null=True)
    Prescription_Date = models.DateField(auto_now=True)
    Validity_Date = models.DateField(auto_now=True)
    Deliver_Date = models.DateField(auto_now=True)
    Prescription_Type = models.CharField(max_length=100)
    Insurance = models.CharField(max_length=100)
    Serial = models.IntegerField(default=0)
    Page = models.IntegerField(default=0)


class PrescriptionItems(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    Price = models.IntegerField(default=0)
    InsurancePrice = models.IntegerField(default=0)


class Book(models.Model):

    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name