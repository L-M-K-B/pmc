from io import StringIO
from geopy.geocoders import ArcGIS
import pandas


def add_data_geo_data(content, file_name):
    df = pandas.read_csv(content)

    loc = ArcGIS()
    try:
        df["Coordinates"] = df["Address"].apply(loc.geocode)
    except KeyError:
        try:
            df["Coordinates"] = df["address"].apply(loc.geocode)
        except KeyError:
            return None, None

    df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x else None)
    df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x else None)
    del df["Coordinates"]

    html_table = df.to_html(index=False)

    new_file_name = f'{file_name.split(".csv")[0]} - updated.csv'
    df.to_csv(f'converted_files/{new_file_name}', index=False)

    return new_file_name, html_table


def process_content(original_file):
    file_name = original_file.filename

    original_content = StringIO(original_file.stream.read().decode("utf-8"))

    return add_data_geo_data(original_content, file_name)

