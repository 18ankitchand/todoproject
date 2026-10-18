from django.db import models


# Create your models here.

# class Users(models.Model):
#     name= models.CharField(_(""), max_length=50)
#     email = models.EmailField(unique=True, max_length=254)






class Task(models.Model):
    title=models.CharField()
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return str(self.title)

