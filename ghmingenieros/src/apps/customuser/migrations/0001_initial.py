# Generated by Django 4.1.3 on 2023-04-14 09:48

import apps.customuser.models.customuser
import apps.customuser.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("ubigeos", "0002_auto_20210325_1040"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(max_length=75, unique=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
            managers=[
                ("objects", apps.customuser.models.customuser.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("seo_title", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "seo_description",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "seo_keywords",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "nick_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Nick Name"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="First Name"
                    ),
                ),
                ("last_name", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "type_document",
                    models.CharField(
                        blank=True,
                        choices=[("DNI", "DNI"), ("CARNET", "Carnet de Extranjeria")],
                        default="DNI",
                        max_length=60,
                        null=True,
                        verbose_name="Type Document",
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Ocupation"
                    ),
                ),
                (
                    "document_number",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("MALE", "Hombre"),
                            ("FEMALE", "Mujer"),
                            ("OTHER", "Otros"),
                        ],
                        max_length=60,
                        null=True,
                        verbose_name="Genero",
                    ),
                ),
                ("phone_number", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "civil_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("MARRIED", "Casado"),
                            ("DIVORCED", "Divorciado"),
                            ("SINGLE", "Soltero"),
                        ],
                        max_length=60,
                        null=True,
                        verbose_name="Estado Civil",
                    ),
                ),
                (
                    "image_profile",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=apps.customuser.utils.custom_user_upload_to,
                        verbose_name="image_profile",
                    ),
                ),
                (
                    "distrito",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ubigeos.distrito",
                    ),
                ),
                (
                    "provincia",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ubigeos.provincia",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ubigeos.region",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Profile",
                "verbose_name_plural": "Users Profiles",
            },
        ),
    ]
