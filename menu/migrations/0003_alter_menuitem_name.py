# Generated by Django 4.2.6 on 2023-10-18 08:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0002_alter_menuitem_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="name",
            field=models.CharField(max_length=50, unique=True, verbose_name="Название"),
        ),
    ]
