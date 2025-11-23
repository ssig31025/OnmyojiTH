
import json

# 1. Detailed Shikigami Data (Preserved)
detailed_shikigami = [
    """    {
        id: "asura",
        name: "Asura",
        rarity: "SSR",
        role: ["DPS"],
        icon: "/images/shikigami/asura_icon.png",
        image: "/images/shikigami/asura_full.png",
        bio: "A god of battle born from the darkness of the abyss. He seeks to destroy the heavens.",
        stats: {
            attack: "SS",
            health: "B",
            defense: "B",
            speed: "119",
            crit: "10%",
            critDmg: "150%",
            effectHit: "0%",
            effectRes: "0%",
        },
        skills: [
            {
                name: "Lotus Eyes",
                icon: "",
                type: "Normal",
                orbCost: 0,
                description: "Attacks one target dealing 100% damage.",
                levelUpEffects: [
                    { level: 2, description: "Damage increased to 105%" },
                    { level: 5, description: "Damage increased to 125%" },
                ],
            },
            {
                name: "Demon Eyes",
                icon: "",
                type: "Passive",
                orbCost: 0,
                description: "When Asura kills an enemy, he gains 1 stack of Madness.",
                levelUpEffects: [],
            },
            {
                name: "Purgatory",
                icon: "",
                type: "Active",
                orbCost: 3,
                description: "Attacks all enemies dealing 315% damage.",
                levelUpEffects: [
                    { level: 5, description: "Damage increased to 335%" },
                ],
            },
        ],
    }""",
    """    {
        id: "onikiri",
        name: "Onikiri",
        rarity: "SSR",
        role: ["DPS"],
        icon: "/images/shikigami/onikiri_icon.png",
        image: "/images/shikigami/onikiri_full.png",
        bio: "The demon cutter sword of the Minamoto clan.",
        stats: {
            attack: "S",
            health: "C",
            defense: "C",
            speed: "117",
            crit: "11%",
            critDmg: "150%",
            effectHit: "0%",
            effectRes: "0%",
        },
        skills: [
            {
                name: "Ghost Cut",
                icon: "",
                type: "Normal",
                orbCost: 0,
                description: "Attacks one target dealing 80% damage.",
                levelUpEffects: [],
            },
        ],
    }""",
    """    {
        id: "sp-tamamo",
        name: "Blazing Tamamo",
        rarity: "SP",
        role: ["DPS"],
        icon: "",
        image: "",
        bio: "The fox spirit in his prime power.",
        stats: {
            attack: "SS",
            health: "C",
            defense: "C",
            speed: "115",
            crit: "12%",
            critDmg: "150%",
            effectHit: "0%",
            effectRes: "0%",
        },
        skills: [],
    }""",
    """    {
        id: "yamausagi",
        name: "Yamausagi",
        rarity: "R",
        role: ["Support", "Puller"],
        icon: "",
        image: "",
        bio: "A cute rabbit riding a demon frog.",
        stats: {
            attack: "B",
            health: "B",
            defense: "B",
            speed: "115",
            crit: "0%",
            critDmg: "150%",
            effectHit: "0%",
            effectRes: "0%",
        },
        skills: [],
    }""",
    """    {
        id: "taira-no-masakado",
        name: "Taira no Masakado",
        rarity: "SSR",
        role: ["DPS", "Support"],
        icon: "/images/shikigami/taira-no-masakado/skin1.png",
        image: "/images/shikigami/taira-no-masakado/skin1.png",
        bio: "A powerful Onmyoji who wields the artifact Futsunomitama. He can switch between Offensive and Defensive stances based on his stats.",
        stats: {
            attack: "4020 (SS)",
            health: "10254 (B)",
            defense: "595 (SS)",
            speed: "116 (S)",
            crit: "10% (S)",
            critDmg: "160%",
            effectHit: "0%",
            effectRes: "0%",
        },
        skills: [
            {
                name: "Soaring Strike",
                icon: "/images/shikigami/taira-no-masakado/skill1.webp",
                type: "Normal",
                orbCost: 0,
                description: "Amidst chaos, kneel before me. Taira no Masakado attacks a single target dealing damage equal to 100% of his ATK.",
                levelUpEffects: [
                    { level: 2, description: "Damage increases to 105%." },
                    { level: 3, description: "Damage increases to 110%." },
                    { level: 4, description: "Damage increases to 115%." },
                    { level: 5, description: "Damage increases to 125%." },
                ],
            },
            {
                name: "Time Rift Rotation",
                icon: "/images/shikigami/taira-no-masakado/skill2.webp",
                type: "Passive",
                orbCost: 0,
                description: `The tides of battle turn.
Exclusive effect. At the start of the battle, Taira no Masakado's starting ATK exceeds 700% DEF, enters Offensive Stance; otherwise enters Defensive Stance. Wields artifact Futsunomitama. [Cast] Switches stance.

<b>Offensive Stance (攻击架势)</b> <img src="/images/shikigami/taira-no-masakado/Offensive Stance.webp" />: When casting Eternal Blazing Sun, enhances Futsunomitama once.

<b>Defensive Stance (防守架势)</b> <img src="/images/shikigami/taira-no-masakado/Defensive Stance.webp" />: When attacked, recovers HP equal to 500% of starting DEF (up to 70% of starting ATK) and enhances Futsunomitama once (can be enhanced once per turn).

<b>Futsunomitama</b> <img src="/images/shikigami/taira-no-masakado/Futsunomitama.webp" />: After every 3 enhancements, Taira no Masakado immediately enters Rift in Time.

<b>Transferred Damage</b>: One of the types of damage, cannot crit, is due to some shikigami skills being able to distribute damage, such as Shouzu's link and Ushi no Toki's doll.

<b>Recover</b>: Different from healing or restoring, cannot Crit, unaffected by reduced healing effects and does not trigger effects related to healing.

<b>Control Effect</b>: Freeze, Sleep, Confuse, Taunt, Silence, Bind, Morph, Daze, Provocation, Deep Freeze, Frostbound, Shadowbound, Fettered, Ruined, and Rest in Ice are considered to be control effects. The final 9 cannot be dispelled. Frostbound cannot be dispelled or removed.

<b>Rift in Time (时之隙)</b>: Traverse in the rupture of time and space where actions are not counted towards a turn and are regarded as outside of turn actions.`,
                levelUpEffects: [
                    { level: 2, description: "After Rift in Time ends, reduces own duration of received debuffs and control effects by 1 turn." },
                    { level: 3, description: "While in Rift in Time, Eternal Blazing Sun's orb cost is reduced by 2." },
                    { level: 4, description: "Defensive Stance's recover effect also applies to other allies (70% effectiveness)." },
                    { level: 5, description: "While in Offensive Stance, each time Futsunomitama is enhanced, Eternal Blazing Sun's AoE multiplier increases by 5% (max 15%)." },
                ],
            },
            {
                name: "Eternal Blazing Sun",
                icon: "/images/shikigami/taira-no-masakado/skill3.webp",
                type: "Active",
                orbCost: 3,
                description: `Halting the war with my might, no legion's power can compare to mine.
Taira no Masakado attacks all enemies 3 times, dealing 64% ATK damage each hit. Then he deals ruin damage equal to 18% of total damage dealt to selected enemy. If an enemy is defeated, gains 3 orbs and strengthens Futsunomitama once.

<b>Ruin Damage</b>: One of the types of damage, ignores DEF and damage reduction effects.

<b>Futsunomitama</b> <img src="/images/shikigami/taira-no-masakado/Futsunomitama.webp" />: After every 3 enhancements, Taira no Masakado immediately enters Rift in Time.

<b>Rift in Time (时之隙)</b>: Traverse in the rupture of time and space where actions are not counted towards a turn and are regarded as outside of turn actions.`,
                levelUpEffects: [
                    { level: 2, description: "Increases AoE damage to 68%." },
                    { level: 3, description: "Increases AoE damage to 72%." },
                    { level: 4, description: "Increases AoE damage to 76%." },
                    { level: 5, description: "AoE damage increases to 80%; for each enemy defeated, receives 7% less damage and ruin damage coefficient increases by 5% (up to 5 times)." },
                ],
            },
        ],
    }"""
]

# 2. Raw List of Shikigami Names
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

# 3. Parse Raw Text
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

# 4. Construct File Content
header = """import { Shikigami } from "@/types/shikigami";

export const shikigamiData: Shikigami[] = [
"""

footer = "];\n"

content = header

# Add detailed blocks
for block in detailed_shikigami:
    content += block + ",\n"

# Add simple blocks
for shiki in shikigami_list:
    # Convert to JSON string but try to match formatting
    # We'll just use json.dumps for simplicity, it's valid TS
    block = json.dumps(shiki, indent=4)
    # Indent it to match the file structure (4 spaces)
    indented_block = ""
    lines = block.split('\n')
    for line in lines:
        indented_block += "    " + line + "\n"
    
    content += indented_block + ",\n"

content += footer

# 5. Write File
file_path = r"C:\Users\CHUTIMAN.C\Desktop\onmyojiTH\onmyoji-db\src\lib\data\shikigami.ts"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Regenerated shikigami.ts with {len(detailed_shikigami)} detailed entries and {len(shikigami_list)} simple entries.")
