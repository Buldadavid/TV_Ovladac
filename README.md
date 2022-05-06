# TV_Ovladac

- works with TVheadend on PI
- put /TV files into /home/USER/ and run fce.py for all programs or "App.py for only favourite progs - OLD".
- IP address (flask) 10.0.0.200:5000

# ToDOList
- přidat fci epg.py stahne iptv.xml je pokud je potřeba iptv.xml se obsahuje epg na celý týden

```
m1 = today.strftime("%m%d")

if m1 < stopL[4:8] :
    #print("jeste jo")
    ## sem dát zbytek fce
else:
    print("uz ne")
    #os.system("wget http://localhost:9981/xmltv/channels --user=admin --password=admin -O /home/pi/TV/Programy/iptvGuide.xml")
    ## sem dát zbytek fce
```
- nebo jeste muzu skusit aby se dalo v EPG kliknou na porat a prepla by se telka
upravit v epg.py
```
ff.write(f"<tr><td id= '{barva}'><a href='http://10.0.0.200:5000/JMENO PROGRAMU'><input type='submit' value='{kanal} {za} {ko} {porad}'></a></td></tr>\n")

```
- JMENO PROGRAMU jeste neumim udelat
