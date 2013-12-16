# KFTP

## Özet
KFTP UDP üzerinden çalışan bir dosya transfer protokolüdür. 

## Amaç
Dosya transferi yapan basit bir protokol oluşturmak. UDP üzerine tasarlanmıştır. Dosyaları birden çok makinadan bir makina üzerine taşımayı amaçlar. Çok basit tasarlanmış ve karmaşıklıklar 7. katman uygulamasına bırakılmıştır. FTP nin temel özelliklerini sağlamaktadır. Sadece dosya okur ve yazar. Listeleme, kullanıcı otantike etme gibi diğer özellikler bu versiyona eklenmemiştir. 

## Adımlar
* Dosya ismi ve okuma/yazma isteği sunucuya gider.
* Sunucuda ACK yada dosyanın olmaması/okunamaması ile ilgili NACK gelir.
* İstemci sunucudan dosya bilgilerini isteyen INFO komutunu gönderir.
* INFO cevap olarak dosya büyüklüğü gönderir. Ve dosya adını temsil eden bir numara gönderir.
* Her mesajın doğruluğu UDP-Checksum başlığı sayesinde bilinir.
* GET <dosya temisili adı> ile UDP nin veri kısmında kaç sunucudan çekileceği bilgisi verilir.
* Böylece n tane sunucudan istenilen parça istenebilir.
* Tüm veri bittiğinde sunucudan DONE mesajı gelir.
* İsteğe bağlı olarak sha1sum sunucudan istenir ve indirilen veri ile karşılaştırılır.
* Tüm sunuculardan DONE gelince transfer biter.
* GETS ile gelmeyen spesifik bir parça istenebilir.
* Tüm paketlerin önünde bir opscode olabilir.

## Paketler
* Read request (RRQ) > ACK/NACK
* Info request (IRQ) > ACK/NACK
* Get  request (GRQ) > data
* Gets request (SRQ) > data
* Data package (DPK) > data

### RRQ
* Dosya adı bilgisi
* Okuma/Yazma modu seçimi

> string     1byte    2byte      1byte

> Filename  |   0  |    Mode    |   0  |

* ACK -> uygun.
* NACK + Error Code -> uygun değil.

**NOT:** Dosya adı büyüklüğü sorun olabilir.

### IRQ
* Dosyayı temsilen verilen sayı
* Kaç parça gönderileceği.

> 8byte        1byte   20byte   1byte

> file_number  |  0  |   Count  |   0  |

* ACK -> uygun
* NACK + Error Code -> uygun değil

**NOT:** file number büyüklüğü sunucunun verdiği dosya sayısı hizmetini azaltabilir. Count dosya büyüklüğüne yetecekmi sorunu.

### GRQ
* Dosya temsilen verilen sayı
* Toplam kaç yerden istendiği
* Sunucu sırası.

> 8byte       1byte      2byte       1byte    2byte

> file_number  |  0  |  server_count  |  0  |  server_number

* DP ler sırayla gelir.

### SRQ
* Dosyayı temsilen verilen sayı
* Dosyanın kaçıncı parçası isteneceği

> 8byte       1byte   20byte
> file_number  |  0  | file_sequence

* DP gelir.

**NOT:** Bu istek sayesinde sırayla gelen dosya paraçlarında sorun olduğunda specifik bir parça elde edilinebilir.

### DATA
* Dosyaynın kaçıncı parçası olduğu.
* Dosya verisi.

> 8byte       1byte   2byte
> file_number  |  0  |  Mode  |  data

* Mode 0 ise paketin sonu demek.
* Mode 1 ise data paketi demek

**NOT:** data nın boyutu ayarlanmalı ve sunucular bilgilendirilmeli.

## Sonuç
Amacı UDP nin hızını kullanabilen temel bir FTP oluşturabilmek. Ufak paketler halinde alınan bilgiler client tarafında birleştirilmeli ve doğruluğundan emin olunmalı. Data nın büyüklüğü tartışılmalı ve uygun değer seçilmeli.




