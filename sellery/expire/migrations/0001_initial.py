# Generated by Django 4.1.2 on 2022-10-15 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('fridge_lower', models.DurationField(null=True)),
                ('fridge_upper', models.DurationField(null=True)),
                ('freezer_lower', models.DurationField(null=True)),
                ('freezer_upper', models.DurationField(null=True)),
                ('pantry_lower', models.DurationField(null=True)),
                ('pantry_upper', models.DurationField(null=True)),
                ('default_pref', models.CharField(choices=[('FRI', 'Fridge'), ('FRE', 'Freezer'), ('PAN', 'Pantry')], default='FRI', max_length=3)),
            ],
        ),
    ]
