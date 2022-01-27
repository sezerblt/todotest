from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class TodoModel(models.Model):
    title =   models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
