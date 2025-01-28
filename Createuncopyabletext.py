import random

while True:


    def dopass(metin):

        x = random.randint(1,128)
        passs=""
        for harf in metin:

            ascii=ord(harf)
            ascii=ascii+x
            defr=chr(ascii)
            passs=passs+defr

        print("Default:",metin,"New password:",passs)
    sifresiz=input("Enter for create new password:")
    dopass(sifresiz)
    con = int(input("İf you want contıune press 1,if dont press 0: "))
    if con == 1:
        continue
    if con == 0:
        break
