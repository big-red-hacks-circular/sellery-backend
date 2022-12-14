# Generated by Django 3.2.14 on 2022-10-16 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expire',
            name='freezer_lower',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expire',
            name='freezer_upper',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expire',
            name='fridge_lower',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expire',
            name='fridge_upper',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expire',
            name='pantry_lower',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expire',
            name='pantry_upper',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
