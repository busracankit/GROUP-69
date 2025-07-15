import streamlit as st
import pandas as pd
import plotly.express as px

# --- CSV dosyalarını oku ---
color_df = pd.read_csv("color_deficiency.csv")
direction_df = pd.read_csv("direction_deficiency.csv")
letter_df = pd.read_csv("letter_deficiency.csv")
word_df = pd.read_csv("word_deficiency.csv")

# --- Ön işleme ---
def preprocess(df, hata_col, kategori_adi):
    df = df.copy()
    df["category"] = kategori_adi + "_" + df[hata_col].astype(str)
    return df[["week", "category", "success_rate"]]

# --- Verileri dönüştür ---
color_clean = preprocess(color_df, "renk_hatasi", "renk")
direction_clean = preprocess(direction_df, "yon_hatasi", "yon")
letter_clean = preprocess(letter_df, "harf_hatasi", "harf")
word_clean = preprocess(word_df, "kelime_hatasi", "kelime")

# --- Hepsini birleştir ---
all_data = pd.concat([color_clean, direction_clean, letter_clean, word_clean], ignore_index=True)

# --- Başarı Grafiği ---
st.title("🧠 Disleksi Gelişim Paneli")
st.subheader("📈 Haftalık Başarı Grafiği")

weekly_avg = all_data.groupby(["week", "category"], as_index=False).mean()
fig = px.line(weekly_avg, x="week", y="success_rate", color="category", markers=True)
fig.update_layout(yaxis_range=[0, 100], template="plotly_dark")
st.plotly_chart(fig)

# --- Zayıf Alanlar + Öneri ---
st.subheader("📉 Haftalık Zayıf Alanlar ve Öneriler")

zayif_alanlar = (
    weekly_avg.sort_values(["week", "success_rate"])
    .groupby("week")
    .head(3)
    .reset_index(drop=True)
)

# --- Öneri sözlüğü ---
oneriler = {
    "renk_sarı": "Sarı rengi ayırt etmeye yönelik renk karşılaştırma egzersizleri önerilir.",
    "renk_yeşil": "Yeşil tonları için dikkat geliştirme oyunları kullanabilirsin.",
    "renk_kırmızı": "Kırmızı rengi hızlı tanıma üzerine alıştırmalar yapılmalı.",
    "yon_sağ-sol": "Sağ ve sol kavramlarını pekiştirmek için fiziksel yön egzersizleri önerilir.",
    "yon_saat yönü-tersi": "Saat yönü kavramı için saat çizimi ve yön okları ile uygulamalı aktiviteler yapabilirsin.",
    "yon_yukarı-aşağı": "Yukarı-aşağı yönlerini vücut hareketleriyle öğrenmeye yönelik oyunlar etkilidir.",
    "yon_sağ çapraz-sol çapraz": "Çapraz yönleri içeren dikkat ve koordinasyon oyunları kullanılabilir.",
    "harf_b-d": "b ve d harflerini ayırt etmeye yönelik ayna egzersizleri ve yazma çalışmaları önerilir.",
    "harf_k-t": "Benzer harfler olan k ve t için eşleştirme kartları kullanılabilir.",
    "harf_m-n": "m-n harf farkını artırmak için sesli heceleme ve yazım egzersizleri önerilir.",
    "kelime_çalışan-çalışkan": "Benzer sözcükler için anlam farkı çalışmaları önerilir.",
    "kelime_gül-gül": "Çok anlamlı kelimelerle ilgili hikâye yazma ve cümle kurma çalışmaları önerilir."
}

zayif_alanlar["Öneri"] = zayif_alanlar["category"].map(oneriler)
st.dataframe(zayif_alanlar)
