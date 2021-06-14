# Ejemplo 2
import xml.etree.ElementTree as ET

def dict_to_xml(tag, d):
    element = ET.Element(tag)
    for key, val in d.items():
        child = ET.Element(key)
        child.text = str(val)
        element.append(child)

    return element

test_dict = {
    'name' : 'facebook',
    'country' : 'USA',
    'year' : 2004
}

xml_tree = dict_to_xml("company", test_dict)

print(ET.tostring(xml_tree))