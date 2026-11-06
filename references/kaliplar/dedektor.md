# Dedektör kalıpları (§42-§45)

Bu dosya SKILL.md'deki Kalıp Dizini'nin ayrıntısıdır. Kalıp numaraları SKILL.md ile aynıdır; "bkz. §n" göndermeleri bu numaralara gider. "Sonra" örneklerindeki rakam, kurum ve sahneler gösterim içindir; gerçek işte kaynakta yoksa uydurma (SKILL.md, Görevin, madde 5).


Bu bölümdeki kalıplar, açık kaynak yapay zeka dedektörlerinin (GPTZero klonları, GLTR, DetectGPT, slop dedektörleri) kaynak kodundan tersine mühendislikle çıkarıldı. Dedektörler kelimelere değil ölçülebilir yapıya bakar; bu kalıplar da o yüzden yapısaldır.

### 42. Açılış Tekrarı

**Sorun:** Dedektörler cümlelerin ve paragrafların ilk kelimelerinin dağılımını ölçer: ilk kelimelerin benzersizlik oranı düşükse, aynı açılış dört ve üzeri tekrarlanıyorsa veya art arda üç paragraf "Ancak / Ayrıca / Dahası" gibi bağlaçlarla açılıyorsa metin işaretlenir. "Her [isim] [fiil]..." kalıbıyla açılan paragraflar da ("Her marka bir hikaye anlatır... Her müşteri bir yolculuktadır...") aynı ailedendir. Cümle ve paragraf açılışlarını çeşitlendir.

**Önce:**
> Uygulama zaman kazandırıyor. Uygulama ayrıca maliyetleri düşürüyor. Uygulama ekip içi iletişimi de kolaylaştırıyor. Uygulama bu yönleriyle rakiplerinden ayrışıyor.

**Sonra:**
> Uygulama zaman kazandırıyor, maliyeti de düşürüyor. Ekip içi iletişim tarafı ise beklemediğimiz bir artı oldu; rakiplerde bu üçü bir arada yok.


### 43. Özet Sandviçi ve Yol Haritalı Giriş

**Sorun:** Belge biçimindeki en güçlü dedektör sinyallerinden biri: giriş paragrafı yazının bölümlerini önceden sıralar ("Bu yazıda önce X'i, ardından Y'yi ele alacağız"), kapanış paragrafı da girişin kelimelerini geri çağırıp aynı şeyi bir daha söyler. Dedektörler ilk ve son paragraf arasındaki kelime çifti örtüşmesini ölçer; insan yazısında bu örtüşme sıfıra yakındır. Girişte yol haritası verme, kapanışta girişi tekrarlama; sona yeni ve somut bir şey koy ya da metni son fikirle bitir.

**Önce:**
> Bu yazıda uzaktan çalışmanın avantajlarını, zorluklarını ve geleceğini ele alacağız. [...] Sonuç olarak, uzaktan çalışmanın avantajları, zorlukları ve geleceği hakkında söylenebilecek çok şey var.

**Sonra:**
> (Yol haritası cümlesi silinir, yazı doğrudan ilk somut tespitle açılır ve en son bulguyla biter.)


### 44. Gri Kelime Duvarı

**Sorun:** GLTR gibi dedektörler her kelimenin, dil modelinin o noktada tahmin edeceği "en olası" kelimelerden olup olmadığına bakar. Yapay zeka metninde neredeyse her kelime en güvenli seçimdir; metin boydan boya "gri"dir, hiçbir kelime şaşırtmaz. İnsan yazısında düşük olasılıklı seçimler vardır: beklenmedik ama yerinde bir fiil, bir deyim, yöresel bir ifade, modelin tahmin edemeyeceği kişisel bir detay. Yeniden yazarken her cümlenin "en tahmin edilebilir" halinden en az birkaç yerde sap; ama zorlama egzotik kelimeyle değil, gerçek spesifiklikle.

**Önce:**
> Toplantı verimli geçti. Önemli kararlar alındı ve sonraki adımlar belirlendi. Ekip motivasyonu yüksekti.

**Sonra:**
> Toplantı iki saat sürdü ama asıl iş son on dakikada bitti: Fiyat kararını erteleyip ambalajı öne çektik. Çıkışta kimse asansörü beklemedi, herkes merdivenden konuşa konuşa indi.


### 45. Aşırı Düzeltme Kokusu

**Sorun:** Doğallaştırmanın kendisi de bir imza bırakabilir. Zorlama kesik cümleler, her paragrafa serpiştirilmiş "X değil. Y." yumrukları, sahte pürüzler, yapmacık argo: bu "anti-slop sicili" yeni nesil dedektörlerin ayrıca eğitildiği bir hedef (Turnitin 2025'te piyasadaki doğallaştırma araçlarının çıktısına özel tespit modülü duyurdu). İkinci tuzak, eş anlamlı değiştirmenin yeterli sanılması: kelimeleri değiştirip cümle yapısını korumak dedektörlerin ölçtüğü ritim parmak izini olduğu gibi bırakır. Piyasadaki doğallaştırma araçlarının bilinen artefaktları da bu kalıba girer; 19 aracı inceleyen DAMAGE çalışmasının (arXiv:2501.03437) taksonomisiyle: bağlama oturmayan tuhaf eşanlamlı ikamesi, metnin seviyesinin aniden düşmesi (akademik paragrafın ilkokul diline inmesi), araç artıkları ve bozulan dil bilgisi. En iyi araçlarda bile akıcılık kazanma oranı yüzde 26'da kalıyor. Üçüncü tuzak ikame tikidir: "kritik bir rol oynuyor", "kusursuz bir şekilde" gibi öbekleri silerken her cümleye refleksle "doğrudan", "aslında", "ciddi ölçüde", "gerçekten" sokmak. Model yeni bir dolgu kelimesine kilitlenir; çoğu zaman en doğal çözüm zarfı tamamen atıp fiili yalnız bırakmaktır. Doğallık ölçülü olandır; bir iki pürüz yeter, her cümle sürpriz olmak zorunda değil.

**Önce (aşırı düzeltilmiş):**
> Verim mi? Arttı. Hem de nasıl. Maliyet düştü, moral tavan. Kimse inanmıyordu. Yanıldılar. Hepsi.

**Sonra:**
> Verim gerçekten arttı, maliyet de düştü. İşin garibi, pilotun başında buna ekipten kimse ihtimal vermiyordu.
