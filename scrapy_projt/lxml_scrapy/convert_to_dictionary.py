import xml.etree.ElementTree as etree

employees = {
    'employee_0': '<Person><Attribute name="name"><Value>Bill Johnson</Value></Attribute><Attribute name="city"><Value>New York</Value></Attribute><Attribute name="email"><Value>bill.johnson@email.com</Value></Attribute></Person>',
    'employee_1': '<Person><Attribute name="name"><Value>Amanda Philips</Value></Attribute><Attribute name="city"><Value>Los Angeles</Value></Attribute><Attribute name="email"><Value>amanda.philips@email.com</Value></Attribute></Person>'
}
mydict ={}
for identifier_key in employees:
    xml = etree.fromstring(employees[identifier_key])

    for key in xml:
        mydict.update()
        key_str = key.attrib["name"]

        for value in key:
            value_str = value.text
            employees[identifier_key][key_str] = value_str
