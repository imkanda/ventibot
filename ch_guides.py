import discord


class Guides:

    def amber(self):
        amber = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: ATK \n"
                        "Passive: Decrease stamina consumption by 20% for party while gliding \n"
                        "Can be played as DPS or Support \n"
                        "Good for exploration/puzzles, would not recommend using for anything else",
            colour=discord.Colour.red()
        )
        amber.set_author(name="Amber")
        amber.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774479654970982420/amber.png")
        amber.add_field(name="Weapons (DPS)", value="Royal Bow ☆☆☆☆ \n Rust ☆☆☆☆ \n Amos' "
                                                    "Bow ☆☆☆☆☆",
                        inline=True)
        amber.add_field(name="Weapons (Support)", value="Stringless ☆☆☆☆ \n Favonius Warbow ☆☆☆☆",
                        inline=True)
        amber.add_field(name="Artifacts (DPS)", value="4x Wanderer's Troupe \n"
                                                      "<:flowerwhite:774424948558397511> HP \n"
                                                      "<:featherwhite:774424948369653762> ATK \n"
                                                      "<:hourglasswhite:774424948784627712> ATK% \n"
                                                      "<:cupwhite:774424948399276034> Pyro DMG% \n"
                                                      "<:headpiecewhite:774420351756927006> ATK% \n"
                                                      "Substats: ATK%, Crit Rate (≥ 50%), Crit DMG", inline=False)
        amber.add_field(name="Artifacts (Support)", value="4x Noblesse Oblige or Exile \n"
                                                          "<:flowerwhite:774424948558397511> HP \n"
                                                          "<:featherwhite:774424948369653762> ATK \n"
                                                          "<:hourglasswhite:774424948784627712> Energy Recharge \n"
                                                          "<:cupwhite:774424948399276034> Pyro DMG% \n"
                                                          "<:headpiecewhite:774420351756927006> ATK% \n"
                                                          "Substats: Energy Recharge, ATK%, Crit Rate (≥ 50%)",
                        inline=True)
        amber.add_field(name="Talent Priority", value="Normal Atk, Elem. Burst, Elem. Skill", inline=False)
        amber.set_footer(text="Character Builds - @kanda#8717")
        return amber

    def barbara(self):
        barbara = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: HP \n"
                        "Passive: Perfect Cooking restoration food has 12% chance to double the product \n"
                        "Literal heal bot \n"
                        "Amazing value at C6 \n"
                        "Heal amount stacks off Max HP",
            colour=discord.Colour.blue()
        )
        barbara.set_author(name="Barbara")
        barbara.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774731300413767690/barbara.png")
        barbara.add_field(name="Weapons", value="Prototype Malice ☆☆☆☆ \n"
                                                "Thrilling Tales of Dragon Slayers ☆☆☆",
                          inline=False)
        barbara.add_field(name="Artifacts", value="4x Maiden's or Exile \n"
                                                  "<:flowerwhite:774424948558397511> HP \n"
                                                  "<:featherwhite:774424948369653762> ATK \n"
                                                  "<:hourglasswhite:774424948784627712> HP% \n"
                                                  "<:cupwhite:774424948399276034> HP% \n"
                                                  "<:headpiecewhite:774420351756927006> Healing Bonus \n"
                                                  "Substats: HP%, Elem. Mastery, ATK%", inline=False)
        barbara.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal Atk", inline=True)
        barbara.set_footer(text="Character Builds - @kanda#8717")
        return barbara

    def beidou(self):
        beidou = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Electro DMG \n"
                        "Passive: Decrease stamina consumption by 20% for party while swimming \n"
                        "Electro hybrid DPS \n"
                        "Learn to time elemental skill with enemy attacks for max DMG and ultimate Dark Souls vibes \n"
                        "Has to have Ascension 4 to be fully effective \n"
                        "Debate Club [R5] > Prototype Animus [R2] until level weapon lvl 70"
                        "Elemental burst applies Electro status to herself, can be used for status-cleansing",
            colour=discord.Colour.purple()
        )
        beidou.set_author(name="Beidou")
        beidou.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774844541895180288/beidou.png")
        beidou.add_field(name="Weapons", value="Wolf's Gravestone ☆☆☆☆☆ \n"
                                               "Prototype Animus [R2+] ☆☆☆☆ \n"
                                               "Serpent Spine ☆☆☆☆ \n"
                                               "Debate Club ☆☆☆",
                         inline=False)
        beidou.add_field(name="Artifacts", value="4x Gladiator's Finale \n"
                                                 "<:flowerwhite:774424948558397511> HP \n"
                                                 "<:featherwhite:774424948369653762> ATK \n"
                                                 "<:hourglasswhite:774424948784627712> ATK% \n"
                                                 "<:cupwhite:774424948399276034> Electro DMG% \n"
                                                 "<:headpiecewhite:774420351756927006> ATK% \n"
                                                 "Substats: ATK(%), Crit Rate (≥ 50%), Crit Dmg", inline=False)
        beidou.add_field(name="Talent Priority", value="Normal ATK, Elem. Skill, Elem. Burst", inline=True)
        beidou.set_footer(text="Character Builds - @kanda#8717")
        return beidou

    def bennett(self):
        bennett = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Energy Recharge \n"
                        "Passive: 25% time reduction when dispatched on expeditions in Mondstat \n"
                        "Support unit for burst DMG \n"
                        "Prioritize Elem. burst usage for burst windows \n"
                        "Ulti is based off Max HP for heal, ATK for ATK Buff",
            colour=discord.Colour.red()
        )
        bennett.set_author(name="Bennett")
        bennett.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774847501073121280/bennett.png")
        bennett.add_field(name="Weapons", value="Skyward Blade ☆☆☆☆☆ \n"
                                                "Aquila Favonia ☆☆☆☆☆ \n"
                                                "Favonius Sword ☆☆☆☆ \n"
                                                "Flute ☆☆☆☆☆",

                          inline=False)
        bennett.add_field(name="Artifacts", value="4x Noblesse Oblige \n"
                                                  "<:flowerwhite:774424948558397511> HP \n"
                                                  "<:featherwhite:774424948369653762> ATK \n"
                                                  "<:hourglasswhite:774424948784627712> Energy Recharge \n"
                                                  "<:cupwhite:774424948399276034> Pyro DMG% \n"
                                                  "<:headpiecewhite:774420351756927006> ATK% \n"
                                                  "Substats: Energy Recharge, ATK(%), Elem. Mastery",
                          inline=False)
        bennett.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK", inline=True)
        bennett.set_footer(text="Character Builds - @kanda#8717")
        return bennett

    def chongyun(self):
        chongyun = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: ATK \n"
                        "Passive: 25% time reduction when dispatched on expeditions in Liyue \n"
                        "Can be used for support or as main DPS \n"
                        "If using as support, do not build with Diluc or Keqing as it will override their natural "
                        "auto attack buff they receive \n"
                        "His elemental burst is calculated as Claymore damage, which means it breaks shields/geo at a "
                        "much easier rate and can proc shatter \n"
                        "Debate Club [R5] > Prototype Animus [R2] until weapon lvl 70",
            colour=discord.Colour(0xccffff)
        )
        chongyun.set_author(name="Chongyun")
        chongyun.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774852902472253490/chongyun.png")
        chongyun.add_field(name="Weapons", value="Wolf's Gravestone ☆☆☆☆☆ \n"
                                                 "Skyward Pride ☆☆☆☆☆ \n"
                                                 "Prototype Animus [R2+] ☆☆☆☆ \n"
                                                 "Debate Club [R5] ☆☆☆",
                           inline=False)
        chongyun.add_field(name="Artifacts", value="4x Gladiator's Finale or 4x Martial Artist \n"
                                                   "<:flowerwhite:774424948558397511> HP \n"
                                                   "<:featherwhite:774424948369653762> ATK \n"
                                                   "<:hourglasswhite:774424948784627712> ATK% \n"
                                                   "<:cupwhite:774424948399276034> Cryo DMG% \n"
                                                   "<:headpiecewhite:774420351756927006> ATK% \n"
                                                   "Substats: ATK(%), Crit Rate (≥ 50%), Crit DMG",
                           inline=False)
        chongyun.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK", inline=True)
        chongyun.set_footer(text="Character Builds - @kanda#8717")
        return chongyun

    def diluc(self):
        diluc = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Crit Rate \n"
                        "Passive: Refunds 15% of the ores used when crafting Claymore-type weapons \n"
                        "Arguably best melee DPS unit in the game \n"
                        "Wolf's Gravestone = WoF, anything else = Gladitor's \n"
                        "Proper combo is weaving 2 attacks in between Elem. Skill uses \n"
                        "Debate Club [R5] > Prototype Animus [R2] until weapon lvl 70",
            colour=discord.Colour.red()
        )
        diluc.set_author(name="Diluc")
        diluc.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774855003608186880/Diluc.png")
        diluc.add_field(name="Weapons", value="Wolf's Gravestone ☆☆☆☆☆ \n"
                                              "Prototype Animus ☆☆☆☆\n"
                                              "Debate Club ☆☆☆",

                        inline=False)
        diluc.add_field(name="Artifacts", value="4x Crimson Witch of Flames or 4x Gladiator's Finale\n"
                                                "<:flowerwhite:774424948558397511> HP \n"
                                                "<:featherwhite:774424948369653762> ATK \n"
                                                "<:hourglasswhite:774424948784627712> ATK% \n"
                                                "<:cupwhite:774424948399276034> Pyro DMG% \n"
                                                "<:headpiecewhite:774420351756927006> Crit DMG \n"
                                                "Substats: ATK(%), Crit Rate (≥ 50%), Crit DMG",
                        inline=False)
        diluc.add_field(name="Talent Priority", value="Elem. Skill, Elem. Burst, Normal ATK", inline=True)
        diluc.set_footer(text="Character Builds - @kanda#8717")
        return diluc

    def diona(self):
        diona = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Cryo DMG \n"
                        "Passive: Perfect Cooking restoration food has 12% chance to double the product \n"
                        "Great support with easy sources of Superconduct/Melt along with healing and shields \n"
                        "Works well with Razor to give him extra protection \n"
                        "Ascension 4 is a bit underwhelming but worthy sacrifice for the rest of her kit",
            colour=discord.Colour(0xccffff)
        )
        diona.set_author(name="Diona")
        diona.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/779237805821263912/diona.png")
        diona.add_field(name="Weapons", value="Sacrifical Bow ☆☆☆☆ \n"
                                              "Favonius Warbow ☆☆☆☆ \n"
                                              "Stringless ☆☆☆☆",

                        inline=False)
        diona.add_field(name="Artifacts", value="4x Maiden Beloved or 2x Maiden 2x Exile/Scholar \n"
                                                "<:flowerwhite:774424948558397511> HP \n"
                                                "<:featherwhite:774424948369653762> ATK \n"
                                                "<:hourglasswhite:774424948784627712> Energy Recharge \n"
                                                "<:cupwhite:774424948399276034> HP% \n"
                                                "<:headpiecewhite:774420351756927006> Healing Bonus \n"
                                                "Substats: Energy Recharge, HP(%), Elem. Mastery", inline=False)
        diona.add_field(name="Talent Priority", value="Elem. Skill, Elem. Burst, Normal ATK", inline=True)
        diona.set_footer(text="Character Builds - @kanda#8717")
        return diona

    def fischl(self):
        fischl = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: ATK% \n"
                        "Passive: 25% time reduction when dispatched on expeditions in Mondstat \n"
                        "Top tier unit because of C1 and C6 \n"
                        "Can be used as DPS, secondary DPS, or full utility/support \n"
                        "Electro Dmg always good no matter what constellation level \n"
                        "Stacking ATK provides massive gains from C1/C6",
            colour=discord.Colour.purple()
        )
        fischl.set_author(name="Fischl")
        fischl.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774860500969586688/fischl.png")
        fischl.add_field(name="Weapons (DPS)", value="Skyward Harp [R2+] ☆☆☆☆☆ \n"
                                                     "Amos' Bow [R2+] ☆☆☆☆☆ \n"
                                                     "Rust [R5] ☆☆☆☆ \n"
                                                     "Skyward Harp [R0] ☆☆☆☆☆ \n"
                                                     "Amos' Bow [R0] ☆☆☆☆☆ \n"
                                                     "Rust [R0] ☆☆☆☆ \n"
                                                     "Compound Bow ☆☆☆☆ \n"
                                                     "Slingshot ☆☆☆",
                         inline=True)
        fischl.add_field(name="Weapons (Support)", value="Stringless ☆☆☆☆ \n"
                                                         "Fav. Warbow ☆☆☆☆",
                         inline=True)
        fischl.add_field(name="Artifacts (DPS)", value="4x Thundering Fury or 2x Bloodstained 2x Gladiator's \n"
                                                       "<:flowerwhite:774424948558397511> HP \n"
                                                       "<:featherwhite:774424948369653762> ATK \n"
                                                       "<:hourglasswhite:774424948784627712> ATK% \n"
                                                       "<:cupwhite:774424948399276034> Electro DMG% \n"
                                                       "<:headpiecewhite:774420351756927006> Crit DMG \n"
                                                       "Substats: ATK(%), Crit Rate (≥ 50%), Crit DMG",
                         inline=False)
        fischl.add_field(name="Artifacts (Support)", value="4x Thundering Fury or 2x Gambler 2x Thundering Fury \n"
                                                           "<:flowerwhite:774424948558397511> HP \n"
                                                           "<:featherwhite:774424948369653762> ATK \n"
                                                           "<:hourglasswhite:774424948784627712> Energy Recharge \n"
                                                           "<:cupwhite:774424948399276034> Electro DMG% \n"
                                                           "<:headpiecewhite:774420351756927006> ATK% \n"
                                                           "Substats: Energy Recharge, ATK%, Crit Rate (≥ 50%)",
                         inline=True)
        fischl.add_field(name="Talent Priority", value="DPS: Normal ATK, Elem. Skill, Elem. Burst \n"
                                                       "Support: Elem. Skill, Elem. Burst, Normal ATK", inline=True)
        fischl.set_footer(text="Character Builds - @kanda#8717")
        return fischl

    def jean(self):
        jean = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Healing Bonus \n"
                        "Passive: Perfect Cooking restoration food has 12% chance to double the product \n"
                        "Good unit for both outputting DMG and healing \n"
                        "Can pull off interesting mechanics with use of Elem. Skill \n"
                        "Swirl reacting is valuable for almost any team",
            colour=discord.Colour.green()
        )
        jean.set_author(name="Jean")
        jean.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774867007547375616/jean.png")
        jean.add_field(name="Weapons", value="Aquila Favonia ☆☆☆☆☆ \n"
                                             "Skyward Blade ☆☆☆☆☆ \n"
                                             "Flute ☆☆☆☆ \n"
                                             "Iron Sting ☆☆☆☆",
                       inline=True)
        jean.add_field(name="Artifacts", value="4x Gladiator's Finale \n"
                                               "<:flowerwhite:774424948558397511> HP \n"
                                               "<:featherwhite:774424948369653762> ATK \n"
                                               "<:hourglasswhite:774424948784627712> ATK% \n"
                                               "<:cupwhite:774424948399276034> ATK% \n"
                                               "<:headpiecewhite:774420351756927006> "
                                               "ATK% \n"
                                               "Substats: ATK(%), Energy Recharge, HP(%)",
                       inline=False)
        jean.add_field(name="Artifacts (Support)", value="4x Viridescent Venerer\n"
                                                         "<:flowerwhite:774424948558397511> HP \n"
                                                         "<:featherwhite:774424948369653762> ATK \n"
                                                         "<:hourglasswhite:774424948784627712> "
                                                         "Elem. Mastery \n"
                                                         "<:cupwhite:774424948399276034> Elem. "
                                                         "Mastery \n"
                                                         "<:headpiecewhite:774420351756927006> "
                                                         "Elem. Mastery \n"
                                                         "Substats: ATK(%), Elem. Mastery, "
                                                         "Energy Recharge",
                       inline=True)
        jean.add_field(name="Talent Priority", value="Elem. Skill, Normal ATK, Elem. Burst",
                       inline=False)
        jean.set_footer(text="Character Builds - @kanda#8717")
        return jean

    def kaeya(self):
        kaeya = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Energy Recharge \n"
                        "Passive: Decrease stamina consumption by 20% for party while sprinting \n"
                        "Decent F2P Support unit \n"
                        "High natural energy recharge keeps Elem. Burst uptime high \n"
                        "Completely free for all players with good exploration passive talent",
            colour=discord.Colour(0xccffff)
        )
        kaeya.set_author(name="Kaeya")
        kaeya.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775043314780209182/kaeya.png")
        kaeya.add_field(name="Weapons", value="Sacrificial Sword ☆☆☆☆ \n"
                                              "Skyward Blade ☆☆☆☆☆ \n"
                                              "Favonius Sword ☆☆☆",
                        inline=False)
        kaeya.add_field(name="Artifacts", value="4x Noblesse Oblige or 4x Insructor \n"
                                                "<:flowerwhite:774424948558397511> HP \n"
                                                "<:featherwhite:774424948369653762> ATK \n"
                                                "<:hourglasswhite:774424948784627712> ATK% \n"
                                                "<:cupwhite:774424948399276034> Cryo DMG% \n"
                                                "<:headpiecewhite:774420351756927006> Energy Recharge \n"
                                                "Substats: Energy Recharge, ATK(%), Elem. Mastery",
                        inline=True)
        kaeya.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK", inline=False)
        kaeya.set_footer(text="Character Builds - @kanda#8717")
        return kaeya

    def keqing(self):
        keqing = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Crit DMG \n"
                        "Passive: 25% time reduction when dispatched on expeditions in Liyue \n"
                        "Amazing DPS unit with AoE kill potential \n"
                        "Versatile, can focus on Phys DMG or Electro DMG \n"
                        "Elem. Skill makes her playstyle flashy and helps during exploration",
            colour=discord.Colour.purple()
        )
        keqing.set_author(name="Keqing")
        keqing.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775048364185223268/keqing.png")
        keqing.add_field(name="Weapons (Phys/Crit Build)", value="Aquila Favonia ☆☆☆☆☆ \n"
                                                                 "Flute ☆☆☆☆ \n"
                                                                 "Black Sword ☆☆☆☆",
                         inline=True)
        keqing.add_field(name="Weapons (Electro DMG Build)", value="Aquila Favonia ☆☆☆☆☆ \n"
                                                                   "Black Sword ☆☆☆☆ \n"
                                                                   "Lion's Roar ☆☆☆☆",
                         inline=True)
        keqing.add_field(name="Artifacts (Phys/Crit Build)", value="2x Gladiator 2x Bloodstained Chivalry \n"
                                                                   "<:flowerwhite:774424948558397511> HP \n"
                                                                   "<:featherwhite:774424948369653762> ATK \n"
                                                                   "<:hourglasswhite:774424948784627712> ATK% \n"
                                                                   "<:cupwhite:774424948399276034> ATK% \n"
                                                                   "<:headpiecewhite:774420351756927006> Crit DMG \n"
                                                                   "Substats: ATK(%), Crit Rate (≥ 50%), "
                                                                   "Crit DMG",
                         inline=False)
        keqing.add_field(name="Artifacts (Electro DMG Build)", value="4x Thundering Fury\n"
                                                                     "<:flowerwhite:774424948558397511> HP \n"
                                                                     "<:featherwhite:774424948369653762> ATK \n"
                                                                     "<:hourglasswhite:774424948784627712> ATK% \n"
                                                                     "<:cupwhite:774424948399276034> Electro DMG% \n"
                                                                     "<:headpiecewhite:774420351756927006> ATK% \n"
                                                                     "Substats: ATK(%), Crit Rate (≥ 50%), "
                                                                     "Crit DMG",
                         inline=True)
        keqing.add_field(name="Talent Priority", value="(Physical) Normal ATK, Elem. Burst, Elem. Skill \n"
                                                       "(Electro) Elem. Skill, Normal ATK, Elem. Burst",
                         inline=False)
        keqing.set_footer(text="Character Builds - @kanda#8717")
        return keqing

    def klee(self):
        klee = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Pyro DMG \n"
                        "Passive: Displays the location of nearby resources unique to Mondstadt on the mini-map \n"
                        "High natural Pyro DMG \n"
                        "Makes use of animation cancels for quick charged attacks \n"
                        "Hit stuns/knocks back even large enemies with shields",
            colour=discord.Colour.red()
        )
        klee.set_author(name="Klee")
        klee.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775053505702395904/Klee.png")
        klee.add_field(name="Weapons", value="Skyward Atlas ☆☆☆☆☆ \n"
                                             "Eye of Perception ☆☆☆☆ \n",
                       inline=True)
        klee.add_field(name="Artifacts", value="4x Crimson Witch of Flames or 2x Crimson 2x Gladiator's \n"
                                               "<:flowerwhite:774424948558397511> HP \n"
                                               "<:featherwhite:774424948369653762> ATK \n"
                                               "<:hourglasswhite:774424948784627712> ATK% \n"
                                               "<:cupwhite:774424948399276034> Pyro DMG% \n"
                                               "<:headpiecewhite:774420351756927006> ATK% \n"
                                               "Substats: ATK(%), Crit Rate (≥ 50%), Crit DMG",
                       inline=False)
        klee.add_field(name="Talent Priority", value="Elem. Skill, Normal ATK, Elem. Burst",
                       inline=False)
        klee.set_footer(text="Character Builds - @kanda#8717")
        return klee

    def lisa(self):
        lisa = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Elem. Mastery \n"
                        "Passive: 20% chance to refund a portion of the crafting materials used when crafting potions \n"
                        "Decent F2P Support unit \n"
                        "Primarily used for elemental reactions \n"
                        "Pairs well with Anemo units to keep mobs in her ult as it knocks back on hit",
            colour=discord.Colour.purple()
        )
        lisa.set_author(name="Lisa")
        lisa.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775063110079086622/lisa.png")
        lisa.add_field(name="Weapons", value="Wine and Song ☆☆☆☆ \n"
                                             "Skyward Atlas ☆☆☆☆☆ \n"
                                             "Eye of Perception ☆☆☆☆",
                       inline=True)
        lisa.add_field(name="Artifacts", value="4x Noblesse Oblige or Exile \n"
                                               "<:flowerwhite:774424948558397511> HP \n"
                                               "<:featherwhite:774424948369653762> ATK \n"
                                               "<:hourglasswhite:774424948784627712> Energy Recharge/ATK% \n"
                                               "<:cupwhite:774424948399276034> Electro DMG% \n"
                                               "<:headpiecewhite:774420351756927006> Energy Recharge/ATK% \n"
                                               "Substats: ATK(%), Elem. Mastery, Energy Recharge",
                       inline=False)
        lisa.add_field(name="Talent Priority", value="Elem. Skill, Elem. Burst, Normal ATK",
                       inline=False)
        lisa.set_footer(text="Character Builds - @kanda#8717")
        return lisa

    def mona(self):
        mona = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Energy Recharge \n"
                        "Passive: 25% chance to refund a portion of the crafting materials used when crafting Weapon "
                        "Ascension materials \n"
                        "Support unit who empowers DPS units \n"
                        "Extremely high value from her kit, can also deal significant DMG \n"
                        "~~Arguably the cutest girl in the game~~ \n"
                        "Water sprint great for exploration \n"
                        "Ascension 4 is why Energy Recharge is heavily favored inside the build",
            colour=discord.Colour.blue()
        )
        mona.set_author(name="Mona")
        mona.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775066790837092423/mona.png")
        mona.add_field(name="Weapons", value="Wine and Song ☆☆☆☆ \n"
                                             "Favonius Codex ☆☆☆☆ \n"
                                             "Mappa Mare ☆☆☆☆",
                       inline=True)

        mona.add_field(name="Artifacts", value="4x Noblesse Oblige or Exile \n"
                                               "<:flowerwhite:774424948558397511> HP \n"
                                               "<:featherwhite:774424948369653762> ATK \n"
                                               "<:hourglasswhite:774424948784627712> Energy Recharge \n"
                                               "<:cupwhite:774424948399276034> Hydro DMG% \n"
                                               "<:headpiecewhite:774420351756927006> ATK% \n"
                                               "Substats: Energy Recharge, ATK(%), Elem. Mastery",
                       inline=False)
        mona.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK",
                       inline=False)
        mona.set_footer(text="Character Builds - @kanda#8717")
        return mona

    def ningguang(self):
        ningguang = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Geo DMG \n"
                        "Passive: Displays the location of nearby ore veins on the mini-map \n "
                        "Strong DPS caster unit \n"
                        "Great single-target burst \n"
                        "Scales extremely well with high constellation levels",
            colour=discord.Colour(0xf5d760)
        )
        ningguang.set_author(name="Ningguang")
        ningguang.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775071788013977630/ningguang.png")
        ningguang.add_field(name="Weapons", value="Memory of Dust ☆☆☆☆☆ \n"
                                                  "Lost Prayer to the Sacred Winds ☆☆☆☆☆ \n"
                                                  "Skyward Atlas ☆☆☆☆☆ \n"
                                                  "Solar Pearl ☆☆☆☆ \n"
                                                  "Eye of Perception ☆☆☆☆ \n"
                                                  "Mappa Mare ☆☆☆☆ \n"
                                                  "Magic Guide ☆☆☆",
                            inline=True)

        ningguang.add_field(name="Artifacts", value="2x Archaic Petra 2x Gladiator's or 2x Petra 2x Noblesse \n"
                                                    "<:flowerwhite:774424948558397511> HP \n"
                                                    "<:featherwhite:774424948369653762> ATK \n"
                                                    "<:hourglasswhite:774424948784627712> ATK% \n"
                                                    "<:cupwhite:774424948399276034> Geo DMG% \n"
                                                    "<:headpiecewhite:774420351756927006> ATK% \n"
                                                    "Substats: ATK(%), Crit Rate (≥ 50%), Crit DMG",
                            inline=False)
        ningguang.add_field(name="Talent Priority", value="Normal ATK, Elem. Burst, Elem. Skill",
                            inline=False)
        ningguang.set_footer(text="Character Builds - @kanda#8717")
        return ningguang

    def noelle(self):
        noelle = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: DEF% \n"
                        "Passive: Perfect Cooking DEF-boosting food has 12% chance to double the product \n"
                        "Melee unit that can deal DPS while also providing shields and small healing \n"
                        "Elem. Burst ATK scales off of DEF \n"
                        "Can truly come online as a strong DPS unit at C6 \n"
                        "Debate Club [R5] > Prototype Animus [R2] until weapon lvl 70",
            colour=discord.Colour(0xf5d760)
        )
        noelle.set_author(name="Noelle")
        noelle.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775077747491471370/Noelle.png")
        noelle.add_field(name="Weapons", value="Skyward Pride [R1] ☆☆☆☆☆ \n"
                                               "Serpent Spine ☆☆☆☆ \n"
                                               "Whiteblind [R1+] ☆☆☆☆ \n"
                                               "Prototype Animus [R2+] ☆☆☆☆ \n"
                                               "Debate Club [R5] ☆☆☆",
                         inline=True)
        noelle.add_field(name="Artifacts", value="4x Retracing Bolide or 4x Gladiator's \n"
                                                 "<:flowerwhite:774424948558397511> HP \n"
                                                 "<:featherwhite:774424948369653762> ATK \n"
                                                 "<:hourglasswhite:774424948784627712> DEF% \n"
                                                 "<:cupwhite:774424948399276034> Geo DMG% (DEF% if C6) \n"
                                                 "<:headpiecewhite:774420351756927006> DEF% \n"
                                                 "Substats: DEF(%), ATK(%), Crit Rate (≥ 50%)",
                         inline=False)
        noelle.add_field(name="Talent Priority", value="Normal ATK, Elem. Burst, Elem. Skill",
                         inline=False)
        noelle.set_footer(text="Character Builds - @kanda#8717")
        return noelle

    def qiqi(self):
        qiqi = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Healing Bonus \n"
                        "Passive: Displays the location of nearby resources unique to Liyue on the mini-map \n"
                        "Currently best healer in the game \n"
                        "Heals off of normal ATKs, similar to Jean",
            colour=discord.Colour(0xccffff)
        )
        qiqi.set_author(name="Qiqi")
        qiqi.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775081415460126720/qiqi.png")
        qiqi.add_field(name="Weapons", value="Aquila Favonia ☆☆☆☆☆ \n"
                                             "Skyward Blade ☆☆☆☆☆ \n"
                                             "Flute ☆☆☆☆",
                       inline=True)
        qiqi.add_field(name="Artifacts", value="2x Gladiator's 2x Maiden Beloved \n"
                                               "<:flowerwhite:774424948558397511> HP \n"
                                               "<:featherwhite:774424948369653762> ATK \n"
                                               "<:hourglasswhite:774424948784627712> ATK% \n"
                                               "<:cupwhite:774424948399276034> ATK% or Cryo DMG% \n"
                                               "<:headpiecewhite:774420351756927006> Healing Bonus \n"
                                               "Substats: ATK(%), Energy Recharge, Elem. Mastery",
                       inline=False)
        qiqi.add_field(name="Talent Priority", value="Elem. Skill, Normal ATK, Elem. Burst",
                       inline=False)
        qiqi.set_footer(text="Character Builds - @kanda#8717")
        return qiqi

    def razor(self):
        razor = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Phys DMG % \n"
                        "Passive: Decrease stamina consumption by 20% for party while sprinting \n"
                        "Close range DPS \n"
                        "Not suitable for swap-out playstyle \n"
                        "Debate Club [R5] > Prototype Animus [R2] until weapon lvl 70 \n"
                        "Elemental burst applies Electro status to himself, can be used for status-cleansing",
            colour=discord.Colour.purple()
        )
        razor.set_author(name="Razor")
        razor.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775082739283001374/razor.png")
        razor.add_field(name="Weapons", value="Wolf's Gravestone ☆☆☆☆☆ \n Prototype Animus ☆☆☆☆ \n Debate "
                                              "Club ☆☆☆",
                        inline=False)
        razor.add_field(name="Artifacts", value="4x Gladiator's Finale \n "
                                                "<:flowerwhite:774424948558397511> HP \n"
                                                "<:featherwhite:774424948369653762> ATK \n"
                                                "<:hourglasswhite:774424948784627712> ATK% \n"
                                                "<:cupwhite:774424948399276034> Phys DMG% \n"
                                                "<:headpiecewhite:774420351756927006> Crit DMG \n"
                                                "Substats: ATK(%), Crit Rate (≥ 50%), Crit DMG",
                        inline=False)
        razor.add_field(name="Talent Priority", value="Normal ATK, Elem. Burst, Elem. Skill", inline=True)
        razor.set_footer(text="Character Builds - @kanda#8717")
        return razor

    def sucrose(self):
        sucrose = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Anemo DMG \n"
                        "Passive: 10% to obtain double the product when crafting Character and Weapon Enhancement "
                        "Materials \n"
                        "Great support for elemental reactions \n"
                        "Elem. Mastery battery at Ascension 4 \n"
                        "Passive talent is incredibly useful for crafting",
            colour=discord.Colour.green()
        )
        sucrose.set_author(name="Sucrose")
        sucrose.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775082757302779934/Sucrose.png")
        sucrose.add_field(name="Weapons", value="Mappa Mare ☆☆☆☆ \n"
                                                "Sacrifical Fragments ☆☆☆☆",
                          inline=True)
        sucrose.add_field(name="Artifacts", value="4x Viridescent Venerer or Instructor \n"
                                                  "<:flowerwhite:774424948558397511> HP \n"
                                                  "<:featherwhite:774424948369653762> ATK \n"
                                                  "<:hourglasswhite:774424948784627712> Elemental Mastery \n"
                                                  "<:cupwhite:774424948399276034> Anemo DMG \n"
                                                  "<:headpiecewhite:774420351756927006> ATK% \n"
                                                  "Substats: Elem. Mastery, Energy Recharge, ATK(%)",
                          inline=False)
        sucrose.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK",
                          inline=False)
        sucrose.set_footer(text="Character Builds - @kanda#8717")
        return sucrose

    def tartaglia(self):
        tartaglia = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Hydro DMG \n"
                        "Passive: Increases party members' Normal Attack level by 1 \n"
                        "Fluid DPS who flows between ranged bow user and melee dagger user \n"
                        "Highest scaling Elemental Burst \n"
                        "Incredible Hydro DMG \n"
                        "Use Retracing Bolide artifact set if you are using Noelle on same team \n"
                        "Build may change once Hydro artifact set is released later in patch 1.1",
            colour=discord.Colour.blue()
        )
        tartaglia.set_author(name="Tartaglia (Childe)")
        tartaglia.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/779227075537141811/childe.png")
        tartaglia.add_field(name="Weapons", value="Skyward Harp ☆☆☆☆ \n"
                                                  "Rust ☆☆☆☆",
                            inline=True)
        tartaglia.add_field(name="Artifacts", value="2x Gladiator's 2x Noblesse (Rust) \n "
                                                    "2x Gladiator's 2x Bloodstained Chivalry (Skyward Harp)\n"
                                                    "<:flowerwhite:774424948558397511> HP \n"
                                                    "<:featherwhite:774424948369653762> ATK \n"
                                                    "<:hourglasswhite:774424948784627712> ATK% \n"
                                                    "<:cupwhite:774424948399276034> Hydro DMG \n"
                                                    "<:headpiecewhite:774420351756927006> Crit DMG \n"
                                                    "Substats: ATK(%), Crit DMG, Crit Rate (≥ 50%)",
                            inline=False)
        tartaglia.add_field(name="Talent Priority", value="Elem. Skill, Normal ATK, Elem. Burst",
                            inline=False)
        tartaglia.set_footer(text="Character Builds - @kanda#8717")
        return tartaglia

    def anemo(self):
        anemo = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: ATK% \n"
                        "Main character, every player gets for free \n"
                        "Useful for any team/party as Swirl reaction is invaluable \n"
                        "Capable of getting C6 naturally which makes the unit scale as you gain AR",
            colour=discord.Colour.green()
        )
        anemo.set_author(name="Traveler (Anemo)")
        anemo.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775087936852066384/traveler_female.png")
        anemo.add_field(name="Weapons", value="Iron Sting ☆☆☆☆ \n"
                                              "Skyrider Sword ☆☆☆☆",
                        inline=True)
        anemo.add_field(name="Artifacts", value="4x Viridescent Venerer or Instructor \n"
                                                "<:flowerwhite:774424948558397511> HP \n"
                                                "<:featherwhite:774424948369653762> ATK \n"
                                                "<:hourglasswhite:774424948784627712> Elemental Mastery \n"
                                                "<:cupwhite:774424948399276034> Anemo DMG \n"
                                                "<:headpiecewhite:774420351756927006> ATK% \n"
                                                "Substats: Energy Recharge, ATK(%), Elem. Mastery",
                        inline=False)
        anemo.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK",
                        inline=False)
        anemo.set_footer(text="Character Builds - @kanda#8717")
        return anemo

    def geo(self):
        geo = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: ATK% \n"
                        "Main character, every player gets for free \n"
                        "Elem. Skill is useful/required when exploring to collect Oculi and complete puzzles \n"
                        "Capable of getting C6 naturally which makes the unit scale as you gain AR \n"
                        "Has use if you lack a claymore user or another Geo unit to counter Geo mobs",
            colour=discord.Colour(0xf5d760)
        )
        geo.set_author(name="Traveler (Geo)")
        geo.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775090685854482442/traveler_male.png")
        geo.add_field(name="Weapons", value="Skyward Blade ☆☆☆☆☆ \n"
                                            "Favonius Sword ☆☆☆☆",
                      inline=True)
        geo.add_field(name="Artifacts", value="4x Noblesse Oblige or Exile \n"
                                              "<:flowerwhite:774424948558397511> HP \n"
                                              "<:featherwhite:774424948369653762> ATK \n"
                                              "<:hourglasswhite:774424948784627712> ATK% \n"
                                              "<:cupwhite:774424948399276034> Geo DMG \n"
                                              "<:headpiecewhite:774420351756927006> ATK% \n"
                                              "Substats: Energy Recharge, ATK(%), Elem. Mastery",
                      inline=False)
        geo.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK",
                      inline=False)
        geo.set_footer(text="Character Builds - @kanda#8717")
        return geo

    def venti(self):
        venti = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Energy Recharge \n"
                        "Passive: Passive: Decrease stamina consumption by 20% for party while gliding \n"
                        "S+ tier unit across the board in all categories \n"
                        "Elem. Skill is useful/required when exploring to collect Oculi and complete puzzles \n"
                        "Mainly used as a battery for Energy Recharge and elemental reactions with Elem. Burst \n"
                        "Could be used for DPS with C1 and an aimed shot build",
            colour=discord.Colour.green()
        )
        venti.set_author(name="Venti")
        venti.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775091449942507560/venti.png")
        venti.add_field(name="Weapons", value="Stringless ☆☆☆☆ \n"
                                              "Sacrifical Bow ☆☆☆☆",
                        inline=True)
        venti.add_field(name="Artifacts", value="4x Viridescent Venerer or Exile \n"
                                                "<:flowerwhite:774424948558397511> HP \n"
                                                "<:featherwhite:774424948369653762> ATK \n"
                                                "<:hourglasswhite:774424948784627712> Energy Recharge \n"
                                                "<:cupwhite:774424948399276034> Anemo DMG \n"
                                                "<:headpiecewhite:774420351756927006> ATK% \n"
                                                "Substats: ATK(%), Elem. Mastery, Energy Recharge",
                        inline=False)
        venti.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK",
                        inline=False)
        venti.set_footer(text="Character Builds - @kanda#8717")
        return venti

    def xiangling(self):
        xiangling = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Elemental Mastery \n"
                        "Passive: Perfect Cooking ATK-boosting food has 12% chance to double the product \n"
                        "Simple Pyro polearm unit \n"
                        "Versatile, can play main DPS for F2P players, or in the support role if you need a pyro"
                        "unit \n"
                        "Support build relies on energy recharge for Elem. Burst uptime"
                        "DPS build relies on Crescent Pike and abusing her fast ATK combo speed",
            colour=discord.Colour.red()
        )
        xiangling.set_author(name="Xiangling")
        xiangling.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775092653372735519/xiangling.png")
        xiangling.add_field(name="Weapons (Support)", value="Skyward Spine ☆☆☆☆☆ \n"
                                                            "Prototype Grudge ☆☆☆☆ \n"
                                                            "Dragon's Bane ☆☆☆☆",
                            inline=True)
        xiangling.add_field(name="Weapons (DPS)", value="Crescent Pike ☆☆☆☆",
                            inline=True)
        xiangling.add_field(name="Artifacts (Support)", value="4x Noblesse Oblige or Exile \n"
                                                              "<:flowerwhite:774424948558397511> HP \n"
                                                              "<:featherwhite:774424948369653762> ATK \n"
                                                              "<:hourglasswhite:774424948784627712> Energy "
                                                              "Recharge \n"
                                                              "<:cupwhite:774424948399276034> Pyro DMG% \n"
                                                              "<:headpiecewhite:774420351756927006> ATK% \n"
                                                              "Substats: Elem. Mastery, ATK(%), "
                                                              "Energy Recharge",
                            inline=False)
        xiangling.add_field(name="Artifacts (DPS)", value="2x Gladiator's 2x Boodstained Chivalry or 4x "
                                                          "Gladiator's\n"
                                                          "<:flowerwhite:774424948558397511> HP \n"
                                                          "<:featherwhite:774424948369653762> ATK \n"
                                                          "<:hourglasswhite:774424948784627712> ATK% \n"
                                                          "<:cupwhite:774424948399276034> Phys DMG% \n"
                                                          "<:headpiecewhite:774420351756927006> "
                                                          "Crit DMG \n"
                                                          "Substats: ATK(%), Crit Rate (≥ 50%), Crit DMG",
                            inline=True)
        xiangling.add_field(name="Talent Priority", value="(Support) Elem. Skill, Elem. Burst, Normal ATK \n"
                                                          "(DPS) Normal ATK, Elem. Skill, Elem. Burst",
                            inline=False)
        xiangling.set_footer(text="Character Builds - @kanda#8717")
        return xiangling

    def xingqiu(self):
        xingqiu = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: ATK% \n"
                        "Passive: 25% chance to refund a portion of the crafting materials used when crafting "
                        "Character Talent materials \n"
                        "Solid Hydro support that delivers heals and damage reduction \n"
                        "Can be a reliable source of Hydro reactions from his Elem. Burst \n"
                        "Powerful support with a Hydro DPS unit at Constellation 2 \n"
                        "Passive talent is extremely useful when crafting",
            colour=discord.Colour.blue()
        )
        xingqiu.set_author(name="Xingqiu")
        xingqiu.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775095718825164820/xingqiu.png")
        xingqiu.add_field(name="Weapons (Support)", value="Sacrifical Sword ☆☆☆☆ \n"
                                                          "Skyward Blade ☆☆☆☆☆ \n"
                                                          "Favonius Sword ☆☆☆☆ \n"
                                                          "Skyrider Sword ☆☆☆ ",
                          inline=True)
        xingqiu.add_field(name="Artifacts (Support)", value="2x Exile 2x Scholar \n"
                                                            "<:flowerwhite:774424948558397511> HP \n"
                                                            "<:featherwhite:774424948369653762> ATK \n"
                                                            "<:hourglasswhite:774424948784627712> ATK% \n"
                                                            "<:cupwhite:774424948399276034> Hydro DMG \n"
                                                            "<:headpiecewhite:774420351756927006> Crit Rate \n"
                                                            "Substats: Energy Recharge (180% - 200%), Elem. Mastery, "
                                                            "ATK(%)",
                          inline=False)
        xingqiu.add_field(name="Talent Priority", value="Elem. Skill, Elem. Burst, Normal ATK",
                          inline=False)
        xingqiu.set_footer(text="Character Builds - @kanda#8717")
        return xingqiu

    def contents(self):
        contents = discord.Embed(
            description="Table of Contents",
            colour=discord.Colour.gold()
        )
        contents.set_footer(text='Table of Contents')
        contents.set_image(url="https://cdn.discordapp.com/attachments/773757621520957493/775115758417215508"
                               "/genshin_impact_logo.png")
        contents.set_author(name='Venti', icon_url='https://cdn.discordapp.com/attachments/772150088599863296'
                                                   '/772174650234372146/41.png')
        contents.add_field(name=chr(173), value='<:amber:779443715713400883> [Amber Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805493261762611)')
        contents.add_field(name=chr(173),
                           value='<:barbara:779443715806199889> [Barbara Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805498907295784)')
        contents.add_field(name=chr(173),
                           value='<:beidou:779443715910795324> [Beidou Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805512882978837)')
        contents.add_field(name=chr(173),
                           value='<:bennett:779443715293970503> [Bennett Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805525923725322)')
        contents.add_field(name=chr(173),
                           value='<:chongyun:779443715738566657> [Chongyun Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805535167447050)')
        contents.add_field(name=chr(173),
                           value='<:diluc:779443715882221578> [Diluc Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805544340783123)')
        contents.add_field(name=chr(173),
                           value='<:diona:779443715709337681> [Diona Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805549058588762)')
        contents.add_field(name=chr(173),
                           value='<:fischl:779443715696623626> [Fischl Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805556670988311)')
        contents.add_field(name=chr(173),
                           value='<:jean:779443715675521024> [Jean Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805561398362132)')
        contents.add_field(name=chr(173),
                           value='<:kaeya:779443715688235068> [Kaeya Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805565932797962)')
        contents.add_field(name=chr(173),
                           value='<:keqing:779443715717857320> [Keqing Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805574497697802)')
        contents.add_field(name=chr(173),
                           value='<:klee:779443715768057976> [Klee Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805582311948358)')
        contents.add_field(name=chr(173),
                           value='<:lisa:779443715885367336> [Lisa Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805585889296384)')
        contents.add_field(name=chr(173),
                           value='<:mona:779443715395026955> [Mona Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805593615073310)')
        contents.add_field(name=chr(173),
                           value='<:ningguang:779443715449946144> [Ningguang Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805613080969260)')
        contents.add_field(name=chr(173),
                           value='<:noelle:779443715709337630> [Noelle Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805621918105650)')
        contents.add_field(name=chr(173),
                           value='<:qiqi:779443715727032330> [Qiqi Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805627173961728)')
        contents.add_field(name=chr(173),
                           value='<:razorgenshin:779443715768844318> [Razor Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805633364230184)')
        contents.add_field(name=chr(173),
                           value='<:sucrose:779443715542351903> [Sucrose Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805637898010644)')
        contents.add_field(name=chr(173),
                           value='<:childe:779443715155820595> [Tartaglia (Childe) Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805651652050994)')
        contents.add_field(name=chr(173),
                           value='<:Traveler:779443714987786241> [Traveler (Anemo) Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805658844495893)')
        contents.add_field(name=chr(173),
                           value='<:Traveler:779443714987786241> [Traveler (Geo) Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805662523162624)')
        contents.add_field(name=chr(173),
                           value='<:venti:779443715382050858> [Venti Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805673633480705)')
        contents.add_field(name=chr(173),
                           value='<:xiangling:779443715625320478> [Xiangling Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805678549729301)')
        contents.add_field(name=chr(173),
                           value='<:xingqiu:779443715511943218> [Xingqiu Build & Info](https://discordapp.com/channels/712808446180720651/779438920571027497/779805689345736714)')
        return contents

