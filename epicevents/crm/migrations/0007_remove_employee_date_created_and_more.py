# Generated by Django 4.1 on 2022-08-28 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0006_employee_user_alter_client_date_created_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="date_created",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="date_update",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="email",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="mobile",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="phone",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="team",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="user",
        ),
        migrations.AddField(
            model_name="employee",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="password",
            field=models.CharField(
                default="test", max_length=128, verbose_name="password"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="client",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 17, 15, 54, 643227)
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 17, 15, 54, 643227)
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 17, 15, 54, 643227)
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 17, 15, 54, 643227)
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="payment_due",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 17, 15, 54, 643227)
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 17, 15, 54, 643227)
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="date_update",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 17, 15, 54, 643227)
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 28, 17, 15, 54, 643227)
            ),
        ),
    ]
