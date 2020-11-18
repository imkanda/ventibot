import discord
import random
from mangascrape import Scrape
import asyncio
scrape = Scrape()


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

    async def manga_check(self):
        await self.wait_until_ready()
        # grabs manga-updates channel
        ch = self.get_channel(778448461162086440)
        while not self.is_closed():
            print('Updating manga..')
            sl_string = scrape.sl_update()
            # runs update function, if it comes back with an actual return it will send it to the channel
            if sl_string:
                await ch.send(sl_string)
            csm_string = scrape.csm_update()
            # runs update function, if it comes back with an actual return it will send it to the channel
            if csm_string:
                await ch.send(csm_string)
            snk_string = scrape.snk_update()
            # runs update function, if it comes back with an actual return it will send it to the channel
            if snk_string:
                await ch.send(snk_string)
            jjk_string = scrape.jjk_update()
            # runs update function, if it comes back with an actual return it will send it to the channel
            if jjk_string:
                await ch.send(jjk_string)
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
        # on message it will grab the list created from get_list function and randomly mention someone in the list
        if message.content.startswith('!winner'):
            for role in message.author.roles:
                if 'Fatui Harbringers' or "Makima's Dog" == role.name:
                    giveaway_winner = random.choice(self.get_list(message))
                    winner_message = 'Congrats {}, you have won the giveaway!'.format(giveaway_winner.name)
                    await message.channel.send(winner_message)
        # function can be used to call embeds or something else, just here in case I ever need it
        if message.content == '.manga':
            await message.channel.send(scrape.snk_chapter_check())

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

    # bot login confirmation #
    async def on_ready(self):
        print('Logged on as', self.user)

    # functions to run when bot logs in #
    async def on_connect(self):
        # once bot connects to discord it will begin the manga check loop
        await self.loop.create_task(self.manga_check())

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