import pandas as pd
df=pd.read_csv("youtube-ing.csv")
# 1- İlk 10 kaydı getiriniz.
result=df.head(10)
# 2- İkinci 8 kaydı getiriniz.
result=df[5:20].head(8)
# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result=df.columns
result=len(df.columns)
# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
result = df.drop(columns=["thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"],axis=1)
# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result=df["likes"].mean()
result=df["dislikes"].mean()
# 6- ilk 50 videonun like kolonlarını getiriniz.
result=df["likes"].head(50).mean()
# 7- En çok görüntülenen video hangisidir ?
result=df[df["views"].max()==df["views"]]["title"]
# 8- En düşük görüntülenen video hangisidir?
result=df[df["views"].min()==df["views"]]["title"]
# # 9- En fazla görüntülenen ilk 10 video hangisidir ?
result=df.sort_values("views",ascending=False).head(10)
# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result=df.groupby("category_id")["likes"].mean()
# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız
result=df.groupby("category_id")["comment_count"].mean()
# 12- Her kategoride kaç video vardır ?
result=df.groupby("category_id").value_counts()
# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"]=df["title"].apply(len)
# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# df["tag_count"]=df["tags"].apply(lambda x: len(x.split("|")))
# result=df["tag_count"]
def tag_count(tag):
    return len(tag.split("|"))
df["tag_count"]=df["tags"].apply(tag_count)              
result=df["tag_count"]            
# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)
def like_dislike_rate(dataset):
    likelist = list(dataset["likes"])
    dislikelist = list(dataset["dislikes"])

    ratelist = []
    for like, dislike in zip(likelist, dislikelist):
        if (like + dislike == 0):
            ratelist.append(0)
        else:
            ratelist.append(like / (like + dislike))
    return ratelist

df["like_rate"] = like_dislike_rate(df)
result = df.sort_values("like_rate",ascending=False)[["title","likes","dislikes","like_rate"]]
print(result)