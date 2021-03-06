# Generated by Django 4.0.3 on 2022-03-24 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("author_name", models.CharField(max_length=60)),
                ("content", models.CharField(max_length=500)),
                ("creation_date", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=60)),
                ("link", models.CharField(max_length=60)),
                ("creation_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("amount_of_upvotes", models.IntegerField(default=0)),
                ("author_name", models.CharField(max_length=60)),
            ],
        ),
    ]
