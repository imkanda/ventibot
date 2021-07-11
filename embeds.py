import discord


class Embeds:

    # embeds #

    # welcome message embed, inputs member's name and the channel ID for #self-roles in the message
    def welcome_message(self, channel, member):
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
        return welcome_message

    # embed inside #self-roles for choosing game role, either Travelers for Genshin or Sins for 7DS: Grand Cross
    def roles_game(self):
        roles_game = discord.Embed(
            description="React to gain access to Blue Protocol chat channels!",
            colour=discord.Colour.red()
        )
        roles_game.set_footer(text="Game Roles")
        roles_game.add_field(name='Blue Protocol',
                             value='React with <:blueprotocol:809677319937196064> for Blue Protocol role', inline=True)
        return roles_game

    # embed inside #self-roles for choosing genshin server
    def server_select(self):
        server_select = discord.Embed(
            description="React to display your Genshin server/region!",
            colour=discord.Colour.red()
        )
        server_select.set_footer(text="Server Select")
        server_select.add_field(name='NA', value='React with 🇺🇸 for NA', inline=False)
        server_select.add_field(name='EU', value='React with 🇪🇺 for EU', inline=True)
        server_select.add_field(name='AS', value='React with 🇯🇵 for AS', inline=False)
        server_select.add_field(name='SAR', value='React with 🇭🇰 for SAR', inline=True)
        return server_select

    # embed inside #rules-and-info for info on roles in the server
    def role_info(self):
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
        role_info.add_field(name='Guest/Friends',
                            value="Users who don't play games or haven't visited <#749485522447237211> "
                                  "yet!", inline=False)
        role_info.add_field(name='Bots', value='Friendly Discord bots', inline=False)
        return role_info

    # embed inside #self-roles for choosing world level, was requested by the server to better see who they can actually
    # co-op with for relevant rewards or just to help out
    def world_level(self):
        world_level = discord.Embed(
            description="React to assign your current world level, can be changed at any time!",
            colour=discord.Colour.red()
        )
        world_level.set_footer(text="World Level Assign")
        world_level.add_field(name=chr(173), value='React with <:WL0:773789639127465986> for World Level 0 (AR 1-19)',
                              inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL1:773789389742276620> for World Level 1 (AR 20-24)',
                              inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL2:773789389594558477> for World Level 2 (AR 25-29)',
                              inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL3:773789389968375808> for World Level 3 (AR 30-34)',
                              inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL4:773789389934428190> for World Level 4 (AR 35-39)',
                              inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL5:773789390001668106> for World Level 5 (AR 40-44)',
                              inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL6:773789390010449941> for World Level 6 (AR 45-49)',
                              inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL7:773789562329497601> for World Level 7 (AR 50-54)',
                              inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value=chr(173), inline=True)
        world_level.add_field(name=chr(173), value='React with <:WL8:807465009432625174> for World Level 8 (AR 55+)',
                              inline=True)
        return world_level

    # .help embed
    def help_embed(self):
        help_embed = discord.Embed(
            description='Venti bot commands',
            colour=discord.Colour.green()
        )
        help_embed.set_footer(text='Commands')
        help_embed.add_field(name='Avatar Scraper', value='Type .avatar to post your own avatar, or mention a person '
                                                          'to post their avatar in chat', inline=False)
        help_embed.add_field(name='Daily Login', value='Type .daily to earn your daily primogems. Usable once every '
                                                       '24 hours, date and time is tracked in UTC', inline=False)
        help_embed.add_field(name='Wish (Casual)', value="Type .wish in <#784964222899453972> to do a multi pull "
                                                         "for fun, no catalog tracking but it also doesn't cost "
                                                         "any primogems", inline=False)
        help_embed.add_field(name='Wish (Multi/Tracking)', value='Type .wish multi in <#787520738118598656> to do a '
                                                                 'multi pull, costs 1600 primogems and will add any '
                                                                 '4 and 5 star units you get to your catalog',
                             inline=False)
        help_embed.add_field(name='Wish (Single/Tracking)', value='Type .wish single in <#787520738118598656> to do a '
                                                                  'single pull, costs 160 primogems and will add any '
                                                                  '4 and 5 star units you get to your catalog',
                             inline=False)
        help_embed.add_field(name='Primogems Check', value='Type .primos in <#787520738118598656> to check how many '
                                                           'primogems you currently have', inline=False)
        help_embed.add_field(name='Pity Check', value='Type .pity in <#787520738118598656> to check your current pity '
                                                      'progress towards your next five star or four star unit',
                             inline=False)
        help_embed.add_field(name='Catalog', value='Type .catalog in any channel to post your current catalog of '
                                                   'units you have pulled in <#787520738118598656>')
        help_embed.add_field(name=chr(173), value='Will update this embed as more commands are added, feel free to '
                                                  'suggest '
                                                  'anything you think of in <#749485642517446717>!', inline=False)
        return help_embed

    # Manga Updates role embed
    def manga_embed(self):
        manga_embed = discord.Embed(
            description='React to get manga chapter updates!',
            colour=discord.Colour.red()
        )
        manga_embed.set_footer(text='Manga Updates')
        manga_embed.add_field(name=chr(173), value='React with 📚 to access \n<#778448461162086440>')
        manga_embed.add_field(name='Currently Monitoring:', value='• Attack on Titan\n'
                                                                  '• Chainsaw Man\n'
                                                                  '• Solo Leveling\n'
                                                                  '• Jujutsu Kaisen\n'
                                                                  '• Berserk\n'
                                                                  '• Black Clover\n'
                                                                  '• Tower of God\n'
                                                                  '• One Piece')
        return manga_embed
