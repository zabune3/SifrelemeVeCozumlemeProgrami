import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def sezar_sifrele(metin, kaydirma):
    sifrelimetin = ""
    for harf in metin:
        if harf.isalpha():  # Sadece alfabetik karakterleri şifreler
            asciikod = ord(harf)
            if harf.isupper():
                yeni_asciikod = (asciikod - ord('A') + kaydirma) % 26 + ord('A')
            else:
                yeni_asciikod = (asciikod - ord('a') + kaydirma) % 26 + ord('a')
            sifrelimetin += chr(yeni_asciikod)
        else:
            sifrelimetin += harf  # Harf olmayan karakterler olduğu gibi kalır

    with open("sezar.txt", "a", encoding="utf-8") as f:
        f.write(sifrelimetin + "\n")

    print("Dosyaya kaydedildi")
    return "sezar.txt"


def sezar_sifrecoz(kaydirma, sifrelimetin=None):
    if sifrelimetin is None:
        with open("sezar.txt", "r", encoding="utf-8") as f:
            sifrelimetin = f.read().strip()

    metin = ""
    for harf in sifrelimetin:
        if harf.isalpha():  # Sadece alfabetik karakterleri çözer
            asciikod = ord(harf)
            if harf.isupper():
                yeni_asciikod = (asciikod - ord('A') - kaydirma) % 26 + ord('A')
            else:
                yeni_asciikod = (asciikod - ord('a') - kaydirma) % 26 + ord('a')
            metin += chr(yeni_asciikod)
        else:
            metin += harf  # Harf olmayan karakterler olduğu gibi kalır

    print("Şifreli: " + sifrelimetin + " Şifresiz: " + metin)

    # PDF çıktısı istenip istenmediğini kontrol et
    pdf_istek = input("PDF çıktısı almak ister misiniz? (E/H): ")
    if pdf_istek.upper() == "E":
        pdf_olustur(metin, "Sezar_Sifre_Cozme.pdf")

    os.remove("sezar.txt")  # Dosyayı sil


def vigenere_sifrele(metin, anahtar):
    sifrelimetin = ""
    anahtar_uzunluk = len(anahtar)

    for i, harf in enumerate(metin):
        if harf.isalpha():  # Sadece alfabetik karakterleri şifreler
            asciikod = ord(harf)
            anahtar_harf = anahtar[i % anahtar_uzunluk]
            anahtar_asciikod = ord(anahtar_harf)

            if harf.isupper():
                yeni_asciikod = (asciikod + anahtar_asciikod - 2 * ord('A')) % 26 + ord('A')
            else:
                yeni_asciikod = (asciikod + anahtar_asciikod - 2 * ord('a')) % 26 + ord('a')

            sifrelimetin += chr(yeni_asciikod)
        else:
            sifrelimetin += harf  # Harf olmayan karakterler olduğu gibi kalır

    with open("vigenere.txt", "a", encoding="utf-8") as f:
        f.write(sifrelimetin + "\n")

    print("Dosyaya kaydedildi")
    return "vigenere.txt"


def vigenere_sifrecoz(anahtar, sifrelimetin=None):
    if sifrelimetin is None:
        with open("vigenere.txt", "r", encoding="utf-8") as f:
            sifrelimetin = f.read().strip()

    metin = ""
    anahtar_uzunluk = len(anahtar)

    for i, harf in enumerate(sifrelimetin):
        if harf.isalpha():  # Sadece alfabetik karakterleri çözer
            asciikod = ord(harf)
            anahtar_harf = anahtar[i % anahtar_uzunluk]
            anahtar_asciikod = ord(anahtar_harf)

            if harf.isupper():
                yeni_asciikod = (asciikod - anahtar_asciikod + 26) % 26 + ord('A')
            else:
                yeni_asciikod = (asciikod - anahtar_asciikod + 26) % 26 + ord('a')

            metin += chr(yeni_asciikod)
        else:
            metin += harf  # Harf olmayan karakterler olduğu gibi kalır

    print("Şifreli: " + sifrelimetin + " Şifresiz: " + metin)

    # PDF çıktısı istenip istenmediğini kontrol et
    pdf_istek = input("PDF çıktısı almak ister misiniz? (E/H): ")
    if pdf_istek.upper() == "E":
        pdf_olustur(metin, "Vigenere_Sifre_Cozme.pdf")

    os.remove("vigenere.txt")  # Dosyayı sil


