from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The email must be set")
        if not password:
            raise ValueError("The password must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_adminuser(self, email, password,**extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_verified', True)

        return self.create_user(email, password, **extra_fields)



    def create_superuser(self, email, password, **extra_fields):

        # if not email.endswith('@prabhubank.com'):
        #     raise ValueError("Only @prabhubank.com email addresses allowed")

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_verified', True)


        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    """
    Models for users
    """

    GENDER_TYPE = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    )

    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=255, blank=True)
    contact_number = models.CharField(validators=[MinLengthValidator(7)], max_length=10, null=True, unique=True)
    gender=models.CharField(max_length=50, choices=GENDER_TYPE,null=True)
    dob=models.DateField(null=True)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)


    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.fullname

    def get_short_name(self):
        return self.fullname

    def has_perm(self, perm, obj=None):
        # import pdb;pdb.set_trace()
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

    # class Meta:
    #     permissions=[
    #         ('create_user','Can create a user'),
    #         ('list_user','Can list all the user'),
    #         ('update_user','Can update detail of all user'),
    #         ('delete_users','Can delete any user')
    #     ]
