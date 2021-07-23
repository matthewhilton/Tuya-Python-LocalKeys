import xml.etree.ElementTree as ET
import json
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import csv

Tk().withdraw()
filepath = askopenfilename()
print(filepath)

tree = ET.parse(filepath)
root = tree.getroot()

jsontext = root[7].text
data = json.loads(jsontext)

devices = data['deviceRespBeen']

with open('keys.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['name', 'uuid', 'localkey'])

    for device in devices:
        name = device['name']
        uuid = device['uuid']
        key = device['localKey']

        writer.writerow([name, uuid, key])

print('Done!')