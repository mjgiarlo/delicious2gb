import sys
import json
from lxml import etree

# SET THIS VARIABLE PER README
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
