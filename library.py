


class library:
    def _init_ (self, baslik,yazar, sayfa_sayisi, yayin_yili):
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.yayin_yili = yayin_yili

    def bilgileri_goster(self):
      dosya = open("books.txt","a+")
      dosya.seek(0)
      for satir in dosya.read().splitlines():
        icerik = satir.split(",")
        print(f"kitap adi: {icerik[0]}\nyazar adi: {icerik[1]}\n") 
    def kitap_ekle(self):
      dosya = open("books.txt","a+")
      dosya.seek(0)
      kitap_adi=input("kitap adi giriniz:")
      yazar_adi=input("yazar adi giriniz:")
      sayfa_sayisi=input("sayfa sayisi giriniz:")
      yayin_yili=input("yayin yili giriniz:")
      dosya.write(f"{kitap_adi},{yazar_adi},{sayfa_sayisi},{yayin_yili}\n")
      print("Kitap dosyaya eklendi")

    def kitap_kaldir(self):
      dosya = open("books.txt","a+")
      dosya.seek(0)
      liste=[]
      kitap_adi=input("kitap adi giriniz:")
      for satir in dosya.read().splitlines():
        liste.append(satir)

      for kitap in liste:
        kitap_ismi=kitap.split(",") 
        if kitap_ismi[0]==kitap_adi:
          liste.remove(kitap)
          dosya2=open("books.txt","w")
          for yeni in liste:
            dosya2.write(yeni+"\n")

    def _del_(self):
      dosya.close()


     
       

while True:
  print("Library Menu")
  print("1-Kitaplari listele")
  print("2-Kitaplari ekle")
  print("3-Kitaplari kaldir")
  print("4-Cikis")

  secim=input("yapmak istediğinizi seçiniz(1/2/3/4):")
  kutuphaneobje=library()
  if secim == "1":  
    kutuphaneobje.bilgileri_goster()
  elif secim =="2":
    kutuphaneobje.kitap_ekle()
  elif secim== "3":
    kutuphaneobje.kitap_kaldir()
  elif secim== "4":
    print("Kutuphaneden çıkılıyor")
    break

  else: 
    print("Geçersiz seçim")

 





