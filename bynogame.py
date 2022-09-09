from pyquery import PyQuery
from datetime import datetime

import uruntakip
import veriekle


def bynogame(firma, url):

    try:
        logo = "https://cdn.bynogame.com/site-images/bynogame-logo-siyah-01.svg"
        headers = {'User-Agent': 'Mozilla/5.0'}
        veri = PyQuery(url,headers)
        urunSonuc = veri(".card-title.mt-2.mb-0").items("h6")
        fiyatSonuc = veri(".col-lg-4").items("span:eq(2)")
        for urun, fiyat in zip(urunSonuc, fiyatSonuc):
            tarih = datetime.now()
            print(urun.text())
            veriekle.verisorgula(firma, urun.text(), fiyat.text(), tarih, logo, url)

    except:
        print("Hata: "+url)

