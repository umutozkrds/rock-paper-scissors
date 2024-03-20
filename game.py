import random
puan = 0
secenekler = ["taş","kağıt","makas"]
while True:
    my = input("taş mı kağıt mı makas mı ?")
    pc = random.choice(secenekler)
    
    if my not in secenekler:
        print("yanlış yazım veya hatalı seçim yaptınız lütfen tekrar deneyiniz.")
    continue
    if pc == my:
        print(f"Berabere Kaldınız.. puanınız :{puan}")
        
    elif (my == "taş" and pc =="makas") or (my == "makas" and pc =="kağıt") or (my == "kağıt" and pc =="taş"):
        puan += 1
        print(f"Tebrikler kazandın puanınız :{puan}")
    else:
        puan -= 1
        print(f"Kaybettiniz.. puanınız :{puan} ")