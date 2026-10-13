from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

article_regex_validator = RegexValidator(
    regex=r"^[A-Z]{2}-\d{4}$",
    message="Артикул має формат AB-1234.",
    code="invalid_article",
)

def validate_article(value):
    if not value:
        return

    if len(value) != 7 or value[2] != "-":
        raise ValidationError(
            "Артикул повинен містити дві літери, дефіс і чотири цифри.",
            code="invalid_article_length",
            params={"value": value},
        )

    prefix, number = value.split("-", 1)

    if not prefix.isalpha() or not prefix.isascii() or not prefix.isupper():
        raise ValidationError(
            "Префікс артикулу має складатися з двох великих латинських літер.",
            code="invalid_article_prefix",
            params={"value": value},
        )

    if len(number) != 4 or not number.isdigit():
        raise ValidationError(
            "Після дефіса артикул повинен містити чотири цифри.",
            code="invalid_article_number",
            params={"value": value},
        )
