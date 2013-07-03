from django.db import models
from cms.models import CMSPlugin

class CodeArea(CMSPlugin):
    codefield = models.TextField(verbose_name="Text")
