# Generated by Django 4.1 on 2022-08-27 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0003_client_company_name_client_date_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 17, 36, 11, 720971)
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 17, 36, 11, 720971)
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 17, 36, 11, 720971)
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 17, 36, 11, 720971)
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="payment_due",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 17, 36, 11, 720971)
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 17, 36, 11, 705346)
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 17, 36, 11, 705346)
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 17, 36, 11, 720971)
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 17, 36, 11, 720971)
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 27, 17, 36, 11, 720971)
            ),
        ),
    ]