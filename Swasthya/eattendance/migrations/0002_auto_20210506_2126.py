# Generated by Django 2.1.7 on 2021-05-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eattendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Ins',
        ),
    ]
