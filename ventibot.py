import discord
import random
import asyncio
import time
import pandas as pd
from wish import Wish
from embeds import Embeds
from mangascrape import Scrape


wish = Wish()
embeds = Embeds()
scrape = Scrape()


class MyClient(discord.Client):
    embedDic = {}

    async def manga_check(self):
        await self.wait_until_ready()
        # grabs manga-updates channel
        ch = self.get_channel(778448461162086440)
        while not self.is_closed():
            print('Updating manga..')

            # get all updated manga from scraper then make and send embeds for them
            new_manga_list = scrape.new_ch_check()
            for new_manga in new_manga_list:
                manga_embed = discord.Embed(
                    description=new_manga['desc'],
                    colour=discord.Colour.red()
                )
                manga_embed.add_field(name=new_manga["ch"], value=f"[View Here]({new_manga['link']})")
                manga_embed.set_thumbnail(url=new_manga['thumbnail'])
                await ch.send(embed=manga_embed)
            print('Manga update finished!')
            # sleeps for 15 minutes then loops through again to try and catch new updates when they release
            await asyncio.sleep(1800)

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
            if message.content == '.game':
                await message.channel.send(embed=embeds.roles_game())
            # if message.content == '.manga_embed':
            #     await message.channel.send(embed=embeds.manga_embed())
            # if message.content == '.role_embed':
            #     await message.channel.send(embed=embeds.role_info())
            # if message.content == '.srvselect_embed':
            #     await message.channel.send(embed=embeds.server_select())
            # if message.content == '.world_embed':
            #     await message.channel.send(embed=embeds.world_level())
            # if message.content == '.info_embed':
            #     await message.channel.send(embed=embeds.role_info())
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
                            if str(user_uname) == "Yato#2558":
                                await message.channel.send('Stop abusing my boy Yato')
                                return
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
                            if user_uname == "Yato#2558":
                                await message.channel.send('Stop abusing my boy Yato')
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
            if message.content.startswith('.wish'):

                rarity_gif = 'https://c.tenor.com/Th97yaBk5kMAAAAd/genshin.gif'
                embed_colour = discord.Colour(0x82d9f9)

                simulation = False
                wish_num = False
                if message.content == '.wish multi':
                    wish_num = 10
                elif message.content == '.wish single':
                    wish_num = 1
                elif message.content == '.wish':
                    simulation = True
                    wish_num = 10
                elif len(message.content) > 5:
                    try:
                        wish_num = int(message.content[5:])
                        simulation = True
                    except ValueError:
                        await message.channel.send("Please enter a valid int!")
                if wish_num:
                    highest_rarity, _wish = wish.wish(message.author.id, wish_num, simulation)
                    if not highest_rarity:  # too broke to multi
                        await message.channel.send(f'Sorry {message.author.mention}, you do not have enough primos for this wish amount')
                        return
                    if highest_rarity == "5*":
                        if wish_num > 1:
                            rarity_gif = 'https://c.tenor.com/BPGMrc6S2YAAAAAd/genshin.gif'
                        else:
                            rarity_gif = 'https://c.tenor.com/A2bebZZ0ILAAAAAS/genshin.gif'
                        embed_colour = discord.Colour.gold()
                    elif highest_rarity == "4*":  # what do we do if highest rarity is 3*
                        if wish_num > 1:
                            rarity_gif = 'https://c.tenor.com/7pBGCuD2JHcAAAAd/genshin.gif'
                        else:
                            rarity_gif = 'https://c.tenor.com/-N667geZEPIAAAAd/genshin.gif'
                        embed_colour = discord.Colour.purple()

                    wishing_embed = discord.Embed(
                        description=f'{message.author.mention}, {wish_num} stars fall from the sky..',
                        colour=discord.Colour(0x82d9f9)
                    )
                    wishing_embed.set_image(url=rarity_gif)
                    wishing_embed.set_footer(text='Wishes')
                    await message.channel.send(embed=wishing_embed)

                    # simulating pack opening
                    time.sleep(4)

                    wish_embed = discord.Embed(
                        description='{}, below are your pulls!'.format(message.author.mention),
                        colour=embed_colour
                    )
                    for pulled in _wish:
                        wish_embed.add_field(name=chr(173), value=f'{pulled[1]} {pulled[0][1:]}', inline=False)
                    wish_embed.set_footer(text='Wishes')
                    await message.channel.send(embed=wish_embed)

            if message.content == '.daily':
                userid = message.author.id
                # cooldown = message.created_at
                # primos = wish.daily_primo(userid, cooldown)
                primos = wish.daily_primo(userid)
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
                    primo_check = wish.primo_transaction(userid, 0)
                    primos = str(primo_check)
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
                    pity = wish.get_pity(userid)
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
                wishes = wish.get_wishes(userid)
                if catalog == 'NONE' or wishes == 'NONE':
                    await message.channel.send(f'{message.author.mention}, you have not been registered yet. Use .daily to gain '
                                               'primos to wish and earn units!')
                elif catalog == {}:
                    await message.channel.send(f'{message.author.mention}, you currently have no units.')
                else:
                    catalog_embed = discord.Embed(
                        description=f"{message.author.mention}'s units earned over {wishes} total wishes",
                        colour=discord.Colour.green()
                    )
                    for unit in catalog:
                        catalog_embed.add_field(name=chr(173), value=unit)
                    catalog_embed.set_footer(text='Catalog')
                    await message.channel.send(embed=catalog_embed)

    # role add and remove based on reaction, you need to add the message ID with the others. may be able to improve
    # this process to look cleaner on this end but it works
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 809645998174634014:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            guest_role = discord.utils.get(member.guild.roles, name="Guest")

            if payload.user_id == self.user:
                return
            elif member is not None:
                if payload.emoji.name == "✅":
                    await member.add_roles(guest_role)
                    general = self.get_channel(749485433309757451)
                    general_welcome = 'hi everyone, please welcome {}!! feel free to grab roles from <#749485522447237211> or hang out as guest. ' \
                                      'whatever floats your boat <a:chika:773705341660692521>'.format(member.mention)
                    await general.send(general_welcome)
                    return

        # if message_id = roles_game embed in #self-roles
        if message_id == 807492809547317258:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            guest_role = discord.utils.get(member.guild.roles, name="Guest")

            if payload.user_id == self.user:
                return
            elif member is not None:
                if payload.emoji.name == "genshinimpact":
                    genshin_role = discord.utils.get(guild.roles, name="Travelers")
                    await member.add_roles(genshin_role)
                if guest_role in member.roles:
                    await member.remove_roles(guest_role)
        if message_id == 809678757643419668:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            guest_role = discord.utils.get(member.guild.roles, name="Guest")

            if payload.user_id == self.user:
                return
            elif member is not None:
                if payload.emoji.name == "Sins":
                    gc_role = discord.utils.get(guild.roles, name="Sins")
                    await member.add_roles(gc_role)
                if guest_role in member.roles:
                    await member.remove_roles(guest_role)
        if message_id == 809679346889261066:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            guest_role = discord.utils.get(member.guild.roles, name="Guest")

            if payload.user_id == self.user:
                return
            elif member is not None:
                if payload.emoji.name == "duel":
                    dl_role = discord.utils.get(guild.roles, name="Duel Links")
                    await member.add_roles(dl_role)
                if guest_role in member.roles:
                    await member.remove_roles(guest_role)
        if message_id == 809679855020146729:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            guest_role = discord.utils.get(member.guild.roles, name="Guest")

            if payload.user_id == self.user:
                return
            elif member is not None:
                if payload.emoji.name == "blueprotocol":
                    bp_role = discord.utils.get(guild.roles, name="Protocol")
                    await member.add_roles(bp_role)
                if guest_role in member.roles:
                    await member.remove_roles(guest_role)
        # if message_id = any of the other CURRENT embeds in #self-roles
        if message_id == 807493162527621140 or 807493735344373771 or 807493770898702346 or 807493802427809792:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if payload.user_id == 749451840281641000:
                    return
                elif member is not None:
                    await member.add_roles(role)
        if message_id == 807493162527621140 or 807493923164520489 or 809674296053596200:
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
                if payload.emoji.name == "💹":
                    stonks_role = discord.utils.get(guild.roles, name='Stonks')
                    await member.add_roles(stonks_role)

    # the opposite of the reaction_remove command, I have it set up to give Guest role back if they were to not have
    # any active reactions to the roles_game embed but not to do so if they're removing react from any of the other
    # embeds
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        guest_role = discord.utils.get(member.guild.roles, name="Guest")
        game_roles = discord.utils.get(member.guild.roles, name='Sins' or 'Travelers' or 'Protocol')
        if message_id == 807492809547317258:
            if payload.emoji.name == "genshinimpact":
                genshin_role = discord.utils.get(guild.roles, name="Travelers")
                await member.remove_roles(genshin_role)
                if game_roles not in member.roles:
                    await member.add_roles(guest_role)
        if message_id == 809678757643419668:
            if payload.emoji.name == "Sins":
                gc_role = discord.utils.get(guild.roles, name='Sins')
                await member.remove_roles(gc_role)
                if game_roles not in member.roles:
                    await member.add_roles(guest_role)
        if message_id == 809679855020146729:
            if payload.emoji.name == "blueprotocol":
                bp_role = discord.utils.get(guild.roles, name='Protocol')
                await member.remove_roles(bp_role)
                if game_roles not in member.roles:
                    await member.add_roles(guest_role)
        if message_id == 809679346889261066:
            if payload.emoji.name == "duel":
                duel_role = discord.utils.get(guild.roles, name='Duel Links')
                await member.remove_roles(duel_role)
        # if message_id = any of the other CURRENT embeds in #self-roles
        if message_id == 807493162527621140 or 807493735344373771 or 807493770898702346 or 807493802427809792:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if message_id == 807493162527621140 or 807493923164520489 or 809674296053596200:
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
                if payload.emoji.name == "📚":
                    mangafiends_role = discord.utils.get(guild.roles, name="manga fiends")
                    await member.remove_roles(mangafiends_role)
                if payload.emoji.name == "💹":
                    stonks_role = discord.utils.get(guild.roles, name='Stonks')
                    await member.remove_roles(stonks_role)

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

intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run('')
