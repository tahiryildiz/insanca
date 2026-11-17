# Alanlara göre yazım

> Bu dosya MesutARIDORU'nun [İnsanlık öldü mü?](https://github.com/MesutARIDORU/insanlik-oldu-mu) skill'indeki `references/sectors.md` dosyasından uyarlandı (MIT lisansı). Kalıp kodları insanca'nın § numaralarına çevrildi. "Sonra" örnekleri olgu kilidine uyar: kaynakta olmayan her bilgi köşeli parantezli yer tutucudur.

Metin tanımı (`turler.md`) yazının biçimini söyler: e-posta mı, şartname mi, öykü mü. Alan ise yazının konusunu ve okurunu söyler: aynı e-posta bir bankadan çıkınca başka, bir okuldan çıkınca başka okunur. 1. adımda alanı belirledikten sonra buradaki bölümünü oku. `scripts/olcum.py --guide` metnin tahmin edilen alanının bölümünü de yazdırır, belirli bir alanınkini almak için: `scripts/olcum.py --guide "Finans"`.

Her bölümde aynı başlıklar var:
- **Kim okur:** Alanın okurları ve her birine giden metnin sicili.
- **Model burada nasıl yazar:** O alanda yapay zekanın bıraktığı tipik izler.
- **Dokunma:** Değişirse zarar doğuracak bilgiler.
- **Yazım:** Alanda sık geçen sayı, birim, kısaltma ve ad yazımı (kurallar `yazim-ve-terim.md` dosyasında).
- **Önce / Sonra:** Kısa bir örnek. Sonra metni önce metninde olmayan hiçbir bilgiyi eklemez, eksik bilgiyi köşeli parantezle sorar.

## Her alanda geçerli olanlar

- **Rakam, tarih, süre, tutar, doz, madde numarası** harfi harfine kalır. Yuvarlama, birim değiştirme ya da "yaklaşık" ekleme de değişikliktir.
- **Yasal uyarı ve bilgilendirme cümleleri** kısaltılmaz, sadeleştirilmez, silinmez: risk bildirimi, yan etki uyarısı, cayma hakkı, kişisel veri aydınlatması. Dilleri yapay görünse bile metnin sahibine sor.
- **İddianın gücü** korunur. "Yüksek getiri sağlayabilir" cümlesi "yüksek getiri sağlar" olmaz, "tedaviye yardımcı olabilir" cümlesi "tedavi eder" olmaz.
- **Kurum, ürün ve unvan adları** metnin sahibinin yazdığı gibi kalır.

---

## Yazılım ve teknoloji

**Kim okur:**
- Geliştirici ekibi: yerleşik İngilizce terimler kalır (deploy, PR, release).
- Ürünü kullanan genel okur: insanların kullandığı Türkçe (yayına almak, güncelleme).
- Kurumsal müşterinin BT yöneticisi: teknik ama satış dili taşımayan, net metin.

**Model burada nasıl yazar:**
- Sürüm notunda heyecan anonsu ve emoji: "Heyecan verici yeni sürümümüzle karşınızdayız! 🚀" (§28, §26).
- Ne değiştiğini söylemeyen sıfatlar: "güçlü", "esnek", "sorunsuz", "kullanıcı deneyimini bir üst seviyeye taşıyan" (§8, §16).
- Ekip içi notta aşırı çeviri: "çekme isteği", "konuşlandırma" (§54).
- Kesinti açıklamasında failsiz edilgen: "Bir sorun yaşanmış olup giderilmiştir." Ne olduğu, ne kadar sürdüğü, kimi etkilediği yazmaz (§18).
- Hata mesajında terapist sesi: "Bu durumun can sıkıcı olabileceğini anlıyoruz." (§35)

**Dokunma:** Kod, komut, sürüm numarası, hata kodu, API ve kütüphane adları, arayüz etiketleri, güvenlik duyurusundaki açık numarası (CVE) ve etkilenen sürüm aralığı, kesinti raporundaki saatler.

**Yazım:** Yabancı terime ek kesmeyle gelir, okunuşa göre uyar: PR'ı, API'ye, deploy'dan. Sürüm numarası olduğu gibi kalır: "4.2.1 sürümü".

**Önce:**
> Hizmetlerimizde kısa süreli bir kesinti yaşanmış olup, ekiplerimizin özverili çalışmaları sonucunda sorun kısa sürede giderilmiştir. Yaşanan aksaklıktan dolayı özür dileriz.

**Sonra:**
> [tarih] günü [saat aralığı] arasında [hangi hizmet] çalışmadı. Sorunu giderdik, nedeni [neydi?]. Tekrarlanmaması için [ne yapılıyor?]. Bu süre için özür dileriz.

