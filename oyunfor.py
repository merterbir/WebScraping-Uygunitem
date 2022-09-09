from pyquery import PyQuery
from datetime import datetime

import uruntakip
import veriekle


def oyunfor(firma, url):
    try:
        logo="https://www.oyunfor.com/Public/standart/web/dist/img/logo.png"
        hdrs = {'User-Agent': 'Mozilla / 5.0 (X11 Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 52.0.2743.116 Safari / 537.36'}

        veri = PyQuery(url,hdrs)
        urunSonuc = veri(".col-md-65.col-70.col-lg-40.col-xl-50.p-0").items("h3")
        fiyatSonuc = veri(".ePrice").items("span")
        for urun, fiyat in zip(urunSonuc, fiyatSonuc):
            tarih = datetime.now()
            veriekle.verisorgula(firma,urun.text(),fiyat.text(),tarih ,logo , url)
    except:
        print("Hata: "+url)



