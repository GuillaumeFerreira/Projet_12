# Generated by Django 4.1 on 2022-09-05 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0024_alter_event_event_status"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Employee",
        ),
    ]