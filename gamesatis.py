from pyquery import PyQuery
from datetime import datetime

import uruntakip
import veriekle


def gamesatis(firma, url):
    try:
        logo="https://images.gamesatis.com/assets/logo.svg"
        headers = {'User-Agent': 'Mozilla/5.0'}
        veri = PyQuery(url,headers)
        urunSonuc = veri(".wrapper.relative").items("h2")
        fiyatSonuc = veri(".price.price-tl").items("")
        for urun, fiyat in zip(urunSonuc, fiyatSonuc):
            tarih = datetime.now()
            veriekle.verisorgula(firma,urun.text(),fiyat.text(),tarih, logo, url)
    except:
        print("Hata: " + url)
