from pyquery import PyQuery
from datetime import datetime

import uruntakip
import veriekle


def foxngame(firma, url):
    try:
        logo="https://files.sikayetvar.com/lg/cmp/13/134307.png?1615193234"
        headers = {'User-Agent': 'Mozilla/5.0'}
        veri = PyQuery(url,headers)
        urunSonuc = veri(".item.box-shadow").items("h2")
        fiyatSonuc = veri(".item.box-shadow").items(".new")
        for urun, fiyat in zip(urunSonuc, fiyatSonuc):
            tarih = datetime.now()
            veriekle.verisorgula(firma,urun.text(),fiyat.text(),tarih, logo, url)
    except:
        print("Hata: " + url)

