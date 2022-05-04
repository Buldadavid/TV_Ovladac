import xml.etree.ElementTree as ET
from datetime import datetime
from datetime import date
import sys

sys.stdout = open("/home/pi/TV/epg.txt", "w")

today = date.today()
d1 = today.strftime("%d")
#print(d1)

now = datetime.now()
ctime = int(now.strftime("%H"))
cctime = now.strftime("%H:%M")
ctimee = (int(ctime) +3)
#print(ctimee)

tree = ET.parse('/home/pi/TV/Programy/iptvGuide.xml')
root = tree.getroot()
#print(root)

for programme in root.findall('programme'):
    porad = programme.find('title').text
    start = programme.attrib['start']
    stop = programme.attrib['stop']
    channel = programme.attrib['channel']
    za = start[8:10]+":"+start[10:12]
    ko = stop[8:10]+":"+stop[10:12]

    if channel == "36e6c878e5fef604094a70bacee2cd6c" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
        kanal = "ČT1"
        print(kanal,za,ko,porad)
        
    if channel == "68043b642284e246c82723178b18f846" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
        kanal = "ČT2"
        print(kanal,za,ko,porad)

    if channel == "f3ea5080f442773e4843666b76e22ed1" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
        kanal = "NOVA"
        print(kanal,za,ko,porad)
        
    if channel == "92ee8c12c8787b3fd4545204591abe18" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
        kanal = "NOVA CINEMA"
        print(kanal,za,ko,porad)

    if channel == "a8ece1d3e98e4807ac05b0eef675f062" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
        kanal = "NOVA FUN"
        print(kanal,za,ko,porad)
        
    if channel == "3eac239d56747bf05c95fc73c63deede" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
        kanal = "PRIMA"
        print(kanal,za,ko,porad)

    if channel == "e115399635e9fef8f9c120f023e3d3db" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
        kanal = "PRIMA COOL"
        print(kanal,za,ko,porad)
        
    if channel == "80149d93f0764c1b82aa86494deb0245" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
        kanal = "PRIMA ZOOM"
        print(kanal,za,ko,porad)
        
    if channel == "5aaf422ee23108e38907319f77a96421" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
        kanal = "PRIMA MAX"
        print(kanal,za,ko,porad)
        
sys.stdout.close()