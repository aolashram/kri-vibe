# Generated by Django 2.1.7 on 2021-05-27 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0005_auto_20210525_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dietitem',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='itemcategory',
            name='default_unit_value',
        ),
        migrations.RemoveField(
            model_name='itemcategory',
            name='measurement_unit',
        ),
        migrations.AddField(
            model_name='dietitem',
            name='default_unit_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='dietitem',
            name='measurement_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='med.MeasurementUnit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dietorder',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='measurementunit',
            name='measurement',
            field=models.CharField(choices=[('Milligram', 'mg'), ('Gram', 'g'), ('Kilogram', 'kg'), ('Milliliter', 'ml'), ('Liter', 'l')], max_length=20),
        ),
    ]