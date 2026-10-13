from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "article",
            "description",
            "price",
            "weight",
            "production_date",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "article": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),
            "weight": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),
            "production_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }

        labels = {
            "title": "Назва товару",
            "article": "Артикул",
            "description": "Опис товару",
            "price": "Ціна (грн)",
            "weight": "Вага (кг)",
            "production_date": "Дата виробництва",
        }

        help_texts = {
            "title": "Введіть назву товару.",
            "article": "Формат: AB-1234.",
            "description": "Опишіть основні характеристики товару.",
            "price": "Вкажіть ціну, більшу за 0.",
            "weight": "Вкажіть вагу в кілограмах.",
            "production_date": "Виберіть дату виробництва.",
        }

    def clean_article(self):
        article = self.cleaned_data.get("article", "")
        return article.strip().upper()
