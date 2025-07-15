# 📦 Gerekli kütüphaneler
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# 📁 1. Verileri oku
color_df = pd.read_csv("color_deficiency.csv")
direction_df = pd.read_csv("direction_deficiency.csv")
letter_df = pd.read_csv("letter_deficiency.csv")
word_df = pd.read_csv("word_deficiency.csv")

# 🔢 2. Ortalama başarıları hesapla
def get_avg(df, col_name):
    avg = df.groupby("user_id")["success_rate"].mean().reset_index()
    avg.columns = ["user_id", col_name]
    return avg

avg_color = get_avg(color_df, "avg_color_score")
avg_direction = get_avg(direction_df, "avg_direction_score")
avg_letter = get_avg(letter_df, "avg_letter_score")
avg_word = get_avg(word_df, "avg_word_score")

# 🔗 3. Hepsini birleştir
df = avg_color.merge(avg_direction, on="user_id") \
              .merge(avg_letter, on="user_id") \
              .merge(avg_word, on="user_id")

# 🚨 4. Zayıf alanları belirle
def detect_weak_areas(row, threshold=60):
    weak = []
    if row["avg_color_score"] < threshold:
        weak.append("color")
    if row["avg_direction_score"] < threshold:
        weak.append("direction")
    if row["avg_letter_score"] < threshold:
        weak.append("letter")
    if row["avg_word_score"] < threshold:
        weak.append("word")
    return weak

df["weak_areas"] = df.apply(detect_weak_areas, axis=1)

# 🎯 5. Egzersiz öneri motoru
exercise_suggestions = {
    "color": ["Renkli kelime bulmaca", "Renk sıralama oyunu"],
    "direction": ["Yön eşleme", "Ok yönü takip oyunu"],
    "letter": ["Harf ayırt etme", "Sesli-harf eşleme"],
    "word": ["Kelime tamamlama", "Eş sesli ayırt etme"]
}

def suggest_exercises(weak_areas):
    return [exercise for area in weak_areas for exercise in exercise_suggestions.get(area, [])]

df["exercise_recommendations"] = df["weak_areas"].apply(suggest_exercises)

# 💾 6. Sonuçları dışa aktar (opsiyonel)
df.to_csv("user_profiles_with_recommendations.csv", index=False)

# 🖥️ 7. Streamlit arayüzü
st.set_page_config(page_title="LetStep Öğrenme Profili", layout="centered")
st.title("LetStep Bireysel Öğrenme Profili")
st.write("Kullanıcıların temel beceri alanlarındaki başarı oranlarını ve önerilen egzersizleri inceleyin.")

# 👤 Kullanıcı seçimi
user_id = st.selectbox("Kullanıcı Seçin", df["user_id"].unique())
user = df[df["user_id"] == user_id].iloc[0]

# 📊 Bar Grafik: Başarı Skorları
scores = {
    "Renk": user["avg_color_score"],
    "Yön": user["avg_direction_score"],
    "Harf": user["avg_letter_score"],
    "Kelime": user["avg_word_score"]
}

st.subheader("Temel Beceri Skorları (%)")
fig, ax = plt.subplots()
ax.bar(scores.keys(), scores.values(), color=["#6699CC", "#66CC99", "#FF9966", "#CC6666"])
ax.axhline(60, color='red', linestyle='--', label='Eşik Değeri (%60)')
ax.set_ylim(0, 100)
ax.set_ylabel("Başarı Oranı")
ax.set_title(f"Kullanıcı {user_id} Skorları")
ax.legend()
st.pyplot(fig)

# 🔍 Zayıf Alanlar + Açıklamalar
st.subheader("Öğrenme Güçlüğü Gözlemleri")
alan_bilgisi = {
    "color": "Renk ayrımı, kelime tanımada dikkat becerileriyle ilişkilidir.",
    "direction": "Yön algısı, b/d/p/q gibi harf karışmalarını önlemede önemlidir.",
    "letter": "Harf tanıma, temel okuma becerisinin temelidir.",
    "word": "Kelime tanıma, akıcı ve anlamlı okumayı sağlar."
}

if user["weak_areas"]:
    for alan in user["weak_areas"]:
        st.markdown(f"- **{alan.capitalize()}**: {alan_bilgisi.get(alan, 'Açıklama bulunamadı.')}")
else:
    st.success("Bu kullanıcıda belirgin bir öğrenme güçlüğü gözlemlenmemiştir.")

# 📌 Egzersiz Önerileri
st.subheader("Hedeflenmiş Uygulama Önerileri")
if user["exercise_recommendations"]:
    for ex in user["exercise_recommendations"]:
        st.markdown(f"- {ex}")
else:
    st.info("Bu kullanıcı için özel öneri bulunmamaktadır.")
