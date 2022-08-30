# Generated by Django 4.1 on 2022-08-30 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0013_remove_event_client_event_contract_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="employee_contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
