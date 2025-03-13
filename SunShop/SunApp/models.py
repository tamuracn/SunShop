from django.db import models

# Create your models here.
"""
Everytime you make changes to the models.py file, you need to run the following commands into terminal:
python manage.py makemigrations
python manage.py migrate

"""
class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    # content = models.TextField()
    # date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.content

