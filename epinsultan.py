from pyquery import PyQuery
from datetime import datetime

import uruntakip
import veriekle


def epinsultan(firma, url):
    try:
        logo="https://www.epinsultan.com/upload/kurumsal-kimlik/logo.png"
        headers = {'User-Agent': 'Mozilla/5.0'}
        veri = PyQuery(url,headers)
        urunSonuc = veri(".col-12.col-lg-4.ad").items("a")
        fiyatSonuc = veri(".col-6.col-lg-3.nmr3").remove("span").remove("strong").items("")
        for urun, fiyat in zip(urunSonuc, fiyatSonuc):
            tarih = datetime.now()
            veriekle.verisorgula(firma,urun.text(),fiyat.text(),tarih, logo, url)
    except:
        print("Hata: "+url)
