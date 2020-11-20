import discord


class Guides:

    def amber(self):
        amber = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: ATK \n Can be played as DPS or Support \n Good for exploration/puzzles, "
                        "would not recommend using for anything else",
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
                                                      "Substats: ATK%, Crit Rate (50% MAX), Crit DMG", inline=False)
        amber.add_field(name="Artifacts (Support)", value="4x Noblesse Oblige or Exile \n"
                                                          "<:flowerwhite:774424948558397511> HP \n"
                                                          "<:featherwhite:774424948369653762> ATK \n"
                                                          "<:hourglasswhite:774424948784627712> Energy Recharge \n"
                                                          "<:cupwhite:774424948399276034> Pyro DMG% \n"
                                                          "<:headpiecewhite:774420351756927006> ATK% \n"
                                                          "Substats: Energy Recharge, ATK%, Crit Rate (50% MAX)",
                        inline=True)
        amber.add_field(name="Talent Priority", value="Normal Atk, Elem. Burst, Elem. Skill", inline=False)
        amber.set_footer(text="Character Builds")
        return amber

    def barbara(self):
        barbara = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: HP \n"
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
        barbara.set_footer(text="Character Builds")
        return barbara

    def beidou(self):
        beidou = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Electro DMG \n"
                        "Good hybrid DPS \n"
                        "Good AoE dmg with ult \n"
                        "Has to take hits to be fully effective",
            colour=discord.Colour.purple()
        )
        beidou.set_author(name="Beidou")
        beidou.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774844541895180288/beidou.png")
        beidou.add_field(name="Weapons", value="Wolf's Gravestone ☆☆☆☆☆ \n"
                                               "Prototype Animus ☆☆☆☆\n"
                                               "Debate Club ☆☆☆",
                         inline=False)
        beidou.add_field(name="Artifacts", value="4x Gladiator's Finale \n"
                                                 "<:flowerwhite:774424948558397511> HP \n"
                                                 "<:featherwhite:774424948369653762> ATK \n"
                                                 "<:hourglasswhite:774424948784627712> ATK% \n"
                                                 "<:cupwhite:774424948399276034> Phys DMG% \n"
                                                 "<:headpiecewhite:774420351756927006> ATK% \n"
                                                 "Substats: ATK(%), Crit Rate, Crit Dmg", inline=False)
        beidou.add_field(name="Talent Priority", value="Normal ATK, Elem. Skill, Elem. Burst", inline=True)
        beidou.set_footer(text="Character Builds")
        return beidou

    def bennett(self):
        bennett = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Energy Recharge \n"
                        "Support unit for burst DMG \n"
                        "Prioritize Elem. burst usage for burst windows \n"
                        "Ulti is based off Max HP for heal, ATK for ATK Buff",
            colour=discord.Colour.red()
        )
        bennett.set_author(name="Bennett")
        bennett.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774847501073121280/bennett.png")
        bennett.add_field(name="Weapons", value="Lion's Roar ☆☆☆☆ \n"
                                                "Flute ☆☆☆☆\n"
                                                "Sacrificial Sword ☆☆☆☆\n"
                                                "Aquila Favonia ☆☆☆☆☆",

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
        bennett.set_footer(text="Character Builds")
        return bennett

    def chongyun(self):
        chongyun = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: ATK \n"
                        "Can be used for support or as main DPS \n"
                        "If using as support, do not build with Razor or Beidou \n",
            colour=discord.Colour(0xccffff)
        )
        chongyun.set_author(name="Chongyun")
        chongyun.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774852902472253490/chongyun.png")
        chongyun.add_field(name="Weapons", value="Wolf's Gravestone ☆☆☆☆☆ \n"
                                                 "Prototype Animus ☆☆☆☆ \n"
                                                 "Debate Club ☆☆☆",
                           inline=False)
        chongyun.add_field(name="Artifacts", value="4x Gladiator's Finale or 4x Glacier & Snowfield\n"
                                                   "<:flowerwhite:774424948558397511> HP \n"
                                                   "<:featherwhite:774424948369653762> ATK \n"
                                                   "<:hourglasswhite:774424948784627712> ATK% \n"
                                                   "<:cupwhite:774424948399276034> Cryo DMG% \n"
                                                   "<:headpiecewhite:774420351756927006> ATK% \n"
                                                   "Substats: ATK(%), Crit Rate (50% MAX), Crit DMG",
                           inline=False)
        chongyun.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK", inline=True)
        chongyun.set_footer(text="Character Builds")
        return chongyun

    def diluc(self):
        diluc = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Crit Rate \n"
                        "Arguably best melee DPS unit in the game \n"
                        "Wolf's Gravestone = WoF, anything else = Gladitor's \n"
                        "Proper combo is weaving 2 attacks in between Elem. Skill uses",
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
                                                "Substats: ATK(%), Crit Rate (50% MAX), Crit DMG",
                        inline=False)
        diluc.add_field(name="Talent Priority", value="Elem. Skill, Elem. Burst, Normal ATK", inline=True)
        diluc.set_footer(text="Character Builds")
        return diluc

    def diona(self):
        diona = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Cryo DMG \n"
                        "Great support with easy sources of Superconduct/Melt along with healing and shields \n"
                        "Works well with Razor to give him extra protection \n"
                        "Ascension 4 is a bit underwhelming but worthy sacrifice for the rest of her kit",
            colour=discord.Colour(0xccffff)
        )
        diona.set_author(name="Diona")
        diona.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/779237805821263912/diona.png")
        diona.add_field(name="Weapons", value="Sacrifical Bow ☆☆☆☆ \n"
                                              "Favonius Warbow ☆☆☆☆",

                        inline=False)
        diona.add_field(name="Artifacts", value="4x Maiden Beloved or 2x Maiden 2x Retracing Bolide\n"
                                                "<:flowerwhite:774424948558397511> HP \n"
                                                "<:featherwhite:774424948369653762> ATK \n"
                                                "<:hourglasswhite:774424948784627712> Energy Recharge \n"
                                                "<:cupwhite:774424948399276034> HP% \n"
                                                "<:headpiecewhite:774420351756927006> Healing Bonus \n"
                                                "Substats: Energy Recharge, HP(%), Elem. Mastery", inline=False)
        diona.add_field(name="Talent Priority", value="Elem. Skill, Elem. Burst, Normal ATK", inline=True)
        diona.set_footer(text="Character Builds")
        return diona

    def fischl(self):
        fischl = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: ATK% \n"
                        "Top tier unit because of C1 and C4 \n"
                        "Stacking ATK provides massive gains from C1 \n"
                        "Electro Dmg always good no matter what constellation level \n"
                        "Requires high constellation for actual good utility",
            colour=discord.Colour.purple()
        )
        fischl.set_author(name="Fischl")
        fischl.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/774860500969586688/fischl.png")
        fischl.add_field(name="Weapons (Secondary DPS)", value="Compound Bow ☆☆☆☆ \n"
                                                               "Rust ☆☆☆☆",
                         inline=True)
        fischl.add_field(name="Weapons (Support)", value="Stringless ☆☆☆☆ \n"
                                                         "Fav. Warbow ☆☆☆☆",
                         inline=True)
        fischl.add_field(name="Artifacts", value="4x Thundering Fury\n"
                                                 "<:flowerwhite:774424948558397511> HP \n"
                                                 "<:featherwhite:774424948369653762> ATK \n"
                                                 "<:hourglasswhite:774424948784627712> ATK% \n"
                                                 "<:cupwhite:774424948399276034> Electro DMG% \n"
                                                 "<:headpiecewhite:774420351756927006> ATK% \n"
                                                 "Substats: ATK(%), Crit Rate (50% MAX), Crit DMG",
                         inline=False)
        fischl.add_field(name="Talent Priority", value="Elem. Skill, Normal ATK, Elem. Burst", inline=True)
        fischl.set_footer(text="Character Builds")
        return fischl

    def jean(self):
        jean = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Healing Bonus \n"
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
        jean.set_footer(text="Character Builds")
        return jean

    def kaeya(self):
        kaeya = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Energy Recharge \n"
                        "Decent F2P Support unit \n"
                        "High natural energy recharge keeps Elem. Burst uptime high \n"
                        "Completely free for all players with good exploration passive talent",
            colour=discord.Colour(0xccffff)
        )
        kaeya.set_author(name="Kaeya")
        kaeya.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775043314780209182/kaeya.png")
        kaeya.add_field(name="Weapons", value="Sacrificial Sword ☆☆☆☆ \n"
                                              "Flute ☆☆☆☆ \n"
                                              "Skyrider Sword ☆☆☆",
                        inline=False)
        kaeya.add_field(name="Artifacts", value="4x Noblesse Oblige or Exile \n"
                                                "<:flowerwhite:774424948558397511> HP \n"
                                                "<:featherwhite:774424948369653762> ATK \n"
                                                "<:hourglasswhite:774424948784627712> ATK% \n"
                                                "<:cupwhite:774424948399276034> Cryo DMG% \n"
                                                "<:headpiecewhite:774420351756927006> Energy Recharge \n"
                                                "Substats: Energy Recharge, ATK(%), Elem. Mastery",
                        inline=True)
        kaeya.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK", inline=False)
        kaeya.set_footer(text="Character Builds")
        return kaeya

    def keqing(self):
        keqing = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Crit DMG \n"
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
                                                                   "Substats: ATK(%), Crit Rate (50% MAX), "
                                                                   "Crit DMG",
                         inline=False)
        keqing.add_field(name="Artifacts (Electro DMG Build)", value="4x Thundering Fury\n"
                                                                     "<:flowerwhite:774424948558397511> HP \n"
                                                                     "<:featherwhite:774424948369653762> ATK \n"
                                                                     "<:hourglasswhite:774424948784627712> ATK% \n"
                                                                     "<:cupwhite:774424948399276034> Electro DMG% \n"
                                                                     "<:headpiecewhite:774420351756927006> ATK% \n"
                                                                     "Substats: ATK(%), Crit Rate (50% MAX), "
                                                                     "Crit DMG",
                         inline=True)
        keqing.add_field(name="Talent Priority", value="(Physical) Normal ATK, Elem. Burst, Elem. Skill \n"
                                                       "(Electro) Elem. Skill, Normal ATK, Elem. Burst",
                         inline=False)
        keqing.set_footer(text="Character Builds")
        return keqing

    def klee(self):
        klee = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Pyro DMG \n"
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
                                               "Substats: ATK(%), Crit Rate (50% MAX), Crit DMG",
                       inline=False)
        klee.add_field(name="Talent Priority", value="Elem. Skill, Normal ATK, Elem. Burst",
                       inline=False)
        klee.set_footer(text="Character Builds")
        return klee

    def lisa(self):
        lisa = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Elem. Mastery \n"
                        "Decent F2P Support unit \n"
                        "Primarily used for elemental reactions \n"
                        "Elem. Burst is helpful for bosses but can be bad vs mobs as it knocks back",
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
        lisa.set_footer(text="Character Builds")
        return lisa

    def mona(self):
        mona = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Energy Recharge \n"
                        "Support unit who empowers DPS units \n"
                        "Extremely high value from her kit, can also deal significant DMG \n"
                        "~~Arguably the cutest girl in the game~~ \n"
                        "Amazing passive talent, her sprint also great for exploration \n"
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
        mona.set_footer(text="Character Builds")
        return mona

    def ningguang(self):
        ningguang = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Geo DMG \n"
                        "Strong DPS caster unit \n"
                        "Great single-target burst \n"
                        "Scales extremely well with high constellation levels \n"
                        "Passive talent makes mining ore veins a lot easier in the world",
            colour=discord.Colour(0xf5d760)
        )
        ningguang.set_author(name="Ningguang")
        ningguang.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775071788013977630/ningguang.png")
        ningguang.add_field(name="Weapons", value="Skyward Atlas ☆☆☆☆☆ \n"
                                                  "Memory of Dust ☆☆☆☆☆ \n"
                                                  "Eye of Perception ☆☆☆☆",
                            inline=True)

        ningguang.add_field(name="Artifacts", value="2x Archaic Petra 2x Gladiator's or 2x Petra 2x Noblesse \n"
                                                    "<:flowerwhite:774424948558397511> HP \n"
                                                    "<:featherwhite:774424948369653762> ATK \n"
                                                    "<:hourglasswhite:774424948784627712> ATK% \n"
                                                    "<:cupwhite:774424948399276034> Geo DMG% \n"
                                                    "<:headpiecewhite:774420351756927006> ATK% \n"
                                                    "Substats: ATK(%), Crit Rate (50% MAX), Crit DMG",
                            inline=False)
        ningguang.add_field(name="Talent Priority", value="Elem. Burst, Normal ATK, Elem. Skill",
                            inline=False)
        ningguang.set_footer(text="Character Builds")
        return ningguang

    def noelle(self):
        noelle = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: DEF% \n"
                        "Melee unit that can deal DPS while also providing shields and small healing \n"
                        "Elem. Burst ATK scales off of DEF \n"
                        "Can truly come online as a strong DPS unit at C6",
            colour=discord.Colour(0xf5d760)
        )
        noelle.set_author(name="Noelle")
        noelle.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775077747491471370/Noelle.png")
        noelle.add_field(name="Weapons", value="Whiteblind ☆☆☆☆ \n"
                                               "White Iron Greatsword ☆☆☆",
                         inline=True)
        noelle.add_field(name="Artifacts", value="4x Retracing Bolide or Exile \n"
                                                 "<:flowerwhite:774424948558397511> HP \n"
                                                 "<:featherwhite:774424948369653762> ATK \n"
                                                 "<:hourglasswhite:774424948784627712> DEF% \n"
                                                 "<:cupwhite:774424948399276034> Geo DMG% (DEF% if C6) \n"
                                                 "<:headpiecewhite:774420351756927006> DEF% \n"
                                                 "Substats: DEF(%), ATK(%), Crit Rate (50% MAX)",
                         inline=False)
        noelle.add_field(name="Talent Priority", value="Elem. Burst, Normal ATK, Elem. Skill",
                         inline=False)
        noelle.set_footer(text="Character Builds")
        return noelle

    def qiqi(self):
        qiqi = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Healing Bonus \n"
                        "Currently best healer in the game \n"
                        "Heals off of normal ATKs, similar to Jean \n"
                        "Passive talent is useful for acquiring resources in Liyue",
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
        qiqi.set_footer(text="Character Builds")
        return qiqi

    def razor(self):
        razor = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Phys DMG % \n Close range DPS \n Not suitable for swap-out playstyle",
            colour=discord.Colour.purple()
        )
        razor.set_author(name="Razor")
        razor.set_thumbnail(url="https://cdn.discordapp.com/attachments/773757621520957493/775082739283001374/razor.png")
        razor.add_field(name="Weapons", value="Wolf's Gravestone ☆☆☆☆☆ \n Prototype Animus ☆☆☆☆ \n Debate "
                                              "Club ☆☆☆",
                        inline=False)
        razor.add_field(name="Artifacts", value="4x Gladiator's Finale \n "
                                                "<:flowerwhite:774424948558397511> HP \n"
                                                "<:featherwhite:774424948369653762> ATK \n"
                                                "<:hourglasswhite:774424948784627712> ATK% \n"
                                                "<:cupwhite:774424948399276034> Phys DMG% \n"
                                                "<:headpiecewhite:774420351756927006> Crit DMG \n"
                                                "Substats: ATK(%), Crit Rate (50% MAX), Crit DMG",
                        inline=False)
        razor.add_field(name="Talent Priority", value="Normal ATK, Elem. Burst, Elem. Skill", inline=True)
        razor.set_footer(text="Character Builds")
        return razor

    def sucrose(self):
        sucrose = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Anemo DMG \n"
                        "Great support for elemental reactions \n"
                        "Elem. Mastery battery at Ascension 4 \n"
                        "Passive talent is incredibly useful for crafting",
            colour=discord.Colour.green()
        )
        sucrose.set_author(name="Sucrose")
        sucrose.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775082757302779934/Sucrose.png")
        sucrose.add_field(name="Weapons", value="Sacrifical Fragments ☆☆☆☆ \n"
                                                "Mappa Mare ☆☆☆☆",
                          inline=True)
        sucrose.add_field(name="Artifacts", value="4x Viridescent Venerer or Instructor \n"
                                                  "<:flowerwhite:774424948558397511> HP \n"
                                                  "<:featherwhite:774424948369653762> ATK \n"
                                                  "<:hourglasswhite:774424948784627712> Elemental Mastery \n"
                                                  "<:cupwhite:774424948399276034> Anemo DMG \n"
                                                  "<:headpiecewhite:774420351756927006> ATK% \n"
                                                  "Substats: Elem. Mastery, ATK(%), Energy Recharge",
                          inline=False)
        sucrose.add_field(name="Talent Priority", value="Elem. Burst, Elem. Skill, Normal ATK",
                          inline=False)
        sucrose.set_footer(text="Character Builds")
        return sucrose

    def tartaglia(self):
        tartaglia = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Hydro DMG \n"
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
                                                    "Substats: ATK(%), Crit DMG, Crit Rate (50% MAX)",
                            inline=False)
        tartaglia.add_field(name="Talent Priority", value="Elem. Skill, Normal ATK, Elem. Burst",
                            inline=False)
        tartaglia.set_footer(text="Character Builds")
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
        anemo.set_footer(text="Character Builds")
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
        geo.set_footer(text="Character Builds")
        return geo

    def venti(self):
        venti = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Energy Recharge \n"
                        "S+ tier unit across the board in all categories \n"
                        "Elem. Skill is useful/required when exploring to collect Oculi and complete puzzles \n"
                        "Mainly used as a battery for Energy Recharge and elemental reactions with Elem. Burst \n"
                        "Could be used for DMG with C1 and an aimed shot build",
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
        venti.set_footer(text="Character Builds")
        return venti

    def xiangling(self):
        xiangling = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: Elemental Mastery \n"
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
                                                          "Substats: ATK(%), Crit Rate (50% MAX), Crit DMG",
                            inline=True)
        xiangling.add_field(name="Talent Priority", value="(Support) Elem. Skill, Elem. Burst, Normal ATK \n"
                                                          "(DPS) Normal ATK, Elem. Skill, Elem. Burst",
                            inline=False)
        xiangling.set_footer(text="Character Builds")
        return xiangling

    def xingqiu(self):
        xiangqiu = discord.Embed(
            title="Character Build & Info",
            description="Ascension Boost: ATK% \n"
                        "Solid Hydro support that delivers heals and damage reduction \n"
                        "Can be a reliable source of Hydro reactions from his Elem. Burst \n"
                        "Powerful support with a Hydro DPS unit at Constellation 2 \n"
                        "Passive talent is extremely useful when crafting",
            colour=discord.Colour.blue()
        )
        xiangqiu.set_author(name="Xingqiu")
        xiangqiu.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/773757621520957493/775095718825164820/xingqiu.png")
        xiangqiu.add_field(name="Weapons (Support)", value="Skyward Blade ☆☆☆☆☆ \n"
                                                           "Favonius Sword ☆☆☆☆ \n"
                                                           "Iron Sting ☆☆☆☆",
                           inline=True)
        xiangqiu.add_field(name="Artifacts (Support)", value="4x Noblesse Oblige or Exile \n"
                                                             "<:flowerwhite:774424948558397511> HP \n"
                                                             "<:featherwhite:774424948369653762> ATK \n"
                                                             "<:hourglasswhite:774424948784627712> ATK% \n"
                                                             "<:cupwhite:774424948399276034> Hydro DMG \n"
                                                             "<:headpiecewhite:774420351756927006> ATK% \n"
                                                             "Substats: Energy Recharge, Elem. Mastery, ATK(%)",
                           inline=False)
        xiangqiu.add_field(name="Talent Priority", value="Elem. Skill, Elem. Burst, Normal ATK",
                           inline=False)
        xiangqiu.set_footer(text="Character Builds")
        return xiangqiu

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
        contents.add_field(name=chr(173), value='<:amber:773662632200372224> [Amber Build & Info]('
                                                'https://discordapp.com/channels/749438385042751549/749466052068376649/775134310936215572)')
        contents.add_field(name=chr(173),
                           value='<:barbara:773662631068172298> [Barbara Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775134555132002304)')
        contents.add_field(name=chr(173),
                           value='<:beidou:773662631159791616> [Beidou Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775134656705593365)')
        contents.add_field(name=chr(173),
                           value='<:bennett:773662631063453716> [Bennett Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775134766365933618)')
        contents.add_field(name=chr(173),
                           value='<:chongyun:773666659096723466> [Chongyun Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775134837760589824)')
        contents.add_field(name=chr(173),
                           value='<:diluc:773666659084795927> [Diluc Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775134908191473664)')
        contents.add_field(name=chr(173),
                           value='<:fischl:773666659360571422> [Fischl Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775134979743154206)')
        contents.add_field(name=chr(173),
                           value='<:jean:773666659156230145> [Jean Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135068682321950)')
        contents.add_field(name=chr(173),
                           value='<:kaeya:773666659281797120> [Kaeya Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135141286641705)')
        contents.add_field(name=chr(173),
                           value='<:keqing:773666659156099112> [Keqing Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135211507023952)')
        contents.add_field(name=chr(173),
                           value='<:klee:773666659281666088> [Klee Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135280415637504)')
        contents.add_field(name=chr(173),
                           value='<:lisa:773666659159900170> [Lisa Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135357267476501)')
        contents.add_field(name=chr(173),
                           value='<:mona:773666659080601610> [Mona Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135430009552906)')
        contents.add_field(name=chr(173),
                           value='<:ningguang:773666659192930315> [Ningguang Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135494576144386)')
        contents.add_field(name=chr(173),
                           value='<:noelle:773666659180871740> [Noelle Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135551488786453)')
        contents.add_field(name=chr(173),
                           value='<:qiqi:773666659100524544> [Qiqi Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135609882673187)')
        contents.add_field(name=chr(173),
                           value='<:razorgenshin:773666658983870484> [Razor Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135684930306069)')
        contents.add_field(name=chr(173),
                           value='<:sucrose:773666658941141072> [Sucrose Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135785757310976)')
        contents.add_field(name=chr(173),
                           value='<:Traveler:775114785821032470> [Traveler (Anemo) Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135846273384460)')
        contents.add_field(name=chr(173),
                           value='<:Traveler:775114785821032470> [Traveler (Geo) Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135903601524787)')
        contents.add_field(name=chr(173),
                           value='<:venti:773667045225136158> [Venti Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775135963570765835)')
        contents.add_field(name=chr(173),
                           value='<:xiangling:773667044968628224> [Xiangling Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775136028083093514)')
        contents.add_field(name=chr(173),
                           value='<:xingqiu:773667044846469162> [Xingqiu Build & Info](https://discordapp.com/channels/749438385042751549/749466052068376649/775136096110903317)')
