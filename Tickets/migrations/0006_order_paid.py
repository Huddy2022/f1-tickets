# Generated by Django 3.2.20 on 2023-08-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0005_auto_20230827_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
