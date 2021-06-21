# Generated by Django 2.1.7 on 2021-04-01 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='BankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=150, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=20, null=True)),
                ('account_no', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('1', 'Mr.'), ('3', 'Mrs.'), ('2', 'Ms.'), ('4', 'Dr.')], max_length=1, null=True)),
                ('first_name', models.CharField(max_length=60)),
                ('middle_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(max_length=60)),
                ('sur_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('marital_status', models.CharField(choices=[('SI', 'Single'), ('MA', 'Married'), ('WI', 'Widowed'), ('DI', 'Divorced'), ('SE', 'Seperated')], max_length=2)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('aadhaar_number', models.CharField(max_length=20)),
                ('pan_number', models.CharField(max_length=10)),
                ('qualification', models.TextField()),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('registration_details', models.TextField(verbose_name=())),
                ('emp_code', models.CharField(max_length=20)),
                ('ccim_employment_status', models.CharField(choices=[('Y', 'YES'), ('N', 'No')], default='N', max_length=1)),
                ('date_of_join', models.DateField()),
                ('date_of_confirmation', models.DateField(blank=True, null=True)),
                ('employment_status', models.CharField(max_length=20)),
                ('pf_number', models.CharField(blank=True, max_length=20, null=True)),
                ('esi_number', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.Address')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.BankInfo')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Employee.Department')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Designation')),
                ('line_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.Employee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Country'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.District'),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.State'),
        ),
    ]