def affine_sifrele(metin, a, b):
    sifrelimetin = ""
    for harf in metin:
        if harf.isalpha():  # Sadece alfabetik karakterleri şifreler
            asciikod = ord(harf)
            if harf.isupper():
                yeni_asciikod = ((a * (asciikod - ord('A')) + b) % 26) + ord('A')
            else:
                yeni_asciikod = ((a * (asciikod - ord('a')) + b) % 26) + ord('a')
            sifrelimetin += chr(yeni_asciikod)
        else:
            sifrelimetin += harf  # Harf olmayan karakterler olduğu gibi kalır

    with open("affine.txt", "a", encoding="utf-8") as f:
        f.write(sifrelimetin + "\n")

    print("Dosyaya kaydedildi")
    return "affine.txt"


def affine_sifrecoz(a, b, sifrelimetin=None):
    if sifrelimetin is None:
        with open("affine.txt", "r", encoding="utf-8") as f:
            sifrelimetin = f.read().strip()

    # Çözme işlemi için tersini bulmak için modüler ters hesaplama yapılabilir
    def moduler_ters(a, m):
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

    metin = ""
    a_ters = moduler_ters(a, 26)

    for harf in sifrelimetin:
        if harf.isalpha():  # Sadece alfabetik karakterleri çözer
            asciikod = ord(harf)
            if harf.isupper():
                yeni_asciikod = (a_ters * (asciikod - ord('A') - b)) % 26 + ord('A')
            else:
                yeni_asciikod = (a_ters * (asciikod - ord('a') - b)) % 26 + ord('a')
            metin += chr(yeni_asciikod)
        else:
            metin += harf  # Harf olmayan karakterler olduğu gibi kalır

    print("Şifreli: " + sifrelimetin + " Şifresiz: " + metin)

    # PDF çıktısı istenip istenmediğini kontrol et
    pdf_istek = input("PDF çıktısı almak ister misiniz? (E/H): ")
    if pdf_istek.upper() == "E":
        pdf_olustur(metin, "Affine_Sifre_Cozme.pdf")

    os.remove("affine.txt")  # Dosyayı sil


def atbash_sifrele(metin):
    sifrelimetin = ""
    for harf in metin:
        if harf.isalpha():  # Sadece alfabetik karakterleri şifreler
            asciikod = ord(harf)
            if harf.isupper():
                yeni_asciikod = ord('Z') - (asciikod - ord('A'))
            else:
                yeni_asciikod = ord('z') - (asciikod - ord('a'))
            sifrelimetin += chr(yeni_asciikod)
        else:
            sifrelimetin += harf  # Harf olmayan karakterler olduğu gibi kalır

    with open("atbash.txt", "a", encoding="utf-8") as f:
        f.write(sifrelimetin + "\n")

    print("Dosyaya kaydedildi")
    return "atbash.txt"


def atbash_sifrecoz(sifrelimetin=None):
    if sifrelimetin is None:
        with open("atbash.txt", "r", encoding="utf-8") as f:
            sifrelimetin = f.read().strip()

    metin = ""
    for harf in sifrelimetin:
        if harf.isalpha():  # Sadece alfabetik karakterleri çözer
            asciikod = ord(harf)
            if harf.isupper():
                yeni_asciikod = ord('Z') - (asciikod - ord('A'))
            else:
                yeni_asciikod = ord('z') - (asciikod - ord('a'))
            metin += chr(yeni_asciikod)
        else:
            metin += harf  # Harf olmayan karakterler olduğu gibi kalır

    print("Şifreli: " + sifrelimetin + " Şifresiz: " + metin)

    # PDF çıktısı istenip istenmediğini kontrol et
    pdf_istek = input("PDF çıktısı almak ister misiniz? (E/H): ")
    if pdf_istek.upper() == "E":
        pdf_olustur(metin, "Atbash_Sifre_Cozme.pdf")

    os.remove("atbash.txt")  # Dosyayı sil


