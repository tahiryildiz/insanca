# Yazım, Terim ve Arayüz Metni Başvurusu

SKILL.md'deki §32 (noktalama), §54 (teknik terim) ve §55 (ürün ve arayüz metni) için ayrıntılı tablolar. Kalıp tespiti SKILL.md'de; burası "doğrusu ne?" sorusuna hızlı cevap için.

Ses kalibrasyonu her zaman kazanır: Yazarın kendi örneği bir tercihi tutarlı biçimde kullanıyorsa (ör. hep `14:30`, hep "server") ona dokunma.

## 1. Rakam, saat ve aralık

| Konu | Yapay zekanın yazdığı | Türkçede | Not |
|---|---|---|---|
| Ondalık | `3.14`, `%42.5` | `3,14`, `%42,5` | Ondalık ayraç virgüldür. |
| Binlik | `10,000` | `10.000` | Binlik ayraç noktadır; dört basamaklı sayılarda (`2026`, `5000`) ayraç kullanılmaz. |
| Yüzde | `25%`, `% 25` | `%25` | İşaret sayıdan önce, bitişik. |
| Saat | `14:30` | `14.30` | TDK nokta önerir. Arayüz, log ve kod metninde `14:30` olduğu gibi kalır. |
| Saate gelen ek | `13.00'da`, `14.30'te` | `13.00'te`, `14.30'da` | Ek okunuşa göre gelir: "on üçte", "on dört otuzda". |
| Aralık | `2020–2024`, `2020 - 2024` | `2020-2024` | Kısa çizgi, boşluksuz. Orta çizgi (–) Türkçede kullanılmaz (bkz. §22). |

## 2. Virgül

- `ve`, `veya`, `ya da`, `yahut` bağlaçlarından önce virgül konmaz: "Sistem hızlı ve kararlı."
- Tekrarlı bağlaçlarda (`hem... hem`, `ne... ne`, `ya... ya`) araya virgül konmaz: "hem hızı artırır hem maliyeti düşürür."
- Zarf-fiilden sonra virgül genelde gereksizdir: "Veriyi çekip, temizledik" değil, "Veriyi çekip temizledik". Art arda sıralanan zarf-fiiller arasına konabilir.
- Özneden ve "sayesinde", "nedeniyle" gibi edat öbeklerinden sonra İngilizce alışkanlığıyla atılan virgülü kaldır (bkz. §32).
- `ama`, `fakat`, `ancak` öncesindeki virgül TDK'de yasak değildir ve gerçek düzyazıda yaygındır; ona dokunma. Bazı kaynaklar bunu "kesin yasak" diye sunar; bu skill o maddeyi bilerek almaz.

## 3. Sık bitişik/ayrı yazım hataları

| Doğrusu | Sık yanlış | Kısa gerekçe |
|---|---|---|
| birçok, birkaç, biraz | bir çok, bir kaç | Belirsizlik sözleri bitişik. |
| pek çok, pek az | pekçok | "pek" ile kurulanlar ayrı. |
| hiçbir, herhangi bir | hiç bir, her hangi bir | "hiçbir" ve "herhangi" bitişik, ardındaki "bir" ayrı. |
| bir şey, her şey, hiçbir şey | birşey, herşey | "şey" her zaman ayrı. |
| art arda, yan yana, iç içe | ard arda, yanyana | İkilemeler ayrı. |
| yanı sıra | yanısıra | "sıra" ile kurulanlar ayrı. |
| iş birliği, güç birliği | işbirliği | "birlik" ile kurulan tamlamalar ayrı. |
| fark etmek, terk etmek, ayırt etmek | farketmek, terketmek | Ses olayı yoksa yardımcı fiil ayrı. |
| kaydetmek, affetmek, reddetmek | kayıt etmek, red etmek | Ses düşmesi ya da türemesi varsa bitişik. |
| ya da | yada | Her zaman ayrı. |
| demek ki, öyle ki, kaldı ki | demekki, öyleki | Bağlaç olan "ki" ayrı. |
| çünkü, belki, sanki, halbuki, oysaki, mademki | çünki, halbu ki | Kalıplaşmış birkaç "ki" bitişik. |

Bağlaç "de/da" için §32 geçerli.

## 4. Teknik terimler

Üç küme var; metne başlamadan hangi kümede olduğuna bak.

