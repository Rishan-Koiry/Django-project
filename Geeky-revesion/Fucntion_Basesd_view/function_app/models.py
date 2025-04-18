from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)  # Adding the 'deleted' field for soft delete

    def __str__(self):
        return self.name
