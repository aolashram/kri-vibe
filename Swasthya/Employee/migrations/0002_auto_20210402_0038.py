# Generated by Django 2.1.7 on 2021-04-02 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='district',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='bank',
        ),
        migrations.AddField(
            model_name='employee',
            name='account_no',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='bank_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='branch_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Employee.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Employee.District'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='ifsc_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='pincode',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Employee.State'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='BankInfo',
        ),
    ]
