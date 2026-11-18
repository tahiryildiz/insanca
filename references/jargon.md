# Alan terimleri ve iş jargonu

> Bu dosya MesutARIDORU'nun [İnsanlık öldü mü?](https://github.com/MesutARIDORU/insanlik-oldu-mu) skill'indeki `references/jargon.md` dosyasından uyarlandı (MIT lisansı). Kalıp kodları insanca'nın § numaralarına çevrildi. Yabancı terime gelen ek ve "uç nokta" türü zorla çeviriler için `yazim-ve-terim.md` (§54) geçerlidir; bu dosya ona kitle ayrımını, alan tablolarını, plaza dilini ve moda sözleri ekler.

Teknik, kurumsal ya da bir alana özgü metni düzeltmeden önce bu dosyayı oku. Alanın genel rehberi (`alanlar.md`) okuru ve hassas noktaları anlatır, bu dosya terimleri. Burada ölçü sözlük değil, kullanım: Bir terimin "doğru" karşılığı, metnin okurunun gerçekten kullandığı sözdür. Sözlükte bulunup kullanımda tutmamış karşılıklar metni yapaylaştırır. Örneğin "deadline" için "süre sonu" demek, ekip içi bir yazışmayı resmî tebliğe çevirir. Böyle karşılıklar önerme.

## Altı kural

1. **Önce kitleyi belirle.**
   - Geliştirici ekibe ya da şirket içine giden metinde yerleşik İngilizce terimler kalır.
   - Genel okura giden metinde insanların gerçekten kullandığı Türkçe karşılık tercih edilir.
   - Resmî ya da kamuya dönük metinde kurumun kendi terimlerine uyulur.
2. **Bir kavrama tek ad.** Aynı metinde "deploy", "yayına alma" ve "dağıtım" dönüşümlü kullanılıyorsa iz budur (§54). Birini seç, sonuna kadar onu kullan.
3. **Dokunulmayanlar.** Kod, komut, dosya ve klasör adları, ürün ve şirket adları, arayüzdeki düğme ve menü etiketleri, API ve kütüphane adları olduğu gibi kalır.
4. **Ek getirme.** Yabancı terime Türkçe ek kesme işaretiyle gelir: PR'ı, API'ye, deploy'dan. Fiil yaparken yaygın biçim "etmek"tir: deploy etmek, merge etmek. "-lemek" eki konuşmada yaygındır ("deploy'lamak"), yazıda daha az görülür. Ekip içi mesaj yazıya dökülmüş konuşmadır, orada ikisi de doğaldır ("branch'i push'ladım", "merge'lendi"); yazar hangisini kullanıyorsa o kalır, aynı mesajda ikisi karışmaz.
5. **Açıklama bir kez.** Genel okurun bilmeyebileceği bir terimi ilk geçtiği yerde bir kez aç, sonra açıklamasız kullan. Her terime parantez eklemek ayrı bir kalıptır (§31).
6. **Uydurma.** Bir terimin Türkçesi yerleşmemişse yeni karşılık icat etme. İngilizcesini bırak ya da ne yaptığını anlat.

## Yazılım ve ürün geliştirme

| Terim | Ekip içi, geliştirici | Genel okur | Not |
|---|---|---|---|
| deploy | deploy etmek | canlıya almak, yayına almak | "Konuşlandırmak" ekiplerde pek kullanılmaz (aşırı çeviri) |
| release | release, sürüm | yeni sürüm | |
| commit | commit atmak | (ayrıntıya girme) | "Taahhüt" aşırı çeviri |
| pull request | PR açmak | değişiklik önerisi | "Çekme isteği" aşırı çeviri |
| merge | merge etmek | birleştirmek | |
| branch | branch | (ayrıntıya girme) | |
| bug, fix | bug, fix | hata, düzeltme | |
| sprint | sprint | iki haftalık çalışma dönemi | Genel okura gerekiyorsa bir kez açıkla |
| backlog | backlog | bekleyen işler | |
| roadmap | roadmap, yol haritası | yol haritası | "Yol haritası" iki kitlede de yerleşti |
| feature | feature, özellik | özellik | |
| dashboard | dashboard, panel | panel | |
| server, cloud | sunucu, cloud | sunucu, bulut | |
| cache | cache | önbellek | |
| API | API | API | Genel okura bir kez açıklanabilir: "başka yazılımların bağlandığı arayüz" |
| prompt | prompt | komut, talimat | "İstem" karşılığı henüz pek yaygın değil |
| fine-tuning | fine-tuning | ince ayar | |
| onboarding | onboarding | ilk adımlar, tanıtım turu | Ürün içinde yeni kullanıcıya gösterilen akış |
| login | login, giriş | giriş yapmak, oturum açmak | |
| online, offline | online, offline | çevrim içi; internet olmadan | "Çevrim dışı çalışır" yerine "internet olmadan da çalışır" daha doğal |
| feedback | feedback | geri bildirim | "Geri bildirim" her kitlede yerleşti |
| update | update, güncelleme | güncelleme | |
| link | link | bağlantı (resmî), link (gündelik) | |

