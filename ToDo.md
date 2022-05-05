# ToDoLIST

- extrahovat složku epg_new.zip
- upravit program fce.py
```
  @app.route('/program', methods = ['POST', 'GET'])
  def program():
    print("program")
    os.system("wget http://localhost:9981/xmltv/channels --user=admin --password=admin -O /home/pi/TV/Programy/iptvGuide.xml")
    os.system("python3 /home/pi/TV/epg.py")
    #time.sleep(0.1) #?
    return render_template('epg.html')
```
- odkomentovat v novém epg.py 
- #import os
- #os.system("mv epg.html /home/pi/TV/templates") #?
- nahradit egp.py za nový epg.py
