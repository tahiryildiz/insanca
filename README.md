# İnsanca

Yapay zeka Türkçesi kokan metni insan Türkçesine çevirir.

ChatGPT'ye Türkçe bir yazı yazdırdın ve okuyunca sen bile "bunu yapay zeka yazmış" dedin, değil mi? "Günümüzde..." diye açılıyor, her cümle "-maktadır" ile bitiyor, her iddia "mesele X değil, Y" kalıbına sarılmış, son paragraf da "Sonuç olarak..." diye başlayıp kimseye bir şey söylemeyen iyimser bir cümleyle kapanıyor.

İnsanca bu sorunu çözmek için var. Bir agent skill'i olarak metni alıyor, yapay zeka kokusunu tek tek teşhis ediyor ve gerçek bir insanın kaleminden çıkmış gibi okunana kadar yeniden yazıyor. Tamamı düz Markdown olduğu için skill destekleyen her ortamda (Claude Code, OpenCode, Codex vb.) çalışıyor.

İki parçadan oluşuyor: **48 kalıp** yapay zeka izini yakalıyor, **17 akış kuralı** da boşalan yere gerçek Türkçenin ritmini koyuyor. Çünkü kalıp temizlemek işin yarısı; "kapsamlı"yı silip yerine steril bir cümle bırakırsan metin yine kağıt tadı verir.

## Yapay zeka Türkçesi nasıl kokar?

48 kalıbı altı grupta topladım. Aşağıdaki tablolar hızlıca fikir vermek için; her kalıbın uzun önce/sonra örneği [SKILL.md](SKILL.md) içinde.

### 1. Ritim kokusu

Türkçede cümleler genellikle yüklemle biter. Yapay zeka her cümleyi aynı ekle bitirince ortaya istemeden kafiyeli bir metin çıkıyor: kurulmuştur, bulunmaktadır, vermektedir... Bir insan yazarken bunu farkında olmadan kırar. Araya devrik bir cümle girer, bir soru sorar, kısa cümleleri virgülle birbirine bağlar. Yapay zeka ise aynı kalıpta devam eder.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| "-maktadır" kafiyesi | "kurulmuştur... bulunmaktadır... vermektedir..." | "2020'de kuruldu, merkezi İstanbul'da." |
| Metronomik ritim | Bütün cümleler 15-20 kelime | Kısa ve uzun cümleler iç içe |
| Kesik cümle yığını | "Kurallar yıkıldı. Ezberler bozuldu." | Kısa cümleleri virgülle bağla |
| Bağlaç yığını | "Ayrıca... Öte yandan... Dolayısıyla..." | Geçişi fikrin kendisiyle yap |
| Paragraf sonu mini özeti | Her paragraf "Kısacası..." ile bitiyor | Paragrafı geçişle bitir |
| Açılış tekrarı | Dört cümle üst üste "Uygulama..." ile başlıyor | Açılışları çeşitlendir |

### 2. Kelime ve kalıp kokusu

Bazı kelimeler artık resmen yapay zeka kelimesi olarak biliniyor: kapsamlı, kilit, yenilikçi, dönüşüm yolculuğu... Ama tek başına bir kelime bir şey kanıtlamaz. Asıl sorun şu: Bu kelimeler hep birlikte geliyor ve altlarındaki cümle çoğu zaman hiçbir şey söylemiyor.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| AI kelime dağarcığı | "kapsamlı... kilit... değer katmak... oyun değiştirici" | Somut, sade karşılıklar |
| Önem şişirmesi | "kritik bir dönüm noktası olmuştur" | Ne olduğunu söyle, yorumu okura bırak |
| "Mesele X değil, Y" | "Bu sadece bir taktik değil, zihniyet değişimi" | İddiayı doğrudan söyle |
| Üçleme kuralı | "ilham, bilgi ve networking" | Doğal sayıda öğe |
| Yalancı aralıklar | "küçük alışkanlıklardan büyük hedeflere" | Konuları doğrudan listele |
| Eşanlamlı döngüsü | "şirket... firma... kuruluş... marka" | Aynı kelimeyi tekrar etmekten korkma |
| "-arak" sahte derinliği | "toprakla kurulan bağı gözler önüne sererek" | Kuyruğu kes ya da kaynaklı bilgiye çevir |
| Boş doğrular | "Güven zamanla inşa edilir" | Tersi savunulabilir, somut iddia |
| Aforizma formülleri | "Tasarım, güvenin dilidir" | Somut iddiayı yaz |
| Dolgu ifadeler | "Önemle belirtmek gerekir ki" | Sil, doğrudan söyle |
| Aşırı kaçamak | "etkili olabileceği düşünülebilir" | "etkileyebilir" |
| Gri kelime duvarı | Her kelime en güvenli seçim | Beklenmedik ama yerinde detay |
| "Asıl" takıntısı ve iki nokta tanımları | "Asıl mesele şu: X" | Önce söyle, sonra adlandır |
| Yapı nakli | "X'le kalmıyor, Y oluyor" (kalıp boyanmış) | Kıyafeti değil iskeleti değiştir |
| Koşaç kaçışı | "sergi alanı işlevi görmektedir" | "Galeri, derneğin sergi alanı." |

