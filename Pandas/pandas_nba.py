import pandas as pd
df=pd.read_csv("Pandas/nba.csv")
# 1- iLK 10 kaydı getirin
result=df.head(10)
# 2- Toplam kaç kayıt vardır ?
result=len(df.index)
# 3- Tüm oyuncuların toplam maaş ortalaması?
result=df["Salary"].mean()
# 4- En yüksek maaş ne kadardır?
result=df["Salary"].max()
# 5- En yüksek maaşı olan oyuncu kimdir?
result=df.Name[df["Salary"].argmax()]
# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takım?
result = df[(df.Age >= 20) & (df.Age < 25)][["Name", "Team", "Age"]]
# 7- "John Holland" isimli oyuncunun oynadığı takım?
result=df[df.Name=="John Holland"]["Team"]
# 8-Takımlara göre oyuncuların ortalama maaş bilgisi
result = pd.to_numeric(df["Salary"], errors="coerce").fillna(0)
# 9- Kaç farklı takım vardır
result=len(df.groupby("Team"))
result=df["Team"].nunique()
# 10- Her takımda kaç oyuncu oynuyor?
result=df["Team"].value_counts()
# 11- İsmi içind "and" gecen kayıtlar?
df["Name"].fillna("", inplace=True)  # NaN değerleri boş bir dizeyle doldur
result = df[df["Name"].str.contains("and")]
print(result)