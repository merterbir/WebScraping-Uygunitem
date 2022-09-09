import pyodbc

db = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=uygunitem.com.\MSSQLSERVER2012;DATABASE=uygunite_uygunitem;UID=uygunite_admin;PWD=psw')
cursor = db.cursor()


def verisorgula(firma, isim, fiyat, tarih, logo, url):
    try:

        cursor.execute(
            "SELECT * FROM cekilen_datalar WHERE cekilen_isim LIKE '" + isim + "' AND cekilen_firma LIKE '" + firma + "'")
        datalar = cursor.fetchall()
        if (len(datalar) > 0):
            veriguncelle(firma, isim, fiyat, tarih, logo, url)
            veriekle(firma, isim, fiyat, tarih, logo, url)
        else:
            veriekle(firma, isim, fiyat, tarih, logo, url)
    except:
        print("Veri Sorgularken bir hata yaşandı.")


def veriekle(firma, isim, fiyat, tarih, logo, url):
    try:
        fiyat = fiyat.replace(',', '.')
        fiyat = fiyat.replace('₺', '')
        fiyat = fiyat.replace('TL', '')
        cursor.execute("INSERT INTO cekilen_datalar VALUES(?,?,?,?,?,?,?)", isim, fiyat, firma, tarih, logo, url,1)
        db.commit()
    except:
        print("Veri Eklenirken bir hata yaşandı." + firma)

def veriguncelle(firma, isim, fiyat, tarih, logo, url):
     try:
        fiyat = fiyat.replace(',', '.')
        fiyat = fiyat.replace('₺', '')
        fiyat = fiyat.replace('TL', '')
        cursor.execute("UPDATE cekilen_datalar SET cekilen_durum = 0 WHERE cekilen_isim LIKE ? AND cekilen_firma LIKE ? AND cekilen_durum = 1",(isim,firma))
        db.commit()
     except:
        print("Veri Güncellenirken bir hata yaşandı." + firma)