**Ne değişti:** Kesinti açıklamasında okurun sorduğu üç şey öne geldi: ne zaman, ne çalışmadı, neden. Metinde olmadıkları için yer tutucu bırakıldı. "Özverili çalışmalar" okura bilgi vermediği için çıktı.

## Finans

**Kim okur:**
- Bireysel müşteri: kısa, net, rakamı öne alan metin.
- Kurumsal müşteri ve yatırımcı: terimleri bilen, ayrıntı isteyen okur.
- Kurum içi ekip: finans jargonu kalır (mutabakat, kapanış, nakit akışı).

**Model burada nasıl yazar:**
- Amaca gelmeyen giriş: "Finansal ihtiyaçlarınıza en iyi şekilde yanıt verebilmek adına..." (§17).
- Ne değiştiğini saklayan edilgen: "Faiz oranlarımız güncellenmiştir." Hangi oran, ne kadar, ne zamandan itibaren? (§18)
- Broşür sözleri: "finansal özgürlüğünüze giden yolda", "güvenilir çözüm ortağınız", "size özel ayrıcalıklar" (§2).
- Kaynaksız getiri ve başarı hikâyesi: "Müşterilerimiz yıllık %30'a varan kazanç elde ediyor." (§7) Finansta bu bir yanıltma riskidir. Rakam kaynakta yoksa ekleme, kaynakta varsa dayanağını sor.
- Çeviri e-posta kalıbı: "Detaylı bilgi için bizimle iletişime geçmekten çekinmeyin." (§16)

**Dokunma:** Faiz ve kâr payı oranları, yıllık maliyet oranı, ücret ve komisyonlar, tarihler, vade, risk bildirimleri, "yatırım danışmanlığı kapsamında değildir" türü yasal uyarılar, ürün adları.

**Yazım:** 1.250,50 TL (binlik nokta, kesir virgül). %2,5 (işaretle sayı arasında boşluk yok). Ek kısaltmanın okunuşuna göre gelir: TL'nin, TL'ye. Para birimi yazıyla küçük harfle başlar: lira, dolar, avro.

**Önce:**
> Değerli müşterimiz, finansal ihtiyaçlarınıza en iyi şekilde yanıt verebilmek adına kredi kartı faiz oranlarımız güncellenmiştir. Detaylı bilgi için web sitemizi ziyaret etmekten çekinmeyin.

**Sonra:**
> Sayın [ad soyad], kredi kartınızın faiz oranı [tarih] itibarıyla değişiyor: [eski oran] yerine [yeni oran]. Ayrıntılar [bağlantı] adresinde.

**Ne değişti:** Değişikliğin kendisi ilk cümleye geldi, oranlar ve tarih metinde olmadığı için yer tutucu oldu. Amaca gelmeyen giriş ve "çekinmeyin" kalıbı çıktı.

## Sağlık

**Kim okur:**
- Hasta ve hasta yakını: sade, sakin, ne yapacağını söyleyen metin.
- Sağlık çalışanı: tıbbi terim kalır, kısa ve kesin.
- Kurum içi duyuru: nöbet, prosedür, cihaz.

**Model burada nasıl yazar:**
- Her cümleye serpilmiş teselli: "Endişelenmeniz çok doğal", "Kendinize zaman tanıyın" (§35). Hastaya giden metinde sıcaklık yerindedir, kalıp halinde tekrar edilen teselli değil.
- Kesinlik şişirmesi: "tamamen güvenli", "kesin çözüm", "yan etkisi yoktur" (§1). Sağlıkta bu bir yanıltma riskidir.
- Belirsiz otorite: "Uzmanlar günde sekiz bardak su öneriyor." (§4)
- Klişe giriş: "Sağlık, hayatımızın en değerli hazinesidir." (§29, §6)
- Talimatı "-mesi gerekmektedir" kalıbına gömmek: "İlacın aç karnına alınması gerekmektedir." (§18)

**Dokunma:** İlaç ve etken madde adları, doz, birim, kullanım sıklığı ve süresi, yan etki ve uyarı listeleri, "doktorunuza danışın" uyarısı, randevu ve başvuru bilgileri. Doz ya da sıklık hakkında en küçük belirsizlikte değiştirme, sor.

**Yazım:** 500 mg, 5 ml (sayıyla birim arasında boşluk). %0,9 (yüzde işaretinden sonra boşluk yok). Ölçü birimlerinin uluslararası kısaltmaları kullanılır: mg, ml, kg.

