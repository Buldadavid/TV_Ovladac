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

@app.route('/NOVA', methods = ['POST', 'GET'])
def NOVA():
     print('NOVA')
     os.system('xdg-open /home/pi/TV/Programy/NOVA')
     return redirect('/')
@app.route('/Prima_love', methods = ['POST', 'GET'])
def Prima_love():
     print('Prima_love')
     os.system('xdg-open /home/pi/TV/Programy/Prima_love')
     return redirect('/')
@app.route('/Prima_+1', methods = ['POST', 'GET'])
def Prima_1():
     print('Prima_+1')
     os.system('xdg-open /home/pi/TV/Programy/Prima_+1')
     return redirect('/')
@app.route('/Radio_Cas', methods = ['POST', 'GET'])
def Radio_Cas():
     print('Radio_Cas')
     os.system('xdg-open /home/pi/TV/Programy/Radio_Cas')
     return redirect('/')
@app.route('/1+1', methods = ['POST', 'GET'])
def p1_1():
     print('1+1')
     os.system('xdg-open /home/pi/TV/Programy/1+1')
     return redirect('/')
@app.route('/BARRANDOV_KRIMI', methods = ['POST', 'GET'])
def BARRANDOV_KRIMI():
     print('BARRANDOV_KRIMI')
     os.system('xdg-open /home/pi/TV/Programy/BARRANDOV_KRIMI')
     return redirect('/')
@app.route('/Retro_Music_TV', methods = ['POST', 'GET'])
def Retro_Music_TV():
     print('Retro_Music_TV')
     os.system('xdg-open /home/pi/TV/Programy/Retro_Music_TV')
     return redirect('/')
@app.route('/Prima_SHOW', methods = ['POST', 'GET'])
def Prima_SHOW():
     print('Prima_SHOW')
     os.system('xdg-open /home/pi/TV/Programy/Prima_SHOW')
     return redirect('/')
@app.route('/CRo_RZ_SPORT_T2', methods = ['POST', 'GET'])
def CRo_RZ_SPORT_T2():
     print('CRo_RZ_SPORT_T2')
     os.system('xdg-open /home/pi/TV/Programy/CRo_RZ_SPORT_T2')
     return redirect('/')
@app.route('/Seznam.cz_TV', methods = ['POST', 'GET'])
def Seznam():
     print('Seznam.cz_TV')
     os.system('xdg-open /home/pi/TV/Programy/Seznam.cz_TV')
     return redirect('/')
@app.route('/RELAX', methods = ['POST', 'GET'])
def RELAX():
     print('RELAX')
     os.system('xdg-open /home/pi/TV/Programy/RELAX')
     return redirect('/')
@app.route('/CS_Mystery', methods = ['POST', 'GET'])
def CS_Mystery():
     print('CS_Mystery')
     os.system('xdg-open /home/pi/TV/Programy/CS_Mystery')
     return redirect('/')
@app.route('/Nova', methods = ['POST', 'GET'])
def Nova():
     print('Nova')
     os.system('xdg-open /home/pi/TV/Programy/Nova')
     return redirect('/')
@app.route('/Nova_Cinema', methods = ['POST', 'GET'])
def Nova_Cinema():
     print('Nova_Cinema')
     os.system('xdg-open /home/pi/TV/Programy/Nova_Cinema')
     return redirect('/')
@app.route('/Prima_ZOOM', methods = ['POST', 'GET'])
def Prima_ZOOM():
     print('Prima_ZOOM')
     os.system('xdg-open /home/pi/TV/Programy/Prima_ZOOM')
     return redirect('/')
@app.route('/Cesky_Impuls', methods = ['POST', 'GET'])
def Cesky_Impuls():
     print('Cesky_Impuls')
     os.system('xdg-open /home/pi/TV/Programy/Cesky_Impuls')
     return redirect('/')
@app.route('/Radio_Dechovka', methods = ['POST', 'GET'])
def Radio_Dechovka():
     print('Radio_Dechovka')
     os.system('xdg-open /home/pi/TV/Programy/Radio_Dechovka')
     return redirect('/')
