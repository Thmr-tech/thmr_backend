from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(_("الإسم الرباعي"), max_length=255)
    national_id = models.CharField(
        _("رقم الهوية"),
        max_length=255,
        unique=True,
        validators=[RegexValidator(
            r'^\d{10}$', 'National ID must be exactly 10 digits.')]
    )
    telephone = models.CharField(
        _("رقم الهاتف"),
        max_length=255,
        unique=True,
        validators=[RegexValidator(
            r'^\d{10}$', 'Telephone must be exactly 10 digits.')]
    )
    family_funds_box_number = models.CharField(_("رقم الصندوق"), max_length=255, unique=True)
    family_funds_box_name = models.CharField(_("اسم الصندوق"), max_length=255, blank=True, null=True)
    family_funds_regulations = models.FileField(_(" اللائحة الاساسية للصندو"), upload_to='regulations/', blank=True, null=True)
    signup_type = models.CharField(max_length=10)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'national_id', 'telephone', 'family_funds_box_number', 'family_funds_box_name', 'family_funds_regulations', 'signup_type']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.family_funds_box_name}"

