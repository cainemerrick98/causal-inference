import requests
from zipfile import ZipFile
from io import BytesIO
import pandas as pd

def get_data(file_name: str):
    url = "https://economics.mit.edu/sites/default/files/inline-files/Lee2008%20%281%29.zip"
    response = requests.get(url)
    with ZipFile(BytesIO(response.content)) as zip_file:
        with zip_file.open(f"Lee2008/{file_name}") as data_file:
            if file_name.endswith(".dta"):
                data = pd.read_stata(data_file)
            elif file_name.endswith(".txt") or file_name.endswith(".do"):
                data = data_file.read().decode('utf-8')
    return data


if __name__ == "__main__":
    df = get_data("individ_final.dta")
    print(df.head())
    readme = get_data("readme.txt")
    print(readme)
    public_use = get_data("public_use.do")
    print(public_use)
