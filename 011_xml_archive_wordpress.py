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
python 011_xml_archive_wordpress.py

"""
from bs4 import BeautifulSoup
import html


with open("sample_3.xml", "rb") as f:
  xml_bytes = f.read()
xml_content = xml_bytes.decode("utf-8")
soup = BeautifulSoup(xml_content, "xml")

# print(soup)
# items = soup.find("item")
# print(items)


items = soup.find_all("item")
# Find the 'content:encoded' tag and get its text
encoded_content = soup.find('content:encoded').text

# Assuming `items` is your list of items

# Create an HTML file
with open('output_v011.html', 'w') as f:
    # Write the HTML header
    f.write('<html>\n<body>\n')

    # Loop through the items
    for index, item in enumerate(items):
        # Extract the title
        title = item.find('title').text
        # Extract the link
        link = item.find('link').text
        # Extract the pubDate
        pubDate = item.find('pubDate').text
        # Extract the content
        content = item.find('content:encoded').text

        # Extract values from the 'category' tags
        categories = soup.find_all('category')



        # Write the item data to the HTML file
        f.write(f'\n\n')
        f.write(f'<h1>Item {index}</h1>\n')
        f.write(f'<h2>{title}</h2>\n')
        f.write(f'<code>\n')
        for category in categories:
            f.write(f'{category.text},')
        f.write(f'</code>\n')
        f.write(f'<p><strong>Link:</strong><a href="{html.escape(link)}">{html.escape(link)}</a>\n</p>\n')
        f.write(f'<p>{content}</p>\n')
        f.write(f'<hr>\n\n')
        

    # Write the HTML footer
    f.write('</body>\n</html>')