@app.route('/Prima_COOL', methods = ['POST', 'GET'])
def Prima_COOL():
     print('Prima_COOL')
     os.system('xdg-open /home/pi/TV/Programy/Prima_COOL')
     return redirect('/')
@app.route('/Radio_Impuls', methods = ['POST', 'GET'])
def Radio_Impuls():
     print('Radio_Impuls')
     os.system('xdg-open /home/pi/TV/Programy/Radio_Impuls')
     return redirect('/')
@app.route('/CRo_VLTAVA_T2', methods = ['POST', 'GET'])
def CRo_VLTAVA_T2():
     print('CRo_VLTAVA_T2')
     os.system('xdg-open /home/pi/TV/Programy/CRo_VLTAVA_T2')
     return redirect('/')
@app.route('/SPORT_5', methods = ['POST', 'GET'])
def SPORT_5():
     print('SPORT_5')
     os.system('xdg-open /home/pi/TV/Programy/SPORT_5')
     return redirect('/')
@app.route('/Prima', methods = ['POST', 'GET'])
def Prima():
     print('Prima')
     os.system('xdg-open /home/pi/TV/Programy/Prima')
     return redirect('/')
@app.route('/Slager_original', methods = ['POST', 'GET'])
def Slager_original():
     print('Slager_original')
     os.system('xdg-open /home/pi/TV/Programy/Slager_original')
     return redirect('/')
@app.route('/CRo_PLUS_T2', methods = ['POST', 'GET'])
def CRo_PLUS_T2():
     print('CRo_PLUS_T2')
     os.system('xdg-open /home/pi/TV/Programy/CRo_PLUS_T2')
     return redirect('/')
@app.route('/rtm_plus_Liberecko', methods = ['POST', 'GET'])
def rtm_plus_Liberecko():
     print('rtm_plus_Liberecko')
     os.system('xdg-open /home/pi/TV/Programy/rtm_plus_Liberecko')
     return redirect('/')
@app.route('/Ocko_STAR', methods = ['POST', 'GET'])
def Ocko_STAR():
     print('Ocko_STAR')
     os.system('xdg-open /home/pi/TV/Programy/Ocko_STAR')
     return redirect('/')
@app.route('/Nova_Action', methods = ['POST', 'GET'])
def Nova_Action():
     print('Nova_Action')
     os.system('xdg-open /home/pi/TV/Programy/Nova_Action')
     return redirect('/')
@app.route('/Prima_STAR', methods = ['POST', 'GET'])
def Prima_STAR():
     print('Prima_STAR')
     os.system('xdg-open /home/pi/TV/Programy/Prima_STAR')
     return redirect('/')
@app.route('/KINO_BARRANDOV', methods = ['POST', 'GET'])
def KINO_BARRANDOV():
     print('KINO_BARRANDOV')
     os.system('xdg-open /home/pi/TV/Programy/KINO_BARRANDOV')
     return redirect('/')
@app.route('/Paramount_Network', methods = ['POST', 'GET'])
def Paramount_Network():
     print('Paramount_Network')
     os.system('xdg-open /home/pi/TV/Programy/Paramount_Network')
     return redirect('/')
@app.route('/CT_3_HD_T2', methods = ['POST', 'GET'])
def CT_3_HD_T2():
     print('CT_3_HD_T2')
     os.system('xdg-open /home/pi/TV/Programy/CT_3_HD_T2')
     return redirect('/')
@app.route('/Prima_MAX', methods = ['POST', 'GET'])
def Prima_MAX():
     print('Prima_MAX')
     os.system('xdg-open /home/pi/TV/Programy/Prima_MAX')
     return redirect('/')
@app.route('/Radio_Dalnice', methods = ['POST', 'GET'])
def Radio_Dalnice():
     print('Radio_Dalnice')
     os.system('xdg-open /home/pi/TV/Programy/Radio_Dalnice')
     return redirect('/')
