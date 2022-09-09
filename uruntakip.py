import pyodbc

import mail_gonder

db = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=uygunitem.com.\MSSQLSERVER2012;DATABASE=uygunite_uygunitem;UID=uygunite_admin;PWD=psw'

)
cursor = db.cursor()
cursor2 = db.cursor()

def uruntakipsorgu():
    try:

        cursor.execute(
            "SELECT * FROM uruntakip")
        uruntakipdb = cursor.fetchall()
        cursor2.execute(
            "SELECT * FROM cekilen_datalar")
        cekilenurunlerdb = cursor2.fetchall()
        for item in uruntakipdb:
            anahtarKelime= str.split(item[6],",")
            for cekilendata in cekilenurunlerdb:
                durum = 0
                for kelime in anahtarKelime:
                    if kelime not in cekilendata[1]:
                        durum=1
                d1 = cekilendata[4]
                d2 = item[3]

                if(durum == 0 and d1 > d2 and item[2] > cekilendata[2] and cekilendata[7]==1):
                    print("Bulundu")
                    mesaj = "Takip ettiğiniz "+str(cekilendata[1])+" ürünün fiyatı düştü. Yeni fiyatı: " + str(cekilendata[2])+""
                    mail_gonder.mail(item[1],mesaj)





    except:
        print("Urun takip sorgusu yapılırken bir hata yaşandı.")