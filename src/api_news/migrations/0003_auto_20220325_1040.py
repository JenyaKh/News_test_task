# Generated by Django 3.2.12 on 2022-03-25 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api_news", "0002_comment_post"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="post",
        ),
        migrations.AddField(
            model_name="comment",
            name="post_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api_news.post",
            ),
        ),
    ]
