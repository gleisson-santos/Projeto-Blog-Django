# Generated by Django 4.2.1 on 2023-07-19 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categorias", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                (
                    "titulo_post",
                    models.CharField(max_length=255, verbose_name="Titulo"),
                ),
                (
                    "data_post",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Data"
                    ),
                ),
                ("conteudo_post", models.TextField(verbose_name="Conteúdo")),
                ("excerto_post", models.TextField(verbose_name="Excerto")),
                (
                    "imagem_post",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="post_img/%Y/%m/%d",
                        verbose_name="Imagem",
                    ),
                ),
                (
                    "publicado_post",
                    models.BooleanField(default=False, verbose_name="Publicado"),
                ),
                (
                    "autor_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Autor",
                    ),
                ),
                (
                    "categoria_post",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="categorias.categoria",
                        verbose_name="Categoria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PostImage",
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
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="post_img/%Y/%m/%d"
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="posts.post",
                    ),
                ),
            ],
        ),
    ]
