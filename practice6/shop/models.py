from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from .validators import (
    article_regex_validator,
    validate_article,
)

class Product(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Назва товару",
    )

    article = models.CharField(
        max_length=7,
        unique=True,
        verbose_name="Артикул",
        validators=[
            article_regex_validator,
            validate_article,
        ],
    )

    description = models.TextField(
        verbose_name="Опис",
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Ціна",
    )

    weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Вага (кг)",
    )

    production_date = models.DateField(
        verbose_name="Дата виробництва",
    )

    def clean(self):
        super().clean()

        if self.price is not None and self.price <= 0:
            raise ValidationError({
                "price": "Ціна товару повинна бути більшою за 0."
            })

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ["title"]