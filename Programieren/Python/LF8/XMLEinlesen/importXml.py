import xml.etree.ElementTree as ET
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    people = []
    for person in root.findall('Person'):
        nachname = person.find('Nachname').text
        vorname = person.find('Vorname').text
        strasse = person.find('Strasse').text
        plz = person.find('PLZ').text
        ort = person.find('Ort').text
        int_bew = person.find('IntBew').text
        person_data = {
            'Nachname': nachname,
            'Vorname': vorname,
            'Strasse': strasse,
            'PLZ': plz,
            'Ort': ort,
            'IntBew': int_bew
        }
        people.append(person_data)
    return people
# Beispielaufruf
file_name = 'personen.xml'
people_data = parse_xml(file_name)
for person in people_data:
    print(person)