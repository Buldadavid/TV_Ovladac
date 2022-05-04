from flask import Flask, render_template, redirect
import os
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/off', methods = ['POST', 'GET'])
def off():
    print("off")
    os.system("pkill vlc")
    return redirect("/")

@app.route('/vyp', methods = ['POST', 'GET'])
def vyp():
    print("vyp")
    os.system("python3 /home/pi/TV/vypinani_TV.py")
    return redirect("/")

@app.route('/ne', methods = ['POST', 'GET'])
def ne():
    print("ne")
    pyautogui.click(937, 435)
    pyautogui.doubleClick(700,350)
    return redirect("/")

@app.route('/up', methods = ['POST', 'GET'])
def up():
    print("up")
    os.system("amixer -D pulse sset Master 5%+")
    return redirect("/")

@app.route('/full', methods = ['POST', 'GET'])
def full():
    print("full")
    pyautogui.doubleClick(700,350)
    return redirect("/")

@app.route('/down', methods = ['POST', 'GET'])
def down():
    print("down")
    os.system("amixer -D pulse sset Master 5%-")
    return redirect("/")

@app.route('/program', methods = ['POST', 'GET'])
def program():
    print("program")
    os.system("wget http://localhost:9981/xmltv/channels --user=admin --password=admin -O /home/pi/TV/Programy/iptvGuide.xml")
    os.system("python3 /home/pi/TV/epg.py")
    return redirect("http://10.0.0.200/epg.php")

@app.route('/ct1', methods = ['POST', 'GET'])
def ct1():
    print("ct1")
    os.system("xdg-open /home/pi/TV/Programy/ct1")
    return redirect("/")

@app.route('/ct2', methods = ['POST', 'GET'])
def ct2():
    print("ct2")
    os.system("xdg-open /home/pi/TV/Programy/ct2")
    return redirect("/")

@app.route('/nova', methods = ['POST', 'GET'])
def nova():
    print("nova")
    os.system("xdg-open /home/pi/TV/Programy/nova")
    return redirect("/")

@app.route('/nova_cinema', methods = ['POST', 'GET'])
def cinema():
    print("nova_cinema")
    os.system("xdg-open /home/pi/TV/Programy/nova_cinema")
    return redirect("/")

@app.route('/nova_fun', methods = ['POST', 'GET'])
def fun():
    print("nova_fun")
    os.system("xdg-open /home/pi/TV/Programy/nova_fun")
    return redirect("/")

@app.route('/prima', methods = ['POST', 'GET'])
def prima():
    print("prima")
    os.system("xdg-open /home/pi/TV/Programy/prima")
    return redirect("/")

@app.route('/prima_cool', methods = ['POST', 'GET'])
def cool():
    print("prima_cool")
    os.system("xdg-open /home/pi/TV/Programy/prima_cool")
    return redirect("/")

@app.route('/prima_zoom', methods = ['POST', 'GET'])
def zoom():
    print("prima_zoom")
    os.system("xdg-open /home/pi/TV/Programy/prima_zoom")
    return redirect("/")

@app.route('/prima_max', methods = ['POST', 'GET'])
def max():
    print("prima_max")
    os.system("xdg-open /home/pi/TV/Programy/prima_max")
    return redirect("/")

app.run(host='10.0.0.200', port=5000)