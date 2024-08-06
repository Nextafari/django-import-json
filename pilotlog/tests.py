from datetime import datetime

from rest_framework.test import APITestCase

from pilotlog.models import Aircraft
from pilotlog.utils import parse_json_file


class AirCraftTestCases(APITestCase):
    def setUp(self):
        aircraft_data = {
            "user_id": 125800,
            "table": "Aircraft",
            "guid": "00000000-0000-0000-0000-000000000367",
            "meta": {
                "Fin": "",
                "Sea": False,
                "TMG": False,
                "Efis": False,
                "FNPT": 0,
                "Make": "Cessna",
                "Run2": False,
                "Class": 5,
                "Model": "C150",
                "Power": 1,
                "Seats": 0,
                "Active": True,
                "Kg5700": False,
                "Rating": "",
                "Company": "Other",
                "Complex": False,
                "CondLog": 69,
                "FavList": False,
                "Category": 1,
                "HighPerf": False,
                "SubModel": "",
                "Aerobatic": False,
                "RefSearch": "PHALI",
                "Reference": "PH-ALI",
                "Tailwheel": False,
                "DefaultApp": 0,
                "DefaultLog": 2,
                "DefaultOps": 0,
                "DeviceCode": 1,
                "AircraftCode": "00000000-0000-0000-0000-000000000367",
                "DefaultLaunch": 0,
                "Record_Modified": 1616320991,
            },
            "platform": 10,
            "_modified": 1616320991,
        }
        aircraft_data["_modified"] = datetime.fromtimestamp(aircraft_data["_modified"])
        self.aircraft = Aircraft.objects.create(**aircraft_data)

    def test_dynamic_view(self):
        params = "?fields=id,guid,created,_modified"
        url = f"/pilotlog/aircraft/{params}"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)

        # Check for status, message and data keys in response.
        self.assertEqual(len(response.json()), 3)

        # Confirm fields requested were returned.
        self.assertIn("id", response.json()["data"][0])
        self.assertIn("guid", response.json()["data"][0])
        self.assertIn("created", response.json()["data"][0])
        self.assertIn("_modified", response.json()["data"][0])

    def test_aircraft_stats(self):
        url = "/pilotlog/aircraft/stats/"
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, 200)

        # Check for status, message and data keys in response.
        self.assertEqual(len(response.json()), 3)

        # Confirm fields requested were returned.
        self.assertEqual(list, type(response.json()["data"]))
        self.assertIn("meta__Model", response.json()["data"][0])
        self.assertIn("date", response.json()["data"][0])
        self.assertIn("no_of_model", response.json()["data"][0])


class TestParseJSONFile(APITestCase):
    def test_connect_account_error(self):
        parsed_data = parse_json_file()

        self.assertEqual(list, type(parsed_data))
        self.assertEqual(dict, type(parsed_data[0]))
