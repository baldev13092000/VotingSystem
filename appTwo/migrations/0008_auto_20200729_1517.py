# Generated by Django 3.0.3 on 2020-07-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0007_auto_20200729_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default=0),
        ),
    ]
