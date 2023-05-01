from django.db import models
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=250, unique=True, help_text="FAQ")
    answer_text = models.TextField(help_text="Answer to the FAQ")
    list_position = models.AutoField(unique=True, primary_key=True, help_text="The position in the list")
    tags = TaggableManager(_("Tags"), help_text=_("A comma-separated list of tags"))

    def __str__(self):
        return self.question_text
    
    class Meta:
        ordering = ['list_position']
 
