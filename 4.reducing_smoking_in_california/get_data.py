import pandas as pd
 
_URL = (
    "https://raw.githubusercontent.com/matheusfacure/"
    "python-causality-handbook/master/"
    "causal-inference-for-the-brave-and-true/data/smoking.csv"
)
 
# The source CSV encodes states as integer codes (alphabetical among the
# 39 states in the study). Verified against the tidysynth `smoking` data.
_STATE_NAMES = {
    1: "Alabama", 2: "Arkansas", 3: "California", 4: "Colorado",
    5: "Connecticut", 6: "Delaware", 7: "Georgia", 8: "Idaho",
    9: "Illinois", 10: "Indiana", 11: "Iowa", 12: "Kansas",
    13: "Kentucky", 14: "Louisiana", 15: "Maine", 16: "Minnesota",
    17: "Mississippi", 18: "Missouri", 19: "Montana", 20: "Nebraska",
    21: "Nevada", 22: "New Hampshire", 23: "New Mexico",
    24: "North Carolina", 25: "North Dakota", 26: "Ohio",
    27: "Oklahoma", 28: "Pennsylvania", 29: "Rhode Island",
    30: "South Carolina", 31: "South Dakota", 32: "Tennessee",
    33: "Texas", 34: "Utah", 35: "Vermont", 36: "Virginia",
    37: "West Virginia", 38: "Wisconsin", 39: "Wyoming",
}
 
 
def load_smoking(url: str = _URL) -> pd.DataFrame:
    """Download and return the Prop 99 smoking panel as a DataFrame."""
    df = pd.read_csv(url)
    df["state"] = df["state"].map(_STATE_NAMES)
    df["year"] = df["year"].astype(int)
    return df.sort_values(["state", "year"]).reset_index(drop=True)