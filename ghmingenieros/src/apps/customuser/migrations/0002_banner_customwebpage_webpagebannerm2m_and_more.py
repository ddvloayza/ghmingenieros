# Generated by Django 4.1.3 on 2023-05-15 09:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("customuser", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banner",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="banner", verbose_name="image"
                    ),
                ),
            ],
            options={
                "verbose_name": "Banner",
                "verbose_name_plural": "Banners",
            },
        ),
        migrations.CreateModel(
            name="CustomWebPage",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Phone Number"
                    ),
                ),
                (
                    "phone_number_two",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Phone Number Two"
                    ),
                ),
                (
                    "email",
                    models.CharField(blank=True, max_length=200, verbose_name="Email"),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=500, verbose_name="Direccion"
                    ),
                ),
                (
                    "company_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Company Name"
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "CustomWebPage",
                "verbose_name_plural": "CustomWebPages",
            },
        ),
        migrations.CreateModel(
            name="WebPageBannerM2M",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "banner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customuser.banner",
                    ),
                ),
                (
                    "custom_web_page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customuser.customwebpage",
                    ),
                ),
            ],
            options={
                "verbose_name": "WebPageBannerM2M",
                "verbose_name_plural": "WebPageBannerM2Ms ",
            },
        ),
        migrations.AddField(
            model_name="customwebpage",
            name="banners",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="banner_set",
                through="customuser.WebPageBannerM2M",
                to="customuser.banner",
            ),
        ),
    ]
