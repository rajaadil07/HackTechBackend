# Generated by Django 4.1.7 on 2023-03-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Newspaper",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
                ("label", models.CharField(blank=True, max_length=255, null=True)),
                ("text", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
