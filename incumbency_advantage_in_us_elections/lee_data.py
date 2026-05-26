import requests
from zipfile import ZipFile
from io import BytesIO
import pandas as pd

def get_data():
    url = "https://economics.mit.edu/sites/default/files/inline-files/Lee2008%20%281%29.zip"
    response = requests.get(url)
    with ZipFile(BytesIO(response.content)) as zip_file:
        with zip_file.open("Lee2008/individ_final.dta") as data_file:
            df = pd.read_stata(data_file)
    return df


if __name__ == "__main__":
    df = get_data()
    print(df.head())
