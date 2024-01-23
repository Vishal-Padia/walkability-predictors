import logging
import pandas as pd

from zenml import step


class IngestData:
    """
    Data Ingestion class which ingests the data from the source and returns a DataFrame
    """

    def __init__(self, data_path: str):
        """
        Args:
            data_path : Path to the data
        """
        self.data_path = data_path

    def get_data(self):
        """
        Ingesting data from the data path
        """
        logging.info(f"Ingesting the data from the {self.data_path}")
        return pd.read_csv(self.data_path)


@step
def ingest_df(data_path: str) -> pd.DataFrame:
    """
    Ingesting data from the data path

    Args:
        data_path: Path to the data

    Returns:
        pd.DataFrame: The ingested data in the DataFrame format
    """
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting the data {e}")
        raise e
