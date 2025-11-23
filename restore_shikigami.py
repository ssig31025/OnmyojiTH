
import re

file_path = r"C:\Users\CHUTIMAN.C\Desktop\onmyojiTH\onmyoji-db\src\lib\data\shikigami.ts"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the correct blocks
asura_block = """    {
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
    }"""

onikiri_block = """    {
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
    }"""

sp_tamamo_block = """    {
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
    }"""

yamausagi_block = """    {
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
    }"""

taira_block = """    {
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

# Helper to replace block by ID
def replace_block(content, shiki_id, new_block):
    # Find the start of the block
    pattern = r'^\s*{\s*id:\s*"' + shiki_id + r'".*?^\s*},'
    # We need dotall to match across lines, and multiline for anchors
    # But the corrupted block ends with "    }," and inside it has "stats: { ... },"
    # The regex needs to be careful.
    # The corrupted block looks like:
    #     {
    #         id: "asura",
    #         ...
    #         stats: {
    #             ...
    #     },
    
    # So it ends with "    },"
    
    # Let's try to find the block start and the next "    },"
    
    start_marker = f'id: "{shiki_id}"'
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print(f"Could not find {shiki_id}")
        return content
    
    # Find the { before it
    block_start = content.rfind('{', 0, start_idx)
    
    # Find the } after it.
    # The corrupted block ends with "    },"
    # But wait, the "stats" object inside it ends with "    }," too?
    # No, the "stats" object ends with "            effectRes: "0%",\n    },"
    # The deduplication script appended "    }" to it.
    # So it looks like:
    #             effectRes: "0%",
    #     },
    #     {
    
    # Wait, the deduplication script appended "\n    }".
    # So the corrupted block ends with:
    #             effectRes: "0%",
    #     }
    
    # Let's look at the file content again.
    # 20:             effectRes: "0%",
    # 21:     },
    # 22:     {
    
    # So it ends with "    },".
    
    block_end = content.find('    },', start_idx)
    if block_end == -1:
        print(f"Could not find end for {shiki_id}")
        return content
    
    block_end += 6 # Include "    },"
    
    # Replace
    return content[:block_start] + new_block + ",\n" + content[block_end:]

# Replace them
content = replace_block(content, "asura", asura_block)
content = replace_block(content, "onikiri", onikiri_block)
content = replace_block(content, "sp-tamamo", sp_tamamo_block)
content = replace_block(content, "yamausagi", yamausagi_block)
content = replace_block(content, "taira-no-masakado", taira_block)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Restored detailed Shikigami entries.")
