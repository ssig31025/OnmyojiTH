
import json

raw_text = """
2.1. SSN
A
Aoandon Frog
Arakawa Frog
B
D
E
Enma Frog
G
H
Higanbana Frog
I
Ibaraki Frog
Ichimokuren Frog
K
Kachou Fuugetsu Frog
Kaguya Hime Frog
L
Lantern Boy
M
Miketsu Frog
N
O
Ootengu Frog
P
R
Ryoumenbotoke Frog
S
Shishio Frog
Shuten Frog
Susabi Frog
T
Tamamo no Mae Frog
U
Y
Youtou Hime Frog
Yuki Douji Frog

2.2.N
A
Akashita
B
Blue Imp
D
Daruma
E
G
Grave Digger
Green Imp
H
Hahakigami
I
K
L
Lantern Boy
Lantern Soul
M
N
Nurikabe
O
P
Parasite
R
Red Imp
S
T
U
Umbrella
Y
Yellow Imp

2.3R
A
Akaname
Ame Onna
B
Baketanuki
D
Doujo
G
Gaki
H
Heiyou
Hitotsume Kozou
Hotarugusa
J
Jikikaeru
Juzu
K
Kagewani
Kamikui
Kappa
Karasu Tengu
Kochou no Sei
Kodokushi
Koi no Sei
Korouka
Kosode no Te
Kubinashi
Kudagitsune
Kyonshii Imouto
Kyonshii Inu
Kyonshii Otouto
Kyuumei Neko
M
Mushishi
O
Oguna
P
Peach Maki & Karashi
S
Samurai no Rei
Sanbi no Kitsune
Satori
Shouzu
T
Tenjo Kudari
Tesso
U
Usagimaru
Ushi no Toki
Y
Yama Usagi
Yamawaro
Z
Zashiki Warashi

2.4.SR
A
Amanozako
Amezaiku
Aobouzu
B
Bakekujira
C
Chin
D
Doumeki
E
Ebisu
Enenra
F
Futakuchi Onna
Fuuri
G
Garuda
H
Hako no Shoujo
Hakurou
Hangan
Hannya
Hiyoribou
Hone Onna
Hoshiguma Douji
Hououka
User blog:Hzgaming/Itsumade
I
Inugami
Itsumade
Ittan Momen
J
Jorougumo
K
Kainin
Kairaishi
Kamaitachi
Kamimai
Kani Hime
Kaoru
Kawazaru
Kijo Momiji
Kingyo Hime
Kisei
Kiyohime
Komatsumaru
Kujira
Kuro Douji
Kuro Mujou
Kyonshii Ani
Kyuuketsu Hime
M
Mannendake
Miakashi
Momo no Sei
Mouba
N
Nekomata
Ninmenju
Nusubitogami
Nyuunai-suzume
O
Oitsukigami
Okikumushi
Okou
Okuribito
Oshiroi Baba
R
Rukia Kuchiki
S
Sakura no Sei
Sasori Onna
Shiro Douji
Shiro Mujou
Shoyou
T
Tagitsuhime
U
Ubume
Umi no Chou
Umibouzu
Y
Yasha
Youkinshi
Youko
Yuki Onna
Yumekui

2.5.SSR
A
Amaterasu
Aoandon
Arakawa no Aruji
Asura
E
Enma
Enmusubi no Kami
F
Fukengaku
Fuuyoukun
G
Gashadokuro
Gintoki Sakata
H
Hakuzousu
Hatsune Miku
Higanbana
Himiko
Hozuki
I
Ibaraki Douji
Ichigo Kurosaki
Ichimokuren
Inosuke Hashibira
Inuyasha
Izanami
J
Jinkougyou
K
Kachou Fuugetsu
Kagamine Rin & Len
Kagura & Sadaharu
Kaguya Hime
Karuta
Kidoumaru
Kikinyou
Kikyou
Kinnara
Kotodama
Kujaku-Myouou
Kusuriuri
M
Magatsugami
Megurine Luka
Menreiki
Miketsu
Mishige
N
Natsume & Nyanko-sensei
Nekogawa
Nezuko Kamado
Nura Rikuo
O
Onikiri
Ootakemaru
Ootengu
Orochi
R
Ryoumenbotoke
Ryukaku
S
Sakura Kinomoto
Senhime
Sesshoumaru
Shentu Ziye
Shiki
ShikigamiBox
Template:ShikigamiBox
ShikigamiBox/draft
Template:ShikigamiBox/draft
Shiranui
Shishio
Shokurei
Shuten Douji
Susabi
Susanoo
Suzuhiko Hime
Suzuka Gozen
Syaoran Li
T
Taira no Masakado
Taishakuten
Taki
Takiyasha Hime
Tamamo no Mae
Tamatori
Tanjiro Kamado
Tsukuyomi
U
Ungaikyou
W
Wenren Yixuan
Y
Yamakaze
Yato no Kami
Youtou Hime
Yuki Douji
Yuki Gozen
Z
Zenitsu Agatsuma

2.6.SP
A
Akakage Youtou Hime
B
Bakkotsu Kiyohime
Byounen Hotarugusa
D
Daiyamaten Enma
E
Eikyo Senhime
G
Gyoujitsu Ebisu
Gyourou Arakawa no Aruji
H
Hatsurei Yamakaze
Honshin Sanbi no Kitsune
I
Inaba Kaguya Hime
Inari Miketsu
J
Jinshin Shishio
Jinten Tamamo no Mae
Jiyou Takiyasha Hime
K
Kaisei Kachou Fuugetsu
Kamiochi Orochi
Kokorogari Kijo Momiji
Kuusou Menreiki
M
Matsuyoi Ubume
Mujin Yama Usagi
Myoushu Kyuumei Neko
N
Negai Tsumugi Enmusubi no Kami
O
Oniou Shuten Douji
Oura Hannya
R
Reikai Kingyo Hime
Rengoku Ibaraki Douji
Rokumei Ootakemaru
Ryougin Suzuka Gozen
Ryuukou Oitsukigami
S
Seishi Hiyoribou
Semigoori Yuki Onna
Shinjou Hoshiguma Douji
Shinkei Susabi
Shinyuu Inugami
Shoufuku Zashiki Warashi
Shouu Ootengu
Shura Kidoumaru
Soufuu Ichimokuren
T
Tenken Jinshin Onikiri
U
Ukiyo Aoandon
Unjou Fukengaku
Y
Yomei Higanbana
Younen Enenra
Youon Kinnara
Yumebiki Kochou no Sei
Z
Zenshin Ungaikyou

2.7.UR
Y
Yotohime
"""

