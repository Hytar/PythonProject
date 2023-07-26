def MergeSort(array): #fonksiyon tanımlıyoruz
    if len(array) <= 1: #uzunluk 1 veya 1 den küçükse dizi zaten sıralanmıştır
        return array
        
    mid = len(array) // 2 #orta uzulugu bulmak için dizinin uzunlugunu 2 ye bölüyoruz
    array1 = array[:mid]  #ana dizin başından ortasına kadar olan kısmını array1 e eşitler
    array2 = array[mid:]  #Array2 yi de ana dizinin ortasından sonuna kadar eşitler
    #ve suan diziyi ikiye böldük 
    
    array1 = MergeSort(array1)#recursive olur
    array2 = MergeSort(array2)#recursive olur
    return Merge(array1, array2)#Merge i çağırırz ve sonucunu döndürürüz

def Merge(array1, array2):#Merge i tanımlarız
    merged_array = []
    l = r = 0
    while l < len(array1) and r < len(array2):#Eger l ve r değerleri array uzunluklarını geçmezse döngü devam etsin
        if array1[l] < array2[r]:# Hangisiin küçük oldugu karar verilir
            merged_array.append(array1[l])#küçük olan döndüreceğimiz arraya eşitlenir
            l += 1
        else:
            merged_array.append(array2[r])#küçük olan döndüreceğimiz arraya eşitlenir
            r += 1
    
    merged_array.extend(array1[l:])# listede ulaşamadığımız eleman kalmışşa dizine atar
    merged_array.extend(array2[r:])#APPEND baska sayı eklemek,EXTEND baska liste veya sayı dizisi eklemek için kullanılır    
    return merged_array# dizini döndürür

def main():
    sayilar = [1, 2, 7, 9, 0]
    sorted_sayilar = MergeSort(sayilar)
    print(sorted_sayilar)

main()

                    
        
    
    