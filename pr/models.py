from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=50, default="")
    deadline = models.DateField(default="YYYY-MM-DD")
    status = models.CharField(max_length=20, default='in-progress')
    assigned_to = models.ForeignKey( Employee, on_delete=models.CASCADE ,default="")
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name


