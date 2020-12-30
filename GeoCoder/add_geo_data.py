from io import StringIO
from geopy.geocoders import ArcGIS
import pandas


def add_data(content, file_name):
    df = pandas.read_csv(content)

    loc = ArcGIS()
    # TODO: make sure to enable lower case for "Address" --> does solution below work?
    df["Coordinates"] = df["Address" or "address"].apply(loc.geocode)
    df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x else None)
    df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x else None)
    del df["Coordinates"]
    print(df)
    # TODO: transfer from df to csv works, but the file is being saved rather than being returned
    file = df.to_csv('update.csv', index=False)

    return file


def process_content(original_file):
    file_name = original_file.filename

    original_content = StringIO(original_file.stream.read().decode("utf-8"))

    return add_data(original_content, file_name)


# loc = ArcGIS()
# a = loc.geocode("3666 21st, St San Francisco, CA 94114 USA")
# print("a", a.latitude, a.longitude)
#
# b = loc.geocode("3666 21st St San Francisco CA 94114 USA")
# print("b", b.latitude, b.longitude)

# df = pandas.read_csv("example.csv")
# print(df)
# df["Coordinates"] = df["Address" or "address"].apply(loc.geocode)
# df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x else None)
# df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x else None)
# del df["Coordinates"]
# print(df.Coordinates)
