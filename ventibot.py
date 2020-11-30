import discord
import random
import asyncio
from mangascrape import Scrape
from ch_guides import Guides
from discord import Streaming


scrape = Scrape()
guides = Guides()


class MyClient(discord.Client):

    # embeds #

    # welcome message embed, inputs member's name and the channel ID for #self-roles in the message
    async def welcome_message(self, channel, member):
        welcome_message = discord.Embed(
            description='Welcome to The Hole, {}. \n Make sure to check out <#749485522447237211> for obtaining roles.'.format(
                member.mention),
            colour=discord.Colour.blue()
        )
        welcome_message.set_footer(text='Enjoy your stay')
        welcome_message.set_image(
            url='https://cdn.discordapp.com/attachments/772150088599863296/772174651027226654/tenor.gif')
        welcome_message.set_author(name='Venti',
                                   icon_url='https://cdn.discordapp.com/attachments/772150088599863296'
                                            '/772174650234372146/41.png')
        await channel.send(embed=welcome_message)

    # embed inside #self-roles for choosing game role, either Travelers for Genshin or Sins for 7DS: Grand Cross
    async def roles_game(self, message):
        roles_game = discord.Embed(
            description="React to gain the below selections!",
            colour=discord.Colour.red()
        )
        roles_game.set_footer(text="Game Roles")
        roles_game.add_field(name='Genshin Impact',
                             value='React with <:Travelers:773690222118174750> for Genshin Impact', inline=True)
        roles_game.add_field(name='7DS: Grand Cross', value='React with <:Sins:773689968719036496> for Grand Cross',
                             inline=True)
        await message.channel.send(embed=roles_game)

    # embed inside #self-roles for choosing genshin server
    async def server_select(self, message):
        server_select = discord.Embed(
            description="React to display your Genshin server/region!",
            colour=discord.Colour.red()
        )
        server_select.set_footer(text="Server Select")
        server_select.add_field(name='NA', value='React with 🇺🇸 for NA', inline=False)
        server_select.add_field(name='EU', value='React with 🇪🇺 for EU', inline=True)
        server_select.add_field(name='AS', value='React with 🇯🇵 for AS', inline=False)
        server_select.add_field(name='SAR', value='React with 🇭🇰 for SAR', inline=True)
        await message.channel.send(embed=server_select)

    async def role_info(self, message):
        role_info = discord.Embed(
            description="Below is some info on roles here in The Hole",
            colour=discord.Colour.red()
        )
        role_info.set_thumbnail(url=
            "https://cdn.discordapp.com/attachments/772150088599863296/778844565255094312/954bfd00b5ef97c3444b5494541eded8.png")
        role_info.set_footer(text="Server Info")
        role_info.add_field(name="Makima's Dog", value="Kanda's role <:pepeboss:773671306893197323>",
                            inline=False)
        role_info.add_field(name='Fatui Harbingers', value='Server moderators', inline=False)
        role_info.add_field(name='Knights of Favonius', value='Top 5 active in the server ([Leaderboard]'
                                                              '(https://mee6.xyz/leaderboard/749438385042751549))',
                            inline=False)
        role_info.add_field(name='Travelers', value='Genshin Impact players', inline=False)
        role_info.add_field(name='Sins', value='SDS: Grand Cross players', inline=False)
        role_info.add_field(name='Manga Fiends', value='People who want updated when new manga chapters come out in '
                                                       '<#778448461162086440>', inline=False)
        role_info.add_field(name='Server Booster', value='Currently boosting The Hole using their Discord Nitro! '
                                                         '<:kannalove:778843977838624788>', inline=False)
        role_info.add_field(name='Guest/Friends', value="Users who don't play games or haven't visited <#749485522447237211> "
                                                        "yet!", inline=False)
        role_info.add_field(name='Bots', value='Friendly Discord bots', inline=False)
        await message.channel.send(embed=role_info)

    # embed inside #self-roles for choosing world level, was requested by the server to better see who they can actually
    # co-op with for relevant rewards or just to help out
    async def world_level(self, message):
        world_level = discord.Embed(
            description="React to assign your current world level, can be changed at any time!"
        )
        world_level.set_footer(text="World Level Assign")
        world_level.add_field(name=chr(173), value='React with <:WL0:773789639127465986> for World Level 0',
                              inline=True)
        world_level.add_field(name=chr(173), value='AR Ranks 1-19', inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL1:773789389742276620> for World Level 1',
                              inline=True)
        world_level.add_field(name=chr(173), value='AR Ranks 20-24', inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL2:773789389594558477> for World Level 2',
                              inline=True)
        world_level.add_field(name=chr(173), value='AR Ranks 25-29', inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL3:773789389968375808> for World Level 3',
                              inline=True)
        world_level.add_field(name=chr(173), value='AR Ranks 30-34', inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL4:773789389934428190> for World Level 4',
                              inline=True)
        world_level.add_field(name=chr(173), value='AR Ranks 35-39', inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL5:773789390001668106> for World Level 5',
                              inline=True)
        world_level.add_field(name=chr(173), value='AR Ranks 40-44', inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL6:773789390010449941> for World Level 6',
                              inline=True)
        world_level.add_field(name=chr(173), value='AR Ranks 45-49', inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL7:773789562329497601> for World Level 7',
                              inline=True)
        world_level.add_field(name=chr(173), value='AR Ranks 50+', inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        await message.channel.send(embed=world_level)

    async def on_member_update(self, before, after):

        # grabs announcements channel
        ch = self.get_channel(749485617276125286)
        # grabs user
        kanda = self.get_user(629377169663066153)
        twitch_url = 'https://www.twitch.tv/ohkanda'

        if discord.member is kanda:
            # if update is streaming
            if isinstance(after.activity, Streaming):
                # sends message to announcements channel with stream link
                await ch.send(f"{before.mention} is streaming on {self.activity.platorm}: {self.activity.name}.\n"
                              f"Join here: {self.activity.url}")
                # changes presence to watching stream
                await self.change_presence(activity=discord.Streaming(name="Kanda's Twitch stream", url=twitch_url))
            # if update changes and was previously streaming
            elif isinstance(before.activity, Streaming):
                # changes presence back to original
                await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=
                                                                     'a ballad'))
                for message in ch.history:
                    if "streaming" in message.content:
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
            # function can be used to call embeds or something else, just here in case I ever need it
            if message.content == '.amber':
                await message.channel.send(embed=guides.amber())
            if message.content == '.barbara':
                await message.channel.send(embed=guides.barbara())
            if message.content == '.beidou':
                await message.channel.send(embed=guides.beidou())
            if message.content == '.bennett':
                await message.channel.send(embed=guides.bennett())
            if message.content == '.chongyun':
                await message.channel.send(embed=guides.chongyun())
            if message.content == '.diluc':
                await message.channel.send(embed=guides.diluc())
            if message.content == '.diona':
                await message.channel.send(embed=guides.diona())
            if message.content == '.fischl':
                await message.channel.send(embed=guides.fischl())
            if message.content == '.jean':
                await message.channel.send(embed=guides.jean())
            if message.content == '.kaeya':
                await message.channel.send(embed=guides.kaeya())
            if message.content == '.keqing':
                await message.channel.send(embed=guides.keqing())
            if message.content == '.klee':
                await message.channel.send(embed=guides.klee())
            if message.content == '.lisa':
                await message.channel.send(embed=guides.lisa())
            if message.content == '.mona':
                await message.channel.send(embed=guides.mona())
            if message.content == '.ningguang':
                await message.channel.send(embed=guides.ningguang())
            if message.content == '.noelle':
                await message.channel.send(embed=guides.noelle())
            if message.content == '.qiqi':
                await message.channel.send(embed=guides.qiqi())
            if message.content == '.razor':
                await message.channel.send(embed=guides.razor())
            if message.content == '.sucrose':
                await message.channel.send(embed=guides.sucrose())
            if message.content == '.tartaglia':
                await message.channel.send(embed=guides.tartaglia())
            if message.content == '.anemo':
                await message.channel.send(embed=guides.anemo())
            if message.content == '.geo':
                await message.channel.send(embed=guides.geo())
            if message.content == '.venti':
                await message.channel.send(embed=guides.venti())
            if message.content == '.xiangling':
                await message.channel.send(embed=guides.xiangling())
            if message.content == '.xingqiu':
                await message.channel.send(embed=guides.xingqiu())
            if message.content == '.xinyan':
                await message.channel.send("Coming soon! Stay tuned.")
            if message.content == '.zhongli':
                await message.channel.send("Coming soon! Stay tuned.")

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
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=
        'a ballad'))


    # sends welcome_message embed in welcome text channel whenever someone joins and also gives them Guest role so
    # no one in the server will be role-less
    async def on_member_join(self, member):
        ch = self.get_channel(749438385042751552)
        await self.welcome_message(ch, member)
        guest_role = discord.utils.get(member.guild.roles, name="Guest")
        await member.add_roles(guest_role)
        return


client = MyClient()
client.run('')