**Önce:**
> Ameliyat sonrası iyileşme sürecinizde kendinize zaman tanımanız son derece önemlidir. Endişelenmeniz çok doğaldır. Ağrı kesicilerinizi düzenli olarak kullanmanız, iyileşme yolculuğunuzda size destek olacaktır.

**Sonra:**
> Ameliyattan sonra bir süre dinlenin [kaç gün?]. Ağrı kesicinizi düzenli alın [hangi aralıkla? reçetedeki gibi yazalım].

**Ne değişti:** Talimatlar emir kipine geçti, eksik süre ve aralık soruldu. "Endişelenmeniz çok doğaldır" cümlesi hastaya bilgi vermediği için çıktı. Yazar sıcak bir cümle istiyorsa tek bir somut cümleyle geri gelir: "Sorunuz olursa [telefon] numarasından bize ulaşın."

## Eğitim

**Kim okur:**
- Veli: tarih, saat, yer ve ne yapması gerektiği.
- Öğrenci: yaşına göre sade dil.
- Öğretmen ve idare: mevzuat ve kazanım dili.

**Model burada nasıl yazar:**
- Şişirilmiş amaç cümlesi: "Öğrencilerimizin potansiyellerini en üst düzeye çıkarmak amacıyla..." (§1, §17).
- Moda kavram yığını: "21. yüzyıl becerileri", "bütüncül yaklaşım", "öğrenci merkezli" (§8).
- Üçleme: "eğlenceli, öğretici ve ilham verici bir gün" (§10).
- "Katılımınız büyük önem arz etmektedir" kalıbı (§48).
- Kazanım listelerinde tekdüze fiiller: "kavrar, analiz eder, değerlendirir" (§13).

**Dokunma:** Tarih, saat, sınıf ve şube, ders adları, kazanım kodları, yönetmelik maddeleri, not ve kredi değerleri, ücret ve son başvuru tarihi.

**Yazım:** Saat: 09.30'da, 13.00'te. Belirli bir tarihteki ay adı büyük harfle başlar: 15 Eylül'de. Belirli bir tarih bildirmeyen ay adı küçük: eylülde okullar açılır.

**Önce:**
> Değerli velilerimiz, öğrencilerimizin akademik ve sosyal gelişimlerine katkı sağlamak amacıyla düzenlenecek olan veli toplantımıza katılımınız büyük önem arz etmektedir.

**Sonra:**
> Sayın veliler, veli toplantısını [tarih ve saat] [yer] yapacağız. Toplantıda çocuklarınızın okuldaki gelişimini konuşacağız, gelmenizi rica ediyoruz.

**Ne değişti:** Duyurunun kendisi (ne, ne zaman, nerede) başa geldi. "Akademik ve sosyal gelişime katkı" tek bir somut cümleye indi. "Büyük önem arz etmektedir" yerine düz bir rica geldi.

## Hukuk

**Kim okur:**
- Mahkeme ve karşı taraf: hukuki terim ve kalıp korunur.
- Müvekkil: sade dille ne olduğu ve sonraki adım.
- Kişisel verilerini paylaşan herkes: aydınlatma metni, sözleşme özeti.

**Model burada nasıl yazar:**
- Müvekkile giden e-postada broşür ve önem şişirmesi: "kapsamlı bir hukuki değerlendirme sonucunda" (§8, §1).
- Aydınlatma metninde boş doğru: "Kişisel verilerinizin güvenliği bizim için en önemli önceliktir." (§6)
- Sözleşmeye sızmış pazarlama: "eşsiz hizmet anlayışımızla" (§2).
- Uydurma dayanak: var olmayan karar, madde ya da kanun numarası (§36). Hukukta bu en ağır hatadır. Kaynakta olmayan atıf ekleme, kaynaktaki atıfı da değiştirme.

**Dokunma:** Hukuki terimler (temerrüt, ihtar, fesih, cezai şart), "işbu" gibi kalıplar, madde numaraları, kanun ve yönetmelik adları, süreler, taraf adları, dilekçe ve sözleşmenin yapısı. Hukuki metinde varsayılan mod teşhis ya da hafif dokunuştur. Değişikliği uygulamadan önce sor (bkz. `turler.md`).

**Yazım:** Kurum adlarına gelen ek kesmeyle ayrılmaz: Yargıtaya, Türkiye Büyük Millet Meclisine. Unvana gelen ek kesmeyle ayrılır: Av. Ayşe Yılmaz'a. Sonu noktalı kısaltmaya ek kesmesiz gelir: md.si, vb.leri.

