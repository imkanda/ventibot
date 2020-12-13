import discord
import random
import asyncio
import time
import pandas as pd
from wish import Wish
from embeds import Embeds
from mangascrape import Scrape
from ch_guides import Guides
from ch_guides import clientkey
from discord import Streaming

wish = Wish()
embeds = Embeds()
scrape = Scrape()
guides = Guides()


class MyClient(discord.Client):
    embedDic = {}

    async def on_member_update(self, before, after):

        # grabs announcements channel
        ch = self.get_channel(749485617276125286)
        # grabs user
        kanda = self.get_user(629377169663066153)
        twitch_url = 'https://www.twitch.tv/ohkanda'
        subject = before

        if subject == kanda:
            # if update is streaming
            if isinstance(after.activity, Streaming):
                # sends message to announcements channel with stream link
                await ch.send(f"{before.mention} is streaming on {after.activity.platform}: {after.activity.name}.\n"
                              f"Join here: {after.activity.name}")
                # changes presence to watching stream
                await self.change_presence(activity=discord.Streaming(name="Kanda's Twitch stream", url=twitch_url))
            # if update changes and was previously streaming
            elif isinstance(before.activity, Streaming):
                # changes presence back to original
                await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='a '
                                                                                                               'ballad'))
                async for message in ch.history(limit=100):
                    if "streaming" in message.content and message.author == self.user:
                        # deletes message made in announcement channel to reduce clutter
                        await message.delete_message()

    async def manga_check(self):
        await self.wait_until_ready()
        # grabs manga-updates channel
        ch = self.get_channel(778448461162086440)
        while not self.is_closed():
            print('Updating manga..')

            # solo leveling update
            with open("slchapter.txt", "r+") as txt:
                sl_chapter = txt.read()
            # checks to see if chapter from scrape is different to saved
            sl_string = scrape.sl_chapter_check()
            if sl_chapter != sl_string:
                # chapter is different so rewrites file and constructs update message with link to new chapter
                with open("slchapter.txt", "w+") as txt:
                    txt.write(sl_string)
                sl_link = scrape.sl_link()
                sl_embed = discord.Embed(
                    description='New Solo Leveling chapter!',
                    colour=discord.Colour.red()
                )
                sl_embed.add_field(name="{}".format(sl_string), value='[View Here]({})'.format(sl_link))
                sl_embed.set_thumbnail(url='https://cover.nep.li/cover/Solo-Leveling.jpg')
                await ch.send(embed=sl_embed)

            # csm update
            with open("csmchapter.txt", "r+") as txt:
                csm_chapter = txt.read()
            # checks to see if chapter from scrape is different to saved
            csm_string = scrape.csm_chapter_check()
            if csm_chapter != csm_string:
                # chapter is different so rewrites file and constructs update message with link to new chapter
                with open("csmchapter.txt", "w+") as txt:
                    txt.write(csm_string)
                csm_link = scrape.csm_link()
                csm_embed = discord.Embed(
                    description='New Chainsaw Man chapter!',
                    colour=discord.Colour.red()
                )
                csm_embed.add_field(name="{}".format(csm_string), value='[View Here]({})'.format(csm_link))
                csm_embed.set_thumbnail(url='https://cover.nep.li/cover/Chainsaw-Man.jpg')
                await ch.send(embed=csm_embed)

            with open("snkchapter.txt", "r+") as txt:
                snk_chapter = txt.read()
            # checks to see if chapter from scrape is different to saved
            snk_string = scrape.snk_chapter_check()
            if snk_chapter != snk_string:
                # chapter is different so rewrites file and constructs update message with link to new chapter
                with open("snkchapter.txt", "w+") as txt:
                    txt.write(snk_string)
                snk_link = scrape.snk_link()
                snk_embed = discord.Embed(
                    description='New Attack on Titan chapter!',
                    colour=discord.Colour.red()
                )
                snk_embed.add_field(name="{}".format(snk_string), value='[View Here]({})'.format(snk_link))
                snk_embed.set_thumbnail(url='https://cover.nep.li/cover/Shingeki-No-Kyojin.jpg')
                await ch.send(embed=snk_embed)

            # jjk update
            with open("jjkchapter.txt", "r+") as txt:
                jjk_chapter = txt.read()
            # checks to see if chapter from scrape is different to saved
            jjk_string = scrape.jjk_chapter_check()
            if jjk_chapter != jjk_string:
                # chapter is different so rewrites file and constructs update message with link to new chapter
                with open("jjkchapter.txt", "w+") as txt:
                    txt.write(jjk_string)
                jjk_link = scrape.jjk_link()
                jjk_embed = discord.Embed(
                    description='New Jujutsu Kaisen chapter!',
                    colour=discord.Colour.red()
                )
                jjk_embed.add_field(name="{}".format(jjk_string), value='[View Here]({})'.format(jjk_link))
                jjk_embed.set_thumbnail(url='https://cover.nep.li/cover/Jujutsu-Kaisen.jpg')
                await ch.send(embed=jjk_embed)

            # berserk update
            with open("brsrkchapter.txt", "r+") as txt:
                brsrk_chapter = txt.read()
            # checks to see if chapter from scrape is different to saved
            brsrk_string = scrape.brsrk_chapter_check()
            if brsrk_chapter != brsrk_string:
                # chapter is different so rewrites file and constructs update message with link to new chapter
                with open("brsrkchapter.txt", "w+") as txt:
                    txt.write(brsrk_string)
                brsrk_link = scrape.brsrk_link()
                brsrk_embed = discord.Embed(
                    description='New Berserk chapter..? <:kekwtf:773683896688050236>',
                    colour=discord.Colour.red()
                )
                brsrk_embed.add_field(name="{}".format(brsrk_string), value='[View Here]({})'.format(brsrk_link))
                brsrk_embed.set_thumbnail(url='https://cover.nep.li/cover/Berserk.jpg')
                await ch.send(embed=brsrk_embed)

            # black clover update
            with open("bcchapter.txt", "r+") as txt:
                bc_chapter = txt.read()
            # checks to see if chapter from scrape is different to saved
            bc_string = scrape.bc_chapter_check()
            if bc_chapter != bc_string:
                # chapter is different so rewrites file and constructs update message with link to new chapter
                with open("bcchapter.txt", "w+") as txt:
                    txt.write(bc_string)
                bc_link = scrape.bc_link()
                bc_embed = discord.Embed(
                    description='New Black Clover chapter!',
                    colour=discord.Colour.red()
                )
                bc_embed.add_field(name="{}".format(bc_string), value='[View Here]({})'.format(bc_link))
                bc_embed.set_thumbnail(url='https://cover.nep.li/cover/Black-Clover.jpg')
                await ch.send(embed=bc_embed)

            # Tower of God update
            with open("togchapter.txt", "r+") as txt:
                tog_chapter = txt.read()
            # checks to see if chapter from scrape is different to saved
            tog_string = scrape.tog_chapter_check()
            if tog_chapter != tog_string:
                # chapter is different so rewrites file and constructs update message with link to new chapter
                with open("togchapter.txt", "w+") as txt:
                    txt.write(tog_string)
                tog_link = scrape.tog_link()
                tog_embed = discord.Embed(
                    description='New Tower of God chapter!',
                    colour=discord.Colour.red()
                )
                tog_embed.add_field(name="{}".format(tog_string), value='[View Here]({})'.format(tog_link))
                tog_embed.set_thumbnail(url='https://cover.nep.li/cover/Tower-Of-God.jpg')
                await ch.send(embed=tog_embed)

            print('Manga update finished!')
            # sleeps for 15 minutes then loops through again to try and catch new updates when they release
            await asyncio.sleep(600)

    # function for creating list of all users with specific role, used this for giveaways inside the server
    def get_list(self, message):
        server_members = message.guild.members
        # change name for get function to whatever the name of the giveaway role is
        giveaway_role = discord.utils.get(message.guild.roles, name='🥳 Battle Pass Giveaway')
        giveaway_members_list = []

        # cycles through all members in server and their roles, adding anyone with above role
        # to the list, then returns the list once it's done to be used in below function
        for member in server_members:
            if giveaway_role in member.roles:
                giveaway_members_list.append(member)
        return giveaway_members_list

    # on message functions (bot commands) (prefix: '.')
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('.'):
            # on message it will grab the list created from get_list function and randomly mention someone in the list
            if message.content == '.winner':
                for role in message.author.roles:
                    if 'Fatui Harbringers' or "Makima's Dog" == role.name:
                        giveaway_winner = random.choice(self.get_list(message))
                        winner_message = 'Congrats {}, you have won the giveaway!'.format(giveaway_winner.name)
                        await message.channel.send(winner_message)
            # posts a user's avatar in chat
            if message.content.startswith('.avatar'):
                if message.mentions == []:
                    sender = message.author
                    userpfp = sender.avatar_url
                    pfpembed = discord.Embed(
                    )
                    pfpembed.add_field(name='Avatar Scraper', value='user: {}'.format(sender))
                    pfpembed.set_image(url=userpfp)
                    await message.channel.send(embed=pfpembed)
                else:
                    user = message.mentions[0]
                    userpfp = user.avatar_url
                    pfpembed = discord.Embed(
                    )
                    pfpembed.add_field(name='Avatar Scraper', value='user: {}'.format(user))
                    pfpembed.set_image(url=userpfp)
                    await message.channel.send(embed=pfpembed)
            if message.content == '.help':
                await message.channel.send(embed=embeds.help_embed())
            if message.content.startswith('.mute'):
                guild = self.get_guild(749438385042751549)
                mods = discord.utils.get(guild.roles, name="Fatui Harbingers")
                owner = discord.utils.get(guild.roles, name="Makima's Dog")
                author_roles = message.author.roles
                if mods in author_roles:
                    if message.mentions != []:
                        user_uname = message.mentions[0]
                        muted = discord.utils.get(guild.roles, name='Muted')
                        if user_uname is not None:
                            if muted in user_uname.roles:
                                await message.channel.send('User is already muted.')
                                return
                            else:
                                await user_uname.add_roles(muted)
                                await message.channel.send('User has been muted.')
                                return
                if owner in author_roles:
                    if message.mentions != []:
                        user_uname = message.mentions[0]
                        muted = discord.utils.get(guild.roles, name='Muted')
                        if user_uname is not None:
                            if muted in user_uname.roles:
                                await message.channel.send('User is already muted.')
                                return
                            else:
                                await user_uname.add_roles(muted)
                                await message.channel.send('User has been muted.')
                                return
                    else:
                        await message.channel.send('Please mention a user to mute.')
                        return
                else:
                    await message.channel.send('Only staff members can mute.')
                    return
            if message.content.startswith('.unmute'):
                guild = self.get_guild(749438385042751549)
                mods = discord.utils.get(guild.roles, name="Fatui Harbingers")
                owner = discord.utils.get(guild.roles, name="Makima's Dog")
                author_roles = message.author.roles
                if mods in author_roles:
                    if message.mentions != []:
                        user_uname = message.mentions[0]
                        muted = discord.utils.get(guild.roles, name='Muted')
                        if user_uname is not None:
                            if muted in user_uname.roles:
                                await user_uname.remove_roles(muted)
                                await message.channel.send('User has been unmuted.')
                                return
                            else:
                                await message.channel.send('This user is not muted.')
                                return
                if owner in author_roles:
                    if message.mentions != []:
                        user_uname = message.mentions[0]
                        muted = discord.utils.get(guild.roles, name='Muted')
                        if user_uname is not None:
                            if muted in user_uname.roles:
                                await user_uname.remove_roles(muted)
                                await message.channel.send('User has been unmuted.')
                                return
                            else:
                                await message.channel.send('This user is not muted.')
                                return
                    else:
                        await message.channel.send('Please mention a user to mute.')
                        return
                else:
                    await message.channel.send("Only staff members can unmute.")
                    return
            if message.content == '.wish':
                wish_ch = self.get_channel(784964222899453972)
                if message.channel == wish_ch:
                    multipull = wish.wishmulti_nonpity()
                    if "5" in multipull[2]:
                        rarity_gif = 'https://media1.tenor.com/images/4386330cff81cc4b79ea640f833a3a90/tenor.gif?itemid=19460396'
                        embed_colour = discord.Colour.gold()
                    else:
                        rarity_gif = 'https://media1.tenor.com/images/0358d3a4fca9fcc5ec96074de002525f/tenor.gif?itemid=19460235'
                        embed_colour = discord.Colour.purple()
                    emoji_pull = multipull[0]
                    name_pull = multipull[1]
                    first_pull = f"{emoji_pull[0]} {name_pull[0]}"
                    second_pull = f"{emoji_pull[1]} {name_pull[1]}"
                    third_pull = f"{emoji_pull[2]} {name_pull[2]}"
                    fourth_pull = f"{emoji_pull[3]} {name_pull[3]}"
                    fifth_pull = f"{emoji_pull[4]} {name_pull[4]}"
                    sixth_pull = f"{emoji_pull[5]} {name_pull[5]}"
                    seventh_pull = f"{emoji_pull[6]} {name_pull[6]}"
                    eighth_pull = f"{emoji_pull[7]} {name_pull[7]}"
                    ninth_pull = f"{emoji_pull[8]} {name_pull[8]}"
                    tenth_pull = f"{emoji_pull[9]} {name_pull[9]}"

                    wishing_embed = discord.Embed(
                        description='{}, ten stars fall from the sky..'.format(message.author.mention),
                        colour=discord.Colour(0x82d9f9)
                    )
                    wishing_embed.set_image(url=rarity_gif)
                    wishing_embed.set_footer(text='Wishes')
                    await message.channel.send(embed=wishing_embed)

                    time.sleep(4)

                    wish_embed = discord.Embed(
                        description='{}, below are your pulls!'.format(message.author.mention),
                        colour=embed_colour
                    )
                    wish_embed.add_field(name=chr(173), value=first_pull, inline=False)
                    wish_embed.add_field(name=chr(173), value=second_pull, inline=False)
                    wish_embed.add_field(name=chr(173), value=third_pull, inline=False)
                    wish_embed.add_field(name=chr(173), value=fourth_pull, inline=False)
                    wish_embed.add_field(name=chr(173), value=fifth_pull, inline=False)
                    wish_embed.add_field(name=chr(173), value=sixth_pull, inline=False)
                    wish_embed.add_field(name=chr(173), value=seventh_pull, inline=False)
                    wish_embed.add_field(name=chr(173), value=eighth_pull, inline=False)
                    wish_embed.add_field(name=chr(173), value=ninth_pull, inline=False)
                    wish_embed.add_field(name=chr(173), value=tenth_pull, inline=False)
                    wish_embed.set_footer(text='Wishes')
                    await message.channel.send(embed=wish_embed)
                else:
                    await message.channel.send('Please use wish commands in <#784964222899453972> only!')

            if message.content == '.wish multi':
                wish_ch = self.get_channel(787520738118598656)
                if message.channel == wish_ch:
                    userid = message.author.id
                    primo_check = wish.primo_check(userid)
                    if primo_check == 'NONE':
                        await message.channel.send('{}, you have not been registered yet. Use .daily to be able to '
                                                   'wish.'.format(message.author.mention))
                    else:
                        initial_primos = primo_check[0]
                        index = primo_check[1]
                        if int(initial_primos) >= 1600:
                            sub_primos = int(initial_primos) - 1600
                            contents = pd.read_csv('server_wishes.csv', dtype=str)
                            contents.at[index, 'primos'] = sub_primos
                            contents.to_csv('server_wishes.csv', index=False)
                            multipull = wish.wishmulti_pity(userid, index)
                            emoji_pull = multipull[0]
                            name_pull = multipull[1]
                            wish.dupes(userid, index, name_pull)
                            if "5" in multipull[2]:
                                rarity_gif = 'https://media1.tenor.com/images/4386330cff81cc4b79ea640f833a3a90/tenor.gif?itemid=19460396'
                                embed_colour = discord.Colour.gold()
                            else:
                                rarity_gif = 'https://media1.tenor.com/images/0358d3a4fca9fcc5ec96074de002525f/tenor.gif?itemid=19460235'
                                embed_colour = discord.Colour.purple()
                            first_pull = f"{emoji_pull[0]} {name_pull[0]}"
                            second_pull = f"{emoji_pull[1]} {name_pull[1]}"
                            third_pull = f"{emoji_pull[2]} {name_pull[2]}"
                            fourth_pull = f"{emoji_pull[3]} {name_pull[3]}"
                            fifth_pull = f"{emoji_pull[4]} {name_pull[4]}"
                            sixth_pull = f"{emoji_pull[5]} {name_pull[5]}"
                            seventh_pull = f"{emoji_pull[6]} {name_pull[6]}"
                            eighth_pull = f"{emoji_pull[7]} {name_pull[7]}"
                            ninth_pull = f"{emoji_pull[8]} {name_pull[8]}"
                            tenth_pull = f"{emoji_pull[9]} {name_pull[9]}"

                            wishing_embed = discord.Embed(
                                description='{}, ten stars fall from the sky..'.format(message.author.mention),
                                colour=discord.Colour(0x82d9f9)
                            )
                            wishing_embed.set_image(url=rarity_gif)
                            wishing_embed.set_footer(text='Wishes')
                            await message.channel.send(embed=wishing_embed)

                            time.sleep(4)

                            wish_embed = discord.Embed(
                                description='{}, below are your pulls!'.format(message.author.mention),
                                colour=embed_colour
                            )
                            wish_embed.add_field(name=chr(173), value=first_pull, inline=False)
                            wish_embed.add_field(name=chr(173), value=second_pull, inline=False)
                            wish_embed.add_field(name=chr(173), value=third_pull, inline=False)
                            wish_embed.add_field(name=chr(173), value=fourth_pull, inline=False)
                            wish_embed.add_field(name=chr(173), value=fifth_pull, inline=False)
                            wish_embed.add_field(name=chr(173), value=sixth_pull, inline=False)
                            wish_embed.add_field(name=chr(173), value=seventh_pull, inline=False)
                            wish_embed.add_field(name=chr(173), value=eighth_pull, inline=False)
                            wish_embed.add_field(name=chr(173), value=ninth_pull, inline=False)
                            wish_embed.add_field(name=chr(173), value=tenth_pull, inline=False)
                            wish_embed.set_footer(text='Wishes')
                            await message.channel.send(embed=wish_embed)
                            wish_count = int(wish.wishes_check(userid)) + 10
                            contents = pd.read_csv('server_wishes.csv', dtype=str)
                            contents.at[index, 'wishes'] = wish_count
                            contents.to_csv('server_wishes.csv', index=False)
                        else:
                            await message.channel.send('Sorry {}, you do not have enough primos for this wish '
                                                       'amount'.format(message.author.mention))
                else:
                    wish_casual = self.get_channel(784964222899453972)
                    if message.channel == wish_casual:
                        await message.channel.send("You're in <#784964222899453972>, use .wish. (NO CATALOG TRACKING)")
                    else:
                        await message.channel.send('Please use .wish multi in <#787520738118598656> only!')


            if message.content == '.wish single':
                wish_ch = self.get_channel(787520738118598656)
                if message.channel == wish_ch:
                    userid = message.author.id
                    primo_check = wish.primo_check(userid)
                    if primo_check == 'NONE':
                        await message.channel.send('{}, you have not been registered yet. Use .daily to be able to '
                                                   'wish.'.format(message.author.mention))
                    else:
                        initial_primos = primo_check[0]
                        index = primo_check[1]
                        initial_pitys = wish.pity_check(userid)
                        fourstar_pity = int(initial_pitys[0])
                        fivestar_pity = int(initial_pitys[1])
                        if int(initial_primos) >= 160:
                            sub_primos = int(initial_primos) - 160
                            contents = pd.read_csv('server_wishes.csv', dtype=str)
                            contents.at[index, 'primos'] = sub_primos
                            contents.to_csv('server_wishes.csv', index=False)
                            pull = wish.wishsingle_pity(userid, index)
                            emoji_pull = pull[0]
                            name_pull = pull[1]
                            wish.dupes(userid, index, name_pull)
                            if "5" in pull[2]:
                                rarity_gif = 'https://media1.tenor.com/images/0fd8cfa923ed50e19bf16d76de52055a/tenor.gif'
                                embed_colour = discord.Colour.gold()
                                contents = pd.read_csv('server_wishes.csv', dtype=str)
                                contents.at[index, 'five_pity'] = 0
                                contents.at[index, 'four_pity'] = fourstar_pity + 1
                                contents.to_csv('server_wishes.csv', index=False)
                            elif "4" in pull[2]:
                                rarity_gif = 'https://media1.tenor.com/images/a2d4acc6cce5e248079ae69a4ee872af/tenor.gif'
                                embed_colour = discord.Colour.purple()
                                contents = pd.read_csv('server_wishes.csv', dtype=str)
                                contents.at[index, 'four_pity'] = 0
                                contents.at[index, 'five_pity'] = fivestar_pity + 1
                                contents.to_csv('server_wishes.csv', index=False)
                            else:
                                rarity_gif = 'https://media1.tenor.com/images/9778d97b6d6ed00ceb116b5827c9c435/tenor.gif'
                                embed_colour = discord.Colour(0x82d9f9)
                                contents = pd.read_csv('server_wishes.csv', dtype=str)
                                contents.at[index, 'four_pity'] = fourstar_pity + 1
                                contents.at[index, 'five_pity'] = fivestar_pity + 1
                                contents.to_csv('server_wishes.csv', index=False)

                            first_pull = f"{emoji_pull[0]} {name_pull[0]}"

                            wishing_embed = discord.Embed(
                                description='{}, one star falls from the sky..'.format(message.author.mention),
                                colour=discord.Colour(0x82d9f9)
                            )
                            wishing_embed.set_image(url=rarity_gif)
                            wishing_embed.set_footer(text='Wishes')
                            await message.channel.send(embed=wishing_embed)

                            time.sleep(4)

                            wish_embed = discord.Embed(
                                description='{}, below are your pulls!'.format(message.author.mention),
                                colour=embed_colour
                            )
                            wish_embed.add_field(name=chr(173), value=first_pull, inline=False)
                            wish_embed.set_footer(text='Wishes')
                            await message.channel.send(embed=wish_embed)
                            wish_count = int(wish.wishes_check(userid)) + 1
                            contents = pd.read_csv('server_wishes.csv', dtype=str)
                            contents.at[index, 'wishes'] = wish_count
                            contents.to_csv('server_wishes.csv', index=False)
                        else:
                            await message.channel.send('Sorry {}, you do not have enough primos for this wish '
                                                       'amount'.format(message.author.mention))
                else:
                    wish_casual = self.get_channel(784964222899453972)
                    if message.channel == wish_casual:
                        await message.channel.send("You're in <#784964222899453972>, use .wish. (NO CATALOG TRACKING)")
                    else:
                        await message.channel.send('Please use .wish multi in <#787520738118598656> only!')
            if message.content == '.daily':
                userid = message.author.id
                cooldown = message.created_at
                primos = wish.daily_primo(userid, cooldown)
                if primos:
                    await message.channel.send(f'Dailies completed, nice job {message.author.mention}! You now have'
                                               f' {primos} primos.')
                else:
                    await message.channel.send('{}, you must wait until tomorrow to do your dailies again'.format(
                        message.author.mention))
            if message.content == '.primos':
                wish_ch = self.get_channel(787520738118598656)
                if message.channel == wish_ch:
                    userid = message.author.id
                    primo_check = wish.primo_check(userid)
                    primos = str(primo_check[0])
                    if primo_check == 'NONE':
                        await message.channel.send('{}, you have not been registered yet. Use .daily to gain primos to '
                                                   'wish and earn units!'.format(message.author.mention))
                    else:
                        await message.channel.send(f'{message.author.mention}, you currently have {primos} primos.')
                else:
                    await message.channel.send('Please use .primos in <#787520738118598656> only!')
            if message.content == '.pity':
                wish_ch = self.get_channel(787520738118598656)
                if message.channel == wish_ch:
                    userid = message.author.id
                    pity = wish.pity_check(userid)
                    fourstar_pity = str(pity[0])
                    fivestar_pity = str(pity[1])
                    if pity == 'NONE':
                        await message.channel.send('{}, you have not been registered yet. Use .daily to gain primos to '
                                                   'wish and earn units!'.format(message.author.mention))
                    else:
                        await message.channel.send(f'{message.author.mention}, you are currently at {fourstar_pity}/10 '
                                                   f'for your next four star guarantee, and {fivestar_pity}/90 for your '
                                                   f'next five star guarantee.')
                else:
                    await message.channel.send('Please use .primos in <#787520738118598656> only!')
            if message.content == '.catalog':
                userid = message.author.id
                catalog = wish.catalog_parse(userid)
                emoji_pull = catalog[0]
                name_pull = catalog[1]
                wishes = str(wish.wishes_check(userid))
                if catalog == 'NONE' or wishes == 'NONE':
                    await message.channel.send('{}, you have not been registered yet. Use .daily to gain primos to '
                                               'wish and earn units!'.format(message.author.mention))
                elif catalog[0] == []:
                    await message.channel.send('{}, you currently have no units.'.format(message.author.mention))
                else:
                    catalog_embed = discord.Embed(
                        description=f"{message.author.mention}'s units earned over {wishes} total wishes",
                        colour=discord.Colour.green()
                    )
                    for i in range(len(name_pull)):
                        catalog_embed.insert_field_at(i, name=chr(173), value=f'{emoji_pull[i]} {name_pull[i]}')
                    catalog_embed.set_footer(text='Catalog')
                    await message.channel.send(embed=catalog_embed)

    # role add and remove based on reaction, you need to add the message ID with the others. may be able to improve
    # this process to look cleaner on this end but it works
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        # if message_id = roles_game embed in #self-roles
        if message_id == 773749867121868800:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
            guest_role = discord.utils.get(member.guild.roles, name="Guest")

            if role is not None:

                if payload.user_id == self.user:
                    return
                elif member is not None:
                    await member.add_roles(role)
                    if guest_role in member.roles:
                        await member.remove_roles(guest_role)
        # if message_id = any of the other CURRENT embeds in #self-roles
        if message_id == 773764928497778719 or 773765122983854091 or 773765378803367946 or 773800977148149781:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if payload.user_id == 749451840281641000:
                    return
                elif member is not None:
                    await member.add_roles(role)
        if message_id == 778694747966406666 or 778832000127074326:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if payload.user_id == 749451840281641000:
                return
            elif member is not None:
                if payload.emoji.name == "🇺🇸":
                    na_role = discord.utils.get(guild.roles, name="NA")
                    await member.add_roles(na_role)
                if payload.emoji.name == "🇪🇺":
                    eu_role = discord.utils.get(guild.roles, name="EU")
                    await member.add_roles(eu_role)
                if payload.emoji.name == "🇯🇵":
                    as_role = discord.utils.get(guild.roles, name="AS")
                    await member.add_roles(as_role)
                if payload.emoji.name == "🇭🇰":
                    sar_role = discord.utils.get(guild.roles, name="SAR")
                    await member.add_roles(sar_role)
                if payload.emoji.name == "📚":
                    mangafiends_role = discord.utils.get(guild.roles, name="manga fiends")
                    await member.add_roles(mangafiends_role)

    # the opposite of the reaction_remove command, I have it set up to give Guest role back if they were to not have
    # any active reactions to the roles_game embed but not to do so if they're removing react from any of the other
    # embeds
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        # if message_id = the roles_game embed in #self-roles
        if message_id == 773749867121868800:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
            guest_role = discord.utils.get(member.guild.roles, name="Guest")
            game_roles = discord.utils.get(member.guild.roles, name='Sins' or 'Travelers')
            if role is not None:
                await member.remove_roles(role)
                if game_roles not in member.roles:
                    await member.add_roles(guest_role)
        # if message_id = any of the other CURRENT embeds in #self-roles
        if message_id == 773764928497778719 or 773765122983854091 or 773765378803367946:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if message_id == 778694747966406666:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if payload.user_id == 749451840281641000:
                return
            elif member is not None:
                if payload.emoji.name == "🇺🇸":
                    na_role = discord.utils.get(guild.roles, name="NA")
                    await member.remove_roles(na_role)
                if payload.emoji.name == "🇪🇺":
                    eu_role = discord.utils.get(guild.roles, name="EU")
                    await member.remove_roles(eu_role)
                if payload.emoji.name == "🇯🇵":
                    as_role = discord.utils.get(guild.roles, name="AS")
                    await member.remove_roles(as_role)
                if payload.emoji.name == "🇭🇰":
                    sar_role = discord.utils.get(guild.roles, name="SAR")
                    await member.remove_roles(sar_role)

    # bot login confirmation #
    async def on_ready(self):
        print('Logged on as', self.user)
        # once bot connects to discord it will begin the manga check loop
        await self.loop.create_task(self.manga_check())

    # functions to run when bot logs in #
    async def on_connect(self):
        print('Connected')
        # updates online presence
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='a ballad'))

    # sends welcome_message embed in welcome text channel whenever someone joins and also gives them Guest role so
    # no one in the server will be role-less
    async def on_member_join(self, member):
        ch = self.get_channel(749438385042751552)
        general = self.get_channel(749485433309757451)
        await ch.send(embed=embeds.welcome_message(ch, member))
        guest_role = discord.utils.get(member.guild.roles, name="Guest")
        await member.add_roles(guest_role)
        general_welcome = 'hi everyone, please welcome {}!! feel free to grab roles from <#749485522447237211> for ' \
                          'genshin ' \
                          'stuff ' \
                          'or hang ' \
                          'out as ' \
                          'guest. whatever floats your boat <a:chika:773705341660692521>'.format(member.mention)
        await general.send(general_welcome)
        return


client = MyClient()
client.run('')
