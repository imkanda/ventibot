import discord


class MyClient(discord.Client):

    # embeds #

    async def welcome_message(self, channel, member):
        welcome_message = discord.Embed(
            description='Welcome to The Hole, {}. \n Make sure to check out <#749485522447237211> for obtaining roles.'.format(
                member.mention),
            colour=discord.Colour.blue()
        )
        welcome_message.set_footer(text='Enjoy your stay')
        welcome_message.set_image(
            url='https://cdn.discordapp.com/attachments/772150088599863296/772174651027226654/tenor.gif')
        # welcome_message.set_thumbnail(url='')
        welcome_message.set_author(name='Venti',
                                   icon_url='https://cdn.discordapp.com/attachments/772150088599863296'
                                            '/772174650234372146/41.png')
        # welcome_message.add_field(name='Field Name', value=member.mention, inline=False)
        # welcome_message.add_field(name='Field Name', value='Field Value', inline=True)
        # welcome_message.add_field(name='Field Name', value='Field Value', inline=True)
        await channel.send(embed=welcome_message)

    async def announcement_wip(self, channel):
        announcement_wip = discord.Embed(
            description='WIP Announcement',
            colour=discord.Colour.green()
        )
        await channel.send(embed=announcement_wip)

    async def roles_game(self, message):
        roles_game = discord.Embed(
            description="React to gain the below selections!",
            colour=discord.Colour.red()
        )
        roles_game.set_footer(text="Game Roles")
        # roles_game.set_image(url="") roles_game.set_thumbnail(url='') roles_game.set_author(name='Venti',
        # icon_url='https://cdn.discordapp.com/attachments/772150088599863296/772174650234372146/41.png')
        roles_game.add_field(name='Genshin Impact',
                             value='React with <:Travelers:773690222118174750> for Genshin Impact', inline=True)
        roles_game.add_field(name='7DS: Grand Cross', value='React with <:Sins:773689968719036496> for Grand Cross',
                             inline=True)
        # roles_game.add_field(name='Field Name', value='Field Value', inline=True)
        await message.channel.send(embed=roles_game)

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

    async def rules_info(self, message):
        rules_info = discord.Embed(
            description="Server rules below",
            colour=discord.Colour.red()
        )
        rules_info.set_footer(text='Rules & Info')

    # below command can be edited to call whatever embed you create via a command to post in chat
    async def on_message(self, message):
        member = message.author
        if message.content == '!roles':
            print(member.roles)

    # role add and remove based on reaction, you need to add the message ID with the others. may be able to improve
    # this process to look cleaner on this end but it works
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id

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

    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
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

    # sends welcome_message embed in welcome text channel whenever someone joins #

    async def on_member_join(self, member):
        ch = self.get_channel(749438385042751552)
        await self.welcome_message(ch, member)
        guest_role = discord.utils.get(member.guild.roles, name="Guest")
        await member.add_roles(guest_role)
        return
