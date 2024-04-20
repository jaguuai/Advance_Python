import pandas as pd
#1- Dosya hakkındaki bilgiler
df_read=pd.read_csv("Pandas/imdb.csv")
df=pd.DataFrame(df_read)
# 2- İlk 5 kaydı gösterin
result=df.head(5)
# 3- İlk 10 kaydı gösterin
result=df.head(10)
# 4- Son 5 kaydı gösterin
result=df.tail(5)
# 5- Son 10 kaydı gösterin
result=df.tail(10)
# 6- Sadece Title kolonunu alın
result=df["Title"]
# 7- Sadece Movie_Title kolonunu içeçren ilk 5 kaydı alın
result=df["Title"].head(5)
# 8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın
result=df[["Title","Rated"]].head(5)
# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın
result=df[["Title","Rated"]].tail(7)
# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın
result=df[5:][["Title","Rated"]].head()
# 11- Yayın tarihi 2014 ve 2015 arasında olan filmlerin isimleri

rsult=df[(df["Runtime"] >= 2014 )and (df["Runtime"] <= 2015)]
# 12- Değerlendirme saısı (Num_Rewiews) 100.000 den büyük ya da imdb puanı 8 ile 9 arasındaolan filmlerin listesi
result=df[(df["Num_Rewiews"] > 100.000) |((df["Rating"] > 8) and(df["Rating"] < 9)  ) ]
print(result)