## Finans

| Terim | Ekip içi, uzman | Müşteriye | Not |
|---|---|---|---|
| ekstre | ekstre | hesap özeti, ekstre | "Ekstre" müşteride de yerleşti |
| vade | vade | vade, son ödeme tarihi | |
| faiz, kâr payı | kurumun kullandığı terim | aynı | Katılım bankası "kâr payı" der, "faiz"e çevirme |
| yıllık maliyet oranı | YMO | yıllık maliyet oranı | İlk geçtiği yerde açık yaz |
| EFT, FAST, havale | EFT, FAST | para transferi, EFT | Kısaltmalar müşteride de yerleşti |
| reconciliation | mutabakat | (müşteriye gitmez) | |
| cash flow | nakit akışı | (müşteriye gitmez) | |
| likidite | likidite | nakit, paraya çevrilebilirlik | |
| temerrüt | temerrüt | ödemenin gecikmesi | Sözleşme ve ihtarda "temerrüt" kalır |
| portföy | portföy | yatırımlarınız | |

**Modelin izi:** "finansal çözüm ortağınız", "finansal okuryazarlık yolculuğu", "size özel finansal ayrıcalıklar" (§2). Aynı tutara iki üç ad vermek: "dönem borcu", "ekstre tutarı", "kart borcu" (§54).

## Sağlık

| Terim | Hekime, sağlık çalışanına | Hastaya | Not |
|---|---|---|---|
| hipertansiyon | hipertansiyon | yüksek tansiyon | Gerekiyorsa terim bir kez parantezde |
| miyokard enfarktüsü | MI, miyokard enfarktüsü | kalp krizi | |
| semptom | semptom, bulgu | belirti | |
| endikasyon | endikasyon | ne için kullanıldığı | |
| kontrendikasyon | kontrendikasyon | kullanmaması gerekenler | Prospektüs başlığıysa değiştirme |
| oral, p.o. | oral, p.o. | ağızdan | |
| taburcu, poliklinik | taburcu, poliklinik | aynı | İkisi de hastada yerleşti |
| hasta, danışan | kurumun seçtiği | kurumun seçtiği | Aynı metinde karıştırma |

**Modelin izi:** "sağlıklı bir yaşamın vazgeçilmez parçası", "bütüncül sağlık yaklaşımı", "uzmanlar öneriyor" (§8, §4). Hastaya giden metne Latince terim yığmak ya da hekime giden metni sulandırmak (§21).

## Hukuk

| Terim | Mahkemeye, karşı tarafa | Müvekkile, okura | Not |
|---|---|---|---|
| müvekkil | müvekkil | (müvekkile "siz" diye yazılır) | |
| ihtarname | ihtarname | noterden gönderilen resmî uyarı | Metindeki terim silinmez, açıklama eklenir |
| tebligat | tebligat | resmî bildirim, tebligat | |
| fesih | fesih | sözleşmenin sona erdirilmesi | |
| temerrüt | temerrüt | borcun zamanında ödenmemesi | |
| icra takibi | icra takibi | icra takibi | Yerleşik |
| KVKK | KVKK | Kişisel Verilerin Korunması Kanunu | İlk geçtiği yerde açık yaz |
| aydınlatma metni, açık rıza | aynı | aynı | Yasal adlar değişmez |

**Modelin izi:** Hukuki metne sızan pazarlama sıfatları ("eşsiz hizmet anlayışımızla"), kaynakta olmayan karar ve madde numarası (§36). Hukuki terimi "sadeleştirmek" için silmek. Terim kalır, gerekiyorsa yanına açıklama gelir.

## Kamu ve yerel yönetim

| Kurum dili | Vatandaşa giden duyuruda | Not |
|---|---|---|
| müracaat | başvuru | |
| tebliğ etmek | bildirmek | Resmî yazışmada "tebliğ" kalır |
| hizmete sunulmuştur | açıldı, hizmete girdi | |
| vatandaşlarımız | siz (doğrudan seslenme) | Kurum dilinde "vatandaşlarımız" yaygın, duyuruda "siz" daha doğrudan |
| ilgi (a) yazı | (vatandaşa gitmez) | Resmî yazışma düzeni, değiştirme |
| ihale, kamulaştırma, imar | aynı | Yerleşik terimler |

