# Generated by Django 4.0.6 on 2022-08-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