### 3. Çeviri kokusu

Bu gruptaki metinler sanki önce İngilizce yazılmış da sonra Türkçeye çevrilmiş gibi okunur. Mesela Türkçede özneyi sürekli söylemeyiz; kim olduğu zaten fiilden anlaşılır. Yapay zeka ise her cümleye bir "siz", bir "ben" koyar, İngilizce "a/an" alışkanlığıyla her isme "bir" ekler, üstüne bir de "karmaşık bir goblen" gibi Türkçede kimsenin kurmadığı metaforlar taşır.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| Çeviri kokusu | "karmaşık bir goblen", her cümlede "siz" | Türkçe düşünülmüş kurulum |
| Anons cümleleri | "Gelin derinlemesine dalalım" | İçerikle başla |
| Her Kelimesi Büyük Başlık | "Yükselişi Ve Geleceği" | "Yükselişi ve geleceği" |

### 4. Ton kokusu

Yapay zekanın ton ayarı bir türlü tutmaz. Ya fazla över, ya kurum bülteni gibi konuşur, bazen de ikisini aynı paragrafta yapar :)

| Kalıp | Önce | Sonra |
|-------|------|-------|
| Yağcı ton | "Harika bir soru! Kesinlikle haklısınız!" | Doğrudan cevap ver |
| Terapist modu | "Yalnız değilsiniz, kendinizi suçlamayın" | Konuya gir |
| Sahte samimi açılış | "Dürüst olmak gerekirse..." | Lafı dolandırmadan söyle |
| Broşür dili | "eşsiz deneyim, büyüleyici doku" | Pazarlama değil, bilgi |
| Sicil kayması | "Kanka bu araç olanak tanımaktadır" | Tek sicil seç, orada kal |
| Retorik soru-cevap | "Peki bu ne demek? Cevap basit:" | Doğrudan anlat |
| Sohbet/arayüz artıkları | "Umarım yardımcı olur!", "Regenerate response" | Tamamen kaldır |
| Bürokratik dolgu | "kapsamında... doğrultusunda... noktasında" | Somut fiillerle sade cümle |
| Edilgen anlatım | "ayrılması gerekmektedir" | Kimin yaptığı belli, etken cümle |

### 5. Biçim kokusu

Bazen metnin görünüşü bile yetiyor. Uzun tire mesela: Türkçede zaten neredeyse hiç kullanılmadığı için tek başına güçlü bir işaret. Onu silip yerine noktalı virgül koymak da çözüm sayılmıyor; alan testlerinde 10 noktalı virgüllü bir metin gördük, hepsi göçmüş tireydi.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| Uzun tire | "ücretsiz — şimdilik" | Nokta, virgül, iki nokta veya parantez |
| Kalın vurgu bolluğu | "**OKR**, **KPI**, **Kanvas**" | Vurguyu gerçekten gereken yere sakla |
| Gereksiz maddeleme | "**Performans:** Performans artırıldı" | Düz yazıya çevir |
| Emoji | "🚀 Lansman: 💡 İçgörü:" | Kaldır |
| Parantez açıklaması takıntısı | "temettü (kâr payı)" | Okurun bildiğini açıklama |
| Noktalama ve şapka | Noktalı virgül bolluğu, "hâlâ/zekâ" | Şapkasız ve tutarlı yazım |