**Modelin izi:** "...kapsamında, ...doğrultusunda, ...çerçevesinde" yığını (§17), "hayata geçirilmiştir", "değer katacak", "vizyon projesi" (§1). Mevzuattaki adı "sadeleştirmek": belge ve kanun adları olduğu gibi kalır.

## Perakende ve e-ticaret

| Terim | Ekip içi | Müşteriye | Not |
|---|---|---|---|
| checkout | checkout, ödeme adımı | ödeme | |
| cart abandonment | sepet terk oranı | (müşteriye gitmez) | |
| SKU | SKU, stok kodu | ürün kodu | |
| conversion | dönüşüm, conversion | (müşteriye gitmez) | |
| stock-out | stok bitti | tükendi | |
| cayma hakkı | cayma hakkı | cayma hakkı | Yasal terim, değişmez. Süre kaynakta nasıl yazıyorsa öyle |
| iade, değişim, kargo takibi | aynı | aynı | Yerleşik |

**Modelin izi:** Ürün sayfasında "eşsiz", "vazgeçilmez", "tarzınızı yansıtan" (§2), veride olmayan özellik (§7), bildirimde "sen" ile "siz"in karışması (§21).

## İnsan kaynakları

| Terim | Ekip içi | Adaya, çalışana | Not |
|---|---|---|---|
| onboarding | onboarding | işe başlangıç, oryantasyon | |
| offboarding | offboarding | ayrılış süreci | |
| headcount | headcount, kadro | kadro, çalışan sayısı | |
| turnover | turnover | işten ayrılma oranı | |
| performance review | performans değerlendirmesi | aynı | |
| benefits | yan haklar | yan haklar | |
| remote, hybrid | remote, hibrit | uzaktan, hibrit | "Hibrit" yerleşti |
| mülakat | mülakat | görüşme, mülakat | |

**Modelin izi:** "kariyer yolculuğu", "ailemize katıldı", "dinamik ekip", "değer katan" (§8, §44). İlanda yaşa ya da cinsiyete işaret eden kalıplar ("genç ekip"). Bunu metnin sahibine ayrıca söyle.

## Eğitim

| Kurum dili | Veliye, öğrenciye | Not |
|---|---|---|
| kazanım | öğrencinin bu derste öğreneceği | Öğretim programında "kazanım" kalır |
| ölçme ve değerlendirme | sınav ve not | |
| devamsızlık, karne, e-Okul | aynı | Yerleşik |
| öğretim programı, müfredat | aynı | İkisi de yerleşik, aynı metinde birini seç |
| rehberlik servisi | rehberlik servisi, rehber öğretmen | |

**Modelin izi:** "21. yüzyıl becerileri", "öğrenci merkezli bütüncül yaklaşım", "potansiyelini en üst düzeye çıkarmak" (§8, §1). Veli duyurusunda tarih, saat ve yerin cümlenin sonuna gömülmesi (Sicil Ayarı: ana mesaj ilk cümlede).

## Pazarlama ve iletişim

| Terim | Ajans, ekip içi | Rapor ya da genel okur | Not |
|---|---|---|---|
| engagement | engagement, etkileşim | etkileşim | |
| reach | reach, erişim | erişim | |
| awareness | awareness, bilinirlik | bilinirlik | |
| CTA | CTA | harekete geçirici çağrı | Genel okura çoğu zaman hiç gerekmez |
| lead | lead | potansiyel müşteri | |
| ROI | ROI | yatırım getirisi | |
| influencer | influencer | influencer, içerik üreticisi | İkisi de yaygın |

**Modelin izi:** "markamız heyecanla duyurur", "sektörün öncüsü" ve kaynağı belirsiz araştırma yüzdeleri (§28, §1, §4).

## Ofis ve iş dili ("plaza Türkçesi")

Bu fiiller iç yazışmada ve konuşmada doğal durur. Müşteriye, basına ya da genel okura giden metinde sırıtır. Yapay zeka bunları ya hiç kullanmaz ya da yanlış yerde kullanır.

