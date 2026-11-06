# Kaynak Haritası

İnsanca'yı besleyen ve besleyecek kaynakların envanteri. Durumlar: **işlendi** (skill'de kuralı/kalıbı var) · **sırada** (yüksek öncelikli, madenciliği yapılacak) · **bakılabilir** (orta/düşük öncelik) · **erişilemedi**.

## 0. Skill'in dayandığı kaynaklar (SKILL.md'den taşındı)


- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — WikiProject AI Cleanup'ın binlerce vakadan derlediği rehber
- Türkçe topluluk gözlemleri: Ekşi Sözlük başlıkları (yapay zeka entry'leri, ChatGPT yalakalığı, AI ile makale yazımı), Marketing Türkiye'nin şablon cümle listesi, TÜBİTAK Bilim Genç'in insan/AI metin karşılaştırması, Türkçe SEO ve içerik topluluklarının doğallaştırma pratikleri
- Nicel araştırmalar: Kobak vd. "excess vocabulary" (arXiv:2406.07016), Juzek & Ward "Why Does ChatGPT Delve So Much?" (arXiv:2412.11385) — kelime tellerinin RLHF kaynaklı olduğu ve zamanla eskidiği bulgusu
- Dedektör tersine mühendisliği: GPTZero klonlarının perplexity/burstiness eşikleri, [GLTR](https://github.com/HendrikStrobelt/detecting-fake-text)'nin token sıralaması yaklaşımı, [DetectGPT](https://arxiv.org/abs/2301.11305)'nin olasılık eğriliği bulgusu; açık kaynak slop dedektörlerinin ([unslop](https://github.com/theclaymethod/unslop), [SLOP_Detector](https://github.com/SicariusSicariiStuff/SLOP_Detector), [antislop-sampler](https://github.com/sam-paech/antislop-sampler)) regex listeleri ve ölçüm eşikleri — §42-45 ve Sayısal Denetim bölümünün kaynağı
- Türkçe dedektör araştırması: Türkçe haber metinlerinde ince ayarlı BERT %97 F1 ile insan/AI ayrımı yapabiliyor (arXiv:2602.13504) — sinyal kelimelerde değil, ritim ve sicil düzleşmesinde; skill'in yapı odaklı yaklaşımının Türkçe kanıtı
- Gerçek Türkçe düzyazı okuması: 2012-2019 arası köşe yazıları, denemeler, bloglar ve Ekşi Sözlük debe entry'leri — "Gerçek Türkçe Böyle Akar" bölümünün ve §46'nın kaynağı.
- Sade öğretici anlatım ve anlatım bozuklukları: [turkdili.gen.tr](https://turkdili.gen.tr) (Doç. Dr. Ahmet Kayasandık'ın Türk Dili ders sitesi) — 13-15 numaralı kuralların ve insan hatası tipolojisinin kaynağı. Özellikle [anlatım bozuklukları envanteri](https://turkdili.gen.tr/anlat-m-bozukluklar-.html) (200+ örnek: duruluk, tekrarlama, mantık yanlışı) hem fazlalık temizliği hem yanlış pozitif ayrımı için başvuru. Dikkat: Sitenin yazım ve noktalama sayfaları 2005 TDK kılavuzuna dayanır; yazım sorularında güncel TDK kaynağıyla çapraz kontrol et.
- Deyim ve atasözü haznesi: Ömer Asım Aksoy, "Atasözleri, Deyimler" (TDAY Belleten 1962, TDK) ve MEB atasözleri derlemesi — 16 numaralı kuralın ve `references/deyimler.md` dosyasının kaynağı
- Dilbilim ve derlem kanıtı: TDK "Türkçenin Eğitimi-Öğretiminde Kuramsal ve Uygulamalı Çalışmalar 12" (2022) — 17 numaralı kuralın kaynağı: gönderim/belirginlik hiyerarşisi (Esmer; Givon 1983 çerçevesi) ve Türkçe sıklık derlemlerinde bağlaç dağılımı (ODTÜ Derlemi, Göz 2003, TS Corpus). Not: İnsan hatasının ek/yazım düzeyinde, yapay zeka izinin söylem düzeyinde toplandığına dair karşılaştırma verisi de buradan; örneklemi yabancı öğrenici olduğu için destekleyici kanıt sayılır, tek başına dayanak değil.
- Edebi Türkçe okuması: Hüseyin Rahmi Gürpınar, "Sevda Peşinde" (TDK basımı) — 8-12 numaralı kuralların kaynağı. [TDK e-kitap sayfası](https://tdk.gov.tr/genel/e-kitaplar/) fiilen ücretsiz bir Gürpınar külliyatı; üslup çalışmak için özellikle Şıpsevdi (sicil çarpışması), Gulyabani (halk ağzı), Ben Deli miyim? (iç monolog) ve Efsuncu Baba (diyalog dokusu). Aynı sayfadaki [Eş Dizim Sözlüğü](https://tdk.gov.tr/wp-content/uploads/2019/12/01-T%C3%9CRK%C4%B0YE-T%C3%9CRK%C3%87ES%C4%B0NDE-ADLARLA-%C3%96N-ADLARIN-B%C4%B0RL%C4%B0KTEL%C4%B0K-KULLANIMI-VE-E%C5%9E-D%C4%B0Z%C4%B0M-S%C3%96ZL%C3%9C%C4%9E%C3%9C.pdf) hangi sıfatın hangi adla doğal eşleştiğini gösterir; çeviri kokusu şüphesinde başvur. Korpus arayanlara: [TurkishNLPGuide](https://github.com/nanelimon-organization/TurkishNLPGuide) derlemesi ve özellikle [Bilkent Turkish Writings](https://github.com/selimfirat/bilkent-turkish-writings-dataset) (2014-2018 arası dokuz bin öğrenci denemesi, tamamı yapay zeka öncesi). Çeviri korpuslarını (OPUS, Tatoeba) üslup referansı olarak kullanma; tam da kaçınılan çeviri kokusunu taşırlar.
- Modern anlatı ve diyalog okuması: 2000'ler Türk edebiyatından bir roman ile Amerikan edebiyatından klasik bir romanın çevirisi — 18-25 numaralı kuralların kaynağı. İki korpus, Gürpınar'dan çıkarılan 8-12 numaralı kuralların (ikileme, duyguyu bedenle gösterme, miş'li aktarım, cümle sonu bağlaç) modern edebi Türkçede ve usta işi çeviride aynen yaşadığını bağımsız olarak doğruladı. Çeviri korpusu ayrıca §16 için pozitif kanıt: İyi insan çevirisi, örneklenen hiçbir bölümde tek bir kalıp çeviri metaforu ("goblen" ailesi) taşımıyor; çeviri kokusu çevirinin değil kötü çevirinin imzası.

- [yucezerey/turkish-anti-ai-skill](https://github.com/yucezerey/turkish-anti-ai-skill) (MIT, Yüce Zerey, 2026): §49-§55'in, olgu kilidinin, Sicil Ayarı tablosunun, silme testinin, ikame tikinin ve `references/yazim-ve-terim.md` dosyasının çıkış noktası. Kurallar insanca'nın sesiyle yeniden yazıldı; TDK'de karşılığı olmayan maddeler ("ama öncesi virgül yasağı" gibi) ve kaynaksız sayılar alınmadı. Aynı paragrafın iki skill'le kör yeniden yazımı, insanca'nın ritim eşiğini taslakta görüp nihaide uygulamadığını gösterdi; Süreç'teki zorunlu değişim katsayısı kontrolü oradan geliyor.
- Tezmakale AI Dedektör (KLX 2.0) sayfa, kod ve yanıt incelemesi (Kasım 2026): Kıvrık tırnak işareti (§32) ve dedektör puanlarının metin türüne göre ayarlı olduğu uyarısı (Tespit Rehberi).


Wikipedia'dan temel içgörü: "Büyük dil modelleri bir sonraki kelimeyi istatistiksel olarak tahmin eder. Sonuç, en geniş durum yelpazesine uyan, istatistiksel olarak en olası metne yakınsar."

## 1. Türkçe üslup ve editörlük

| Kaynak | Durum | Katkı |
|---|---|---|
| [RTÜK: Yayınlarda Doğru Türkçe Raporu (2019)](https://arsivdosya.rtuk.gov.tr/assets/Icerik/Download/BilgiMerkezi/rapor-29-01-2019.pdf) | **sırada** | 4.598 gerçek yayın yanlışı, yanlış→doğru tablolu; anlatım bozuklukları (1.714 örnek) ve çeviri yanlışları alt bölümü çeviri kokusu kalıplarına ham veri |
| [Necmiye Alpay, Türkçe Sorunları Kılavuzu (archive.org, tam metin)](https://archive.org/details/necmiye-alpay-turkce-sorunlari-kilavuzu) | **sırada** | Zamir/söz fazlalığı budama, tamlama düzeltme kuralları; OCR metni sayfadan teyitle |
| [Dragoman Türkçe Editör Kılavuzu](https://www.dragoman.ist/tr/dragoman-turkce-editor-kilavuzu/) | **sırada** | Profesyonel çeviri editörlüğünün 4 kontrol alanı; çeviri kokusu giderme çerçevesi |
| [Feyza Hepçilingirler, Türkçe Off (alıntı derlemesi)](https://ismailhakkialtuntas.blogspot.com/2020/11/turkce-off-feyza-hepcilingirler.html) | bakılabilir | Medyatik klişe, eşanlamlı tekrar ("tesadüfen rastladım"), tamlama yanlışları |
| [TDK Türk Dili: Nurullah Ataç özel bölümü](https://tdk.gov.tr/wp-content/uploads/2014/09/20140919.pdf) | bakılabilir | Devrik cümle ve konuşma sıcaklığının yazı diline aşılanması; pozitif ilke kaynağı |
| [AA "Türkçeyi Doğru Kullan" kitapçığı](https://turkdili.gen.tr/files/aa_Turkceyi_Dogru_Kullan_Dogru_bilinen_yanlislar.pdf) | bakılabilir | Yanlış→doğru sözcük çiftleri (yazım ağırlıklı) |
| Ömer Asım Aksoy, Dil Yanlışları | erişilemedi (Scribd) | 2000 sözün eleştirisi; deyimler çalışması zaten işlendi |
| turkdili.gen.tr (Kayasandık) | **işlendi** (v1.6) | Sade öğretici anlatım kuralları 13-15, anlatım bozuklukları envanteri |
| Vikipedi:Biçem el kitabı / Vikipedi:Yapay zekâ | bakılabilir | Türkçe Vikipedi'de "Signs of AI writing" karşılığı YOK; insanca bu alanda öncü |
| TRT Spikerlik kitabı, BBC Türkçe üslup, Hürriyet kılavuzu | erişilemedi/yok | Türk medyası kamuya açık üslup kılavuzu yayımlamıyor; boşluğu RTÜK+AA dolduruyor |

## 2. Akademik, derlem ve sayısal

| Kaynak | Durum | Katkı |
|---|---|---|
| [Ateşman okunabilirlik formülü (karşılaştırma makalesi)](https://www.researchgate.net/publication/380156427) | **işlendi** (v1.9) | Sayısal Denetim'e formül + eşikler girdi |
| [Bezirci & Yılmaz YOD formülü (DergiPark)](https://dergipark.org.tr/en/pub/deumffmd/issue/40831/492667) | **işlendi** (v1.9) | Doğal Türkçe referansı: 9-11 kelime/cümle, 2,6 hece/kelime |
| [Keklik & Yılmaz 2013: bağdaşıklık verileri](https://dergipark.org.tr/tr/download/article-file/202242) | **işlendi** (v1.9) | Bağlaç oranları ve eksiltili anlatım payı (insan referans değerleri) |
| [Vikisözlük sıklık listesi](https://tr.wiktionary.org/wiki/Ek:T%C3%BCrk%C3%A7e_temel_s%C3%B6zl%C3%BCk_(kullan%C4%B1m_s%C4%B1kl%C4%B1%C4%9F%C4%B1na_g%C3%B6re)) | **işlendi** (v1.8) | "Ama" 20. sırada; bağlaç tercihi kanıtı |
| [TS Corpus](https://tscorpus.com) | bakılabilir | 1,8 milyar token, tür bazlı alt derlemler; şüpheli eşdizim doğrulama |
| [Türkçe Ulusal Derlemi](https://www.tnc.org.tr/tr/) | bakılabilir | 50M kelime dengeli derlem; kayıt gerekiyor |
| Göz (2003) Kelime Sıklığı Sözlüğü | erişilemedi (basılı) | Vikisözlük listesi ikame ediyor |
| [Çağdaş Türkçenin Sıklık Sözlüğü tanıtımı](https://dergipark.org.tr/tr/download/article-file/1564333) | bakılabilir | 316M kelimelik güncel derlem (kitap basılı) |
| [UD_Turkish-BOUN/IMST treebank'leri](https://universaldependencies.org/treebanks/tr_imst/index.html) | bakılabilir | Sözdizim istatistiği (ileri kalibrasyon) |
| TDK kurultay kitabı (2022) | **işlendi** (v1.8) | Gönderim merdiveni kuralı; genel verimi düşük |
| [Türkçe BERT dedektör makalesi](https://arxiv.org/abs/2602.13504) | **işlendi** (v1.2) | %97 F1; sinyal ritimde kanıtı |
| Uzun (2006) Metinleştirme Sorunları | erişilemedi (basılı) | Keklik & Yılmaz ikame ediyor |
| [Bilkent Turkish Writings](https://github.com/selimfirat/bilkent-turkish-writings-dataset) | bakılabilir | 9.119 öğrenci denemesi (2014-2018, AI öncesi insan korpusu) |
| [TurkishNLPGuide](https://github.com/nanelimon-organization/TurkishNLPGuide) | **işlendi** (v1.3) | Korpus yol haritası |

## 3. Yapay zeka yazım kalıpları (güncel)

| Kaynak | Durum | Katkı |
|---|---|---|
| [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | **işlendi** + **sırada** | Temel kaynak (v1.0); 2026 ekleri v1.9'da işlendi (koşaç kaçışı, üç aşamalı ret); sayfa canlı, dönemsel tekrar taranmalı |
| [WikiProject AI Cleanup/Guide](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide) | bakılabilir | Regex avlama desenleri ("..., -ing its" ≈ Türkçe zarf-fiil+vurgulamak zinciri) |
| [slop-forensics + EQ-Bench Slop Score](https://eqbench.com/slop-score.html) | **sırada** | Model başına slop profili; "hangi modelden çıkmış" ipucu özelliği için tek veri kaynağı; %60 kelime + %25 not-x-but-y + %15 trigram ağırlık şeması |
| [DAMAGE: doğallaştırma aracı artefaktları (arXiv 2501.03437)](https://arxiv.org/html/2501.03437v1) | **işlendi** (v1.9) | 19 doğallaştırma aracının hata taksonomisi §45'e girdi |
| [tropes.fyi](https://tropes.fyi/) | **işlendi** (v1.9) | "Serves as" ve "Ne X. Ne Y. Sadece Z." kalıpları |
| [stop-slop](https://github.com/hardikpandya/stop-slop) | bakılabilir | Puanlama rubriği fikri, girizgah kalıpları |
| [yucezerey/turkish-anti-ai-skill](https://github.com/yucezerey/turkish-anti-ai-skill) | **işlendi** (v1.13) | MIT. §49-§55, olgu kilidi, sicil tablosu, silme testi, ikame tiki, references/yazim-ve-terim.md. Elenenler: "ama öncesi virgül yasağı" (TDK'de yok), "öte yandan / bununla birlikte tek görülmede sil" (§19'un yoğunluk yaklaşımı daha doğru), kaynaksız oran ve kota sayıları |
| [Tezmakale AI Dedektör (KLX 2.0)](https://tezmakale.com/ai-detector/) | **işlendi** (v1.13) | Sayfa, kod ve canlı yanıt incelemesi: kıvrık tırnak işareti, akademik kalibrasyon (aynı uzunluktaki insan metinlerine göre yüzdelik), ücretsiz katmanda ilk ~255 kelimelik puanlama penceresi |
| [skill-deslop](https://github.com/stephenturner/skill-deslop) | bakılabilir | Akademik bağlam istisnası mantığı (bizde kısmen var) |
| [Scientific American: model imza farkları](https://www.scientificamerican.com/article/chatgpt-and-gemini-ai-have-uniquely-different-writing-styles/) | bakılabilir | Hakemli kanıt: ChatGPT resmi, Gemini konuşkan; model tahmini tablosu için |
| [Adversarial Paraphrasing (arXiv 2506.07001)](https://arxiv.org/abs/2506.07001) | bakılabilir | "Kalıp silme değil insan dağılımına taşıma" felsefesinin akademik dayanağı |
| unslop, SLOP_Detector, antislop-sampler, GLTR, DetectGPT, GPTZero klonu | **işlendi** (v1.2) | Dedektör kalıpları ve sayısal eşikler |
| Kobak vd., Juzek & Ward | **işlendi** (v1.0-1.2) | Kelime telleri eskir bulgusu |
| [TÜBİTAK Bilim Genç](https://bilimgenc.tubitak.gov.tr/makale/bir-metni-chatgptnin-hazirladigi-anlasilabilir-mi) | **işlendi** (v1.0) | İnsan noktalaması/parantez sinyalleri |
| [YÖK](https://proje.yok.gov.tr/tr/page/635) / [TÜBİTAK ÜYZ rehberleri](https://tubitak.gov.tr/sites/default/files/2025-10/UYZ_Rehberi_v03_TR.pdf) | bakılabilir | Etik çerçeve; kalıp içermiyor |
| Ekşi Sözlük başlıkları, Marketing Türkiye, R10 | **işlendi** (v1.0) | Türkçe topluluk gözlemleri |

## 4. Okuma listesi (edebi)

| Kaynak | Durum | Katkı |
|---|---|---|
| Gürpınar, Sevda Peşinde (TDK) | **işlendi** (v1.5) | Kurallar 8-12 |
| Modern Türk romanı (2002) | **işlendi** (v1.11) | Kurallar 18, 21-23 (kuyruklu cümle, etiketsiz iç ses, tavırlı adlandırma, insan listesi); Gürpınar kurallarının modern doğrulaması. Elenenler: kiazm (kalıplaşma riski), "hani şu ... var ya" (dar), baş-son aynası (kitap ölçekli) |
| Klasik Amerikan romanı çevirisi | **işlendi** (v1.11) | Kurallar 18-20, 24-25 (artlama, zaman dokuması, tezlik/sürerlik fiilleri, diyalog etiketi, konuşma parçacıkları); §16 için pozitif kanıt (usta çeviride sıfır kalıp metafor) |
| Gürpınar, Gulyabani / Şıpsevdi / Ben Deli miyim? (TDK e-kitap) | **sırada** | Halk ağzı, sicil çarpışması, iç monolog katmanları |
| [TDK Eş Dizim Sözlüğü](https://tdk.gov.tr/wp-content/uploads/2019/12/01-T%C3%9CRK%C4%B0YE-T%C3%9CRK%C3%87ES%C4%B0NDE-ADLARLA-%C3%96N-ADLARIN-B%C4%B0RL%C4%B0KTEL%C4%B0K-KULLANIMI-VE-E%C5%9E-D%C4%B0Z%C4%B0M-S%C3%96ZL%C3%9C%C4%9E%C3%9C.pdf) | bakılabilir | Sıfat-ad eşdizim doğrulama (çeviri kokusu şüphesinde) |
| Aksoy, Atasözleri-Deyimler (1962) + MEB derlemesi | **işlendi** (v1.7) | references/deyimler.md |
