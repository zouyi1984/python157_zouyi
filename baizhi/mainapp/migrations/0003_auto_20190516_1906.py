# Generated by Django 2.0.6 on 2019-05-16 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190516_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbook',
            old_name='c_introducete',
            new_name='c_introduce',
        ),
        migrations.RenameField(
            model_name='tbook',
            old_name='n_introducete',
            new_name='n_introduce',
        ),
        migrations.RemoveField(
            model_name='tbook',
            name='pages',
        ),
    ]