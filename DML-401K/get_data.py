import pandas as pd

def fetch_401k_data():
    """
    Fetches 401k data from the database.
    """
    url = "https://github.com/VC2015/DMLonGitHub/raw/master/sipp1991.dta"
    df = pd.read_stata(url)

    return df



if __name__ == "__main__":
    data = fetch_401k_data()
    print(data.head())




