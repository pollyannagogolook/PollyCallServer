from django.db import models
from django.urls import reverse

# Create your models here.


class Number(models.Model):
    """A typical class defining a model, derived from the Model class"""

    # Fields
    number = models.CharField(
        max_length=10,
        unique=True,
        help_text="請輸入陌生號碼"
    )

    number_owner = models.CharField(
        max_length=30,
        help_text="是誰來電？"
    )

    should_reject = models.BooleanField(
        help_text="是否該拒接"
    )

    # Metadata: default ordering when returns data

    class Metadata:
        ordering = ["number_field", "number_owner"]

    # Methods
        # get_absolute_info: return url from a personal model's record

    def get_absolute_info(self):
        """Returns the number to access particular instance of NumberModel"""
        return reverse("number_detail", args=[self.id])

        # __str__: return a readable string
    def __str__(self):
        return self.number_owner
