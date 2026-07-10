# İnsanca

ChatGPT'ye Türkçe bir yazı yazdırdın ve okuyunca sen bile "bunu yapay zeka yazmış" dedin, değil mi? "Günümüzde..." diye açılıyor, her cümle "-maktadır" ile bitiyor, her şey "kapsamlı" ve "yenilikçi", son paragraf da "Sonuç olarak..." diye başlayıp kimseye bir şey söylemeyen iyimser bir cümleyle kapanıyor.

İnsanca bu sorunu çözmek için var. Bir agent skill'i olarak metni alıyor, yapay zeka kokusunu tek tek teşhis ediyor ve gerçek bir insanın kaleminden çıkmış gibi okunana kadar yeniden yazıyor. Tamamı düz Markdown olduğu için skill destekleyen her ortamda (Claude Code, OpenCode, Codex vb.) çalışıyor.

## Yapay zeka Türkçesi nasıl kokar?

İnsanca metinde toplam 47 kalıp arıyor. Ben bunları altı grupta topladım. Aşağıdaki tablolar hızlıca fikir vermek için; her kalıbın daha uzun önce/sonra örneğini [SKILL.md](SKILL.md) içinde bulabilirsin.

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

Bazen metnin görünüşü bile yetiyor. Uzun tire mesela: Türkçede zaten neredeyse hiç kullanılmadığı için tek başına güçlü bir işaret.

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

## Sayılarla da bakar

İşin ilginç tarafı şu: İnsanlar bir metnin yapay zeka yazması olup olmadığını hissederek pek bilemiyor. Araştırmalarda isabet oranı yazı tura seviyesinde çıkıyor. Dedektörler bu yüzden hissetmek yerine sayıyor.

