# Generated by Django 2.0.6 on 2019-05-24 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20190524_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taddress',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser'),
        ),
    ]
