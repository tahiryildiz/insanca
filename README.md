# İnsanca

Yapay zeka Türkçesi kokan metni insan Türkçesine çevirir.

ChatGPT, Claude veya Gemini'ye Türkçe bir şey yazdırdığınızda çıkan metni tanırsınız: "Günümüzde..." diye açılır, her cümle "-maktadır" ile biter, her şey "kapsamlı" ve "yenilikçi"dir, son paragraf "Sonuç olarak..." diye başlar ve kimseye bir şey söylemeyen iyimser bir cümleyle kapanır. İnsanca, bir agent skill'i olarak bu metni alır, kokusunu tek tek teşhis eder ve gerçek bir insanın kaleminden çıkmış gibi okunana kadar yeniden yazar.

Tamamı düz Markdown olduğu için skill destekleyen her agent ortamında (Claude Code, OpenCode, Codex vb.) çalışır.

## Yapay zeka Türkçesi nasıl kokar?

İnsanca 45 kalıbı altı koku altında tarar. Hepsinin uzun önce/sonra örnekleri [SKILL.md](SKILL.md) içinde; aşağıdaki tablolar özet.

### 1. Ritim kokusu

Türkçede bütün cümleler yüklemle bittiği için yapay zekanın tekdüzeliği bizde kafiyeye dönüşür. İnsan yazar bunu devrik cümleyle, soruyla, virgülle bağlanmış kısa cümlelerle kırar; model kırmaz.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| "-maktadır" kafiyesi | "kurulmuştur... bulunmaktadır... vermektedir..." | "2020'de kuruldu, merkezi İstanbul'da." |
| Metronomik ritim | Bütün cümleler 15-20 kelime | Kısa/uzun karışık; 3 kelimelik cümlenin yanında 30 kelimelik |
| Kesik cümle yığını | "Kurallar yıkıldı. Ezberler bozuldu." | Kısa cümleleri virgülle bağla, vurgu için tek tük ayrık bırak |
| Bağlaç yığını | "Ayrıca... Öte yandan... Dolayısıyla..." | Geçişi fikrin kendisiyle yap |
| Paragraf sonu mini özeti | Her paragraf "Kısacası..." ile bitiyor | Paragrafı geçişle bitir |
| Açılış tekrarı | Dört cümle üst üste "Uygulama..." ile başlıyor | Açılışları çeşitlendir |

### 2. Kelime ve kalıp kokusu

Damgalanmış kelimeler tek başına suç değil; kümelenince imza. Asıl mesele kelimenin altındaki boş kalıp.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| AI kelime dağarcığı | "kapsamlı... kilit... değer katmak... yolculuk" | Somut, sade karşılıklar |
| Önem şişirmesi | "kritik bir dönüm noktası olmuştur" | Ne olduğunu söyle, ne "ifade ettiğini" değil |
| "Mesele X değil, Y" | "Bu sadece bir taktik değil, zihniyet değişimi" | İddiayı doğrudan söyle |
| Üçleme kuralı | "ilham, bilgi ve networking" | Doğal sayıda öğe |
| Yalancı aralıklar | "küçük alışkanlıklardan büyük hedeflere" | Konuları doğrudan listele |
| Eşanlamlı döngüsü | "şirket... firma... kuruluş... marka" | Aynı kelimeyi tekrar etmekten korkma |
| "-arak" sahte derinliği | "toprakla kurulan bağı gözler önüne sererek" | Kuyruğu kes ya da kaynaklı bilgiye çevir |
| Boş doğrular | "Güven zamanla inşa edilir" | Tersi savunulabilir, somut iddia |
| Aforizma formülleri | "Tasarım, güvenin dilidir" | Somut iddiayı yaz |
| Dolgu ifadeler | "Önemle belirtmek gerekir ki" | Sil, doğrudan söyle |
| Aşırı kaçamak | "etkili olabileceği düşünülebilir" | "etkileyebilir" |
| Gri kelime duvarı | Her kelime en güvenli seçim, hiçbiri şaşırtmıyor | Beklenmedik ama yerinde detay, deyim, spesifiklik |

### 3. Çeviri kokusu

Metin İngilizce düşünülüp Türkçeye çevrilmiş gibi okunur. Türkçe zamir düşüren bir dildir; model düşürmez.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| Çeviri kokusu | "karmaşık bir goblen", her cümlede "siz", "bir" bolluğu | Türkçe düşünülmüş kurulum |
| Anons cümleleri | "Gelin derinlemesine dalalım" | İçerikle başla |
| Her Kelimesi Büyük Başlık | "Yükselişi Ve Geleceği" | "Yükselişi ve geleceği" |