### 6. Güven ve kurgu kokusu

Bu son grup en sinsi olanı, çünkü teller tek tek cümlelerde değil metnin iskeletinde ve kaynaklarında saklanıyor.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| Belirsiz kaynak | "Uzmanlara göre kritik rol oynuyor" | "DSİ'nin 2023 raporuna göre..." |
| Uydurma örnekler | "Ayşe Hanım cirosunu 90 günde 3'e katladı" | Gerçek, doğrulanabilir örnek |
| Uydurma kaynak / bilgi sınırı | "kaynaklarda sınırlı bilgi... muhtemelen..." | Bilinmeyeni söyle ya da çıkar |
| Şablon "zorluklar" bölümü | "Tüm bu zorluklara rağmen..." | Gerçek soruna dair somut veri |
| Klişe girizgah | "Günümüzde... vazgeçilmez hale geldi" | İlk cümlede asıl bilgi |
| Jenerik kapanış | "Sonuç olarak... parlak bir gelecek" | Somut plan veya bilgi |
| Özet sandviçi | Kapanış girişi tekrarlıyor | Sona yeni bir şey koy |
| Kurgu klişeleri | "İçini bir huzursuzluk dalgası kapladı" | Duyguyu sahneyle göster |
| Aşırı düzeltme kokusu | Zorlama kesik cümleler, sahte pürüzler | Ölçülü bırak, bir iki pürüz yeter |

## Gerçek Türkçe böyle akar

Kalıpları temizlemek yetmiyor, boşalan yere bir şey koymak gerekiyor. Skill'in ikinci yarısı bu yüzden var: Gerçek Türkçe düzyazıdan çıkarılmış 17 akış kuralı. Kaynaklar sahici; 2012-2019 arası köşe yazıları, denemeler, bloglar, Ekşi Sözlük'ün beğenilen entry'leri, Hüseyin Rahmi Gürpınar romanı ve Türk kompozisyon geleneği. Birkaçı:

- **Fiilleri virgülle zincirle.** Gerçek köşe yazarı tek cümlede on fiil dizer: "başvurdu, izin istedi, şehre gitti, kabirleri buldu, inceledi, rapor yazdı, gönderdi." Kısa cümleleri noktayla dizmek makine ritmi, virgülle akıtmak insan ritmi.
- **Bağlacı gezdir.** "Çünkü" ve "ama" hep cümle başında oturmaz: "Onların da bir kısmı kayda düştü çünkü."
- **Etiketi vuruştan sonra koy.** Yapay zeka "Asıl soru şu: X" diye anons eder; insan önce söyler, sonra adlandırır: "...değiştirecek mi? Asıl soru budur."
- **Ritmi duygu eğrisine bağla.** Sükûnette cümle uzar, şok anında üç kelimeye düşer. Kısa cümle sahneyi ilerletiyorsa yerindedir, poz veriyorsa kalıptır.
- **Duyguyu bedenle göster.** "Korktu" değil; benzi uçsun, elleri titresin.
- **İkilemeyi geri getir.** "Gittik gittik", "mor mor", "hıçkıra hıçkıra": Türkçenin öz ritim aracı ve çeviri metinlerde ilk kaybolan şey.
- **Deyimi tuz gibi kullan.** 150-250 kelimede en fazla bir deyim, kalıp dokunulmaz, çekim serbest. Tema tema düzenlenmiş güvenli hazne [references/deyimler.md](references/deyimler.md) dosyasında: Ömer Asım Aksoy kaynaklı 115 deyim, 48 atasözü, yanlış bilinen şekiller ve anlam tuzakları.