Ben de aynısını yaptım: GPTZero klonları, [GLTR](https://github.com/HendrikStrobelt/detecting-fake-text), [DetectGPT](https://arxiv.org/abs/2301.11305) ve açık kaynak slop dedektörlerinin kaynak kodlarına bakıp ölçtükleri şeyleri skill'e taşıdım. İnsanca nihai metinde cümle uzunluğu çeşitliliğini, açılış kelimesi dağılımını, zarf-fiil kuyruğu payını, uzun tire ve noktalı virgül sayısını, üçleme yoğunluğunu ve ilk-son paragraf örtüşmesini kontrol ediyor.

Bu araştırmadan iki önemli ders çıktı:

- **Kelime telleri eskiyor, yapısal teller kalıyor.** "Delve" kelimesi damgalanınca modeller kullanmayı bıraktı; "kapsamlı" da muhtemelen aynı yoldan gidecek. Ama tekdüze ritim model nesli değişse de duruyor. Türkçe araştırması da bunu doğruluyor: İnce ayarlı BERT, Türkçe insan/AI metnini yüzde 97 isabetle ayırıyor ve sinyali kelimelerden değil ritimden alıyor.
- **Aşırı düzeltme de bir imza.** Turnitin 2025'te humanizer araçlarının çıktısına özel tespit modülü duyurdu. İnsanca bu yüzden zorlama kesik cümlelere ve sahte pürüzlere kaçmıyor. Zaten amaç dedektör kandırmak değil, iyi Türkçe yazmak.

## Neyi bozmaz

Temizlik kadar önemli bir konu daha var: Sağlam metni katletmemek. Kusursuz dilbilgisi tek başına şüphe sebebi değil, editörden geçmiş olabilir. Akademik metindeki "-maktadır" da öyle, orada doğru üslup zaten o. Tek tük "kapsamlı" veya "ayrıca" görmek bir şey kanıtlamaz; işaret olan, bunların hep birlikte gelmesi. Teller eş ağırlıkta da değil: "Bir yapay zeka modeli olarak" ifadesi kesin kanıtken tek bir "kapsamlı" zayıf bir sinyal. Alıntılara, başlıklara ve özel adlara ise hiç dokunmuyor.

İnsan işaretlerini de koruyor: Tuhaf ve spesifik detaylar, karışık duygular, ara sözler, devrik cümleler, noktalamaya sızmış duygu... Bunları görünce skill metne daha az dokunuyor, daha çok değil.

## Nasıl çalışır

Tek geçişte yazıp bırakmıyor, üç adımlık bir döngü uyguluyor:

1. **Taslak** — kalıpları temizleyip metni yeniden yazar.
2. **Denetim** — kendi taslağına "bu metni hala bariz yapay zeka yapan ne?" diye sorar, kalan telleri listeler ve sayısal eşikleri kontrol eder.
3. **Final** — o telleri de giderip nihai metni teslim eder.

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

Elle kurmak istersen çalışan tek dosya `SKILL.md`; repoyu ortamının skill dizinine klonlaman yeterli:

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

## Örnek

**Önce:**

> Günümüzde şehir hayatının stresinden uzaklaşmak isteyenler için hafta sonu kaçamakları hayatımızın vazgeçilmez bir parçası haline geldi. Geçtiğimiz hafta sonu iki unutulmaz gün geçirdiğim Ayvalık, beklentilerimi fazlasıyla karşıladı!
>
> Ege'nin kalbinde yer alan Ayvalık, zengin tarihi ve büyüleyici doğasıyla ziyaretçilerine eşsiz bir deneyim sunuyor. Taş evleri, dar sokakları ve zeytinlikleriyle bu şirin ilçe — tam anlamıyla bir açık hava müzesi — her köşesinde ayrı bir hikaye barındırıyor.
>
> Cunda Adası'na uğramadan, meşhur papalinasını tatmadan bir Ayvalık gezisi düşünülemez. Peki ya kahvaltı? Kelimenin tam anlamıyla muhteşem. Ayvalık tostu, sokak lezzetlerinden gastronomi dünyasına uzanan bir yolculuk sunuyor.
>
> Ama Ayvalık'ı özel kılan sadece gezilecek yerler değil; hissettirdikleri. Sahilden birkaç sokak içeri girin, ilçenin daha otantik yüzünü keşfedin: rengarenk kapılar, mis gibi zeytinyağı kokusu ve sizi yavaşlamaya davet eden samimi esnaf.
>
> Sonuç olarak Ayvalık, sadece bir tatil beldesi değil, aynı zamanda bir yaşam biçimi. Tekrar gider miyim? Kesinlikle! Siz de yoğun tempodan uzaklaşmak istiyorsanız, bu büyüleyici ilçe sizi bekliyor. ✨

**Sonra:**

> Geçen hafta sonu iki günlüğüne Ayvalık'a kaçtık. Dönüşte arabada hesapladım, iki günün neredeyse yarısı yemek masasında geçmiş...
>
> Cumartesi sabahı Cunda'da kahvaltıyla başladık, o meşhur kalabalığa biz de karıştık. Ayvalık tostu beklemeye değiyor, sonrası çay üstüne çay zaten. Papalina yokmuş. Mevsimi değilmiş, bunu öğrenmek için tezgahtaki adamla on dakika konuşmak gerekti ama o sohbetten bir de zeytinyağcı önerisi çıktı, iyi ki sormuşum.
>
> Asıl güzel kısım planladığımız hiçbir şeyde değildi. Sahilden iki sokak içeri girince turist kalabalığı bitiyor, yerini boyası dökülmüş kapılar ve kapı önünde oturan teyzeler alıyor. Bir tanesiyle yarım saat konuştuk, evinin altmış yıllık hikayesini dinledik. Rotamıza yazdığım taş konakların hiçbiri aklımda o kadar yer etmedi.
>
> Pazar öğleden sonra Şeytan Sofrası'na çıktık. Gün batımı için erken gitmek lazımmış, biz bilmiyorduk. Manzara güzel ama kalabalık ve otopark kargaşası keyfi törpülüyor, bir dahakine oraya harcayacağım vakti Cunda'nın arka sokaklarına veririm.
>
> Giderken tek valizle gitmiştik, dönüşte bagajda beş litre zeytinyağı ve iki kavanoz sakız reçeli vardı. Ayvalık böyle bir yer, insanı fark ettirmeden alışverişe ikna ediyor. Tekrar giderim, ama bu sefer pazartesiyi de izin alırım; iki gün bu ilçeye az.

## Kaynaklar

Kalıpları beş ayrı damardan derledim:

- **Gerçek Türkçe düzyazı okuması** — 2012-2019 arası köşe yazıları, denemeler, bloglar ve Ekşi Sözlük'ün beğenilen entry'leri; skill'in "Gerçek Türkçe Böyle Akar" bölümü buradan çıktı. Korpus arayanlara [TurkishNLPGuide](https://github.com/nanelimon-organization/TurkishNLPGuide) ve [Bilkent Turkish Writings](https://github.com/selimfirat/bilkent-turkish-writings-dataset) iyi başlangıç

- **Türkçe topluluk gözlemleri** — Ekşi Sözlük'ün yapay zeka entry'si ve ChatGPT yalakalığı başlıkları, Marketing Türkiye'nin şablon cümle derlemesi, TÜBİTAK Bilim Genç'in insan/AI metin karşılaştırması, Türkçe SEO ve içerik topluluklarının doğallaştırma pratikleri
- **Dedektör tersine mühendisliği** — [GLTR](https://github.com/HendrikStrobelt/detecting-fake-text), [DetectGPT](https://arxiv.org/abs/2301.11305), GPTZero klonları ve açık kaynak slop dedektörlerinin ([unslop](https://github.com/theclaymethod/unslop), [SLOP_Detector](https://github.com/SicariusSicariiStuff/SLOP_Detector), [antislop-sampler](https://github.com/sam-paech/antislop-sampler)) kaynak kodundaki ölçüm eşikleri ve regex listeleri
- **[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)** — WikiProject AI Cleanup'ın binlerce vakadan derlediği evrensel teller, Türkçeye uyarlandı
- **Nicel araştırmalar** — [Kobak vd.](https://arxiv.org/abs/2406.07016), [Juzek & Ward](https://arxiv.org/abs/2412.11385) ve Türkçe BERT dedektör çalışması ([arXiv:2602.13504](https://arxiv.org/abs/2602.13504)): Kelime telleri eskiyor, yapısal teller kalıyor

## English summary

İnsanca ("humanly" in Turkish) is an agent skill that removes AI-writing tells from Turkish text. Beyond universal patterns, it targets signatures specific to Turkish: the "-maktadır" suffix monotony that turns sentence endings into a rhyme, translation-ese from English (redundant pronouns, "bir" overuse, calqued metaphors), bureaucratic filler stacking, and connector pileups. It also includes patterns reverse-engineered from open-source AI detectors (sentence-length burstiness, opener repetition, summary-sandwich document shape, participial closer share) with measurable thresholds, plus an overcorrection guard. Install with `npx skills add tahiryildiz/insanca`, invoke with `/insanca`.

## Lisans

MIT
