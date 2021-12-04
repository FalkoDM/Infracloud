# Fill in this file with the code from parsing XML exercise
import xml.etree.ElementTree as ET
import re

# use the parse function from ElementTree(ET) and store it xml variable
xml = ET.parse("myfile.xml")
root = xml.getroot()

# create regex to drill down in the xml file
ns = re.match('{.*}', root.tag).group(0)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))

# print the value fo <default-operation> and <test-option>
print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))