Tamamı (miş'li geçmişle aktarım, devrikliğin karakter sesine tahsisi, duruluk ölçüsü, kapanış çeşitliliği...) [SKILL.md](SKILL.md) içinde.

## Sayılarla da bakar

İnsanlar bir metnin yapay zeka yazması olup olmadığını hissederek pek bilemiyor; araştırmalarda isabet oranı yazı tura seviyesinde çıkıyor. Dedektörler bu yüzden hissetmek yerine sayıyor. Ben de aynısını yaptım: GPTZero klonları, [GLTR](https://github.com/HendrikStrobelt/detecting-fake-text), [DetectGPT](https://arxiv.org/abs/2301.11305) ve açık kaynak slop dedektörlerinin kaynak kodlarına bakıp ölçtükleri şeyleri skill'e taşıdım. İnsanca nihai metinde cümle uzunluğu çeşitliliğini, açılış kelimesi dağılımını, zarf-fiil kuyruğu payını, uzun tire ve noktalı virgül sayısını, üçleme yoğunluğunu, iki nokta ve "asıl" sayımını, ilk-son paragraf örtüşmesini kontrol ediyor.

Bu araştırmadan iki önemli ders çıktı:

- **Kelime telleri eskiyor, yapısal teller kalıyor.** "Delve" kelimesi damgalanınca modeller kullanmayı bıraktı; "kapsamlı" da muhtemelen aynı yoldan gidecek. Ama tekdüze ritim model nesli değişse de duruyor. Türkçe araştırması da bunu doğruluyor: İnce ayarlı BERT, Türkçe insan/AI metnini yüzde 97 isabetle ayırıyor ve sinyali kelimelerden değil ritimden alıyor.
- **Aşırı düzeltme de bir imza.** Turnitin 2025'te humanizer araçlarının çıktısına özel tespit modülü duyurdu. İnsanca bu yüzden zorlama kesik cümlelere ve sahte pürüzlere kaçmıyor. Zaten amaç dedektör kandırmak değil, iyi Türkçe yazmak.

## Alan testlerinden

Skill gerçek yapay zeka metinleri üzerinde geliştirildi, her turda kullanıcı eleştirisiyle sıkılaştı. İki örnek ölçüm:

| Metin | "X değil, Y" | Noktalı virgül | Ort. cümle | Kafiye payı |
|-------|--------------|----------------|------------|-------------|
| Kurumsal yapay zeka makalesi | 13 → 0 | 0 → 0 | 7,6 → 16,8 kelime | %22 → %14 |
| E-ticaret trend yazısı | 12 → 0 | 10 → 0 | 15,7 → 14,5 kelime | %19 → %12 |

İlk metin kesik cümle yığınıydı (31 tek satırlık paragraf), ikincisi orta boy metronomdu; ikisinin de iskeleti "X değil, Y" kalıbıydı. Testlerden çıkan en önemli ders skill'in kendisine de girdi: Kelimeleri değiştirip cümle iskeletini korumak kalıbı kaldırmıyor (yapı nakli kalıbı buradan doğdu) ve doğallaştırıcının kendi tikleri de birer kalıp; "asıl" düşkünlüğünü ve her metni soruyla bitirme alışkanlığını bu testler yakaladı.

## Neyi bozmaz

Temizlik kadar önemli bir konu daha var: Sağlam metni katletmemek. Kusursuz dilbilgisi tek başına şüphe sebebi değil, editörden geçmiş olabilir. Akademik metindeki "-maktadır" da öyle, orada doğru üslup zaten o. Tek tük "kapsamlı" veya "ayrıca" görmek bir şey kanıtlamaz; işaret olan, bunların hep birlikte gelmesi. Teller eş ağırlıkta da değil: "Bir yapay zeka modeli olarak" ifadesi kesin kanıtken tek bir "kapsamlı" zayıf bir sinyal.

Özne-yüklem uyumsuzluğu, mantık yanlışı gibi anlatım bozuklukları ise insan işidir; yapay zeka bu hataları nadiren yapar. İnsanca bunları yapay zeka teli saymaz, dil bilgisi hatası olarak ayrıca düzeltir. Alıntılara, başlıklara ve özel adlara hiç dokunmaz. İnsan işaretlerini de korur: Tuhaf ve spesifik detaylar, karışık duygular, ara sözler, devrik cümleler, noktalamaya sızmış duygu... Bunları görünce skill metne daha az dokunur, daha çok değil.

## Nasıl çalışır

Tek geçişte yazıp bırakmıyor, üç adımlık bir döngü uyguluyor:

1. **Taslak** — kalıpları temizleyip metni yeniden yazar.
2. **Denetim** — kendi taslağına iki soru sorar: "Bu metni hala bariz yapay zeka yapan ne?" ve "Kalıpları kaldırdım mı, yoksa yeniden mi giydirdim?" Sayısal eşikleri de burada kontrol eder.
3. **Final** — kalan telleri giderip nihai metni teslim eder.

## Kurulum

Skills CLI ile:

```bash
npx skills add tahiryildiz/insanca
```

Claude Code eklentisi olarak:

```
/plugin marketplace add tahiryildiz/insanca
/plugin install insanca@insanca
```

Elle kurmak istersen repoyu ortamının skill dizinine klonlaman yeterli:

```bash
git clone https://github.com/tahiryildiz/insanca.git ~/.claude/skills/insanca
```

## Kullanım

```
/insanca

[metnini buraya yapıştır]
```

Ya da doğrudan iste: "Şu metni doğallaştır: ..."

### Kendi sesinle

Jenerik temiz çıktı yerine kendi tarzını istiyorsan, kendi yazından 2-3 paragraf ver:

```
/insanca

Ses eşleştirmesi için kendi yazımdan bir örnek:
[kendi yazın]

Şimdi şu metni doğallaştır:
[yapay zeka metni]
```

Skill senin cümle ritmini, kelime seviyeni ve alışkanlıklarını çıkarıp yeniden yazımı onlarla kuruyor.

## Örnekler

Üç ayrı türden örnek: gündelik hayat, iş ve genel kültür. Üçüncüsü önemli bir şeyi de gösteriyor; ansiklopedik metinde skill kişilik enjekte etmiyor, sicil bilgilendirici kalıyor, sadece kalıplar gidiyor.

### 1. Gündelik hayat: tatil yazısı

**Önce:**

> Günümüzde şehir hayatının stresinden uzaklaşmak isteyenler için hafta sonu kaçamakları hayatımızın vazgeçilmez bir parçası haline geldi. Geçtiğimiz hafta sonu iki unutulmaz gün geçirdiğim Ayvalık, beklentilerimi fazlasıyla karşıladı!
>
> Ege'nin kalbinde yer alan Ayvalık, zengin tarihi ve büyüleyici doğasıyla ziyaretçilerine eşsiz bir deneyim sunuyor. Taş evleri, dar sokakları ve zeytinlikleriyle bu şirin ilçe — tam anlamıyla bir açık hava müzesi — her köşesinde ayrı bir hikaye barındırıyor.
>
> Sonuç olarak Ayvalık, sadece bir tatil beldesi değil, aynı zamanda bir yaşam biçimi. Tekrar gider miyim? Kesinlikle! Siz de yoğun tempodan uzaklaşmak istiyorsanız, bu büyüleyici ilçe sizi bekliyor. ✨

**Sonra:**

> Geçen hafta sonu iki günlüğüne Ayvalık'a kaçtık. Dönüşte arabada hesapladım, iki günün neredeyse yarısı yemek masasında geçmiş...
>
> Cumartesi sabahı Cunda'da kahvaltıyla başladık, o meşhur kalabalığa biz de karıştık. Ayvalık tostu beklemeye değiyor, sonrası çay üstüne çay zaten. Papalina yokmuş. Mevsimi değilmiş, bunu öğrenmek için tezgahtaki adamla on dakika konuşmak gerekti ama o sohbetten bir de zeytinyağcı önerisi çıktı, iyi ki sormuşum.
>
> Giderken tek valizle gitmiştik, dönüşte bagajda beş litre zeytinyağı ve iki kavanoz sakız reçeli vardı. Ayvalık böyle bir yer, insanı fark ettirmeden alışverişe ikna ediyor. Tekrar giderim, ama bu sefer pazartesiyi de izin alırım; iki gün bu ilçeye az.

Ne değişti: Klişe girizgah ("Günümüzde..."), broşür dili, uzun tireler, "sadece X değil Y" kapanışı ve emoji gitti; yerine somut sahneler, virgülle akan cümleler ve gerçek bir gezi sesi geldi.

### 2. İş: trend raporu özeti

**Önce:**

> 2026 e-ticaret gündemine baktığımda gördüğüm tablo oldukça net: Önümüzdeki dönemde rekabeti belirleyecek unsur, markaların ne kadar çok kampanya yaptığı değil; müşterinin satın alma yolculuğundaki sürtünmeyi ne kadar azalttığı olacak.
>
> 1) Teslimat ve iade artık operasyonel bir konu değil, doğrudan ciro konusu. Sepet terkinde fiyat kadar teslimat maliyeti, teslimat hızı, iade kolaylığı ve süreç şeffaflığı belirleyici hale gelmiş durumda. Kısacası müşteri satın alma kararını sadece ürünle vermiyor; teslimat deneyimini de satın alıyor.
>
> Kısacası yeni dönemde asıl rekabet, ürünü satmakta değil; müşterinin satın alma kararını mümkün olduğunca kolay, hızlı ve güvenli hale getirmekte yaşanacak.

**Sonra:**

> 2026 e-ticaret trend raporlarından birini okudum bu hafta, beş başlıkta notlarımı paylaşayım. Okurken aklımda hep aynı soru vardı, sepeti dolduran müşteri neden ödeme sayfasında vazgeçiyor? Raporun neredeyse her bölümü dönüp dolaşıp oraya çıkıyor, müşteriyi kaybettiren şey çoğu zaman satın almanın zahmeti çıkıyor.
>
> 1) Teslimat ve iade doğrudan ciro kalemi olmuş. Sepet terki verilerinde fiyatın yanına dört kalem daha eklenmiş: teslimat maliyeti, teslimat hızı, iadenin kolaylığı, sürecin şeffaflığı. Müşteri ürünle birlikte teslimat deneyimini de satın alıyor, rapor da bu başlığı operasyon bölümünden çıkarıp gelir bölümüne taşımış zaten.
>
> İndirim savaşına girmeden büyümek isteyenlere rapor aslında tek bir yol tarif ediyor, müşterinin yolundaki taşları tek tek ayıklamak. Teslimatı, iadeyi, ödemeyi ve kanal geçişlerini pürüzsüzleştiren markalar 2026'da ayrışacak gibi görünüyor.

