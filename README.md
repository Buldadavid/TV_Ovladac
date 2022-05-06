# TV_Ovladac

- works with TVheadend on PI
- put /TV files into /home/USER/ and run fce.py for all programs or "App.py for only favourite progs - OLD".
- IP address (flask) 10.0.0.200:5000

# ToDOList
- upravit epg.py - stahne se iptv.xml jen pokud je potřeba iptv.xml obsahuje epg na celý týden
- upravit v fce.py /prog
    smazat staženi iptv.xml
- v EPG se dá kliknou na porat a prepne se telka
- epg.py - mělo by to fungovat
```
import xml.etree.ElementTree as ET
from datetime import datetime
from datetime import date
import os

today = date.today()
d1 = today.strftime("%d")
m1 = today.strftime("%m%d")
#print(d1)
#print(m1)

now = datetime.now()
ctime = int(now.strftime("%H"))
cctime = now.strftime("%H:%M")
ctimee = (int(ctime) +3)
#print(ctimee)

tree = ET.parse('iptv.xml')
root = tree.getroot()
#print(root)

prog = [programme for programme in tree.findall('programme')]

last = prog[-1]
stopL = last.attrib['stop']
print(stopL[4:8])

if m1 < stopL[4:8] :
    #print("jeste jo")
    
    with open('epg.html', 'a') as ff:
        ff.write('<!DOCTYPE html>\n')
        ff.write('<html><head><link rel="stylesheet" href="static/mystyle.css">\n')
        ff.write('<meta charset="8859">\n')
        ff.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        ff.write('<title>Ovladač</title>\n')
        ff.write('</head><style></style><body><h1>TV EPG</h1><table>\n')
        ff.close() 
    
    for programme in root.findall('programme'):
        porad = programme.find('title').text
        start = programme.attrib['start']
        stop = programme.attrib['stop']
        channel = programme.attrib['channel']
        za = start[8:10]+":"+start[10:12]
        ko = stop[8:10]+":"+stop[10:12]
    
        def fce():
            if ko > cctime and za < cctime:
                barva = "nic"
            else:
                barva = "nic2"

            with open('epg.html', 'a') as ff:
                ff.write(f"<tr><td id= '{barva}'><a href='http://10.0.0.200:5000/{route}'><input type='submit' value='{kanal} {za} {ko} {porad}' id= '{barva}'></a></td></tr>\n")
                ff.close()            

        if channel == "36e6c878e5fef604094a70bacee2cd6c" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "ČT1"
            route = "CT_1_HD_T2"
            fce()
            
        if channel == "68043b642284e246c82723178b18f846" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "ČT2"
            route = "CT_2_HD_T2"
            fce()

        if channel == "f3ea5080f442773e4843666b76e22ed1" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "NOVA"
            route = "Nova"
            fce()
            
        if channel == "92ee8c12c8787b3fd4545204591abe18" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "NOVA CINEMA"
            route = "Nova_Cinema"
            fce()

        if channel == "a8ece1d3e98e4807ac05b0eef675f062" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "NOVA FUN"
            route = "Nova_Fun"
            fce()
            
        if channel == "3eac239d56747bf05c95fc73c63deede" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "PRIMA"
            route = "Prima"
            fce()

        if channel == "e115399635e9fef8f9c120f023e3d3db" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "PRIMA COOL"
            route = "Prima_COOL"
            fce()
            
        if channel == "80149d93f0764c1b82aa86494deb0245" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "PRIMA ZOOM"
            route = "Prima_ZOOM"
            fce()
            
        if channel == "5aaf422ee23108e38907319f77a96421" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "PRIMA MAX"
            route = "Prima_MAX"
            fce()
            
    with open('epg.html', 'a') as ff:
        ff.write('</table>\n')
        ff.write('<a href="http://10.0.0.200:5000">\n')
        ff.write('    <input type="button" value="Zpět" id = "greet1" />\n')
        ff.write('</a>\n')
        ff.write('</body>\n')
        ff.write('</html>\n')
        ff.close() 

        #os.system("mv epg.html /home/pi/TV/templates/epg.html")
else:
    print("uz ne")
    os.system("wget http://localhost:9981/xmltv/channels --user=admin --password=admin -O /home/pi/TV/Programy/iptvGuide.xml")
    
    with open('epg.html', 'a') as ff:
        ff.write('<!DOCTYPE html>\n')
        ff.write('<html><head><link rel="stylesheet" href="static/mystyle.css">\n')
        ff.write('<meta charset="8859">\n')
        ff.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        ff.write('<title>Ovladač</title>\n')
        ff.write('</head><style></style><body><h1>TV EPG</h1><table>\n')
        ff.close() 
    
    for programme in root.findall('programme'):
        porad = programme.find('title').text
        start = programme.attrib['start']
        stop = programme.attrib['stop']
        channel = programme.attrib['channel']
        za = start[8:10]+":"+start[10:12]
        ko = stop[8:10]+":"+stop[10:12]
    
        def fce():
            if ko > cctime and za < cctime:
                barva = "nic"
            else:
                barva = "nic2"

            with open('epg.html', 'a') as ff:
                ff.write(f"<tr><td id= '{barva}'><a href='http://10.0.0.200:5000/{route}'><input type='submit' value='{kanal} {za} {ko} {porad}' id= '{barva}'></a></td></tr>\n")
                ff.close()            

        if channel == "36e6c878e5fef604094a70bacee2cd6c" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "ČT1"
            route = "CT_1_HD_T2"
            fce()
            
        if channel == "68043b642284e246c82723178b18f846" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "ČT2"
            route = "CT_2_HD_T2"
            fce()

        if channel == "f3ea5080f442773e4843666b76e22ed1" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "NOVA"
            route = "Nova"
            fce()
            
        if channel == "92ee8c12c8787b3fd4545204591abe18" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "NOVA CINEMA"
            route = "Nova_Cinema"
            fce()

        if channel == "a8ece1d3e98e4807ac05b0eef675f062" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "NOVA FUN"
            route = "Nova_Fun"
            fce()
            
        if channel == "3eac239d56747bf05c95fc73c63deede" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "PRIMA"
            route = "Prima"
            fce()

        if channel == "e115399635e9fef8f9c120f023e3d3db" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "PRIMA COOL"
            route = "Prima_COOL"
            fce()
            
        if channel == "80149d93f0764c1b82aa86494deb0245" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "PRIMA ZOOM"
            route = "Prima_ZOOM"
            fce()
            
        if channel == "5aaf422ee23108e38907319f77a96421" and start[6:8] == d1 and int(start[8:10])<ctimee and ko>=cctime:
            kanal = "PRIMA MAX"
            route = "Prima_MAX"
            fce()
            
    with open('epg.html', 'a') as ff:
        ff.write('</table>\n')
        ff.write('<a href="http://10.0.0.200:5000">\n')
        ff.write('    <input type="button" value="Zpět" id = "greet1" />\n')
        ff.write('</a>\n')
        ff.write('</body>\n')
        ff.write('</html>\n')
        ff.close() 

    os.system("mv epg.html /home/pi/TV/templates/epg.html")


```
- mystyle.css - mělo by to fungovat
```
h1   {color: white;
    font: 45px Times;
    font-weight: bold;
    text-align:center;
}
body {
background-color: #444444;
font: Arial, sans-serif;
}
.center {
  margin-left: auto;
  margin-right: auto;
  width: 100px;
}
#greet1 {
    background-color: #222222;
    border:  none;
    border-radius: 5px;
    color: white;
    font: 20px Arial, sans-serif;
    height: 50px;
    width: 100%;
}
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
}
table, td {
  border: 1px solid black;
}
tr{height: 60px;}
#nic{
background-color: #91ffaf;
color: black;
}
#nic2{
color: white;
}
input[type=submit] {
background-color: transparent; border-color: transparent; 
}
```