### 4. Ton kokusu

Model ya herkesi memnun etmeye çalışır ya da kurum bülteni gibi konuşur; ikisinin arasını tutturamaz.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| Yağcı ton | "Harika bir soru! Kesinlikle haklısınız!" | Doğrudan cevap ver |
| Terapist modu | "Yalnız değilsiniz, kendinizi suçlamayın" | Konuya gir |
| Sahte samimi açılış | "Dürüst olmak gerekirse..." | Lafı dolandırmadan söyle |
| Broşür dili | "eşsiz deneyim, büyüleyici doku" | Bilgi ver, pazarlama |
| Sicil kayması | "Kanka bu araç olanak tanımaktadır" | Tek sicil seç, orada kal |
| Retorik soru-cevap | "Peki bu ne demek? Cevap basit:" | Doğrudan anlat |
| Sohbet/arayüz artıkları | "Umarım yardımcı olur!", "Regenerate response" | Tamamen kaldır |
| Bürokratik dolgu | "kapsamında... doğrultusunda... noktasında" | Somut fiillerle sade cümle |
| Edilgen anlatım | "ayrılması gerekmektedir" | Faili belli etken cümle |

### 5. Biçim kokusu

Metnin görünüşü de koku verir; uzun tire Türkçede zaten neredeyse hiç kullanılmadığı için tek başına imzadır.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| Uzun tire | "ücretsiz — şimdilik" | Nokta, virgül, iki nokta veya parantez |
| Kalın vurgu bolluğu | "**OKR**, **KPI**, **Kanvas**" | Vurgu enflasyonunu bitir |
| Gereksiz maddeleme | "**Performans:** Performans artırıldı" | Düz yazıya çevir |
| Emoji | "🚀 Lansman: 💡 İçgörü:" | Kaldır |
| Parantez açıklaması takıntısı | "temettü (kâr payı)" | Okurun bildiğini açıklama |
| Noktalama ve şapka | Noktalı virgül bolluğu, "hâlâ/zekâ" | Şapkasız, TDK'ya uygun, tutarlı |

### 6. Güven ve kurgu kokusu

Metnin iskeletinde ve kaynaklarında saklanan teller; dedektörlerin "en güçlü tekil sinyal" dedikleri de burada.

| Kalıp | Önce | Sonra |
|-------|------|-------|
| Belirsiz kaynak | "Uzmanlara göre kritik rol oynuyor" | "DSİ'nin 2023 raporuna göre..." |
| Uydurma örnekler | "Ayşe Hanım cirosunu 90 günde 3'e katladı" | Gerçek, doğrulanabilir örnek |
| Uydurma kaynak / bilgi sınırı | "kaynaklarda sınırlı bilgi... muhtemelen..." | Bilinmeyeni söyle ya da çıkar |
| Şablon "zorluklar" bölümü | "Tüm bu zorluklara rağmen..." | Gerçek soruna dair somut veri |
| Klişe girizgah | "Günümüzde... vazgeçilmez hale geldi" | İlk cümlede asıl bilgi |
| Jenerik kapanış | "Sonuç olarak... parlak bir gelecek" | Somut plan veya bilgi |
| Özet sandviçi | Giriş bölümleri sıralıyor, kapanış girişi tekrarlıyor | Sona yeni bir şey koy |
| Kurgu klişeleri | "İçini bir huzursuzluk dalgası kapladı" | Duyguyu sahneyle göster |
| Aşırı düzeltme kokusu | Zorlama kesik cümleler, sahte pürüzler | Bir iki pürüz yeter, ölçülü bırak |

## Sayılarla da bakar

İnsanların yapay zeka metnini "hissederek" ayırt etme isabeti yazı turadan farksız; dedektörler bu yüzden sayar. İnsanca'nın dedektör kalıpları (§42-45) ve Sayısal Denetim bölümü, açık kaynak dedektörlerin (GPTZero klonları, GLTR, DetectGPT, slop dedektörleri) kaynak kodundan tersine mühendislikle çıkarıldı. Skill nihai metinde şunları kontrol eder: cümle uzunluğu çeşitliliği, açılış kelimesi dağılımı, zarf-fiil kuyruğu payı, uzun tire ve noktalı virgül sayısı, üçleme yoğunluğu, ilk-son paragraf örtüşmesi.

İki önemli not, yine dedektör araştırmasından:

