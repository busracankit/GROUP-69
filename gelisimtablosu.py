import pandas as pd
import plotly.express as px

# --- CSV dosyalarını oku ---
color_df = pd.read_csv("color_deficiency.csv")
direction_df = pd.read_csv("direction_deficiency.csv")
letter_df = pd.read_csv("letter_deficiency.csv")
word_df = pd.read_csv("word_deficiency.csv")

# --- Ön işleme fonksiyonu ---
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

# --- Haftalık ortalamayı al ---
weekly_avg = all_data.groupby(["week", "category"], as_index=False).mean()

# --- Grafiği çiz ---
fig = px.line(
    weekly_avg,
    x="week",
    y="success_rate",
    color="category",
    markers=True,
    title="🧠 Haftalık Başarı Gelişimi (Kategori Bazlı)"
)

fig.update_layout(
    xaxis_title="Hafta",
    yaxis_title="Başarı Oranı (%)",
    yaxis_range=[0, 100],
    template="plotly_dark"
)

fig.show()
