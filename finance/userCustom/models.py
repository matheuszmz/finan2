import re

from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=15, unique=True,
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                      _('Enter a valid username.'), _('invalid'))])
    name = models.CharField(_('name'), max_length=60)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    birthday = models.DateField(_('Data de Aniversário'))
    cellphone = models.CharField(_('Celular'), max_length=15,
                                 validators=[validators.RegexValidator(re.compile('(\(\d{2}\)\s)(\d{5}\-\d{4})'),
                                                                       _('Enter a valid cellphone.'), _('invalid'))])
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the userCustom can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_(
                                        'Designates whether this userCustom should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False,
                                    help_text=_('Designates whether this userCustom has confirmed his account.'))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'birthday', 'cellphone']
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.name

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
