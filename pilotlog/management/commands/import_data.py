from datetime import datetime

from django.core.management.base import BaseCommand

from pilotlog.models import (Aircraft, Airfield, Flight, ImagePic, LimitRules,
                             MyQuery, MyQueryBuild, Pilot, Qualification,
                             SettingConfig)
from pilotlog.utils import parse_json_file


class Command(BaseCommand):
    help = "Import pilot log data from JSON file"

    def handle(self, *args, **kwargs):
        model_names = {
            "settingconfig": SettingConfig,
            "pilot": Pilot,
            "qualification": Qualification,
            "aircraft": Aircraft,
            "myquerybuild": MyQueryBuild,
            "airfield": Airfield,
            "flight": Flight,
            "myquery": MyQuery,
            "limitrules": LimitRules,
            "imagepic": ImagePic,
        }

        data = parse_json_file()

        for item in data:
            model_name = item["table"].lower()
            model = model_names[model_name]

            if model_name == "flight":
                # Since guid == AirCraftCode in .json file.
                guid = item["meta"]["AircraftCode"]
                item["aircraft"] = Aircraft.objects.get(guid=guid)

            item["_modified"] = datetime.fromtimestamp(item["_modified"])
            model.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Successfully imported pilot log data"))
