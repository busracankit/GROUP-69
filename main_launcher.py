import pandas as pd

# Dosyayı oku
df = pd.read_csv("color_deficiency.csv")

# Sütun adlarını yazdır
print(df.columns)
