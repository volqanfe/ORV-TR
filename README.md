# ORV Türkçe Çeviri Projesi

Bu proje, "Omniscient Reader's Viewpoint" (전지적 독자 시점) web romanının Türkçe çevirisini barındırmak için oluşturulmuş bir statik websitedir.

## 📁 Proje Yapısı

```
orv-turkish-translation/
├── index.html          # Ana sayfa (Bölüm 1)
├── styles.css          # Stil dosyası
├── README.md           # Bu dosya
└── (gelecekteki bölümler için ek HTML dosyaları)
```

## 🚀 Nasıl Kullanılır

### 1. Yerel Test
- `index.html` dosyasını herhangi bir web tarayıcısında açın
- Çeviri kalitesini ve formatlamayı kontrol edin

### 2. Ücretsiz Hosting Seçenekleri

#### GitHub Pages (Önerilen)
1. GitHub hesabı oluşturun (ücretsiz)
2. Yeni bir repository oluşturun
3. Tüm dosyaları repository'ye yükleyin
4. Settings > Pages bölümünden GitHub Pages'i etkinleştirin
5. Siteniz `https://kullaniciadi.github.io/repository-adi` adresinde yayınlanır

#### Netlify
1. [Netlify.com](https://netlify.com)'da hesap oluşturun
2. "New site from Git" seçeneğini kullanın
3. GitHub repository'nizi bağlayın
4. Otomatik deployment başlar

#### Vercel
1. [Vercel.com](https://vercel.com)'da hesap oluşturun
2. GitHub repository'nizi import edin
3. Otomatik deployment başlar

## ✏️ Çeviri Süreci

### Manuel Çeviri (Önerilen)
1. Orijinal metni kopyalayın
2. HTML etiketlerini koruyarak Türkçe'ye çevirin
3. `<p class="orv_line">` yapısını muhafaza edin
4. Özel formatlamaları (mesaj pencereleri, sistem bildirimleri) koruyun

### Yarı-Otomatik Çeviri
1. LibreTranslate veya Google Translate API kullanın
2. Metni çevirin, sonra HTML yapısına yerleştirin
3. Kalite kontrolü yapın

## 🎨 Stil Özellikleri

Website orijinal tasarımı taklit eder:
- Koyu tema
- Responsive tasarım
- Orijinal tipografi
- Mesaj penceresi formatları
- Navigasyon elementleri

## 📝 Yeni Bölüm Ekleme

1. `index.html`'i kopyalayın
2. Dosya adını değiştirin (örn: `ch_2.html`)
3. İçeriği yeni bölümle değiştirin
4. Navigasyon linklerini güncelleyin
5. Ana sayfaya bölüm linkini ekleyin

## 🔧 Özelleştirme

### CSS Değişkenleri
```css
:root {
    --primary: #1a1a1a;        /* Ana arka plan */
    --secondary: #2a2a2a;      /* İçerik arka planı */
    --text-primary: #e3e3e3;   /* Ana metin rengi */
    --text-secondary: #b3b3b3; /* İkincil metin rengi */
    --accent: #4a9eff;         /* Vurgu rengi */
}
```

### Özel Formatlar
- `.orv_system` - Sistem mesajları
- `.orv_window` - Pencere mesajları
- `.orv_constellation` - Takımyıldızı mesajları
- `.orv_quote` - Alıntılar
- `.orv_notice` - Notlar

## 📱 Responsive Tasarım

Website hem masaüstü hem de mobil cihazlarda düzgün çalışır:
- Esnek layout
- Dokunmatik navigasyon
- Okuma dostu tipografi

## 🆓 Maliyet

Tüm çözüm tamamen ücretsizdir:
- Hosting: GitHub Pages/Netlify/Vercel ücretsiz planları
- Domain: Alt domain ücretsiz (özel domain isteğe bağlı)
- Maintenance: Sadece zaman

## 🔄 Güncelleme Süreci

1. Yerel dosyaları düzenleyin
2. Git ile değişiklikleri commit edin
3. Repository'ye push yapın
4. Otomatik deployment başlar

## 💡 İpuçları

- Her bölümü ayrı HTML dosyası olarak oluşturun
- Tutarlı dosya adlandırma kullanın (`ch_1.html`, `ch_2.html`, vb.)
- Çeviri yaparken orijinal formatlamayı koruyun
- Düzenli backup alın
- Çeviri kalitesini kontrol edin

## 🤝 Katkıda Bulunma

Bu proje açık kaynaklıdır. Çeviri iyileştirmeleri ve öneriler için:
1. Repository'yi fork edin
2. Değişikliklerinizi yapın
3. Pull request gönderin

## 📞 Destek

Teknik sorunlar için GitHub Issues kullanın veya dokümantasyonu inceleyin.

