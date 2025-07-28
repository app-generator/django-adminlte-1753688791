# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customer(models.Model):

    #__Customer_FIELDS__
    kode pelanggan = models.CharField(max_length=255, null=True, blank=True)
    jenis badan usaha = models.CharField(max_length=255, null=True, blank=True)
    nama pelanggan = models.CharField(max_length=255, null=True, blank=True)
    alamat pelanggan = models.TextField(max_length=255, null=True, blank=True)
    kontak pelanggan = models.CharField(max_length=255, null=True, blank=True)
    npwp pelanggan = models.IntegerField(null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Customer Address(models.Model):

    #__Customer Address_FIELDS__
    kode pelanggan = models.ForeignKey(Customer, on_delete=models.CASCADE)
    alamat pelanggan - 1 = models.TextField(max_length=255, null=True, blank=True)
    alamat pelanggan - 2 = models.TextField(max_length=255, null=True, blank=True)
    alamat pelanggan - 3 = models.TextField(max_length=255, null=True, blank=True)
    alamat pelanggan - 4 = models.TextField(max_length=255, null=True, blank=True)
    alamat pelanggan - 5 = models.TextField(max_length=255, null=True, blank=True)
    alamat pelanggan - 6 = models.TextField(max_length=255, null=True, blank=True)

    #__Customer Address_FIELDS__END

    class Meta:
        verbose_name        = _("Customer Address")
        verbose_name_plural = _("Customer Address")



#__MODELS__END
