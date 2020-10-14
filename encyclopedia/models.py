from django.db import models

# Create your models here.
class newPage(models.Model):
    title = models.CharField(max_length=120, unique=True, error_messages={"unique": "This title is not unique", "blank": "This field has not to be blank"}, help_text="Must be a unique title"),
    content = models.TextField(max_length=200, blank=False),
    