from sqlalchemy import create_engine, text
import logging
import pandas as pd

# Name our logger so we know that logs from this module come from the data_ingestion module
logger = logging.getLogger('data_ingestion')

# Set a basic logging message up that prints out a timestamp, the name of our logger, and the message
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#config_params: central place where we store all of the specific details of the data pipeline
config_params = {
    "sql_query": """
SELECT *
FROM geographic_features
LEFT JOIN weather_features USING (Field_ID)
LEFT JOIN soil_and_crop_features USING (Field_ID)
LEFT JOIN farm_management_features USING (Field_ID)
            """, 
    "db_path": 'sqlite:///Maji_Ndogo_farm_survey_small.db', 
    "columns_to_rename": {'Annual_yield': 'Crop_type', 'Crop_type': 'Annual_yield'},
    "values_to_rename": {'cassaval': 'cassava', 'wheatn': 'wheat', 'teaa': 'tea'}, 
    "weather_mapping_csv":"https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/Weather_data_field_mapping.csv",
    "weather_csv_path": "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Maji_Ndogo/Weather_station_data.csv",
    "regex_patterns" :{
        'Rainfall': r'(\d+(\.\d+)?)\s?mm',
        'Temperature': r'(\d+(\.\d+)?)\s?C',
        'Pollution_level': r'=\s*(-?\d+(\.\d+)?)|Pollution at \s*(-?\d+(\.\d+)?)'
        }
}

# START FUNCTION
def create_db_engine(db_path):
    """
    Create and return an SQLAlchemy database engine.

    Parameters:
    - db_path (str): The connection string for the database.

    Returns:
    - engine (sqlalchemy.engine.Engine): The SQLAlchemy database engine object.
    """
    try:
        engine = create_engine(db_path)
        # Test connection
        with engine.connect() as conn:
            pass
        # test if the database engine was created successfully
        logger.info("Database engine created successfully.")
        return engine  # Return the engine object if it all works well
    except ImportError:  # If we get an ImportError, inform the user SQLAlchemy is not installed
        logger.error("SQLAlchemy is required to use this function. Please install it first.")
        raise
    except Exception as e:  # If we fail to create an engine inform the user
        logger.error(f"Failed to create database engine. Error: {e}")
        raise
    

def query_data(engine, sql_query):
    """
    Execute a SQL query on the provided database engine and return the result as a DataFrame.

    Parameters:
    - engine (sqlalchemy.engine.Engine): The SQLAlchemy database engine object.
    - sql_query (str): The SQL query to be executed.

    Returns:
    - df (pandas.DataFrame): The result of the SQL query as a DataFrame.
    """
    try:
        with engine.connect() as connection:
            df = pd.read_sql_query(text(sql_query), connection)
        if df.empty:
            # Log a message or handle the empty DataFrame scenario as needed
            msg = "The query returned an empty DataFrame."
            logger.error(msg)
            raise ValueError(msg)
        logger.info("Query executed successfully.")
        return df
    except ValueError as e:
        logger.error(f"SQL query failed. Error: {e}")
        raise
    except Exception as e:
        logger.error(f"An error occurred while querying the database. Error: {e}")
        raise

def read_from_web_CSV(URL):
    """
    Read a CSV file from the web and return the data as a DataFrame.

    Parameters:
    - URL (str): The URL of the CSV file.

    Returns:
    - df (pandas.DataFrame): The data from the CSV file as a DataFrame.
    """
    try:
        df = pd.read_csv(URL)
        logger.info("CSV file read successfully from the web.")
        return df
    except pd.errors.EmptyDataError as e:
        logger.error("The URL does not point to a valid CSV file. Please check the URL and try again.")
        raise
    except Exception as e:
        logger.error(f"Failed to read CSV from the web. Error: {e}")
        raise
##END FUNCTION