**Önce:**
> Değerli müvekkilimiz, davanızın seyri hakkında sizleri bilgilendirmek isteriz. Mahkeme, kapsamlı bir değerlendirme sonucunda bilirkişi incelemesine karar vermiş olup, sürecin olumlu ilerlediğini söylemek mümkündür.

**Sonra:**
> Sayın [ad soyad], mahkeme dosyanızda bilirkişi incelemesine karar verdi. Bize göre dava şimdilik olumlu ilerliyor. Bilirkişi raporu gelince [ne zaman bekleniyor?] sizi yeniden bilgilendireceğim.

**Ne değişti:** Karar ilk cümleye geldi. Avukatın görüşü aynı temkinle kaldı: "söylemek mümkündür" yerine "bize göre". Sonraki adımın tarihi metinde yok, yer tutucu bırakıldı. "Kapsamlı bir değerlendirme sonucunda" çıktı, mahkemenin değerlendirmesini anlatmıyordu.

## Perakende ve e-ticaret

**Kim okur:**
- Müşteri: ürün sayfası, sipariş ve kargo bildirimi, iade bilgisi.
- Pazaryerindeki satıcı: kural ve komisyon duyurusu.
- Mağaza ve depo ekibi: ekip içi dil.

**Model burada nasıl yazar:**
- Ürün açıklamasında bilgi yerine sıfat: "Tarzınızı yansıtan bu eşsiz çanta, şıklığı ve konforu bir araya getiriyor." (§2, §10)
- Uydurma özellik: veride olmayan "su geçirmez", "ömür boyu dayanıklı" (§7). Ürün açıklamasında bu yanıltıcı reklamdır.
- Kampanyada aciliyet kalıbı: "Kaçırılmayacak fırsat!", "Stoklar tükenmeden hemen keşfedin!" (§2)
- Sipariş e-postasında sohbet artığı: "Siparişiniz hakkında bilmeniz gereken her şey burada!" (§33, §28)

**Dokunma:** Ölçüler, malzeme oranları, beden tablosu, fiyat, kampanya koşulları ve tarihleri, garanti ve iade süreleri, kargo süresi, "stoklarla sınırlıdır" gibi koşul notları.

**Yazım:** %100 pamuk. 1.299,90 TL. Ölçü: 45 x 30 x 15 cm.

**Önce:**
> Tarzınızı yansıtan bu eşsiz sırt çantası, şıklığı, konforu ve fonksiyonelliği bir araya getiriyor. Günlük hayatınızın vazgeçilmezi olacak!

**Sonra:**
> [malzeme] sırt çantası, [hacim] litre. [Kaç gözü var? Dizüstü bilgisayar sığıyor mu, kaç inç?]

**Ne değişti:** Önce metninde ürün hakkında tek bir bilgi yok. Sonra metni bunu açıkça gösteriyor: müşterinin aradığı her bilgi yer tutucu. Sıfatlar ancak bir özelliği anlatıyorsa geri gelir: "Su geçirmez kumaş" (veride varsa).

## Kamu ve yerel yönetim

**Kim okur:**
- Vatandaş: ne olacak, ne zaman, nerede, ne yapmam gerekiyor.
- Basın: açıklama ve bülten.
- Kurum içi: yazışma kuralları ve resmî yazı dili.

**Model burada nasıl yazar:**
- Bürokratik ek yığını: "...kapsamında, ...doğrultusunda, ...amacıyla başlatılan çalışmalar çerçevesinde" (§17).
- Önem şişirmesi: "ilçemize değer katacak", "kentimizin vizyonuna uygun" (§1).
- Kim, ne zaman yapacak belli olmayan edilgen: "Gerekli çalışmalar yapılacaktır." (§18)
- Açılış haberinde vecize: "Bu eser, geleceğe bırakılan en güzel mirastır." (§39)

**Dokunma:** Kurum adları, mevzuat atıfları, başvuru koşulları, ücretler, tarih ve saatler, adresler, kesinti ve kapanış saatleri.

**Yazım:** Kurum adının her kelimesi büyük harfle başlar ve ek kesmeyle ayrılmaz: Büyükşehir Belediyesine, Sağlık Bakanlığından. Tarih: 21.10.2026 ya da 21 Ekim 2026. Saat aralığı: 09.00-17.00.

**Önce:**
> Belediyemiz tarafından vatandaşlarımızın yaşam kalitesinin artırılması amacıyla başlatılan altyapı yenileme çalışmaları kapsamında, Atatürk Caddesi'nde su kesintisi yaşanacaktır.

