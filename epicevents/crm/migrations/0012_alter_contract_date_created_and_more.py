# Generated by Django 4.1 on 2022-08-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0011_alter_contract_amount_alter_contract_client_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="contract",
            name="date_update",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="contract",
            name="payment_due",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="event",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="date_update",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_date",
            field=models.DateTimeField(),
        ),
    ]
