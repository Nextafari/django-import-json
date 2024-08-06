import csv
import json
from pathlib import Path
from typing import List, Dict


def read_json_file() -> List[Dict]:
    file_path = Path('./import - pilotlog_mcc.json')

    # replace escape sequence from data to handle
    # json.decoder.JSONDecodeError: Expecting property name
    # enclosed in double quotes: line 1 column 3 (char 2)
    line_data = file_path.read_text().replace("\\", "")

    data = json.loads(line_data)

    return data


def export_csv(
                aircraft_queryset,
                flight_queryset,
                *args, **kwargs):

    first_header = ['ForeFlight Logbook Import']
    aircraft_title = ['Aircraft Table']
    aircraft_data_types = [
        'Text', 'Text', 'Text', 'YYYY', 'Text', 'Text', 'Text',
        'Text', 'Text', 'Text', 'Boolean', 'Boolean', 'Boolean', 'Boolean']
    aircraft_headers = [
        'AircraftCode', 'EquipmentType', 'TypeCode', 'Year', 'Make',
        'Model', 'Category', 'Class', 'GearType', 'EngineType', 'Complex',
        'HighPerformance', 'Pressurized', 'TAA']

    flight_title = ['Flight Table']
    flight_data_types = [
        'Date', 'Text', 'Text', 'Text', 'Text', 'hhmm', 'hhmm', 'hhmm', 'hhmm',
        'hhmm', 'hhmm', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Decimal',
        'Decimal', 'Decimal', 'Number', 'Decimal', 'Number', 'Number', 'Number',
        'Number', 'Number', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Decimal',
        'Decimal', 'Number', 'Packed Detail', 'Packed Detail', 'Packed Detail',
        'Packed Detail', 'Packed Detail', 'Packed Detail', 'Decimal', 'Decimal',
        'Decimal', 'Decimal', 'Text', 'Text', 'Packed Detail', 'Packed Detail',
        'Packed Detail', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Boolean',
        'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Text', 'Decimal', 'Decimal',
        'Number', 'Date', 'DateTime', 'Boolean', 'Text']
    flight_headers = [
        'Date', 'AircraftCode', 'From', 'To', 'Route', 'TimeOut', 'TimeOff',
        'TimeOn', 'TimeIn', 'OnDuty', 'OffDuty', 'TotalTime', 'PIC', 'SIC',
        'Night', 'Solo', 'CrossCountry', 'NVG', 'NVGOps', 'Distance',
        'DayTakeoffs', 'DayLandingsFullStop', 'NightTakeoffs', 'NightLandingsFullStop',
        'AllLandings', 'ActualInstrument', 'SimulatedInstrument', 'HobbsStart',
        'HobbsEnd', 'TachStart', 'TachEnd', 'Holds', 'Approach1', 'Approach2',
        'Approach3', 'Approach4', 'Approach5', 'Approach6', 'DualGiven', 'DualReceived',
        'SimulatedFlight', 'GroundTraining', 'InstructorName', 'InstructorComments',
        'Person1', 'Person2', 'Person3', 'Person4', 'Person5', 'Person6', 'FlightReview',
        'Checkride', 'IPC', 'NVGProficiency', 'FAA6158', '[Text]CustomFieldName',
        '[Numeric]CustomFieldName', '[Hours]CustomFieldName', '[Counter]CustomFieldName',
        '[Date]CustomFieldName', '[DateTime]CustomFieldName', '[Toggle]CustomFieldName',
        'PilotComments']

    file_path = Path('./export - logbook_template.csv')

    with file_path.open('w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(first_header)
        writer.writerow([])

        writer.writerow(aircraft_title)
        writer.writerow(aircraft_data_types)
        writer.writerow(aircraft_headers)

        # ==================== AIRCRAFT ==================== #
        aircraft_data = aircraft_queryset.values('meta')
        for data in aircraft_data:
            writer.writerow(
                [data['meta'].get(col) for col in aircraft_headers]
            )

        writer.writerow([])
        writer.writerow([])
        writer.writerow([])
        writer.writerow([])

        # ==================== END AIRCRAFT ==================== #

        # ==================== FLIGHT ==================== #

        writer.writerow(flight_title)
        writer.writerow(flight_data_types)
        writer.writerow(flight_headers)

        flight_data = flight_queryset.values('meta')
        for data in flight_data:
            writer.writerow(
                [data['meta'].get(col) for col in aircraft_headers]
            )

        # ==================== END FLIGHT ==================== #
    return 'all done!!!'