lines = raw_text.split('\n')
current_rarity = ""
shikigami_list = []
existing_ids = ["asura", "onikiri", "sp-tamamo", "yamausagi", "taira-no-masakado"]

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    if "2.1. SSN" in line:
        current_rarity = "SSN"
        continue
    elif "2.2.N" in line:
        current_rarity = "N"
        continue
    elif "2.3R" in line:
        current_rarity = "R"
        continue
    elif "2.4.SR" in line:
        current_rarity = "SR"
        continue
    elif "2.5.SSR" in line:
        current_rarity = "SSR"
        continue
    elif "2.6.SP" in line:
        current_rarity = "SP"
        continue
    elif "2.7.UR" in line:
        current_rarity = "UR"
        continue
        
    if len(line) == 1: # Skip single letters A, B, C...
        continue
        
    if "User blog:" in line or "Template:" in line or "ShikigamiBox" in line:
        continue

    name = line
    id = name.lower().replace(" ", "-").replace("&", "and").replace("'", "")
    
    if id in existing_ids:
        continue
        
    shikigami = {
        "id": id,
        "name": name,
        "rarity": current_rarity,
        "role": [],
        "icon": "",
        "image": "",
        "bio": "Bio coming soon...",
        "stats": {
            "attack": "B",
            "health": "B",
            "defense": "B",
            "speed": "100",
            "crit": "0%",
            "critDmg": "150%",
            "effectHit": "0%",
            "effectRes": "0%",
        },
        "skills": []
    }
    shikigami_list.append(shikigami)

    shikigami_list.append(shikigami)

# Read existing TS file
ts_file_path = r"C:\Users\CHUTIMAN.C\Desktop\onmyojiTH\onmyoji-db\src\lib\data\shikigami.ts"
with open(ts_file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the end of the array
last_bracket_index = content.rfind("];")

if last_bracket_index != -1:
    # Prepare new data string (without the outer brackets of the list)
    new_data_json = json.dumps(shikigami_list, indent=4)
    # Remove first [ and last ]
    new_data_inner = new_data_json.strip()[1:-1]
    
    # Add a comma if the previous list wasn't empty (it shouldn't be)
    new_content = content[:last_bracket_index] + "," + new_data_inner + "\n];\n" + content[last_bracket_index+2:]
    
    with open(ts_file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully appended new Shikigami to shikigami.ts")
else:
    print("Could not find closing bracket in shikigami.ts")
