# Generated by Django 4.0.6 on 2022-07-29 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JTR', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jtr',
            options={'ordering': ['id'], 'verbose_name': 'Направления', 'verbose_name_plural': 'Направления'},
        ),
    ]