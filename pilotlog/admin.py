from django.contrib import admin

from pilotlog.models import (Aircraft, Airfield, Flight, ImagePic, LimitRules,
                             MyQuery, MyQueryBuild, Pilot, Qualification,
                             SettingConfig)


@admin.register(SettingConfig)
class SettingConfigAdmin(admin.ModelAdmin):
    list_display = ["id", "guid", "created"]


@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = ["id", "guid", "created"]


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ["id", "guid", "created"]


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ["id", "guid", "created"]


@admin.register(MyQueryBuild)
class MyQueryBuildAdmin(admin.ModelAdmin):
    list_display = ["id", "guid", "created"]


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ["id", "guid", "created"]


@admin.register(Airfield)
class AirfieldAdmin(admin.ModelAdmin):
    list_display = ["id", "guid", "created"]


@admin.register(MyQuery)
class MyQueryAdmin(admin.ModelAdmin):
    list_display = ["id", "guid", "created"]


@admin.register(LimitRules)
class LimitRulesAdmin(admin.ModelAdmin):
    list_display = ["id", "guid", "created"]


@admin.register(ImagePic)
class ImagePicAdmin(admin.ModelAdmin):
    list_display = ["id", "guid", "created"]
