from random import choice, randint
# 100 ta rang (oddiy o‘zbekcha nomlar bilan)
ranglar = {
    "qora": (0, 0, 0),
    "oq": (255, 255, 255),
    "qizil": (255, 0, 0),
    "yashil": (0, 255, 0),
    "ko'k": (0, 0, 255),
    "sariq": (255, 255, 0),
    "pushti": (255, 192, 203),
    "to'q sariq": (255, 165, 0),
    "siyohrang": (128, 0, 128),
    "kulrang": (128, 128, 128),
    "och kulrang": (192, 192, 192),
    "jigarrang": (139, 69, 19),
    "oltin": (255, 215, 0),
    "kumush": (192, 192, 192),
    "osmon ko'k": (135, 206, 235),
    "firuza": (64, 224, 208),
    "och yashil": (144, 238, 144),
    "to'q yashil": (0, 100, 0),
    "marvarid": (220, 20, 60),
    "sabzi rang": (255, 127, 80),
    "bej": (245, 245, 220),
    "shokolad": (210, 105, 30),
    "och ko'k": (173, 216, 230),
    "to'q ko'k": (0, 0, 139),
    "moviy": (0, 191, 255),
    "indigo": (75, 0, 130),
    "malina": (220, 20, 60),
    "lavanda": (230, 230, 250),
    "yomg'ir rang": (70, 130, 180),
    "tilla": (218, 165, 32),
    "kora yashil": (85, 107, 47),
    "yog'och": (160, 82, 45),
    "olcha": (222, 49, 99),
    "ko'mir": (54, 69, 79),
    "namakob": (112, 128, 144),
    "kofe": (111, 78, 55),
    "och qizil": (255, 99, 71),
    "och pushti": (255, 182, 193),
    "yozgi osmon": (135, 206, 250),
    "yangi barg": (50, 205, 50),
    "yashil olma": (154, 205, 50),
    "kaktus": (34, 139, 34),
    "ko'kimtir": (0, 128, 128),
    "firuzabop": (72, 209, 204),
    "och sariq": (255, 255, 224),
    "limon": (255, 250, 205),
    "banan": (227, 207, 87),
    "och jigarrang": (222, 184, 135),
    "qum rang": (244, 164, 96),
    "tog' kulrangi": (119, 136, 153),
    "oq kulrang": (245, 245, 245),
    "yoqut": (224, 17, 95),
    "zumrad": (80, 200, 120),
    "olov": (255, 69, 0),
    "gilos": (178, 34, 34),
    "apelsin": (255, 140, 0),
    "uzum": (153, 50, 204),
    "lavlagi": (142, 0, 0),
    "ko'k dengiz": (46, 139, 87),
    "nil rang": (0, 255, 255),
    "to'q nil": (0, 139, 139),
    "och nil": (224, 255, 255),
    "o't yashil": (124, 252, 0),
    "bahor yashil": (0, 255, 127),
    "yozgi yashil": (60, 179, 113),
    "ko'k pushti": (219, 112, 147),
    "och binafsha": (221, 160, 221),
    "to'q binafsha": (148, 0, 211),
    "qizg'ish jigarrang": (165, 42, 42),
    "kulrang ko'k": (176, 196, 222),
    "och oltin": (255, 239, 184),
    "sher rang": (193, 154, 107),
    "somon": (250, 240, 190),
    "och moviy": (191, 239, 255),
    "quyuq pushti": (199, 21, 133),
    "yorqin qizil": (255, 36, 0),
    "och olov": (255, 160, 122),
    "och firuza": (175, 238, 238),
    "to'q firuza": (0, 128, 128),
    "zaytun": (128, 128, 0),
    "sariq yashil": (173, 255, 47),
    "yashil ko'k": (0, 255, 255),
    "tog' ko'k": (70, 130, 180),
    "magenta": (255, 0, 255),
    "och magenta": (238, 130, 238),
    "quyuq magenta": (139, 0, 139),
    "pista": (152, 251, 152),
    "lavanta ko'k": (106, 90, 205),
    "ko'k binafsha": (138, 43, 226),
    "gullar pushti": (255, 20, 147),
    "sham rang": (253, 245, 230),
    "qizil to'q": (178, 0, 0),
    "feruza": (64, 224, 208),
    "shisha rang": (127, 255, 212),
    "qumli oq": (255, 248, 220),
    "to'q oltin": (184, 134, 11),
    "oyoq kulrang": (105, 105, 105),
    "och quyuq yashil": (85, 107, 47),
    "to'q kulrang": (47, 79, 79)
}

# Funksiya
def rang(nomi: str):
    return ranglar.get(nomi.lower(), (0, 0, 0))  # agar topilmasa qora qaytaradi

def tasodifiy_rang():
    return choice(list(ranglar.values()))

def yorqin_rang():
    """Yorqin (och) tasodifiy rang qaytaradi"""
    return (randint(128, 255), randint(128, 255), randint(128, 255))

def toq_rang():
    """To‘q (quyuq) tasodifiy rang qaytaradi"""
    return (randint(0, 128), randint(0, 128), randint(0, 128))

def rang_aralash(r1: tuple, r2: tuple):
    """Ikki rangni aralashtirib, yangi rang hosil qiladi"""
    return tuple((r1[i] + r2[i]) // 2 for i in range(3))

def rang_hex(nomi: str):
    """Rang nomini HEX formatga o‘tkazadi (#RRGGBB)"""
    rgb = rang(nomi)
    return '#%02x%02x%02x' % rgb

def yaqin_rang(rgb: tuple):
    """Berilgan RGB qiymatga eng yaqin rang nomini qaytaradi"""
    min_farq = float('inf')
    eng_yaqin = None
    for nom, kod in ranglar.items():
        farq = sum((rgb[i] - kod[i])**2 for i in range(3))
        if farq < min_farq:
            min_farq = farq
            eng_yaqin = nom
    return eng_yaqin