- **Kelime telleri eskir, yapısal teller kalır.** "Delve" damgalanınca modeller bıraktı; "kapsamlı" da aynı yoldan gidecek. Tekdüze ritim ve kafiyeli cümle sonları ise model neslinden bağımsız sürüyor. Türkçe araştırması da bunu doğruluyor: ince ayarlı BERT, Türkçe insan/AI metnini %97 isabetle ayırıyor ve sinyali kelimelerden değil ritim ve sicil düzleşmesinden alıyor.
- **Aşırı düzeltme de bir imzadır.** Turnitin 2025'te humanizer araçlarının çıktısına özel tespit modülü duyurdu. İnsanca bu yüzden zorlama kesik cümlelere ve sahte pürüzlere kaçmaz; işi dedektör kandırmak değil, iyi Türkçe yazmak.

## Neyi bozmaz

Temizlik kadar önemlisi, sağlam metni katletmemek. İnsanca şunları yanlış alarm saymaz: kusursuz dilbilgisi (editörden geçmiş olabilir), akademik metindeki "-maktadır" (orada doğru sicil odur), tek tük "kapsamlı" veya "ayrıca" (işaret kelime değil, kümelenmedir), kaynaksız iddia (internetin çoğu kaynaksızdır). Teller eş ağırlıkta da değildir: "Bir yapay zeka modeli olarak" kesin kanıtken tek bir "kapsamlı" yumuşak bir sinyaldir. Alıntılara, başlıklara ve özel adlara dokunmaz.

İnsan işaretlerini de korur: tuhaf ve spesifik detaylar, karışık duygular, ara sözler, devrik cümleler, noktalamaya sızmış duygu. Bunları görünce skill metne daha az dokunur, daha çok değil.

## Nasıl çalışır

Tek geçişte yeniden yazıp bırakmaz; üç adımlık bir döngü uygular:

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

Elle: çalışan tek dosya `SKILL.md`, o yüzden repoyu ortamınızın skill dizinine klonlamak yeterli:

```bash
git clone https://github.com/tahiryildiz/insanca.git ~/.claude/skills/insanca
```

## Kullanım

```
/insanca

[metninizi buraya yapıştırın]
```

Ya da doğrudan isteyin: "Şu metni doğallaştır: ..."

### Kendi sesinizle

Jenerik "temiz" çıktı yerine kendi tarzınızı istiyorsanız, kendi yazınızdan 2-3 paragraf verin:

```
/insanca

Ses eşleştirmesi için kendi yazımdan bir örnek:
[kendi yazınız]

Şimdi şu metni doğallaştır:
[yapay zeka metni]
```

Skill; cümle ritminizi, kelime seviyenizi ve alışkanlıklarınızı çıkarır, yeniden yazımı onlarla kurar.

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

Kalıplar dört damardan derlendi:

- **Türkçe topluluk gözlemleri** — Ekşi Sözlük'ün yapay zeka entry'si ve ChatGPT yalakalığı başlıkları, Marketing Türkiye'nin şablon cümle derlemesi, TÜBİTAK Bilim Genç'in insan/AI metin karşılaştırması, Türkçe SEO ve içerik topluluklarının doğallaştırma pratikleri
- **Dedektör tersine mühendisliği** — [GLTR](https://github.com/HendrikStrobelt/detecting-fake-text), [DetectGPT](https://arxiv.org/abs/2301.11305), GPTZero klonları ve açık kaynak slop dedektörlerinin ([unslop](https://github.com/theclaymethod/unslop), [SLOP_Detector](https://github.com/SicariusSicariiStuff/SLOP_Detector), [antislop-sampler](https://github.com/sam-paech/antislop-sampler)) kaynak kodundaki ölçüm eşikleri ve regex listeleri
- **[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)** — WikiProject AI Cleanup'ın binlerce vakadan derlediği evrensel teller, Türkçeye uyarlandı
- **Nicel araştırmalar** — [Kobak vd.](https://arxiv.org/abs/2406.07016), [Juzek & Ward](https://arxiv.org/abs/2412.11385) ve Türkçe BERT dedektör çalışması ([arXiv:2602.13504](https://arxiv.org/abs/2602.13504)): kelime telleri eskiyor, yapısal teller kalıyor

## English summary

İnsanca ("humanly" in Turkish) is an agent skill that removes AI-writing tells from Turkish text. Beyond universal patterns, it targets signatures specific to Turkish: the "-maktadır" suffix monotony that turns sentence endings into a rhyme, translation-ese from English (redundant pronouns, "bir" overuse, calqued metaphors), bureaucratic filler stacking, and connector pileups. It also includes patterns reverse-engineered from open-source AI detectors (sentence-length burstiness, opener repetition, summary-sandwich document shape, participial closer share) with measurable thresholds, plus an overcorrection guard. Install with `npx skills add tahiryildiz/insanca`, invoke with `/insanca`.

## Lisans

MIT
