from django.contrib.sites import requests
from requests import request
from drug import views
from .models import Prescription, PrescriptionItems, Physician, Patient
from django import forms
from django.forms import formset_factory


class BookForm(forms.Form):
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )


BookFormset = formset_factory(BookForm, extra=1)


class PrescriptionForm(forms.Form):
    PrescriptionDate = forms.DateField()
    ValidityDate = forms.DateField()
    DeliveryDate = forms.DateField()
    Serial = forms.IntegerField()
    Page = forms.IntegerField()
    # PrescriptionType = forms.ModelMultipleChoiceField(queryset=Patient.objects.all())
    InsuranceType = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'q', "class": "form-control my-0 py-1 red-border", }))
    PrescriptionType = forms.CharField()


class PrescriptionItemForm(forms.Form):
    eRx = forms.IntegerField()
    Genericinfo = forms.CharField()
    Number = forms.IntegerField()
    Expiry = forms.IntegerField()
    InsurancePrice = forms.IntegerField()
    Price = forms.IntegerField()


PrescriptionItemFormset = formset_factory(PrescriptionItemForm, extra=1)


class PrescriptionzForm(forms.ModelForm):
    class Meta:
        model = Prescription
        # fields = '__all__'
        fields = ('Page', 'Serial', 'Insurance', 'Prescription_Type')


class PhysicianForm(forms.ModelForm):
    class Meta:
        model = Physician
        fields = '__all__'
        # fields = ('tarikh', 'tarik', 'tari')


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        # fields = ('tarikh', 'tarik', 'tari')


class NameForm3(forms.ModelForm):
    tari = forms.CharField(max_length=100)

    class Meta:
        model = PrescriptionItems
        # fields = '__all__'
        fields = ('Price', 'InsurancePrice', 'tari')