Ne değişti: Orijinalin iskeleti "X değil, Y" kalıbıydı (tam metinde 12 kez) ve 10 noktalı virgülün neredeyse hepsi bu kalıbın ekseniydi; ikisi de sıfırlandı. "Kısacası" özet mühürleri gitti, metin soruyla açılıp yeni bir gözlemle kapanıyor.

### 3. Genel kültür: ansiklopedik metin

**Önce:**

> Göbeklitepe, insanlık tarihinin en önemli keşiflerinden biri olarak kabul edilmektedir. Şanlıurfa'nın kalbinde yer alan bu eşsiz arkeolojik alan, yaklaşık 12.000 yıllık geçmişiyle tarihin akışını değiştiren bir dönüm noktası olmuştur.
>
> Alanda gerçekleştirilen kazılar, T biçimindeki dikilitaşları gün yüzüne çıkarmıştır. Bu dikilitaşlar; üzerlerindeki tilki, yılan ve yaban domuzu kabartmalarıyla dönemin inanç dünyasına ışık tutmakta, dönemin sanat anlayışını gözler önüne sermekte ve araştırmacılara paha biçilmez bilgiler sunmaktadır. Uzmanlar, alanın dini bir merkez olarak kullanıldığını düşünmektedir.
>
> Göbeklitepe sadece bir arkeolojik alan değil, aynı zamanda insanlığın ortak mirasıdır. Sonuç olarak Göbeklitepe, tarihe meraklı herkesin mutlaka görmesi gereken büyüleyici bir destinasyon olarak ziyaretçilerini beklemektedir.

