# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

import uuid
import random
import string

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, Permission, Group)
from .managers import UserManager
from django.db import models

#from baseapp.models import BaseModel

class User(AbstractBaseUser, PermissionsMixin):
	
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_artist = models.BooleanField(
        _('artist status'),
        default=False,
        help_text=_(
            'Designates whether this user can be a store/business name.'),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('last login'), default=timezone.now)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    is_email_verified = models.BooleanField(default=False)
    is_password_changed = models.BooleanField(default=False)
    is_phone_number_verified = models.BooleanField(default=False)
    profile_photo = models.ImageField(
        upload_to='profile_photos/%Y/%m/%d/', null=True)


    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return ('%s %s' % (self.first_name, self.last_name)).strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name
    
    def get_user_stores(self):
        "return all stores created by user"
        return self.stores.filter(manager_fk=self.id)

    def get_user_account(self):
        "return all accounts related to user"
        return self.bank_acount.all()