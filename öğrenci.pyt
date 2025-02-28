ogrenciler = {}

while True:
    print("\n1- Öğrenci Ekle")
    print("2- Tüm Öğrencileri Listele")
    print("3- Öğrenci Sil")
    print("4- Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        numara = input("Öğrenci numarası: ")
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        ogrenciler[numara] = {"Ad": ad, "Soyad": soyad}
        print("Öğrenci eklendi.")

    elif secim == "2":
        if not ogrenciler:
            print("Sistemde öğrenci yok.")
        else:
            for numara, bilgiler in ogrenciler.items():
                print(f"{numara} - Ad: {bilgiler['Ad']}, Soyad: {bilgiler['Soyad']}")

    elif secim == "3":
        numara = input("Silmek istediğiniz öğrencinin numarası: ")
        if numara in ogrenciler:
            del ogrenciler[numara]
            print("Öğrenci silindi.")
        else:
            print("Öğrenci bulunamadı.")

    elif secim == "4":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim, tekrar deneyin!")