# function can be used to call embeds or something else, just here in case I ever need it
#             if message.content == '.amber':
#                 await message.channel.send(embed=guides.amber())
#             if message.content == '.barbara':
#                 await message.channel.send(embed=guides.barbara())
#             if message.content == '.beidou':
#                 await message.channel.send(embed=guides.beidou())
#             if message.content == '.bennett':
#                 await message.channel.send(embed=guides.bennett())
#             if message.content == '.chongyun':
#                 await message.channel.send(embed=guides.chongyun())
#             if message.content == '.diluc':
#                 await message.channel.send(embed=guides.diluc())
#             if message.content == '.diona':
#                 await message.channel.send(embed=guides.diona())
#             if message.content == '.fischl':
#                 await message.channel.send(embed=guides.fischl())
#             if message.content == '.jean':
#                 await message.channel.send(embed=guides.jean())
#             if message.content == '.kaeya':
#                 await message.channel.send(embed=guides.kaeya())
#             if message.content == '.keqing':
#                 await message.channel.send(embed=guides.keqing())
#             if message.content == '.klee':
#                 await message.channel.send(embed=guides.klee())
#             if message.content == '.lisa':
#                 await message.channel.send(embed=guides.lisa())
#             if message.content == '.mona':
#                 await message.channel.send(embed=guides.mona())
#             if message.content == '.ningguang':
#                 await message.channel.send(embed=guides.ningguang())
#             if message.content == '.noelle':
#                 await message.channel.send(embed=guides.noelle())
#             if message.content == '.qiqi':
#                 await message.channel.send(embed=guides.qiqi())
#             if message.content == '.razor':
#                 await message.channel.send(embed=guides.razor())
#             if message.content == '.sucrose':
#                 await message.channel.send(embed=guides.sucrose())
#             if message.content == '.tartaglia':
#                 await message.channel.send(embed=guides.tartaglia())
#             if message.content == '.anemo':
#                 await message.channel.send(embed=guides.anemo())
#             if message.content == '.geo':
#                 await message.channel.send(embed=guides.geo())
#             if message.content == '.venti':
#                 await message.channel.send(embed=guides.venti())
#             if message.content == '.xiangling':
#                 await message.channel.send(embed=guides.xiangling())
#             if message.content == '.xingqiu':
#                 await message.channel.send(embed=guides.xingqiu())
#             if message.content == '.xinyan':
#                 await message.channel.send("Coming soon! Stay tuned.")
#             if message.content == '.zhongli':
#                 await message.channel.send("Coming soon! Stay tuned.")