**Sonra:**
> Atatürk Caddesi'nde altyapı yenileme çalışması yüzünden [tarih] günü [saat aralığı] su kesilecek.

**Ne değişti:** Duyurunun kendisi (kesinti) cümlenin sonundan başına geldi. Vatandaşın ilk sorduğu iki bilgi, tarih ve saat, metinde yok, yer tutucu bırakıldı. "Yaşam kalitesinin artırılması amacıyla" çıktı.

## İnsan kaynakları

**Kim okur:**
- Aday: işin kendisi, koşullar, başvuru yolu.
- Çalışan: duyuru, değerlendirme, politika.
- Yönetici: rapor ve öneri.

**Model burada nasıl yazar:**
- İlanda boş sıfat yığını: "dinamik", "hızlı tempoya ayak uydurabilen", "takım oyuncusu", "analitik düşünme yeteneğine sahip" (§8, §10).
- Ayrımcı okunabilecek kalıp: "genç ve dinamik ekibimize". Yaş ayrımı gibi okunur, metnin sahibine bunu ayrıca söyle.
- Performans değerlendirmesinde şablon övgü: "üstün performansıyla ekibine değer katmaktadır" (§8, §48).
- Ret e-postasında çeviri kalıbı: "Değerli zamanınızı ayırdığınız için teşekkür ederiz. Kariyer yolculuğunuzda başarılar dileriz." (§16, §30)
- Duyuruda "ailemize katıldı" (§44).

**Dokunma:** Pozisyon adı, lokasyon, çalışma modeli, metinde yazan yan haklar, maaş aralığı (yazıyorsa), başvuru son tarihi, kişisel veri notu.

**Yazım:** Unvana gelen ek kesmeyle ayrılır: Ayşe Hanım'a, İnsan Kaynakları Müdürü'ne. Kurum içi birim adına gelen ek ayrılmaz: İnsan Kaynakları Müdürlüğüne.

**Önce:**
> Dinamik ve genç ekibimize katılacak, hızlı tempoya ayak uydurabilen, analitik düşünme yeteneğine sahip, takım çalışmasına yatkın Muhasebe Uzmanı arıyoruz.

**Sonra:**
> Muhasebe Uzmanı arıyoruz. [İşin kendisi: hangi işlemlere bakacak, hangi programı kullanacak?] [Deneyim şartı var mı?]

**Ne değişti:** Sıfatların hiçbiri işin ne olduğunu söylemiyordu. Yerine adayın soracağı sorular geldi. "Genç" çıktı, metnin sahibine nedeni ayrıca yazıldı.

## Pazarlama ve iletişim

**Kim okur:**
- Müşteri: ürünün ne yaptığı, fiyatı, nereden alınacağı.
- Basın: haber değeri olan bilgi, tarih, rakam, alıntı.
- Takipçi: kısa, kişisel, markanın kendi sesi.

**Model burada nasıl yazar:**
- Basın bülteninde önem şişirmesi: "sektörde çığır açan", "öncü markamız" (§1).
- Heyecan anonsu: "heyecanla duyururuz", "gurur duyuyoruz" (§28).
- Uydurma araştırma: "Araştırmalar tüketicilerin %80'inin ... tercih ettiğini gösteriyor." (§4, §7)
- Çağrıda broşür dili: "Hemen keşfedin, ayrıcalıklı dünyamıza katılın." (§2)

**Dokunma:** Kampanya koşulları ve tarihleri, fiyat, yasal dipnotlar, marka ve ürün adları, tescilli slogan, alıntılanan kişinin sözü. Alıntının içinde kalıp görürsen alıntıya dokunma, yazara söyle.

**Yazım:** Marka ve ürün adı metnin sahibinin yazdığı gibi kalır. TDK'ye göre iş yeri adına gelen ek kesmeyle ayrılmaz: Mavi Köşe Bakkaliyesinden. Kampanya tarihi: 1-15 Kasım.

**Önce:**
> Sektörün öncü markası X, yenilikçi yaklaşımıyla tüketicilere eşsiz bir deneyim sunacak olan yeni ürün serisini heyecanla duyurdu.

**Sonra:**
> X, yeni ürün serisini [tarih] duyurdu: [seride hangi ürünler var, fiyat aralığı ne?]. [Seriyi öncekilerden ayıran somut özellik ne?]

**Ne değişti:** Haber cümlesi (kim, neyi, ne zaman duyurdu) kaldı. Okurun ilk soracağı bilgiler metinde olmadığı için yer tutucu oldu. "Öncü", "yenilikçi", "eşsiz deneyim" ve "heyecanla" çıktı.
