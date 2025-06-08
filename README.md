# Basit Python HTTP Sunucusu

Bu proje, Python'un `socket` modülü kullanılarak geliştirilen çok iş parçacıklı (multi-threaded) bir HTTP sunucusudur. Statik dosyalar (HTML, CSS, JS, resim) sunabilir, JSON API endpoint'leri sağlar ve temel MIME türlerini destekler. Uygulamada örnek olarak görsel gösterimi verilmiştir.

## Özellikler

- `GET` isteklerini işler
- Statik dosya servis eder (`/static/`)
- API endpoint’leri (`/api/hello`, `/api/data`)
- MIME türü tanıma
- Çoklu istemci desteği (threading)
- Basit hata işleme (404, 500)
- Resim gösterimi API üzerinden yapılabilir

## 🧪 Örnek Endpoint'ler

| Endpoint           | Açıklama                                |
|--------------------|-------------------------------------    |
| `/`                | `static/index.html` dosyasını döner     |
| `/api/hello`       | JSON formatında mesaj döner             |
| `/api/data`        | JPEG resmi döner (`static/marmara.jpg`) |
| `/static/style.css`| CSS dosyasını döner                     |


## Gereklilikler

- Python 3.8+
- Docker (for containerization)

## Kurulum ve Çalıştırma

1. Projeyi klonlayın:
```bash
git clone https://github.com/hilmiozbay/http-server-oss.git
cd note-app
```

2. Uygulamayı başlatın:
```bash
docker-compose up
```

3. Tarayıcınızda http://localhost:8080 adresine gidin

## Docker Image

Docker Hub'dan direkt olarak image'ı çekebilirsiniz:
```bash
docker pull ozbayhilmi/http-sunucu-uygulama:latest
```

Docker Hub Repository: https://hub.docker.com/repository/docker/ozbayhilmi/http-sunucu-uygulama
