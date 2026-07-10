# İnsanca

Yapay zeka Türkçesi kokan metni insan Türkçesine çevirir.

ChatGPT, Claude veya Gemini'ye Türkçe bir şey yazdırdığınızda çıkan metni tanırsınız: "Günümüzde..." diye açılır, her cümle "-maktadır" ile biter, her şey "kapsamlı" ve "yenilikçi"dir, son paragraf "Sonuç olarak..." diye başlar ve kimseye bir şey söylemeyen iyimser bir cümleyle kapanır. İnsanca, bir agent skill'i olarak bu metni alır, kokusunu tek tek teşhis eder ve gerçek bir insanın kaleminden çıkmış gibi okunana kadar yeniden yazar.

Tamamı düz Markdown olduğu için skill destekleyen her agent ortamında (Claude Code, OpenCode, Codex vb.) çalışır.

## Yapay zeka Türkçesi nasıl kokar?

İnsanca 41 kalıbı tarar. Hepsi önce/sonra örnekleriyle [SKILL.md](SKILL.md) içinde; burada koku koku özeti:

**Ritim kokusu.** Türkçede bütün cümleler yüklemle bittiği için yapay zekanın tekdüzeliği bizde kafiyeye dönüşür: art arda beş cümle "-maktadır" ile biter, hepsi 15-20 kelimedir, paragraflar simetriktir. İnsan yazar bunu devrik cümleyle, soruyla, yarım bırakılmış bir düşünceyle kırar... Bir de tersi var: vurucu olsun diye üst üste dizilmiş kesik cümleler. Türkçede kısa cümleler çoğu zaman noktayla ayrılmaz, virgülle bağlanıp akışa katılır; İnsanca ikisini de düzeltir.

**Kelime ve kalıp kokusu.** "Kapsamlı", "kilit rol", "değer katmak", "dönüşüm yolculuğu". Üçe bölünmüş her şey: üç sıfat, üç fayda, üç örnek. "Mesele X değil, Y" diye paketlenmiş sıradan iddialar. "Güven zamanla inşa edilir" gibi kimsenin itiraz edemeyeceği boş doğrular. İnsanca bunları somut, tartışılabilir cümlelere çevirir.

**Çeviri kokusu.** Metin İngilizce düşünülüp Türkçeye çevrilmiş gibidir: her cümlede gereksiz "siz" ve "ben", İngilizce "a/an"den kalma "bir" bolluğu, "karmaşık bir goblen" gibi kimsenin kurmadığı metaforlar, "günün sonunda", "oyun değiştirici". Türkçe zamir düşüren bir dildir; İnsanca cümleyi Türkçe düşünülmüş haline geri kurar.

**Ton kokusu.** Her soruya "harika bir soru!" diye başlayan yağcılık, iş yazısının ortasında kimse sormadan beliren "yalnız değilsiniz" tesellisi, "dürüst olmak gerekirse..." diye kurulan sahte samimiyet, broşürden fırlamış "eşsiz deneyim"ler. Bir de sicil savrulması: "kanka" ile "-maktadır"ın aynı cümlede buluşması.

**Biçim kokusu.** Uzun tire (Türkçede zaten neredeyse hiç kullanılmaz, bu yüzden kesin imzadır), kalın yazı enflasyonu, düz yazının ortasında gereksiz madde işaretleri, Her Kelimesi Büyük Başlıklar, emoji, şapkalı harf tutarsızlığı, kaldırılan tirenin yerine sızan noktalı virgül bolluğu.

**Güven kokusu.** "Uzmanlara göre", "araştırmalar gösteriyor ki" diye adressiz otoriteler; "Ayşe Hanım cirosunu 90 günde 3'e katladı" gibi uydurma vakalar; var olmayan kitaba dipnot. İnsanca bunları ya gerçek kaynağa bağlatır ya sildirir; tahmini bilgi gibi sunmaz.

## Neyi bozmaz

Temizlik kadar önemlisi, sağlam metni katletmemek. İnsanca şunları yanlış alarm saymaz: kusursuz dilbilgisi (editörden geçmiş olabilir), akademik metindeki "-maktadır" (orada doğru sicil odur), tek tük "kapsamlı" veya "ayrıca" (işaret kelime değil, kümelenmedir), kaynaksız iddia (internetin çoğu kaynaksızdır). Alıntılara, başlıklara ve özel adlara dokunmaz.

