# Generated by Django 4.1 on 2022-09-02 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0022_event_status_team_rename_status_contract_signed_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="team",
        ),
        migrations.DeleteModel(
            name="Team",
        ),
    ]
