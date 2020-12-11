#COZUM 1 - UZUN YOLDAN TUM ALT KUMELERI TARAYARAK BULMA

import time #zaman olcumu icin time kutuphanesini import ettik

def parcalanabilirlik(list1): #bu fonksiyonda amacimiz cagirdigimiz list1 icin kontrolller yapmak
    s = sum(list1) #list1 toplamını s'e atadik
    if s % 2 != 0: #eger  s 2'ye tam bolunmezse
        print("Küme toplamı ikiye bolunmez,iki eş toplamlı alt kume aranamaz") #ekrana bu yazı ciksin
        return False #ve false dondur
    print("Küme toplamı ikiye bölünebilir,iki eş toplamlı alt kume aranabilir") #bu kisimla direkt else gecisi yaptik,bolunebilir seklinde bi yazi yazdirdik
    return alt_kumeler(list1) #eger bolunurse de beni altta olusturdugum alt kume fonksiyonuma at


def alt_kumeler(list1):  #tum alt kumeleri toparlamak adina list1'i cagiriyoruz
    altkume= [[]] #alt kumeler icin bir dizi aciyoruz
    for i in range(len(list1) + 1): #dizi boyunun 1 fazlasi kadar donuyoruz
        for j in range(i + 1, len(list1) + 1):  #j de benim alt kumemin diger elemanlarını ceker gibi,orada da i'nin bi fazlasindan dizi boyunun bi fazlasina kadar donuyoruz
            kume = list1[i:j] #i:j ikililileri halinde toplanabilecek tum parcalari kume elemanı icine sirayla atacagiz
            altkume.append(kume)#donguler her dondugunde kumeler altkume dizinimin icine atilacak
            uygunikili=[] #bos bir uygun ikili dizisi aciyorum
            key=sum(list1)/2 #benim icin onemli olan dizi toplamimin yarisi,cunku sum'un yarisi olan iki es parca arayacagım 
    for k in range(len(altkume)): #altkumeleri taramak adina yeni bir for aciyorum
        if (sum(altkume[k])==key): #alt kumemin toplami key ederse
            uygunikili.append(altkume[k])#uygunikili dizime alt kumemi atiyorum
    if len(uygunikili)==2: #dongu disina yine bir if else acip acaba uygun bi parca atilmis mi ona bakiyorum
        print("Alt küme toplamları eşittir.") #uygun ikili dizim doluysa es parcalara ayirmisimdir
        print("True")
    else:
        print("Alt küme toplamları eşit degildir.") #uygun ikili dizim bossa es iki parca yoktur
        print("False")
        
       
#main    
list1 = [2,5,7] #kullandigim dizi
baslangic_zaman=time.time() #zaman olcme baslangic
parcalanabilirlik(list1) #sonucumu cagiriyorum
bitis_zaman=time.time() #zaman olcme bitis
print(bitis_zaman-baslangic_zaman,"gecen süre") #zaman olcum sonucu 