| Küme | Örnekler | Ne yap |
|---|---|---|
| Sektör İngilizce kullanıyor | endpoint, deploy, commit, merge, rebase, pull request, pipeline, payload, webhook, middleware, migration, script, token, prompt, fine-tuning, RAG | Olduğu gibi bırak. "Uç nokta", "göç betiği", "çekme isteği", "ara katman" okuru durdurur. |
| Yerleşik Türkçesi var | geliştirici, kullanıcı, veritabanı, klasör, arama, doğrulama, canlı ortam | Türkçesini kullan; "developer", "user" diye bırakmak sicili kaydırır. |
| İkisi de yaşıyor | cache / önbellek, server / sunucu, request / istek, response / yanıt, interface / arayüz | Birini seç, metin boyunca koru. Bir cümlede "server", sonrakinde "sunucu" yazma. |

Öz Türkçecilik de tuzaktır: Günlük ve mesleki dilde yaşayan "performans", "strateji", "sistem", "detay" gibi kelimeleri zorlama karşılıklarla değiştirme.

## 5. Yabancı terime gelen ek

Ek yazılışa değil okunuşa göre gelir; kesme işaretiyle ayrılır.

| Terim | Okunuş | Yanlış | Doğru |
|---|---|---|---|
| cache | keş | cache'ı, cache'dan | cache'i, cache'te, cache'ten |
| SQL | es-kü-el | SQL'ı, SQL'da | SQL'i, SQL'de |
| JSON | ceysın | JSON'i, JSON'de | JSON'ı, JSON'da |
| GitHub | githab | GitHub'de, GitHub'i | GitHub'da, GitHub'ı |
| Google | gugıl | Google'de, Google'i | Google'da, Google'ı |
| Docker | dakır | Docker'de | Docker'da, Docker'ı |
| React | riekt | React'ı, React'da | React'i, React'te |
| Node.js | nod ceyes | Node.js'ı | Node.js'i, Node.js'te |
| URL | u-re-le | URL'ı, URL'da | URL'yi, URL'de |
| API | a-pe-i | API'ya | API'ye, API'de |
| CPU | si-pi-yu | CPU'ı | CPU'yu, CPU'da |

Kısaltmanın ekibin ağzında başka okunduğu durumlar olur (API'yi "ey-pi-ay" diye okuyan ekip "API'a" yazar). Okunuş tutarlıysa ve metin boyunca aynıysa dokunma; tutarsızsa birine indir.

## 6. Ürün, uygulama mağazası ve arayüz metni

İngilizce şablondan birebir gelen kalıplar ve Türkçede oturan karşılıkları. Karşılıklar kalıp değil öneridir; ürünün kendi sesine göre seç.

| İngilizce şablon | Çeviri kokan | Türkçede |
|---|---|---|
| Ready to get started? | Başlamaya hazır mısınız? | Hemen başlayın / Ücretsiz deneyin |
| Take X to the next level | X'i bir üst seviyeye taşıyın | X'i büyütün / hızlandırın / geliştirin |
| Empower your team | Ekibinizi güçlendirin | Ekibinizin işini kolaylaştırın |
| Save time and money | Zamandan ve paradan tasarruf edin | Zaman da para da kazanın |
| Tailored to your needs | İhtiyaçlarınıza göre özel olarak tasarlanmış | İşinize göre ayarlanan |
| All-in-one / one-stop shop | Hepsi bir arada çözüm / tek durak noktası | Gereken her şey tek yerde |
| Seamlessly integrates | Kusursuz bir şekilde entegre olur | Ek ayar istemeden bağlanır |
| Unlock the potential | Potansiyelinizin kilidini açın | (Somut faydayı yaz) |
| Game-changer | Oyun değiştirici | (Neyi değiştirdiğini yaz) |
| Leverage | Kaldıraç olarak kullanın | Kullanın / değerlendirin |
| No credit card required | Kredi kartı gerekmemektedir | Kredi kartı gerekmez |
| Send via WhatsApp / Share on X | WhatsApp'ta gönder / X üzerinde paylaş | WhatsApp'tan gönder / X'te paylaş |
| See who opened and edited | Kim açtı, kim düzenledi gör | Kimin açıp düzenlediğini gör |
| Let's dive in! | Hadi başlayalım! / Haydi dalalım! | (Sil, içerikle başla) |

Buton ve başlık metninde kalıp daha çok batar: Okur aynı ekranı her gün görür. Hal ekine ayrıca bak; "-ta gönder", "üzerinde paylaş" gibi İngilizce edat kopyaları en sık kaçan tel.

## Kaynak

Bölüm 1-6'nın çıkış noktası [yucezerey/turkish-anti-ai-skill](https://github.com/yucezerey/turkish-anti-ai-skill) (MIT) referans dosyalarıdır; tablolar insanca'nın ihtiyacına göre seçilip yeniden yazıldı, TDK'de karşılığı bulunmayan maddeler (ör. "ama öncesi virgül yasağı") alınmadı. Yazım kurallarında güncel TDK Yazım Kılavuzu esastır; şüphede ona bak.
