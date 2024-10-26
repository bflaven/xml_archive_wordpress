
# 002_xml_archive_wordpress.md

## PROMPT_1
As a Python, WordPress and XML expert, writes a script in python that dumps in an html file all of each item included in an xml file named "shanghaiconfidential.wordpress.2024-10-25.000.xml".
For each item, the following values must be ouputed:
- grab the value for <title></title> and put in <h1>title</h1>
- grab the value for <pubDate></pubDate> and put in <h2>title</h2>
- grab the value <link></link> and in <a href="link">link</a>
- grab the value <content:encoded></content:encoded> and in <p>...</p>
- grab the value <category domain="post_tag"></category> as Tags: post_tag_1, post_tag_2... etc
- grab the value <category domain="category"></category> as Category: category_1, category_2... etc


Below an example of the item in xml.

```xml
<item>
  <title><![CDATA[20 avril, petits cadeaux empoisonnés. Ou non. ]]></title>
  <link>https://shanghaiconfidential.wordpress.com/2014/04/20/20-avril-petits-cadeaux-empoisonnes-ou-non/</link>
  <pubDate>Sun, 20 Apr 2014 15:51:10 +0000</pubDate>
  <dc:creator>shanghaiconfidential</dc:creator>
  <guid isPermaLink="false">http://shanghaiconfidential.wordpress.com/?p=1589</guid>
  <description/>
  <content:encoded><![CDATA[<strong> <a href="http://shanghaiconfidential.wordpress.com/wp-content/uploads/2014/04/tumblr_mpy1drjboc1qjoiq8o1_1280.jpg"><img class="alignnone size-medium wp-image-1592" src="http://shanghaiconfidential.wordpress.com/wp-content/uploads/2014/04/tumblr_mpy1drjboc1qjoiq8o1_1280.jpg?w=210" alt="tumblr_mpy1drJBoc1qjoiq8o1_1280" width="210" height="300" /></a>  </strong>
    <strong>Le passeport le plus épais du monde. </strong>Je renouvelle mon visa de résidente en Chine et me retrouve pour un temps détentrice de trois passeports agrafés les uns aux autres ; le plus ancien, entièrement noirci, porte le visa d’origine, le second comporte quelques tampons disséminés çà et là et le troisième enfin, flambant neuf, est intouché. Le tout forme un passeport mille-feuille, colossal dont je doute qu’il puisse même passer sous la vitre du guichet de la police des frontières. C’est ballot d'afficher les pays que l’on a visités comme des trophées.  On ne voyage pas pour se garnir de médailles. Mais, avouons notre faiblesse : ces trois passeports absurdes me procurent le plaisir innocent, nostalgique et rêveur d’avoir un peu vécu et parcouru le monde.
    <img class="alignnone size-medium wp-image-1593" src="http://shanghaiconfidential.wordpress.com/wp-content/uploads/2014/04/tumblr_mwf4ldbqmm1s6zgp8o1_r2_1280.jpg?w=240" alt="tumblr_mwf4ldBqmm1s6zgp8o1_r2_1280" width="240" height="300" />]]></content:encoded>
    <category domain="post_tag" nicename="business"><![CDATA[Business]]></category>
    <category domain="category" nicename="chroniques"><![CDATA[Chroniques]]></category>
</item>
```

## output_1
Here is a Python script that uses the ElementTree module to parse the XML file and output the desired HTML format.

```python
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('shanghaiconfidential.wordpress.2024-10-25.000.xml')
root = tree.getroot()

# Open the HTML file for writing
with open('output.html', 'w') as f:
    # Iterate over each item in the XML file
    for item in root.findall('item'):
        # Extract the title
        title = item.find('title').text
        # Extract the link
        link = item.find('link').text
        # Extract the pubDate
        pubDate = item.find('pubDate').text
        # Extract the content
        content = item.find('content:encoded').text
        # Extract the post_tags
        post_tags = [category.text for category in item.findall('category[@domain="post_tag"]')]
        # Extract the categories
        categories = [category.text for category in item.findall('category[@domain="category"]')]

        # Write the extracted data to the HTML file
        f.write(f'<h1>{title}</h1>\n')
        f.write(f'<h2>{pubDate}</h2>\n')
        f.write(f'<a href="{link}">{link}</a>\n')
        f.write(f'<p>{content}</p>\n')
        f.write(f'<p>Tags: {", ".join(post_tags)}</p>\n')
        f.write(f'<p>Categories: {", ".join(categories)}</p>\n')
        
```

This script will create an HTML file named `output.html` and write the extracted data from the XML file in the desired format.
