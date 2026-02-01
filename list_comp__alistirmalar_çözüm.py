##################################################
# List Comprehensions
#################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini
# büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.


import seaborn as sns
import pandas as pd


# veri setinin içindeki max. sütunlar gözükmeli
pd.set_option('display.max_columns', None)

# veri setinin içindeki görüntüyü genişletme
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")

df.head()
df.columns


for col in df.columns:
    print(col)

["NUM_" + col.upper() if df[col].dtype in [int, float] else col.upper() for col in df.columns]

["NUM_" + col.upper() if df[col].dtype != "0" else col.upper() for col in df.columns]

    
# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin
# isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']


[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin
# isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################

#
# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#
og_list = ["abbrev", "no_previous"]

new_col = [col for col in df.columns if col not in og_list]
df[new_col].head()


og_list = [col for col in df.columns if "rev" in col]

# Alternative Solution
new_col2 = [col for col in df.columns if "rev" not in col]
df[new_col2].tail()


##############################################
# Bonus Uygulamalar -List Comprehension
##############################################

# 1 Write a list comprehension that generates a list of all possible substrings of a given string.
string = "myth"
# ['m', 'my', 'myt', 'myth', 'y', 'yt', 'yth', 't', 'th', 'h']

len(string)

sub_string = []
for i in range(len(string)):
    for j in range(i+1, len(string)+1):
        sub_string.append(string[i:j])
print(sub_string)

# List Comprehension
[string[i:j] for i in range(len(string)) for j in range(i+1, len(string)+1)]


# 2 Write a list comprehension that flattens a nested list into a single list.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

single = []

for flat in nested_list:
    for x in flat:
        single.append(x)

print(single)

[x for flat in nested_list for x in flat]


# 3 Write a list comprehension that generates a list of all possible combinations of two strings from two given lists.
list1 = ['a', 'b']
list2 = ['x', 'y']
# ['ax', 'ay', 'bx', 'by']

[c + d for c in list1 for d in list2]


# 4 Write a list comprehension that generates a list of prime numbers up to a given number n.
n = 20
# [2, 3, 5, 7, 11, 13, 17, 19]


def is_prime(nummer):
    if nummer < 2:
        return False
    for i in range(2, int(nummer ** 0.5) + 1):
        if nummer % i == 0:
            return False
    return True


prime_sayilar = []
for number in range(2, n+1):
    if is_prime(number):
        prime_sayilar.append(number)

print(prime_sayilar)


[number for number in range(2, n+1) if is_prime(number)]

# Alternative Solution for List Comprehension
n = 20
[number for number in range(2, n+1) if all(number % i != 0 for i in range(2, int(number**0.5)+1))]


# 5 #Write a list comprehension that finds all numbers in a given list that are divisible by the sum of their digits.
numbers = [12, 23, 34, 45, 56, 67, 78, 89, 90]
# [12, 45, 90]

result = []
for num in numbers:
    if num % sum(map(int, str(num))) == 0:
        result.append(num)

print(result)


# List Comprehension
[num for num in numbers if num % sum(map(int, str(num))) == 0]


# 6  unique elemanları döndüren fonksiyonu yazınız.

no_unique_list = [1, 1, 1, 2, 2, 2, 3, 5, 5, 5, 7, 7, 7, 9, 9, 9]
# [1, 2, 3, 5, 7, 9]


def no_unique(i):
    liste2 = list(set(i))
    return liste2


no_unique(no_unique_list)


# 7 Bir sayı listesi alıp bu listenin içindeki tüm elemanları toplayan fonksiyonu yazınız.
sampleList = [15, 25, 40, 55, 60]
# Liste Elemanlarının Toplamı: 195


def sum(sayi_listesi):
    toplam = 0
    for eleman in sayi_listesi:
        toplam += eleman
    return toplam


sampleList = [15, 25, 40, 55, 60]
toplam = sum(sampleList)
print("Liste Elemanlarının Toplamı:", toplam)

sum([eleman for eleman in sampleList])

# 8 For döngüsü kullanarak faktöriyel hesabını yazınız.
n = 5
# [1, 1, 2, 6, 24, 120]

def faktoriyel(n):
    factorial = [1]
    for i in range(1, n+1):
        faktoriyel = factorial[-1] * i
        factorial.append(faktoriyel)
    return factorial


n = 5
faktoriyeller = faktoriyel(n)
print(faktoriyeller)


# 9 For döngüsü kullanarak girilen sayının faktöriyel hesabını yazan fonksiyonu yazınız

def faktoriyel_hesapla(n):
    faktoriyel = 1
    if n < 0:
        return " Negatif sayıların faktoriyeli tanımsızdır."
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
            faktoriyel *= i
        return faktoriyel


sayi = int(input("Faktoriyel hesaplamak istediğiniz sayıyı giriniz:"))

faktoriyel = faktoriyel_hesapla(sayi)

print(faktoriyel)


# 10 players listesinde kelime uzunluğu 6'den küçük olanları getiren listeyi tanımla
players = ["messi", "ronaldo", "benzema", "mbappe", "haaland"]

liste = []
for i in players:
    if len(i) < 6:
        liste.append(i)
print(liste)


goat = [i for i in players if len(i) < 6]
print(goat)

# 11 Write a program that assigns class 0 for values less than 0.5 and 1 for values greater than or equal to 0.5.
# Print the result to the console as shown below.
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
# [0, 1, 0, 1, 1, 0]

result = []

for prob in probabilities:
    if prob > 0.5:
        result.append(1)
    else:
        result.append(0)

print(result)

[1 if prob > 0.5 else 0 for prob in probabilities]



# 12 Iterate through the indexes list and print to the console only those indexes containing 'IP' or 'S&P'.
indexes = [
    "BOVESPA",
    "DOW JONES COMP",
    "DOW JONES INDU",
    "DOW JONES TRANS",
    "DOW JONES UTIL",
    "IPC",
    "IPSA",
    "MERVAL",
    "NASDAQ COMP",
    "NASDAQ100",
    "S&P500",
    "S&P/TSX COMP",
]
#['IPC', 'IPSA', 'S&P500', 'S&P/TSX COMP']

for index in indexes:
    if 'IP' in index or 'S&P' in index:
        print(index)

[index for index in indexes if 'IP'in index or 'S&P'in index]