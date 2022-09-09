from pyquery import PyQuery
from datetime import datetime

import uruntakip
import veriekle


def playsultan(firma, url):
    try:
        logo="https://img.playanka.com/thumbnail?quality=100&stripmeta=true&type=webp&url=https%3A%2F%2Fcdn.playanka.com%2Fjoppdxfz%2FMedia%2FImages%2FOriginals%2F0001529_0.png&width=220&sign=thVdMt8geU10e0hxQZrKV4ntO29TRNCM-4hqppLeZ-I"
        headers = {'User-Agent': 'Mozilla/5.0'}

        veri = PyQuery(url,headers)
        urunSonuc = veri(".item.box-shadow").items("h2")
        fiyatSonuc = veri(".item.box-shadow").items(".new")
        for urun, fiyat in zip(urunSonuc, fiyatSonuc):
            tarih = datetime.now()
            veriekle.verisorgula(firma,urun.text(),fiyat.text(),tarih, logo, url)
    except:
        print("Hata: "+url)

