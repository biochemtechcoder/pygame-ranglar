# pygame-ranglar
# 🎨 Ranglar (Python kutubxonasi)

Ranglar — bu Pygame va boshqa loyihalarda ishlatish uchun o‘zbekcha nomli ranglar kutubxonasi.  
Endi (255, 255, 0) kabi RGB kodlarini yodlab yurishingiz shart emas, oddiygina:

`python
from ranglar import rang

print(rang("sariq"))  # (255, 255, 0)
print(rang("qora"))   # (0, 0, 0)


---

✨ Imkoniyatlar

100+ tayyor rang (o‘zbekcha nomlar bilan) 🌈

RGB qiymatini oson olish

tasodifiy_rang() → random rang olish

yorqin_rang() → faqat yorqin random rang

toq_rang() → faqat to‘q random rang

rang_aralash(r1, r2) → ikki rangni aralashtirish

rang_hex(nomi) → rangni HEX formatga o‘tkazish

ranglar_royxati() → barcha rang nomlarini ko‘rish

rang_nomi(rgb) → RGB qiymatidan nomini aniqlash

yaqin_rang(rgb) → eng yaqin rang nomini topish

Agar rang topilmasa avtomatik qora (0, 0, 0) qaytaradi

Pygame bilan ishlatish juda qulay



---

📥 O‘rnatish

1. Faylni yuklab oling yoki loyihangizga qo‘shing:

ranglar.py


2. Keyin import qilib ishlating:

from ranglar import rang




---

🚀 Foydalanish misollari

🔹 Oddiy ishlatish

from ranglar import rang

print(rang("qizil"))     # (255, 0, 0)
print(rang("ko'k"))      # (0, 0, 255)
print(rang("noma'lum"))  # (0, 0, 0) → avtomatik qora

🔹 Tasodifiy rang olish

from ranglar import tasodifiy_rang, yorqin_rang, toq_rang

print(tasodifiy_rang())  # masalan: (173, 216, 230)
print(yorqin_rang())     # faqat yorqin rang, masalan: (200, 180, 250)
print(toq_rang())        # faqat to‘q rang, masalan: (50, 30, 100)

🔹 Ranglarni aralashtirish

from ranglar import rang, rang_aralash

qizil = rang("qizil")      # (255, 0, 0)
ko'k = rang("ko'k")        # (0, 0, 255)

yangi = rang_aralash(qizil, ko'k)
print(yangi)  # (127, 0, 127) → binafsha rang

🔹 HEX formatga o‘tkazish

from ranglar import rang_hex

print(rang_hex("qizil"))   # #ff0000
print(rang_hex("yashil"))  # #00ff00

🔹 Barcha ranglar ro‘yxatini ko‘rish

from ranglar import ranglar_royxati

print(ranglar_royxati())       # barcha rang nomlari
print(len(ranglar_royxati()))  # nechta rang borligini chiqarish

🔹 Rang nomini RGB qiymatdan aniqlash

from ranglar import rang_nomi

print(rang_nomi((255, 0, 0)))     # "qizil"
print(rang_nomi((255, 255, 0)))   # "sariq"
print(rang_nomi((1, 2, 3)))       # "Noma'lum rang"

🔹 Eng yaqin rangni topish

from ranglar import yaqin_rang

print(yaqin_rang((250, 10, 10)))   # "qizil" ga yaqin
print(yaqin_rang((10, 250, 10)))   # "yashil" ga yaqin


---

🎮 Pygame bilan ishlatish

import pygame
from ranglar import rang, tasodifiy_rang, rang_aralash

pygame.init()
ekran = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Ranglar sinovi")

# Fon rangini sariq qilish
ekran.fill(rang("sariq"))

# Tasodifiy rangli to'rtburchak
pygame.draw.rect(ekran, tasodifiy_rang(), (50, 50, 200, 200))

# Ikki rangni aralashtirib chizish
binafsha = rang_aralash(rang("qizil"), rang("ko'k"))
pygame.draw.circle(ekran, binafsha, (300, 200), 80)

pygame.display.flip()

ishla = True
while ishla:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ishla = False

pygame.quit()


---

📜 Ranglar jadvalidan namunalar

Rang nomi RGB qiymati

qora (0, 0, 0)
oq (255, 255, 255)
qizil (255, 0, 0)
yashil (0, 255, 0)
ko'k (0, 0, 255)
sariq (255, 255, 0)
pushti (255, 192, 203)
oltin (255, 215, 0)
firuza (64, 224, 208)
kumush (192, 192, 192)


(jami 100 ta rang mavjud!)
