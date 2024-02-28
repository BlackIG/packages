# validate_data.py

import pandas as pd
import pytest

# Read the sampled data
field_df = pd.read_csv('sampled_field_df.csv')
weather_df = pd.read_csv('sampled_weather_df.csv')

def test_read_field_DataFrame_shape():
    expected_shape = (5654, 19)  
    assert field_df.shape == expected_shape

def test_read_weather_DataFrame_shape():
    expected_shape = (weather_df.shape[0], 4)  
    assert weather_df.shape == expected_shape

def test_field_DataFrame_columns():
    expected_columns = ['Field_ID', 'Elevation', 'Latitude', 'Longitude', 'Location', 'Slope',
                         'Rainfall', 'Min_temperature_C', 'Max_temperature_C', 'Ave_temps',
                         'Soil_fertility', 'Soil_type', 'pH', 'Pollution_level', 'Plot_size',
                         'Annual_yield', 'Crop_type', 'Standard_yield', 'Weather_station']  
    assert list(field_df.columns) == expected_columns

def test_weather_DataFrame_columns():
    expected_columns = ['Weather_station_ID', 'Message', 'Measurement', 'Value']  
    assert list(weather_df.columns) == expected_columns

def test_field_DataFrame_non_negative_elevation():
    assert (field_df['Elevation'] >= 0).all()

def test_crop_types_are_valid():
    valid_crop_types = ['cassava', 'tea', 'wheat', 'potato', 'banana', 'coffee', 'rice', 'maize']  
    assert set(field_df['Crop_type'].unique()) == set(valid_crop_types)
    
def test_positive_rainfall_values():
    assert (field_df['Rainfall'] >= 0).all()

# Add more tests as needed
