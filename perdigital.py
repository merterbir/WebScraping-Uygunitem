from pyquery import PyQuery
from datetime import datetime

import uruntakip
import veriekle


def perdigital(firma, url):
    try:
        logo="https://files.sikayetvar.com/lg/cmp/64/64585.png?1522650125"

        veri = PyQuery(url)
        urunSonuc = veri(".product-cart.mt20").items("h3")
        fiyatSonuc = veri(".product-cart.mt20").find("tr").items("td:eq(3)")
        for urun, fiyat in zip(urunSonuc, fiyatSonuc):
            tarih = datetime.now()
            veriekle.verisorgula(firma,urun.text(),fiyat.text(),tarih,logo ,url )
    except:
        print("Hata: " + url)