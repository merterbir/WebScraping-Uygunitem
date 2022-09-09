
import pyodbc

import bynogame
import epinsultan
import foxngame
import gamesatis
import gecersizsite
import itemsatis
import joyalisveris
import oyunfor
import perdigital
import playsultan
import uruntakip

db = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=uygunitem.com.\MSSQLSERVER2012;DATABASE=uygunite_uygunitem;UID=uygunite_admin;PWD=psw'

)
cursor = db.cursor()

cursor.execute("SELECT * FROM [data_siteler]")
datalar = cursor.fetchall()
for i in datalar:
    url = i[1]
    strurl = str(url)
    strurl = strurl.strip("https://")
    slashindex = strurl.index("/")
    strurl = strurl[0:slashindex]

    if (strurl == "www.bynogame.com"):
        bynogame.bynogame(strurl, i[1])
    elif (strurl == "www.epinsultan.com"):
        epinsultan.epinsultan(strurl, i[1])
    elif (strurl == "www.itemsatis.com"):
        itemsatis.itemsatis(strurl, i[1])
    elif (strurl == "www.gamesatis.com"):
        gamesatis.gamesatis(strurl, i[1])
    elif (strurl == "www.playsultan.com.tr"):
        playsultan.playsultan(strurl, i[1])
    elif (strurl == "www.foxngame.com"):
        foxngame.foxngame(strurl, i[1])
    elif (strurl == "www.joyalisveris.com"):
        joyalisveris.joyalisveris(strurl, i[1])
    elif (strurl == "www.perdigital.com"):
        perdigital.perdigital(strurl, i[1])
    elif (strurl == "www.oyunfor.com"):
        oyunfor.oyunfor(strurl, i[1])
    else:
        gecersizsite.gecersizsite(i[0], i[1])
uruntakip.uruntakipsorgu()