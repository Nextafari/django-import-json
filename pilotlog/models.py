from django.db import models

from django.db.models import Count
from django.db.models.functions import TruncDate


def default_json():
    return {'data': None}


class ImagePic(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    meta = models.JSONField(default=default_json)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.IntegerField()
    _modified = models.DateTimeField()


class SettingConfig(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    meta = models.JSONField(default=default_json)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.IntegerField()
    _modified = models.DateTimeField()


class Pilot(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    meta = models.JSONField(default=default_json)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.IntegerField()
    _modified = models.DateTimeField()


class Qualification(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    meta = models.JSONField(default=default_json)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.IntegerField()
    _modified = models.DateTimeField()


class Aircraft(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    meta = models.JSONField(default=default_json)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.IntegerField()
    _modified = models.DateTimeField()

    def aircraft_stats(self):
        data = (
            self
            .annotate(date=TruncDate('_modified'))
            .values('date')
            .annotate(total_aircrafts=Count('id'))
            .values('date', 'total_aircrafts')
            .annotate(no_of_model=Count('meta__Model'))
            .values('date', 'total_aircrafts', 'no_of_model', 'meta__Model')
        )
        return data


class MyQueryBuild(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    meta = models.JSONField(default=default_json)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.IntegerField()
    _modified = models.DateTimeField()


class Flight(models.Model):
    user_id = models.IntegerField()
    aircraft = models.ForeignKey(to='Aircraft', on_delete=models.CASCADE)
    table = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    meta = models.JSONField(default=default_json)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.IntegerField()
    _modified = models.DateTimeField()


class Airfield(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    meta = models.JSONField(default=default_json)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.IntegerField()
    _modified = models.DateTimeField()


class MyQuery(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    meta = models.JSONField(default=default_json)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.IntegerField()
    _modified = models.DateTimeField()


class LimitRules(models.Model):
    user_id = models.IntegerField()
    table = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    meta = models.JSONField(default=default_json)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.IntegerField()
    _modified = models.DateTimeField()
