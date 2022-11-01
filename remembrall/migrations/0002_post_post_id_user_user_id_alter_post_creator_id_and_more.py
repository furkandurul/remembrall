# Generated by Django 4.1.2 on 2022-11-01 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("remembrall", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_id",
            field=models.CharField(default="0", max_length=200),
        ),
        migrations.AddField(
            model_name="user",
            name="user_id",
            field=models.CharField(default="0", max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="creator_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="remembrall.user",
                to_field="user_id",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_name",
            field=models.CharField(default="new_user", max_length=50),
        ),
    ]