@app.route('/CRo_JAZZ_T2', methods = ['POST', 'GET'])
def CRo_JAZZ_T2():
     print('CRo_JAZZ_T2')
     os.system('xdg-open /home/pi/TV/Programy/CRo_JAZZ_T2')
     return redirect('/')
@app.route('/CRo_RADIOZURNAL_T2', methods = ['POST', 'GET'])
def CRo_RADIOZURNAL_T2():
     print('CRo_RADIOZURNAL_T2')
     os.system('xdg-open /home/pi/TV/Programy/CRo_RADIOZURNAL_T2')
     return redirect('/')
@app.route('/JOJ_Family', methods = ['POST', 'GET'])
def JOJ_Family():
     print('JOJ_Family')
     os.system('xdg-open /home/pi/TV/Programy/JOJ_Family')
     return redirect('/')
@app.route('/Tv_NOE', methods = ['POST', 'GET'])
def Tv_NOE():
     print('Tv_NOE')
     os.system('xdg-open /home/pi/TV/Programy/Tv_NOE')
     return redirect('/')
@app.route('/Nova_Gold', methods = ['POST', 'GET'])
def Nova_Gold():
     print('Nova_Gold')
     os.system('xdg-open /home/pi/TV/Programy/Nova_Gold')
     return redirect('/')
@app.route('/CT_24_HD_T2', methods = ['POST', 'GET'])
def CT_24_HD_T2():
     print('CT_24_HD_T2')
     os.system('xdg-open /home/pi/TV/Programy/CT_24_HD_T2')
     return redirect('/')
@app.route('/Televize_pres_antenu', methods = ['POST', 'GET'])
def Televize_pres_antenu():
     print('Televize_pres_antenu')
     os.system('xdg-open /home/pi/TV/Programy/Televize_pres_antenu')
     return redirect('/')
@app.route('/CRo_D-DUR_T2', methods = ['POST', 'GET'])
def CRoDUR_T2():
     print('CRo_D-DUR_T2')
     os.system('xdg-open /home/pi/TV/Programy/CRo_D-DUR_T2')
     return redirect('/')
@app.route('/CT_1_SM_HD_T2', methods = ['POST', 'GET'])
def CT_1_SM_HD_T2():
     print('CT_1_SM_HD_T2')
     os.system('xdg-open /home/pi/TV/Programy/CT_1_SM_HD_T2')
     return redirect('/')
@app.route('/CRo_DVOJKA_T2', methods = ['POST', 'GET'])
def CRo_DVOJKA_T2():
     print('CRo_DVOJKA_T2')
     os.system('xdg-open /home/pi/TV/Programy/CRo_DVOJKA_T2')
     return redirect('/')
@app.route('/CT_:D/art_HD_T2', methods = ['POST', 'GET'])
def CTD_art_HD_T2():
     print('CT_:D/art_HD_T2')
     os.system('xdg-open /home/pi/TV/Programy/CT_:D/art_HD_T2')
     return redirect('/')
@app.route('/TV_Barrandov', methods = ['POST', 'GET'])
def TV_Barrandov():
     print('TV_Barrandov')
     os.system('xdg-open /home/pi/TV/Programy/TV_Barrandov')
     return redirect('/')
@app.route('/Radio_Cas_Rock', methods = ['POST', 'GET'])
def Radio_Cas_Rock():
     print('Radio_Cas_Rock')
     os.system('xdg-open /home/pi/TV/Programy/Radio_Cas_Rock')
     return redirect('/')
@app.route('/CRo_RADIO_JUNIOR_T2', methods = ['POST', 'GET'])
def CRo_RADIO_JUNIOR_T2():
     print('CRo_RADIO_JUNIOR_T2')
     os.system('xdg-open /home/pi/TV/Programy/CRo_RADIO_JUNIOR_T2')
     return redirect('/')
@app.route('/Naladte_se_na_digitalni_vysilani_CRA', methods = ['POST', 'GET'])
def Naladte_se_na_digitalni_vysilani_CRA():
     print('Naladte_se_na_digitalni_vysilani_CRA')
     os.system('xdg-open /home/pi/TV/Programy/Naladte_se_na_digitalni_vysilani_CRA')
     return redirect('/')
