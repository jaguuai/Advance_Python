import numpy as np

# (10,15,30,45,60) elemanlarına sahip numpy dizisi oluşturunuz
result=np.array([10,15,30,45,60])
# (5-15) arasındaki sayılarla numpy dizisi oluşturunuz
result=np.arange(5,15)
# (50-100) arasındaki saılarla 5 er 5 er artarak numpy dizisi oluşturun
result=np.arange(50,100,5)
# 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz
result=np.zeros(10)
# 10 elemanlı birlerden oluşan bir dizi oluşturunuz
result=np.ones(10)
# (0-100) arası eşit aralıklı 5 sayı üretin
result=np.linspace(0,100,5)
# (10-30) arasında random 5 sayı üretin
result=np.random.randint(10,30,5)
# [-1 ile 1 ] arasında 10 adet sayı üretin
result=np.random.randn(10)
# (3x5) boyutlarında (10-50) arasında rastgele matris
matris=np.random.randint(-50,50,15).reshape(3,5)
print(matris)
# Üretilen matrisin satır ve sütun sayıları toplamlarını bulunuz
row_total=matris.sum(axis=1)
print(row_total)
column_total=matris.sum(axis=0)
print(column_total)
# Üretilen matrisin en büyük, en küçük ,ortalaması ,en büyük değerin indeksi
max_value=matris.max()
min_value=matris.min()
avarange=matris.mean()
max_index=matris.argmax()
print(max_value,min_value,avarange,max_index)
# (10-20) arasındaki sayıları içeren dizinin ilk 3 elemenını seciniz
new_array=np.arange(10,20)
print(new_array[:3])
# Üretilen dizinin elemanlarını tersten yazınız
print(new_array[::-1])
# Üretilen matrisin ilk satırını seçiniz
print(matris[0])
# Üretilen matrisin 2. satır 3.sütundaki elemanı hangisidir?
print(matris[1,2])
# Üretilen matrisin tüm satırlardaki ilk elemanını seçiniz
print(matris[:,0])
# Üretilen matrisin her bir elemanın karesi
result=matris**2
print(result)
# Üretilen matris elemanlarının hangisi pozitif çift sayıdır?(-50,50)
doubles=matris[matris %2==0]
pozitive=doubles[doubles>0]

