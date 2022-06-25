"""
This is an example validation for bad words to be entered when filling a db table (in this case the ORM)
"""
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()
BAD_WORDS = ["punk", "java", "waterfall", "ass"]


def validate_no_bad_words(content):
    if any([word in content.lower() for word in BAD_WORDS]):
        raise ValidationError("This post contains bad words!")


class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, validators=[validate_no_bad_words])
    created_on = models.DateTimeField("date created", auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.content[0:20]}"
