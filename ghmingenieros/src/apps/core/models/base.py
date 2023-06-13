import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models


class BaseModelMixin(models.Model):
    """ """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    updated_at = models.DateTimeField(editable=False, auto_now=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CustomWebPage(BaseModelMixin):
    phone_number = models.CharField(
        max_length=150, blank=True, verbose_name=_("Phone Number")
    )
    phone_number_two = models.CharField(
        max_length=150, blank=True, verbose_name=_("Phone Number Two")
    )
    email = models.CharField(
        max_length=200, blank=True, verbose_name=_("Email")
    )
    address = models.CharField(
        max_length=500, blank=True, verbose_name=_("Direccion")
    )
    company_name = models.CharField(
        max_length=150, blank=True, verbose_name=_("Company Name")
    )
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return "{}".format(self.company_name)

    class Meta:
        verbose_name = _("CustomWebPage")
        verbose_name_plural = _("CustomWebPages")