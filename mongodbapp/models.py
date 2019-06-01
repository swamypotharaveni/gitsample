from django.db import models

class Student(models.Model):
    Name=models.CharField(max_length=20)
    age=models.IntegerField()
    addres=models.TextField()

    def __str__(self):
        return self.Name

