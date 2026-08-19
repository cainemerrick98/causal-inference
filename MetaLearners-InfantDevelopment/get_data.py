import numpy as np
import requests
from io import BytesIO
from sklearn.utils import Bunch

IHDP_URLS = {
    "train": "https://www.fredjo.com/files/ihdp_npci_1-100.train.npz",
    "test": "https://www.fredjo.com/files/ihdp_npci_1-100.test.npz",
}

def fetch_ihdp_data(split="train", replication=0):
    """
    Fetches the Infant Health and Development Program (IHDP) dataset.

    Parameters:
        split (str): The dataset split to fetch. Can be either "train" or "test".
        replication (int): The replication index to fetch.

    Returns:
        X (np.ndarray): The feature matrix.
        y (np.ndarray): The outcome variable.
        w (np.ndarray): The treatment assignment.
    """
    if split not in IHDP_URLS:
        raise ValueError(f"Invalid split '{split}'. Must be 'train' or 'test'.")

    url = IHDP_URLS[split]
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    with np.load(BytesIO(response.content), allow_pickle=True) as npz:
        # every array indexes the replication on its last axis
        x = npz["x"][:, :, replication]
        t = npz["t"][:, replication]
        yf = npz["yf"][:, replication]
        ycf = npz["ycf"][:, replication]
        mu0 = npz["mu0"][:, replication]
        mu1 = npz["mu1"][:, replication]

    # Create a Bunch object to hold the data
    return Bunch(
        data=x.astype(float),
        target=yf.astype(float),
        treatment=t.astype(int),
        tau=(mu1 - mu0).astype(float),
        mu0=mu0.astype(float),
        mu1=mu1.astype(float),
        y_cf=ycf.astype(float),
        feature_names=[f"x{i}" for i in range(x.shape[1])],
        replication=replication,
        DESCR=fetch_ihdp_data.__doc__,
    )

    
   

    return X, y, w



if __name__ == "__main__":
    # Example usage
    data_train = fetch_ihdp_data(split="train")
    data_test = fetch_ihdp_data(split="test")

    print("Train data shapes:", data_train.data.shape, data_train.target.shape, data_train.treatment.shape)
    print("Test data shapes:", data_test.data.shape, data_test.target.shape, data_test.treatment.shape)