**Sonra:**

> Göbeklitepe, Şanlıurfa'nın yaklaşık 15 kilometre kuzeydoğusunda, 12.000 yıllık bir tapınak alanı. Bilinen en eski anıtsal yapılar arasında olduğu için ders kitaplarındaki "önce tarım, sonra tapınak" sıralamasını tartışmaya açtı, çünkü burayı inşa edenler henüz yerleşik düzene geçmemiş avcı toplayıcılardı.
>
> Kazılarda ortaya çıkan T biçimli dikilitaşların boyu 5,5 metreyi buluyor. Üzerlerinde tilki, yılan ve yaban domuzu kabartmaları var, bir kısmında da gövdeye kazınmış kol ve el motifleri; bu yüzden taşların stilize insan figürleri olduğu düşünülüyor. Alanın dini merkez olduğu görüşü ağırlıkta ama kesinleşmiş değil, kazılar sürüyor ve alanın büyük bölümü hala toprak altında.
>
> UNESCO, Göbeklitepe'yi 2018'de Dünya Mirası Listesi'ne aldı. Ziyaret bugün kazı alanının üzerine kurulan çelik örtünün altındaki yürüyüş yolundan yapılıyor.

Ne değişti: "-maktadır" kafiyesi, önem şişirmesi ("dönüm noktası"), "-arak/-ıp ışık tutmakta... gözler önüne sermekte" kuyrukları, belirsiz "uzmanlar" ve turizm broşürü kapanışı gitti. Sicil bozulmadı; metin hala ansiklopedik, birinci tekil yok, sadece bilgi netleşti ve kapanışa yeni somut bilgi geldi.

