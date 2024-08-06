import json

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
                "Sea": false,
                "TMG": false,
                "Efis": false,
                "FNPT": 0,
                "Make": "Cessna",
                "Run2": false,
                "Class": 5,
                "Model": "C150",
                "Power": 1,
                "Seats": 0,
                "Active": true,
                "Kg5700": false,
                "Rating": "",
                "Company": "Other",
                "Complex": false,
                "CondLog": 69,
                "FavList": false,
                "Category": 1,
                "HighPerf": false,
                "SubModel": "",
                "Aerobatic": false,
                "RefSearch": "PHALI",
                "Reference": "PH-ALI",
                "Tailwheel": false,
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
        self.aircraft = Aircraft.objects.create(**aircraft_data)

    def test_dynamic_view(self):
        params = "?fields=id,guid,create,_modified"
        url = f"/pilotlog/aircraft/{params}"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)

        # Check for status, message and data keys in response.
        self.assertEqual(len(response.json()), 3)

        # Confirm fields requested were returned.
        self.assertIn("id", response.json()["data"])
        self.assertIn("guid", response.json()["data"])
        self.assertIn("create", response.json()["data"])
        self.assertIn("_modified", response.json()["data"])

    def test_aircraft_stats(self):
        url = "/pilotlog/aircraft/stats"
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, 200)

        # Check for status, message and data keys in response.
        self.assertEqual(len(response.json()), 3)

        # Confirm fields requested were returned.
        self.assertEqual(list, response.json()["data"])
        self.assertIn("meta__model", response.json()["data"][0])
        self.assertIn("date", response.json()["data"][0])
        self.assertIn("no_of_model", response.json()["data"][0])


class TestParseJSONFile(APITestCase):
    def test_connect_account_error(self):
        parsed_data = parse_json_file()

        self.assertEqual(parsed_data, json)
        self.assertEqual(parsed_data, list)
        self.assertEqual(parsed_data[0], dict)
