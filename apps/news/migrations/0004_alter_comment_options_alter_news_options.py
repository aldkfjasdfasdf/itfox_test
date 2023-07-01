# Generated by Django 4.2.2 on 2023-06-30 18:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_alter_comment_options_alter_news_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ("-date",),
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
        migrations.AlterModelOptions(
            name="news",
            options={"ordering": ("-date",), "verbose_name_plural": "News"},
        ),
    ]