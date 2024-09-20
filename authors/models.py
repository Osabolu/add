from django.db import models
# from authors.models import Author

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"