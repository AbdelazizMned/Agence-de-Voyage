# Generated by Django 5.0.6 on 2024-07-01 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotel",
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
                ("name", models.CharField(max_length=500)),
                (
                    "location",
                    models.CharField(
                        choices=[
                            ("Ariana", "Ariana"),
                            ("Beja", "Beja"),
                            ("Ben Arous", "Ben Arous"),
                            ("Bizerte", "Bizerte"),
                            ("Gabes", "Gabes"),
                            ("Gafsa", "Gafsa"),
                            ("Jendouba", "Jendouba"),
                            ("Kairouan", "Kairouan"),
                            ("Kasserine", "Kasserine"),
                            ("Kebili", "Kebili"),
                            ("Kef", "Kef"),
                            ("Mahdia", "Mahdia"),
                            ("Manouba", "Manouba"),
                            ("Medenine", "Medenine"),
                            ("Monastir", "Monastir"),
                            ("Nabeul", "Nabeul"),
                            ("Sfax", "Sfax"),
                            ("Sidi Bouzid", "Sidi Bouzid"),
                            ("Siliana", "Siliana"),
                            ("Sousse", "Sousse"),
                            ("Tataouine", "Tataouine"),
                            ("Tozeur", "Tozeur"),
                            ("Tunis", "Tunis"),
                            ("Zaghouan", "Zaghouan"),
                        ],
                        max_length=800,
                    ),
                ),
                ("email", models.EmailField(max_length=600)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Season",
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
                ("name", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Single Room", "Single Room"),
                            ("Double Room", "Double Room"),
                            ("Suite", "Suite"),
                            ("Family Room", "Family Room"),
                        ],
                        max_length=500,
                    ),
                ),
                (
                    "price_per_night",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "Hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotels.hotel"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Price",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotels.room"
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotels.season"
                    ),
                ),
            ],
        ),
    ]