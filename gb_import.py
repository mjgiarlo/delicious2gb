"""
Import delicious bookmarks into Google Bookmarks
(Script is adapted from http://blog.persistent.info/2006/10/import-your-delicious-bookmarks-into.html)

First:
  wget 'https://USERNAME:PASSWORD@api.del.icio.us/v1/posts/all' > delicious_bookmarks.xml
Then copy http://persistent.info/delicious2google/main.js to a web-accessible
    directory, putting the URL in the 'url' variable below
Then:
  python gb_import.py delicious_bookmarks.xml > gb_import.html
Then copy gb_import.html to a web-accessible directory
Finally hit gb_import.html over the web
Boom
"""

import sys
import json
from lxml import etree

# SET THIS VARIABLE PER DOCSTRING ABOVE
url = ""

posts = []

for post_xml in etree.parse(sys.argv[1]).getroot():
    post = {}
    post["u"] = post_xml.attrib["href"]
    post["d"] = post_xml.attrib["description"]
    post["e"] = post_xml.attrib["extended"]
    tags = []
    for tag in post_xml.attrib["tag"].split():
      tags.append(tag)
    post["t"] = tags
    posts.append(post)
    
print '<script type="text/javascript" src="%s"></script>' % url

print '''
<h1>Uploading...</h1>
<form id="upload-form" action="https://www.google.com/bookmarks/mark?op=upload" method="POST">
  <input type="hidden" name="" id="data">
</form>
'''

print '<script type="text/javascript">';
print "jsonCallback(%s)" % json.dumps(posts)
print '</script>'