## Kaynaklar

Kalıpları ve kuralları beş ayrı damardan derledim:

- **Gerçek Türkçe düzyazı okuması** — 2012-2019 arası köşe yazıları (Özdil, Ahmet Hakan, Yıldırım Türker, Gülse Birsel), denemeler (Birikim, 5Harfliler), bloglar ve Ekşi Sözlük'ün beğenilen entry'leri; edebi damar için [TDK'nin ücretsiz e-kitapları](https://tdk.gov.tr/genel/e-kitaplar/) (Hüseyin Rahmi Gürpınar külliyatı, ritim ve ikileme kuralları "Sevda Peşinde"den), sade öğretici anlatım için [turkdili.gen.tr](https://turkdili.gen.tr) ve anlatım bozuklukları envanteri
- **Deyim ve atasözü haznesi** — Ömer Asım Aksoy'un kurucu çalışması (TDAY Belleten 1962, TDK) ve MEB derlemesi; [references/deyimler.md](references/deyimler.md) dosyasında
- **Dedektör tersine mühendisliği** — [GLTR](https://github.com/HendrikStrobelt/detecting-fake-text), [DetectGPT](https://arxiv.org/abs/2301.11305), GPTZero klonları ve açık kaynak slop dedektörlerinin ([unslop](https://github.com/theclaymethod/unslop), [SLOP_Detector](https://github.com/SicariusSicariiStuff/SLOP_Detector), [antislop-sampler](https://github.com/sam-paech/antislop-sampler)) kaynak kodundaki ölçüm eşikleri
- **Türkçe topluluk gözlemleri** — Ekşi Sözlük'ün yapay zeka entry'si ve ChatGPT yalakalığı başlıkları, Marketing Türkiye'nin şablon cümle derlemesi, TÜBİTAK Bilim Genç'in insan/AI metin karşılaştırması
- **Nicel araştırmalar** — [Kobak vd.](https://arxiv.org/abs/2406.07016), [Juzek & Ward](https://arxiv.org/abs/2412.11385) ve Türkçe BERT dedektör çalışması ([arXiv:2602.13504](https://arxiv.org/abs/2602.13504)): Kelime telleri eskiyor, yapısal teller kalıyor

## English summary

İnsanca ("humanly" in Turkish) is an agent skill that removes AI-writing tells from Turkish text and rebuilds the prose with the rhythm of real Turkish. It detects 48 patterns, including Turkish-specific signatures English guides miss (the "-maktadır" suffix monotony that turns sentence endings into a rhyme, translation-ese, bureaucratic filler stacking, cataphoric colon definitions) and patterns reverse-engineered from open-source AI detectors, with measurable thresholds and an overcorrection guard. It then applies 17 flow rules distilled from close reading of real pre-AI Turkish prose: comma-chained verbs, mobile connectives, reduplication, reference tracking through Turkish pro-drop, emotion shown through the body, and a curated idiom reference sourced from Ömer Asım Aksoy's foundational work. Install with `npx skills add tahiryildiz/insanca`, invoke with `/insanca`.

## Lisans

MIT
