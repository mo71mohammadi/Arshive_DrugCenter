# Generated by Django 2.1.7 on 2019-03-17 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnGenericName', models.CharField(max_length=300, null=True)),
                ('BrandName', models.CharField(blank=True, max_length=300, null=True)),
                ('DosageForm', models.CharField(max_length=300, null=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('InfluencedDate', models.DateField(null=True)),
                ('Insurance', models.CharField(max_length=50, null=True)),
                ('Hospital', models.CharField(max_length=50, null=True)),
                ('HospitalSazman', models.CharField(max_length=50, null=True)),
                ('Approve', models.CharField(max_length=50, null=True)),
                ('Receiver', models.CharField(blank=True, max_length=50, null=True)),
                ('OrganizationPercent', models.CharField(max_length=300, null=True)),
                ('MamaPermit', models.CharField(max_length=50, null=True)),
                ('MDPermit', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doc_inter',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Severity', models.PositiveSmallIntegerField(default=0)),
                ('Evidence', models.PositiveSmallIntegerField(default=0)),
                ('Onset', models.PositiveSmallIntegerField(default=0)),
                ('Monograph_1', models.CharField(max_length=300, null=True)),
                ('Monograph_2', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DosageForm',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('DosageFormName', models.CharField(max_length=300, null=True)),
                ('DosageFormShortName', models.CharField(max_length=300, null=True)),
                ('Class', models.CharField(max_length=300, null=True)),
                ('Status', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Generic',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='GenericCode')),
                ('EnGenericName', models.CharField(max_length=300, null=True)),
                ('ATCCode', models.IntegerField(default=0)),
                ('ATCName', models.CharField(max_length=300, null=True)),
                ('Essential', models.IntegerField(choices=[(0, 'No'), (1, 'YES')])),
            ],
        ),
        migrations.CreateModel(
            name='Interact_med',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(max_length=300, null=True)),
                ('subject', models.CharField(max_length=300, null=True)),
                ('text', models.TextField(max_length=2000, null=True)),
                ('severityId', models.PositiveSmallIntegerField(null=True)),
                ('severity', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Drug_1', models.PositiveSmallIntegerField(null=True)),
                ('Drug_2', models.PositiveSmallIntegerField(null=True)),
                ('TitleDrug_1', models.CharField(max_length=300, null=True)),
                ('TitleDrug_2', models.CharField(max_length=300, null=True)),
                ('Doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Doc_inter')),
            ],
        ),
        migrations.CreateModel(
            name='Molecule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='MoleculeID')),
                ('MoleculeName', models.CharField(max_length=300, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eRx', models.CharField(max_length=50, unique=True)),
                ('BrandName', models.CharField(max_length=300, null=True)),
                ('FaBrandName', models.CharField(max_length=300, null=True)),
                ('BrandOwner', models.CharField(max_length=300, null=True)),
                ('CoBrandOwner', models.CharField(max_length=300, null=True)),
                ('Provider', models.CharField(max_length=300, null=True)),
                ('Owner', models.CharField(max_length=300, null=True)),
                ('ProductType', models.IntegerField(choices=[(1, 'Drug'), (2, 'Supplement'), (3, 'Cosmetic')])),
                ('ActivePackaging', models.IntegerField(default=0, verbose_name='eRx')),
                ('GTIN', models.BigIntegerField(default=0, verbose_name='ProductBarcod')),
                ('IRC', models.BigIntegerField(default=0)),
                ('IRC_N', models.BigIntegerField(default=0)),
                ('GenericCode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Generic')),
            ],
        ),
        migrations.AddField(
            model_name='generic',
            name='molecule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Molecule'),
        ),
        migrations.AddField(
            model_name='bime',
            name='GenericCode',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drug.Generic'),
        ),
    ]
