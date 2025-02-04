#sözlükler
#sözlükler de tuple ve list gibi farklı veri türleri bulunduran değiştrilebilir veri türüdür. süslü parantezlerle gösterilir. sözlükler iki kısımdan oluşur.
#keys(anahtar)
#value(değer)
#value kısmı bütün veri türünü içerebilir fakat keys kısmı sadece string ve int tipinde olabilir.
gunler = {
    "pazartesi" : 1,
    "salı" : 2,
    "çarşamba" : 3
}
gunler["perşembe"] = 4
print(gunler)
#sözlük öğelerine erişmek 
#her bir değerin anahtar karşılığı olur bildiğimiz anahtarla değere ulaşabiliriz.
#burada dikkat edilmesi gereken nokta, sözlüklere erişirken diğer veri türlerinde olduğundan farklı  köşeli parantezler içinde kullanılır. sözlükler sıralı veri tipleri değillerdir.
sozluk = {"computer" :"bilgisayar" , "driver" : "sürücü" , "printer" :"yazıcı", "output" : "çıktı", "software" : "yazılım", "memory" : "hafıza"}
print(sozluk.keys())
print(sozluk.values())
#print(sozluk.values()) sadece değerleri verir, keys() sadece anahtarları verir.
#items ise hem anahtar hem de değerleri verir.
print(sozluk.items())
#print(sozluk.items()) ile print(sozluk) arasında fark vardır, kullanım amaçları ve yazım şekilleri farklıdır.
#get kullanıcıden bir kelime girilmesi istendiğinde, kelimeyi getirme işlemi sağlar.
kelime = input("bir kelime giriniz: ")
sozluk = {"computer" :"bilgisayar" :, "driver" : "sürücü" :, "printer" :"yazıcı", "output" : "çıktı", "software" : "yazılım", "memory" : "hafıza"}
if kelime in sozluk:
    print(sozluk.get(kelime))
else:
    print("girdiğiniz kelime bulunamadı.")
#sözlük kopyalama
sozluk = {"computer" :"bilgisayar" :, "driver" : "sürücü" :, "printer" :"yazıcı", "output" : "çıktı", "software" : "yazılım", "memory" : "hafıza"}
sozluk2 = sozluk.copy()
print(sozluk2)
#dict nesnesinin constructor özelliği kullanılarak bir sözlük diğer sözlüğe kopyalanması sağlanır.
sozluk = {"computer" :"bilgisayar" :, "driver" : "sürücü" :, "printer" :"yazıcı", "output" : "çıktı", "software" : "yazılım", "memory" : "hafıza"}
yenisozluk = dict(sozluk)
print(yenisozluk)
#clear methodu sözlüğü değil, sözlüğün içini temizler.
sozluk = {"computer" :"bilgisayar" :, "driver" : "sürücü" :, "printer" :"yazıcı", "output" : "çıktı", "software" : "yazılım", "memory" : "hafıza"}
sozluk.clear()
print(sozluk)
#sözlüğü silmek için del kullanılır.
sozluk = {"computer" :"bilgisayar" :, "driver" : "sürücü" :, "printer" :"yazıcı", "output" : "çıktı", "software" : "yazılım", "memory" : "hafıza"}
del sozluk
print(sozluk)
#bir öğeyi silmek için
sozluk = {"computer" :"bilgisayar" :, "driver" : "sürücü" :, "printer" :"yazıcı", "output" : "çıktı", "software" : "yazılım", "memory" : "hafıza"}
del sozluk["computer"]
print(sozluk)
#pop methodu
sozluk = {"computer" :"bilgisayar" :, "driver" : "sürücü" :, "printer" :"yazıcı", "output" : "çıktı", "software" : "yazılım", "memory" : "hafıza"}
sozluk.pop("driver")
print(sozluk)
#popitem son nesneyi siler.
sozluk = {"computer" :"bilgisayar" :, "driver" : "sürücü" :, "printer" :"yazıcı", "output" : "çıktı", "software" : "yazılım", "memory" : "hafıza"}
sozluk.popitem()
print(sozluk)
#setdefault get metodu ile aynıdır. farkı isesizs o anahtatra bir değer vererek yazdırabiliyorsunuz.
#aranan kelime bulunuyorsa ;
sayilar = {"1" : "bir", "2" : "iki", "3" : "üç", "4" : "dört", "5" : "beş"}
print(sayilar.setdefault("4"))
#anahtar yok ise;
print(sayilar.setdefaut("8", "sekiz"))
#output
sozluk = {"computer" :"bilgisayar" :, "driver" : "sürücü" :, "printer" :"yazıcı", "output" : "çıktı", "software" : "yazılım", "memory" : "hafıza"}
sozluk["Output"] = "Çıkış"
print(sozluk)
#update
liste1 = {"ali" : 70, "mehmet" : 50, "kemal" : 60, "mustafa" : 75}
liste2 = {"ali" : 80, "mehmet" : 60, "kemal" : 70, "mustafa" : 85}
liste1.update(liste2)
print(liste1)
#örnekler
sozluk = {}
i = 0
while i < 5:
    turkce = input("bir kelimenin türkçe halini giriniz, sözlük oluşturulacaktır. ")
    ingilizce = input("bir kelimenin ingilizce halini giriniz, sözlük oluşturulacaktır. ")
    i += 1
    sozluk[turkce] = ingilizce
while True:
    kelime = input("türkçe kelime girişi yapınız, ingilizce karşılığı verilecektir. ")
    if kelime in sozluk:
        print(sozluk[kelime])
    else:
        print("kelime sözlükte bulunamadı")

#örnek
sozluk = {}
ingilizce = []
türkçe = []
i = 0
for i in range (1,4):
    tr = (input("türkçe kelime girişi yapınız: "))
    eng = (input("ingilizce kelime girişi yapınız: "))
    i += 1
    türkçe.append(tr)
    ingilizce.append(eng)
    sozluk[tr] = eng
    print("ingilizce listesi:", ingilizce)
    print("türkçe listesi:", türkçe)
    print("sözlük:", sozluk)
anahtar = set(sozluk.keys())
deger = list(sozluk.values())
print(anahtar)
print(deger)