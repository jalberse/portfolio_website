from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.text import slugify

from colorfield.fields import ColorField

class ResumeItem(models.Model):
    title = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    start_date = models.DateField()
    # Null iff currently employed there
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class Bullet(models.Model):
    """
    Bullet point for a resume
    """
    text = models.TextField()
    item = models.ForeignKey(ResumeItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class CodingProject(models.Model):
    """
    Details of a coding project
    """
    title = models.CharField(max_length=256)
    tagline = models.CharField(max_length=256)
    technologies = models.TextField()
    project_link = models.CharField(max_length=256)
    project_link_display_text = models.CharField(max_length=256)
    text = models.TextField()
    
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Gallery(models.Model):
    """
    A gallery with images, gifs, movie files
    """
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Media(models.Model):
    """
    An image, gif to be displayed in a Post or a Gallery
    """
    media = models.ImageField(upload_to="images")
    alttext = models.CharField(max_length=256)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    coding_project = models.ForeignKey(CodingProject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.alttext

class Embed(models.Model):
    """
    Src for an embedded video
    """
    src = models.CharField(max_length=256)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.src