| Söz | Genel okura ya da resmî metinde |
|---|---|
| aksiyon almak | harekete geçmek, adım atmak, bir şey yapmak |
| challenge etmek | itiraz etmek, sorgulamak |
| challenge (isim) | zorluk |
| toplantı set etmek | toplantı ayarlamak |
| sync olmak | konuşmak, bir araya gelmek |
| approve almak | onay almak |
| check etmek | kontrol etmek, bakmak |
| focus olmak | odaklanmak |
| efor sarf etmek | emek vermek, uğraşmak |
| deadline | teslim tarihi, son gün |
| insight | bulgu, gözlem (pazarlamada "içgörü" yerleşti) |
| target | hedef |
| case | örnek, vaka, durum |
| brief | kısa bilgi notu (ajans dilinde "brief" yerleşik) |
| kick-off | başlangıç toplantısı |
| networking | tanışma, ilişki kurma |
| mindset | bakış açısı, zihniyet |
| skill | beceri |
| proaktif | önceden davranan (iş dilinde "proaktif" yerleşti) |
| KPI | performans göstergesi (iş metninde KPI kalabilir) |

## Moda sözler: yerine ne söylenir

Bu sözler (§8) ürünün ne yaptığını söylemeden teknolojik görünmenin yoludur. Çare her seferinde aynı soru: **Somut olarak ne oluyor?** Cevap metinde varsa onu yaz, yoksa yer tutucu bırak ve kullanıcıya sor. Asla uydurma.

| Moda söz | Sorulacak soru | Örnek yön (bilgi metinde varsa) |
|---|---|---|
| dijital dönüşüm | Hangi iş dijitale taşındı? | "Siparişleri artık internetten alıyoruz." |
| uçtan uca | Hangi adımları kapsıyor? | "Siparişten faturaya kadar her adım aynı yerde." |
| ölçeklenebilir | Büyüyünce ne oluyor? | "Kullanıcı sayısı artınca yavaşlamıyor." |
| sorunsuz entegrasyon | Hangi sistemlerle bağlanıyor? | "Muhasebe programınıza doğrudan bağlanıyor." |
| yapay zeka destekli | Yapay zeka hangi işi yapıyor? | "Gelen talepleri konusuna göre ayırıyor." |
| inovasyon, inovatif | İlk kez neyi yapıyor? | "Bunu yapan ilk yerli uygulama." (doğruysa) |
| ekosistem | Hangi ürünler ya da ortaklar? | "Mağaza, kargo ve ödeme aynı hesaptan." |
| sinerji | Birlikte çalışınca ne oluyor? | "Satış ekibi destek kayıtlarını görüyor." |
| değer önerisi, katma değer | Müşteri ne kazanıyor? | "Faturayı beş dakikada kesiyorsunuz." |
| yeni nesil, son teknoloji | Eskisinden farkı ne? | "Önceki sürümün iki katı hızlı." (rakam metinde varsa) |
| optimize etmek | Hızlandı mı, ucuzladı mı, kısaldı mı? | "Rapor süresi on dakikadan ikiye indi." (rakam metinde varsa) |
| verimliliği artırmak | Ne kadar zaman ya da para kazanılıyor? | Rakam yoksa: "[ne kadar? elinde rakam var mı?]" |

## Aşırı çeviri: geliştirici kitlesinde iz

Aşağıdaki karşılıklar sözlüklerde ve bazı resmî belgelerde geçer, ama geliştirici ekiplerin günlük dilinde pek kullanılmaz. Bir ekip içi metinde bunlar görünüyorsa metni büyük ihtimalle bir model çevirmiştir.

- konuşlandırmak (deploy)
- çekme isteği, birleştirme isteği (pull request, merge request)
- taahhüt etmek (commit)
- kapsayıcı (container; ekiplerde "container" ya da "konteyner")
- ara katman yazılımı (middleware)
- istem mühendisliği (prompt engineering)
- sürekli entegrasyon ve sürekli dağıtım (CI/CD; ekiplerde kısaltma kullanılır)
- dal, dalı itmek (branch, push; ekiplerde "branch'i push'lamak" ya da "push etmek")
- uç nokta (endpoint)
- gömme, parça (embedding, chunk)

**Türetilmiş biçimler.** Model yalnız adı değil, addan türeyen sıfat ve fiili de çevirir, iz çoğu zaman orada kalır: "tracked" için "takipli dosya", "merged" için "birleştirilmiş dal", "seeded" için "tohumlanmış veri". Ekipte bunun iki doğal yolu var. Ya terim Türkçe ek alır ("commit'li", "merge'lendi", "seed'lenmiş veri") ya da olan düz Türkçeyle anlatılır ("git bu dosyayı takip ediyordu"). İkisinin arası, yani sözlükte olmayan bir Türkçe sıfat, kimsenin ağzından çıkmaz.

**İstisna:** Bazı kurumlar resmî belgelerinde bu karşılıkları bilerek kullanır. Metin böyle bir kurumun belgesiyse ya da yazar bu terimleri tutarlı biçimde seçmişse kurumun terimine uy.
