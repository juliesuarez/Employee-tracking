from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Fruit(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', null=False, blank=False, default='image')
    description = models.TextField(max_length=1000, null=False, default='Describe the fruit', blank=False)
    created_at = models.DateField(default='YY-MM-DD')
    updated_at = models.DateField(default='YY-MM-DD')      

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(default='YY-MM-DD')

class EducationDetail(models.Model):
    profile = models.ImageField(upload_to="images")
    level_of_education = models.CharField(max_length=100,null=False,blank=False)
    year_of_graduation = models.DateField(default="YY-MM-DD")
    field_of_study = models.CharField(max_length=100,null=False,blank=False)
    grade = models.CharField(max_length=50,null=False,blank=False)
    transcript = models.FileField(upload_to='files')
    additional_feedback = models.TextField()

    def __str__(self):
        return self.grade

class Manage(models.Model):
    name_of_car = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=50)
    color_of_car = models.CharField(max_length=50)
    ownership = models.CharField(max_length=100)
    name_of_driver = models.CharField(max_length=50)

    def __str__(self):
        return self.color_of_car

class Club(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clubs')
    field_name = models.CharField(max_length=100)
    field_value_of_fans = models.IntegerField(default=0)
    league_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="profile")
    date_of_birth = models.DateField(default="YY-MM-DD")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    hire_date = models.DateField(default="YY-MM-DD")
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="profile")
    date_of_birth = models.DateField(default="YY-MM-DD")
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(default="YY-MM-DD")
    end_date = models.DateField(default="YY-MM-DD")

    def __str__(self):
        return self.name
    

class Module(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField(default="YY-MM-DD")
    end_date = models.DateField(default="YY-MM-DD")

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=200)
    file_type = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# class GenericUser(AbstractUser):
#     email = models.EmailField()
#     USERNAME_FIELD = 'email'
#     phone_number = PhoneNumberField()
class GenericUser(AbstractUser):
    email = models.EmailField()
    USERNAME_FIELD = 'email'
    phone_number = PhoneNumberField()
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='genericuser_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='genericuser_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
