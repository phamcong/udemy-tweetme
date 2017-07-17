from django.conf import settings
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db import models
from .validators import validate_content
# Create your models here.

class Tweet(models.Model):
    # add user
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    content     = models.CharField(max_length=140, validators=[validate_content]) # max_length of a tweet post or message.
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk":self.pk})

    def __str__(self):
        return str(self.content)

    # This validation function works but the error doesnt appear at the field containing errors.
    # We define inline validation function for each field of form.
    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == 'abc':
    #         raise ValidationError("Cannot be ABC")
    #     return super(Tweet, self).clean(*args, **kwargs)
