from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyOfficialsManager(BaseUserManager):
    def create_user(self, username, position, firstname, middlename, lastname, purok, contact, email, password=None):
        if not username:
            raise ValueError('Username is required')
        if not position:
            raise ValueError('Position is required')
        if not firstname:
            raise ValueError('First name is required')
        if not lastname:
            raise ValueError('Last name is required')
        if not purok:
            raise ValueError('Purok is required')
        if not contact:
            raise ValueError('Contact is required')

        user = self.model(
            username=username,
            position=position,
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            purok=purok,
            contact=contact,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, position, firstname, middlename, lastname, purok, contact, email, password):
        user = self.create_user(
            username=username,
            position=position,
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            purok=Purok.objects.get(id=purok),
            contact=contact,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Purok(models.Model):
    name = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name


class Official(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    position = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255)

    purok = models.ForeignKey(
        Purok, null=True, on_delete=models.SET_NULL)
    contact = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True, null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['position', 'firstname', 'middlename',
                       'lastname', 'purok', 'contact', 'email']

    objects = MyOfficialsManager()

    def __str__(self):
        return '(' + self.position + ') ' + self.firstname

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Resident(models.Model):
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255)

    purok = models.ForeignKey(
        Purok, null=True, on_delete=models.SET_NULL)
    contact = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.lastname + ', ' + self.firstname


class Case(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.resident.lastname + ', ' + self.resident.firstname


class Post(models.Model):
    official = models.ForeignKey(Official, on_delete=models.CASCADE)
    hashtag = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return '(#' + self.hashtag + ') by ' + self.official.position + ' ' + self.official.firstname


class Request(models.Model):
    type = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, default='pending')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return '(' + self.type + ') ' + self.full_name
