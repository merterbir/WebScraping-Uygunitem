from pyquery import PyQuery
from datetime import datetime
import requests

import uruntakip
import veriekle


def itemsatis(firma, url):
    try:
        logo="https://cdn.itemsatis.com/global/logo/original/zeminsiz.png"
        hdrs = {'User-Agent':'Mozilla / 5.0 (X11 Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 52.0.2743.116 Safari / 537.36'}
        veri = PyQuery(url,hdrs)
        urunSonuc = veri(".products-title").items("")
        fiyatSonuc = veri(".products-price").items("h2")
        for urun, fiyat in zip(urunSonuc, fiyatSonuc):
            tarih = datetime.now()
            veriekle.verisorgula(firma,urun.text(),fiyat.text(),tarih, logo, url)
    except:
        print("Hata: " + url)