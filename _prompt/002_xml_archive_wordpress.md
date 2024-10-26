
# 002_xml_archive_wordpress.md

## PROMPT_1
As a Python, WordPress and XML expert, with BeautifulSoup extract value from this xml tags: 

```xml
<category domain="post_tag" nicename="business"><![CDATA[Business]]></category>
  <category domain="category" nicename="chroniques"><![CDATA[Chroniques]]></category>
```


## output_1
You can use BeautifulSoup to extract the value from the XML tags. Here's a simple example of how you can do it:

```python
from bs4 import BeautifulSoup

data = """
<category domain="post_tag" nicename="business"><![CDATA[Business]]></category>
<category domain="category" nicename="chroniques"><![CDATA[Chroniques]]></category>
"""

soup = BeautifulSoup(data, 'xml')

# Extract values from the 'category' tags
categories = soup.find_all('category')
for category in categories:
    print(category.text)
```

In this example, `BeautifulSoup` is used to parse the XML data. The `find_all` method is then used to find all 'category' tags in the parsed data. The text within each 'category' tag is then printed out.

When you run this script, it will print:

```
Business
Chroniques
```

This is the text within each 'category' tag.