İnsan işaretlerini de korur: tuhaf ve spesifik detaylar, karışık duygular, ara sözler, devrik cümleler, noktalamaya sızmış duygu. Bunlar görünce skill metne daha az dokunur, daha çok değil.

## Nasıl çalışır

Tek geçişte yeniden yazıp bırakmaz; üç adımlık bir döngü uygular:

1. **Taslak** — kalıpları temizleyip metni yeniden yazar.
2. **Denetim** — kendi taslağına "bu metni hala bariz yapay zeka yapan ne?" diye sorar ve kalan telleri listeler.
3. **Final** — o telleri de giderip nihai metni teslim eder.

Kelime değiştirmekle yetinmemesinin bir nedeni var: kelime telleri eskir ("delve" damgalanınca modeller bırakmıştı, "kapsamlı" da aynı yoldan gidecek), yapısal teller kalır. Tekdüze ritim, kafiyeli cümle sonları ve cümleler arası mantık sıçramaları model neslinden bağımsız sürdüğü için İnsanca asıl oraya yüklenir.

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
> Cumartesi sabahı Cunda'da kahvaltıyla başladık, o meşhur kalabalığa biz de karıştık. Ayvalık tostu beklemeye değiyor, sonrası çay üstüne çay zaten. Papalina yokmuş, mevsimi değilmiş; bunu öğrenmek için tezgahtaki adamla on dakika konuşmak gerekti ama o sohbetten bir de zeytinyağcı önerisi çıktı, iyi ki sormuşum.
>
> Asıl güzel kısım planladığımız hiçbir şeyde değildi. Sahilden iki sokak içeri girince turist kalabalığı bitiyor, yerini boyası dökülmüş kapılar ve kapı önünde oturan teyzeler alıyor. Bir tanesiyle yarım saat konuştuk, evinin altmış yıllık hikayesini dinledik. Rotamıza yazdığım taş konakların hiçbiri aklımda o kadar yer etmedi.
>
> Pazar öğleden sonra Şeytan Sofrası'na çıktık. Gün batımı için erken gitmek lazımmış, biz bilmiyorduk; manzara güzel ama kalabalık ve otopark kargaşası keyfi törpülüyor. Bir dahakine oraya harcayacağım vakti Cunda'nın arka sokaklarına veririm.
>
> Giderken tek valizle gitmiştik, dönüşte bagajda beş litre zeytinyağı ve iki kavanoz sakız reçeli vardı. Ayvalık böyle bir yer, insanı fark ettirmeden alışverişe ikna ediyor. Tekrar giderim, ama bu sefer pazartesiyi de izin alırım; iki gün bu ilçeye az.

## Kaynaklar

Kalıplar üç damardan derlendi:

- **Türkçe topluluk gözlemleri** — Ekşi Sözlük'ün yapay zeka entry'si ve ChatGPT yalakalığı başlıkları, Marketing Türkiye'nin şablon cümle derlemesi, TÜBİTAK Bilim Genç'in insan/AI metin karşılaştırması, Türkçe SEO ve içerik topluluklarının doğallaştırma pratikleri
- **[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)** — WikiProject AI Cleanup'ın binlerce vakadan derlediği evrensel teller, Türkçeye uyarlandı
- **Nicel araştırmalar** — [Kobak vd., excess vocabulary](https://arxiv.org/abs/2406.07016) ve [Juzek & Ward](https://arxiv.org/abs/2412.11385): kelime tellerinin RLHF kaynaklı olduğu ve bir yıl içinde eskidiği bulgusu, skill'in yapı odaklı yaklaşımının dayanağı

## English summary

İnsanca ("humanly" in Turkish) is an agent skill that removes AI-writing tells from Turkish text. Beyond universal patterns, it targets signatures specific to Turkish: the "-maktadır" suffix monotony that turns sentence endings into a rhyme, translation-ese from English (redundant pronouns, "bir" overuse, calqued metaphors), bureaucratic filler stacking, connector pileups, and Turkish-specific punctuation habits such as joining short sentences with commas instead of full stops. Install with `npx skills add tahiryildiz/insanca`, invoke with `/insanca`.

## Lisans

MIT
