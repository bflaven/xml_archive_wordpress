# xml_archive_wordpress
**Parse an xml wordpress archive with python so the need is the following or user storie.**

> From an XML exported from WordPress, extract the texts from the file (including titles) and their publication date (in DD/MM/YYYY format). Ideally, sorted from oldest (2012) to newest (2022)

So, the idea is to grab the following tags from the xml file:

```xml
<title>
<!-- eg. title : 20 avril, petits cadeaux empoisonnés. Ou non. 
and so on... -->
<link>
<pubDate>
<guid>
<content:encoded>
<category domain="post_tag">
<category domain="category">
```

I intend to use Python and make some attempts with libraries such as: 
- lxml: https://pypi.org/project/lxml/
- wpparser: https://pypi.org/project/wpparser/
- BeautifulSoup: https://pypi.org/project/beautifulsoup4/


**Create an env with anaconda**
```python
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
python 012_xml_archive_wordpress.py

"""
```

```bash
# get to the dir
cd /Users/brunoflaven/Documents/03_git/

# command to grab the directory
git clone https://github.com/bflaven/xml_archive_wordpress.git xml_archive_wordpress

# get into the groove :)
cd /Users/brunoflaven/Documents/03_git/xml_archive_wordpress

# then the routine
git status
git add .
git commit -am "add files"
git push
```