@app.route('/CT_1_JM_HD_T2', methods = ['POST', 'GET'])
def CT_1_JM_HD_T2():
     print('CT_1_JM_HD_T2')
     os.system('xdg-open /home/pi/TV/Programy/CT_1_JM_HD_T2')
     return redirect('/')
@app.route('/Nova_Fun', methods = ['POST', 'GET'])
def Nova_Fun():
     print('Nova_Fun')
     os.system('xdg-open /home/pi/TV/Programy/Nova_Fun')
     return redirect('/')
@app.route('/CRo_RADIO_WAVE_T2', methods = ['POST', 'GET'])
def CRo_RADIO_WAVE_T2():
     print('CRo_RADIO_WAVE_T2')
     os.system('xdg-open /home/pi/TV/Programy/CRo_RADIO_WAVE_T2')
     return redirect('/')
@app.route('/CNN_Prima_News', methods = ['POST', 'GET'])
def CNN_Prima_News():
     print('CNN_Prima_News')
     os.system('xdg-open /home/pi/TV/Programy/CNN_Prima_News')
     return redirect('/')
@app.route('/CRo_POHODA_T2', methods = ['POST', 'GET'])
def CRo_POHODA_T2():
     print('CRo_POHODA_T2')
     os.system('xdg-open /home/pi/TV/Programy/CRo_POHODA_T2')
     return redirect('/')
@app.route('/RADIO_PROGLAS', methods = ['POST', 'GET'])
def RADIO_PROGLAS():
     print('RADIO_PROGLAS')
     os.system('xdg-open /home/pi/TV/Programy/RADIO_PROGLAS')
     return redirect('/')
@app.route('/REBEL', methods = ['POST', 'GET'])
def REBEL():
     print('REBEL')
     os.system('xdg-open /home/pi/TV/Programy/REBEL')
     return redirect('/')
@app.route('/Prima_KRIMI', methods = ['POST', 'GET'])
def Prima_KRIMI():
     print('Prima_KRIMI')
     os.system('xdg-open /home/pi/TV/Programy/Prima_KRIMI')
     return redirect('/')
@app.route('/CT_sport_HD_T2', methods = ['POST', 'GET'])
def CT_sport_HD_T2():
     print('CT_sport_HD_T2')
     os.system('xdg-open /home/pi/TV/Programy/CT_sport_HD_T2')
     return redirect('/')
@app.route('/Nova_Lady', methods = ['POST', 'GET'])
def Nova_Lady():
     print('Nova_Lady')
     os.system('xdg-open /home/pi/TV/Programy/Nova_Lady')
     return redirect('/')
@app.route('/CT_2_HD_T2', methods = ['POST', 'GET'])
def CT_2_HD_T2():
     print('CT_2_HD_T2')
     os.system('xdg-open /home/pi/TV/Programy/CT_2_HD_T2')
     return redirect('/')
@app.route('/Ocko', methods = ['POST', 'GET'])
def Ocko():
     print('Ocko')
     os.system('xdg-open /home/pi/TV/Programy/Ocko')
     return redirect('/')
@app.route('/CT_1_HD_T2', methods = ['POST', 'GET'])
def CT_1_HD_T2():
     print('CT_1_HD_T2')
     os.system('xdg-open /home/pi/TV/Programy/CT_1_HD_T2')
     return redirect('/')
@app.route('/ABC_TV', methods = ['POST', 'GET'])
def ABC_TV():
     print('ABC_TV')
     os.system('xdg-open /home/pi/TV/Programy/ABC_TV')
     return redirect('/')
@app.route('/UKRAJINSKE_RADIO', methods = ['POST', 'GET'])
def UKRAJINSKE_RADIO():
     print('UKRAJINSKE_RADIO')
     os.system('xdg-open /home/pi/TV/Programy/UKRAJINSKE_RADIO')
     return redirect('/')

app.run(host='10.0.0.200', port=5000)
