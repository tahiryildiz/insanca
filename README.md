# İnsanca

Türkçe metinlerdeki yapay zeka yazım izlerini temizleyen taşınabilir bir agent skill'i. Metni daha doğal, daha akıcı ve gerçek bir insanın kaleminden çıkmış gibi okunur hale getirir. Tamamı düz Markdown olduğu için skill tarzı talimat destekleyen her agent ortamında çalışır.

[blader/humanizer](https://github.com/blader/humanizer) projesinin Türkçe kardeşi; ama birebir çeviri değil. Kalıpların önemli bir kısmı Türkçeye özgü: "-maktadır" monotonluğu, çeviri kokusu, bürokratik dolgu, cümle başı bağlaç yığını gibi teller İngilizce rehberlerde yoktur. Türkçe topluluk gözlemleri (Ekşi Sözlük, içerik ve SEO çevreleri, TÜBİTAK'ın insan/AI metin karşılaştırması) taranarak derlendi.

## Kurulum

### Skills CLI

Çapraz platform skills CLI ile:

```bash
npx skills add tahiryildiz/insanca
```

Mevcut kurulumu güncellemek için:

```bash
npx skills update insanca
```

Desteklenen tüm agent ortamlarına birden kurmak için:

```bash
npx skills add tahiryildiz/insanca --agent '*'
```

### Claude Code eklentisi

Claude Code kullanıcıları İnsanca'yı eklenti olarak da kurabilir:

```
/plugin marketplace add tahiryildiz/insanca
/plugin install insanca@insanca
```

Skill daha sonra `/insanca:insanca` olarak çağrılır.

### Manuel

Çalışan tek dosya `SKILL.md` olduğu için herhangi bir agent ortamı skill'i doğrudan kullanabilir. Ortamınızın skill dizinlerini beklediği yere kurun ya da `SKILL.md` dosyasını mevcut bir skill klasörüne kopyalayın:

```bash
git clone https://github.com/tahiryildiz/insanca.git ~/.claude/skills/insanca
```

Ya da repo zaten klonluysa:

```bash
mkdir -p /skill/dizininiz/insanca
cp SKILL.md /skill/dizininiz/insanca/
```

## Kullanım

Skill'i, agent ortamınız kurulu skill'leri nasıl sunuyorsa öyle çağırın. Yaygın biçimler bir eğik çizgi komutu veya doğrudan istek:

```
/insanca

[metninizi buraya yapıştırın]
```

```
Şu metni doğallaştır: [metniniz]
```

### Ses kalibrasyonu

Kendi yazım tarzınıza uydurmak için kendi yazınızdan bir örnek verin:

```
/insanca

Ses eşleştirmesi için kendi yazımdan bir örnek:
[kendi yazınızdan 2-3 paragraf]

Şimdi şu metni doğallaştır:
[doğallaştırılacak yapay zeka metni]
```

Skill; cümle ritminizi, kelime seçimlerinizi ve alışkanlıklarınızı çözümleyip yeniden yazımda jenerik "temiz" çıktı yerine onları uygular.

## Genel bakış

[Wikipedia'nın "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) rehberi (WikiProject AI Cleanup) temel alındı; üzerine Türkçe kaynaklardan derlenen kalıplar eklendi. Skill ayrıca ilk taslağı "bu metni hâlâ bariz yapay zeka yapan ne?" sorusuyla denetleyen ikinci bir yeniden yazım turu içerir.

### Temel ilke

Kelime telleri eskir, yapısal teller kalır. "Delve" nasıl damgalanıp modellerce terk edildiyse "kapsamlı" da damgalanır ve terk edilir; ama tekdüze cümle ritmi, kafiyeli cümle sonları ve mantık sıçramaları model neslinden bağımsız sürer. Bu yüzden İnsanca kelime avcılığıyla yetinmez; ritmi, kurguyu ve akıl yürütme akışını da onarır.

> "Büyük dil modelleri bir sonraki kelimeyi istatistiksel olarak tahmin eder. Sonuç, en geniş durum yelpazesine uyan, istatistiksel olarak en olası metne yakınsar." — Wikipedia

## Tespit edilen 41 kalıp (Önce/Sonra örnekleriyle)

### İçerik kalıpları

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 1 | **Önem şişirmesi** | "kritik bir dönüm noktası olmuştur" | "1989'da ... için kuruldu" |
| 2 | **Broşür dili** | "Ege'nin incisi, büyüleyici, eşsiz" | "Semt İzmir'in batısında" |
| 3 | **"-arak/-erek" sahte derinlik** | "gözler önüne sererek... yansıtarak..." | Kaynağı olan somut bilgi |
| 4 | **Belirsiz kaynak** | "Uzmanlar kritik rol oynadığını belirtiyor" | "DSİ'nin 2023 raporuna göre..." |
| 5 | **Şablon "zorluklar" bölümü** | "Tüm bu zorluklara rağmen büyümeye devam ediyor" | Gerçek soruna dair somut veri |
| 6 | **Boş doğrular** | "Güven zamanla inşa edilir" | Tersi savunulabilir, somut iddia |
| 7 | **Uydurma örnekler** | "Ayşe Hanım cirosunu 90 günde 3'e katladı" | Gerçek, doğrulanabilir örnek |

### Dil ve dilbilgisi kalıpları

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 8 | **AI kelime dağarcığı** | "kapsamlı... kilit... yenilikçi... değer katmak" | Somut, sade karşılıklar |
| 9 | **"Mesele X değil, Y"** | "Bu sadece bir taktik değil, zihniyet değişimi" | İddiayı doğrudan söyle |
| 10 | **Üçleme kuralı** | "ilham, bilgi ve networking" | Doğal sayıda öğe |
| 11 | **Yalancı aralıklar** | "küçük alışkanlıklardan büyük hedeflere" | Konuları doğrudan listele |
| 12 | **Eşanlamlı döngüsü / takıntılı tekrar** | "şirket... firma... kuruluş... marka" | Aynı kelimeyi tekrar et |
| 13 | **"-maktadır" monotonluğu** | Her cümle "-maktadır" ile bitiyor | Devrik, soru, isim cümlesiyle kır |
| 14 | **Metronomik ritim** | Bütün cümleler 15-20 kelime | Kısa/uzun karışık ritim |
| 15 | **Kesik cümle yığını** | "Kurallar yıkıldı. Ezberler bozuldu." | Değişken uzunlukta somut iddia |
| 16 | **Çeviri kokusu** | "karmaşık bir goblen", gereksiz zamirler | Türkçe düşünülmüş kurulum |
| 17 | **Bürokratik dolgu** | "kapsamında... doğrultusunda... noktasında" | Somut fiillerle sade cümle |
| 18 | **Edilgen/kişisiz anlatım** | "ayrılması gerekmektedir" | Faili belli etken cümle |
| 19 | **Bağlaç yığını** | Her cümle "Ayrıca... Öte yandan..." | Geçişi fikrin kendisiyle yap |
| 20 | **Paragraf sonu mini özetleri** | "Kısacası uyku vazgeçilmezdir." | Paragrafı geçişle bitir |
| 21 | **Sicil kayması** | "Kanka bu araç olanak tanımaktadır" | Tek sicil seç, orada kal |

### Üslup kalıpları

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 22 | **Uzun tire** | "ücretsiz — şimdilik" | Nokta, virgül, iki nokta, parantez |
| 23 | **Kalın vurgu bolluğu** | "**OKR**, **KPI**, **Kanvas**" | "OKR, KPI, Kanvas" |
| 24 | **Gereksiz maddeleme** | "**Performans:** Performans artırıldı" | Düz yazıya çevir |
| 25 | **Her Kelimesi Büyük Başlık** | "Yükselişi Ve Geleceği" | "Yükselişi ve geleceği" |
| 26 | **Emoji** | "🚀 Lansman: 💡 İçgörü:" | Emojileri kaldır |
| 27 | **Retorik soru-cevap** | "Peki bu ne demek? Cevap basit:" | Doğrudan anlat |
| 28 | **Anons cümleleri** | "Gelin derinlemesine dalalım" | İçerikle başla |
| 29 | **Klişe girizgahlar** | "Günümüzde... vazgeçilmez hale geldi" | İlk cümlede asıl bilgi |
| 30 | **Jenerik kapanışlar** | "Sonuç olarak... parlak bir gelecek" | Somut plan veya bilgi |
| 31 | **Parantez açıklaması takıntısı** | "temettü (kâr payı)" | Gereksiz açıklamayı sil |
| 32 | **Noktalama tuhaflıkları** | Noktalı virgül bolluğu, "zekâ/zeka" karışık | TDK yazımı, tutarlı tercih |

### İletişim kalıpları

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 33 | **Sohbet/arayüz artıkları** | "Umarım yardımcı olur!", "Regenerate response" | Tamamen kaldır |
| 34 | **Yağcı ton** | "Harika bir soru! Kesinlikle haklısınız!" | Doğrudan cevap ver |
| 35 | **Terapist modu** | "Yalnız değilsiniz, kendinizi suçlamayın" | Konuya gir |
| 36 | **Bilgi sınırı itirafı / uydurma kaynak** | "kaynaklarda sınırlı bilgi... muhtemelen..." | Bilinmeyeni söyle ya da çıkar |

### Dolgu ve kaçamak

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 37 | **Dolgu ifadeler** | "Önemle belirtmek gerekir ki" | Sil, doğrudan söyle |
| 38 | **Aşırı kaçamak** | "etkili olabileceği düşünülebilir" | "etkileyebilir" |
| 39 | **Aforizma formülleri** | "Tasarım, güvenin dilidir" | Somut iddiayı yaz |
| 40 | **Sahte samimi açılışlar** | "Dürüst olmak gerekirse..." | Lafı dolandırmadan söyle |

### Kurgu kalıpları

| # | Kalıp | Önce | Sonra |
|---|-------|------|-------|
| 41 | **Kurgu klişeleri** | "İçini bir huzursuzluk dalgası kapladı" | Duyguyu sahneyle göster |

## Tam örnek

**Önce (yapay zeka kokan):**
> Günümüzde seyahat, hayatımızın vazgeçilmez bir parçası haline gelmiştir. Geçtiğimiz ay beş unutulmaz gün geçirdiğim Lizbon, kalbimi tam anlamıyla fethetti!
>
> Tejo Nehri'nin kıyısında yer alan Lizbon, zengin tarihi ve dinamik modern yaşamın iç içe geçtiği büyüleyici bir şehir olarak öne çıkıyor. Evet, meşhur yokuşlar zorlayıcı — bacaklarım bunu fazlasıyla hissetti! — ama her tırmanış, sizi nefes kesen panoramik manzaralarla ödüllendiriyor.
>
> 28 numaralı tramvaya binmeden, şehrin tarihi mahallelerini keşfetmeden bir Lizbon gezisi düşünülemez. Peki ya yemekler? Kelimenin tam anlamıyla muhteşem. Pastéis de Belém'in orijinal tarifi, kültürel mirastan lezzet dünyasına uzanan bir yolculuk sunuyor.
>
> Ama Lizbon'u özel kılan sadece gezilecek yerler değil; hissettirdikleri. Ana meydanlardan birkaç adım uzaklaşın, şehrin daha otantik yüzünü keşfedin: güneşli sokaklar, büyüleyici çini cepheler ve sizi yavaşlamaya davet eden samimi yerel halk.
>
> Sonuç olarak Lizbon, sadece bir şehir değil, aynı zamanda bir yaşam biçimi. Tekrar gider miyim? Kesinlikle! Siz de bir sonraki tatilinizi planlıyorsanız, bu büyüleyici şehir sizi bekliyor. ✨

**Sonra (insanca):**
> Geçen ay Lizbon'da beş gün geçirdim ve içimde hâlâ ikisi bir arada: güzel şehir, evet, ama kimsenin söylemediği kadar da yorucu.
>
> Yokuşlar broşürlere girmiyor, oysa hikayenin ta kendisi. Otelim Alfama'daydı; fotoğrafı çok iyi çıkan bir mahalle, pratikte ise her kahve molası altı kat merdiven demek. İkinci gün baldırlarım fikir beyan etmeye başladı. Bir noktadan sonra yürüyüşleri hangi yol iniş diye planlıyordum ki bir şehri gezmenin tuhaf ama herhalde en dürüst yolu bu.
>
> Herkes bin dediği için 28 tramvayına bindim; kırk dakika boyunca bir yabancının sırt çantasıyla burun buruna, aynı köşeyi çeken üç tur kafilesinin arasında. Bir dahakine o güzergahı yürürüm, ya da sabah kahvaltıdan önce binerim. Tatlılar ise şöhretini hak ediyor. Graça'da gösterişsiz bir yerde, fırından yeni çıkmış bir tane yedim ve otuz saniye kadar insanların neden pastane için şehir değiştirdiğini anladım.
>
> Beklemediğim şey, meydanlardan uzaklaşınca şehrin ne kadar sessizleştiğiydi. Herhangi bir meydandan iki sokak yukarısı çamaşır ipi, kırık çini, açık pencere ve sesi sonuna kadar açılmış maç yayını demek. Aklımda kalan Lizbon o; kale değil.
>
> Kale fena değil. Manzara iyi, kuyruk uzun; içeri girince baktığım süre, girmek için beklediğim sürenin yanında komik kaldı. İki günüm olsaydı kaleyi verir, yerine bir öğleden sonra kaybolurdum.
>
> Tekrar giderim ama baharda ve daha iyi ayakkabılarla. Lizbon işinizi kolaylaştırmak için kılını kıpırdatmıyor. Sanırım hoşuma giden de buydu, bacaklarım aynı fikirde olmasa da.

## Kaynaklar

- [blader/humanizer](https://github.com/blader/humanizer) — ilham kaynağı ve yapı modeli
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — birincil kaynak, WikiProject AI Cleanup
- Türkçe topluluk gözlemleri: Ekşi Sözlük başlıkları (yapay zeka entry'leri, ChatGPT yalakalığı), Marketing Türkiye'nin şablon cümle derlemesi, TÜBİTAK Bilim Genç'in insan/AI metin karşılaştırması, Türkçe SEO topluluklarının doğallaştırma pratikleri
- Nicel araştırmalar: [Kobak vd., excess vocabulary](https://arxiv.org/abs/2406.07016) ve [Juzek & Ward, Why Does ChatGPT Delve So Much?](https://arxiv.org/abs/2412.11385) — kelime tellerinin RLHF kaynaklı olduğu ve zamanla eskidiği bulgusu

## English summary

İnsanca ("humanly" in Turkish) is a Turkish-language counterpart of [blader/humanizer](https://github.com/blader/humanizer): a portable agent skill that removes signs of AI-generated writing from Turkish text. It is not a translation. Beyond the universal tells (em dashes, rule of three, significance inflation), it covers Turkish-specific signatures that English guides miss: the "-maktadır" suffix monotony that turns every sentence ending into a rhyme, translation-ese from English (redundant pronouns, "bir" overuse, calqued metaphors like "karmaşık bir goblen"), bureaucratic filler stacking, and sentence-initial connector pileups. Install with `npx skills add tahiryildiz/insanca` and invoke with `/insanca`.

## Sürüm geçmişi

- **1.0.0** — İlk sürüm. 41 kalıp: Wikipedia tabanlı evrensel teller Türkçeye uyarlandı, üzerine Türkçeye özgü kalıplar (kip monotonluğu, çeviri kokusu, bürokratik dolgu, bağlaç yığını, noktalama tuhaflıkları) ve 2025-26 araştırmalarından yeni teller (metronomik ritim, boş doğrular, uydurma örnekler, terapist modu, sicil kayması, kurgu klişeleri) eklendi. Ses kalibrasyonu ve taslak → denetim → final döngüsü dahil.

## Lisans

MIT
