# Generated by Django 4.0.4 on 2022-04-18 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_alter_neighborhood_occupants_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location.neighborhood'),
        ),
    ]