def pdf_olustur(icerik, dosya_adi):
    c = canvas.Canvas(dosya_adi, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Şifresiz Metin:")
    c.drawString(100, 730, icerik)
    c.save()
    print(f"{dosya_adi} dosyası oluşturuldu.")


def ana_menu():
    print("Şifreleme Programı")
    print("1. Sezar Şifreleme")
    print("2. Vigenère Şifreleme")
    print("3. Affine Şifreleme")
    print("4. Atbash Şifreleme")
    secim = input("Lütfen bir şifreleme türü seçin (1, 2, 3 veya 4): ")

    if secim == "1":
        metin = input("Şifrelenecek metni girin: ")
        kaydirma = int(input("Kaydırma miktarını girin: "))
        dosya_adi = sezar_sifrele(metin, kaydirma)
    elif secim == "2":
        metin = input("Şifrelenecek metni girin: ")
        anahtar = input("Anahtar kelimeyi girin: ")
        dosya_adi = vigenere_sifrele(metin, anahtar)
    elif secim == "3":
        metin = input("Şifrelenecek metni girin: ")
        a = int(input("Çarpma faktörünü girin (tam sayı): "))
        b = int(input("Eklenen değeri girin (tam sayı): "))
        dosya_adi = affine_sifrele(metin, a, b)
    elif secim == "4":
        metin = input("Şifrelenecek metni girin: ")
        dosya_adi = atbash_sifrele(metin)
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        return None

    input("Devam etmek için bir tuşa basın...")


def cozum_menu():
    print("Şifre Çözme Programı")
    print("1. Sezar Şifre Çözme")
    print("2. Vigenère Şifre Çözme")
    print("3. Affine Şifre Çözme")
    print("4. Atbash Şifre Çözme")
    secim = input("Lütfen bir şifre çözme türü seçin (1, 2, 3 veya 4): ")

    if secim == "1":
        kaydirma = int(input("Kaydırma miktarını girin: "))
        sifrelimetin = input("Şifreli metni girin (veya boş bırakın, dosyadan okumak için): ")
        if sifrelimetin == "":
            sezar_sifrecoz(kaydirma)
        else:
            sezar_sifrecoz(kaydirma, sifrelimetin)
    elif secim == "2":
        anahtar = input("Anahtar kelimeyi girin: ")
        sifrelimetin = input("Şifreli metni girin (veya boş bırakın, dosyadan okumak için): ")
        if sifrelimetin == "":
            vigenere_sifrecoz(anahtar)
        else:
            vigenere_sifrecoz(anahtar, sifrelimetin)
    elif secim == "3":
        a = int(input("Çarpma faktörünü girin (tam sayı): "))
        b = int(input("Eklenen değeri girin (tam sayı): "))
        sifrelimetin = input("Şifreli metni girin (veya boş bırakın, dosyadan okumak için): ")
        if sifrelimetin == "":
            affine_sifrecoz(a, b)
        else:
            affine_sifrecoz(a, b, sifrelimetin)
    elif secim == "4":
        sifrelimetin = input("Şifreli metni girin (veya boş bırakın, dosyadan okumak için): ")
        if sifrelimetin == "":
            atbash_sifrecoz()
        else:
            atbash_sifrecoz(sifrelimetin)
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        return None

    input("Devam etmek için bir tuşa basın...")


while True:
    print("\nAna Menü:")
    print("1. Şifreleme Programı")
    print("2. Şifre Çözme Programı")
    print("3. Çıkış")
    secim = input("Lütfen bir işlem seçin (1, 2 veya 3): ")

    if secim == "1":
        ana_menu()
    elif secim == "2":
        cozum_menu()
    elif secim == "3":
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")

print("Programdan çıkılıyor...")
