#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
[env]
# Conda Environment
conda create --name lxml_env python=3.9.13
conda info --envs
source activate lxml_env

conda deactivate


# BURN AFTER READING
source activate lxml_env

python -m pip install lxml
python -m pip install wpparser
python -m pip install beautifulsoup4 lxml



# if needed to remove
conda env remove -n [NAME_OF_THE_CONDA_ENVIRONMENT]
conda env remove -n lxml_env

# BURN AFTER READING
conda env remove -n lxml_env



# update conda 
conda update -n base -c defaults conda

# to export requirements
pip freeze > requirements.txt

# [path]
cd /Users/brunoflaven/Documents/02_copy/xml_archive_wordpress/

# launch the file
python 008_xml_archive_wordpress.py

"""
import json

# JSON data as a string
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Parse the JSON data
data = json.loads(json_data)

# Access the data
print(data['name'])  # Output: John
print(data['age'])  # Output: 30
print(data['city'])  # Output: New York









