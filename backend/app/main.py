from fastapi import FastAPI
from .api.routes import router

app = FastAPI(title="AI Data Cleaning Assistant")
app.include_router(router)

""" Veri Yükleme
data_loader/loader.py

Veri Yapisi Analizi

Sayisal / kategorik ayrimi yaptik
data_loader/schema_analyzer.py

Eksik Değer Tespiti
SimpleImputer ve KNNImputer kullandik
analysis/missing_values.py

Aykiri Değer Tespiti

Sayisal sütunlarda Isolation Forest kullandik

Denetimsiz ve hizli bir yöntem
analysis/outliers.py

Öneri Motoru

Her problem için en az 2 alternatif sunduk

Sistem karar vermiyor, kullanici seçiyor
recommendation/recommender.py

Otomatik Pipeline

Seçilen işlemleri sirayla uyguladik

Manuel temizlik otomatik hale geldi
pipeline/cleaning_pipeline.py

Veri Kalitesi Ölçümü

Önce / sonra eksik oranlarini hesaplanacak.
reporting/metrics.py

Web Tabanli Çaliştirma

FastAPI ile backend servis

Swagger ile test

Streamlit ile arayüz
api/routes.py, main.py, streamlit_app.py"""