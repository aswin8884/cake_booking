# Generated by Django 4.2.4 on 2024-02-07 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0006_request_addcakes_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcakes',
            name='bakerid',
        ),
        migrations.AddField(
            model_name='request',
            name='bakerId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cakes.registrationbaker'),
        ),
        migrations.AddField(
            model_name='request',
            name='current_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cakes.registrationuser'),
        ),
        migrations.AddField(
            model_name='addcakes',
            name='bakerId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cakes.registrationbaker'),
        ),
    ]
