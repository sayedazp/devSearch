from django.db import models
from devsearch.basemodel import Base_model as BM
from users.models import Profile
# Create your models here.

class Project(BM):
    owner = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Review(BM):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=2000, null=True, blank=True, choices=VOTE_TYPE)

    def __str__(self) -> str:
        return self.value

class Tag(BM):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
