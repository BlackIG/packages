# Data Pipeline
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description
The datapipeline Python package is designed for efficient handling and processing of data in a pipeline. It offers three main modules - data ingestion, field data processing, and weather data processing. The package enables users to seamlessly read and process field data, analyze weather data, and integrate data from various sources.

**Modules**:

**Data Ingestion:**
Fetches Data: The module includes functions to fetch data from an SQLite database (Maji_Ndogo_farm_survey_small.db) and CSV URLs.
**Field Data Processor:**
Process Field Data: This module provides methods to process and clean field data efficiently. It includes functionalities to handle diverse field data attributes such as elevation, latitude, longitude, soil properties, and crop types.

**Notebook:**
The package includes a Jupyter notebook (datapipeline_sample_usage.ipynb) demonstrating the usage of the pipeline in real-world data processing scenarios. The notebook showcases how the pipeline can be employed for data cleaning and running statistical tests on the processed data.


## Features
- Read and process field data
- Analyze Weather Data The weather data processor module facilitates the analysis of weather-related information. It handles diverse weather metrics, including temperature, rainfall, and pollution levels.
- Statiscal tests (in sample notebook)

## Installation
You can install the package using pip:
```bash
pip install git+https://github.com/BlackIG/

** Usage**
from datapipeline import DataProcessor

# Example Usage
processor = DataProcessor()
processor.load_data('field_data.csv', 'weather_data.csv')
processor.process_data()

Documentation
For detailed documentation, please refer to the Wiki.

Contributing
If you want to contribute to this project, please follow the Contribution Guidelines.

License
This project is licensed under the MIT License 
