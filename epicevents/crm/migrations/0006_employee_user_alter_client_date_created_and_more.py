# Generated by Django 4.1 on 2022-08-28 14:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crm", "0005_client_statuts_client_alter_client_date_created_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="client",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 16, 40, 55, 553118)
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 16, 40, 55, 553118)
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 16, 40, 55, 553118)
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 16, 40, 55, 553118)
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="payment_due",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 16, 40, 55, 553118)
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 16, 40, 55, 553118)
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 16, 40, 55, 553118)
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 16, 40, 55, 553118)
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 16, 40, 55, 553118)
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 16, 40, 55, 553118)
            ),
        ),
    ]
