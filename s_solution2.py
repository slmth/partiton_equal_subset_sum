import time #zaman olcumu icin time kutuphanemi import ediyorum

def parcalanabilir_mi(dizi): #diger cozumde oldugu gibi ayni sekilde parcalanabilirlik kontrolu yapan bi def olusturduk
  toplam = sum(dizi) #s icine dizimin sum'unu atıyorum
  if toplam % 2 != 0: #s 2'ye tam bolunurse,çiftse iki es parca aranabilir
    print("Küme toplamı ikiye bolunmez,iki eş toplamlı alt kume aranamaz")
    return False #bolunmezse false cevir
  print("Küme toplamı ikiye bölünebilir,iki eş toplamlı alt kume aranabilir")

  toplam = int(toplam / 2) #toplamın yarısını veren bir s toplami arayacagiz guncel durum sum'dan,sum/2 ye dusecek

  boy = len(dizi) #dizimin boyunu boy elemanına atiyorum
  dp = [[False for x in range(toplam+1)] for y in range(boy)] #s+1lik dongumdeki tum durumları sanki tablomu doldurur gibi aynı zamanda len kadar donen bir y dongusu icinde ceviriyorum
  #dinamik programlama icin kullanacagımdan dp icine atiyorum ki amac burda false mu true mu durumlarıyla dp kodlamak

 #ben burda bi tablo doldurdugum icin zaten sum 0 tüm alt kumelerimde mevcut varsayımından oturu 0li tüm i-0 durumlarımı True cevirecegim
  for i in range(0, boy):
    dp[i][0] = True 

  #biz satırlara olabilecek max sumları sutunlara da olabilecek tum sirali alt kumeleri atadıgımızda
  #bu alt kumelerden sum degerime esitli j gelecek sekilde bi atama yapip sumumun esit olma durumuna bakiyorum
  for j in range(1, toplam+1):
    dp[0][j] = dizi[0] == j

  for i in range(1, boy): #bu iki ic ice loop donumumde tum toplamlar icin tum alt kumeleri ceviriyorum
    for j in range(1, toplam+1):
     #i indexi olmadan eger o toplami bulabilirsem 
      if dp[i - 1][j]:
        dp[i][j] = dp[i - 1][j] #i-j ikilim icin bi geri adıma bakiyorum
      elif j >= dizi[i]:  #eger bulamazsam da kalan toplam icin yine bir alt kume ariyorum cunku iki es sum parcasi bulmam gerek
        dp[i][j] = dp[i - 1][j - dizi[i]] #i - j icin kumede bir geri adıma karsılık j de dondurdugum sum - dizimin i.degerini inceliyorum

  #ve eleman sayimin eksigi kadar dondurup suma kadar denk geldigimde cizdigim tablo zaten istedigim sonucu verirse ki True hayal edelim
  return dp[boy - 1][toplam] #biz zaten bu dizin icinden iki es parca elde edebilmisiz demektir,egerki istenilen sonucu elde edemezsek de false donecek



def main():
  dizi=[2,5,7] #kullandigim dizi
  baslangic_zaman=time.time() #zaman olcum baslangic
  print((parcalanabilir_mi(dizi))) #fonksiyonumun sonucunu yazdir
  bitis_zaman=time.time() #zaman olcum bitis
  print(bitis_zaman-baslangic_zaman,"gecen süre") #zaman olcum sonuc

main()


 
