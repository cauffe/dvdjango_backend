from django.db import models

#cassandra imports
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# Create your models here.
class MovieCas(Model):
    uu_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title = columns.Text(required=False)
    sql_id = columns.Integer(required=False)


class Movie(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    status = models.CharField(null=True, blank=True, max_length=255)
    price = models.CharField(null=True, blank=True, max_length=255)
    rating = models.CharField(null=True, blank=True, max_length=255)
    release = models.DateTimeField(null=True, blank=True)
    genre = models.ForeignKey('main.Genre', null=True, blank=True)
    studio = models.ForeignKey('main.Studio', null=True, blank=True)

    def __unicode__(self):
        return self.title


class Genre(models.Model):
    genre = models.CharField(null=True, blank=True, max_length=255)


class Studio(models.Model):
    studio = models.CharField(null=True, blank=True, max_length=255)
