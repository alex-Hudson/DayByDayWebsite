# Generated by Django 3.0.3 on 2020-02-28 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200228_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Series'),
        ),
    ]
