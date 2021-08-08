import csv
import json
import random
import ast
import pandas as pd
from datetime import datetime as dt


class Wish:

    def __init__(self):
        self.pullables = {'4*': [('cAmber', '<:amber:779443715713400883>'),
                            ('cBarbara', '<:barbara:779443715806199889>'),
                            ('cBeidou', '<:beidou:779443715910795324>'),
                            ('cBennett', '<:bennett:779443715293970503>'),
                            ('cChongyun', '<:chongyun:779443715738566657>'),
                            ('cDiona', '<:diona:779443715709337681>'),
                            ('cFischl', '<:fischl:779443715696623626>'),
                            ('cKaeya', '<:kaeya:779443715688235068>'),
                            ('cLisa', '<:lisa:779443715885367336>'),
                           ('cNingguang', '<:ningguang:779443715449946144>'),
                            ('cNoelle', '<:noelle:779443715709337630>'),
                            ('cRazor', '<:razorgenshin:779443715768844318>'),
                            ('cSucrose', '<:sucrose:779443715542351903>'),
                            ('cXiangling', '<:xiangling:779443715625320478>'),
                            ('cXingqiu', '<:xingqiu:779443715511943218>'),
                            ('cXinyan', '<:xinyan:779443715508535326>')],
                     '5*': [('cDiluc', '<:diluc:779443715882221578>'),
                            ('cJean', '<:jean:779443715675521024>'),
                            ('cKeqing', '<:keqing:779443715717857320>'),
                            ('cKlee', '<:klee:779443715768057976>'),
                            ('cMona', '<:mona:779443715395026955>'),
                            ('cQiqi', '<:qiqi:779443715727032330>'),
                            ('cTartaglia', '<:childe:779443715155820595>'),
                           ('cVenti', '<:venti:779443715382050858>'),
                            ('cXiao', '<:xiao:779443715437232128>'),
                            ('cZhongli', '<:zhongli:779443715809738763>')],
                     '3*': [('wEbony Bow', '<:ebony_bow:784915675932131388>'),
                            ('wMessenger', '<:messenger:784915675847589959>'),
                            ('wRaven Bow', '<:raven_bow:784915675457650749>'),
                            ('wRecurve Bow', '<:recurve_bow:784915675662516264>'),
                            ('wSharpshooters Oath', '<:sharpshooters_oath:784915675277164565>'),
                            ('wSlingshot', '<:slingshot:784915676015886376>'),
                            ('wAmber Catalyst', '<:amber_catalyst:784915674904395837>'),
                            ('wEmerald Orb', '<:emerald_orb:784915675633811467>'),
                            ('wMagic Guide', '<:magic_guide:784915675553464342>'),
                            ('wOtherwordly Story', '<:otherworldly_story:784915675331821569>'),
                            ('wThrilling Tales of Dragon Slayers', '<:thrilling_tales:784915675675361291>'),
                            ('wTwin Nephrite', '<:twin_nephrite:784915675835531305>'),
                            ('wBloodtainted Greatsword', '<:bloodtainted_greatsword:784915674924711956>'),
                            ('wDebate Club', '<:debate_club:784915675814035546>'),
                            ('wFerrous Shadow', '<:ferrous_shadow:784915675961098260>'),
                            ('wQuartz', '<:quartz:784915675641544704>'),
                            ('wSkyrider Greatsword', '<:skyrider_greatsword:784915675734343741>'),
                            ('wWhite Iron Greatsword', '<:white_iron_greatsword:784915675448606751>'),
                            ('wBlack Tassel', '<:black_tassel:784915674912260176>'),
                            ('wHalberd', '<:halberd:784915675990327296>'),
                            ('wWhite Tassel', '<:white_tassel:784915675532754964>'),
                            ('wCool Steel', '<:cool_steel:784915675042283522>'),
                            ('wDark Iron Greatsword', '<:dark_iron_sword:784915675838676997>'),
                            ('wFillet Blade', '<:fillet_blade:784915675336540171>'),
                            ('wHarbringer of Dawn', '<:harbringer_of_dawn:784915675629879336>'),
                            ('wSkyrider Sword', '<:skyrider_sword:784915675860303882>'),
                            ('wTravelers Handy Sword', '<:traverlers_handy_sword:784915675378352179>')]}
        # {rarity: [(character/wep, emoji)]}

        # rarities for wish functions
        self.rarity_pull = ['5*', '4*', '3*']

    def wish(self, userid, pulls:int = 10, simulation:bool = True):
        # if a pull is a simulation, it does not require a real userid or primogems and does not affect a players pity
        fourstar_pity = 1
        fivestar_pity = 1
        if not simulation:
            fourstar_pity, fivestar_pity = self.get_pity(userid)
            if not self.primo_transaction(userid, pulls*160):
                return False
        highest_rarity = None
        wish_pulls = []

        for pull in range (0,pulls):
            if fivestar_pity == 90:
                rarity = '5*'
            elif fourstar_pity >= 10:
                rarity = '4*'
            else:
                if 76 <= fivestar_pity <= 89:
                    pity = 32
                elif 46 <= fivestar_pity <= 75:
                    pity = 1.2
                else:
                    pity = 0.6
                rarity = random.choices(self.rarity_pull, cum_weights=(pity, 5.1, 94.3))[0]
            if rarity == '5*':
                highest_rarity = "5*"
                fivestar_pity = 1
                fourstar_pity += 1
            elif rarity == '4*':
                if highest_rarity != "5*":
                    highest_rarity = "4*"
                fivestar_pity += 1
                fourstar_pity = 1
            else:
                if not highest_rarity:
                    highest_rarity = "3*"
                fivestar_pity += 1
                fourstar_pity += 1
            pulled = random.choice(self.pullables[rarity])
            wish_pulls.append(pulled)
            if not simulation:
                self.save_pity(userid, [fourstar_pity, fivestar_pity])
                self.add_item(pulled)
        return highest_rarity, wish_pulls

    def get_all_data(self) -> dict:
        with open("wishes.json", "r") as wishes_file:
            wishes_dict = json.load(wishes_file)
        return wishes_dict

    def get_user_data(self, userid: int) -> dict:
        wishes_dict = self.get_all_data()
        if userid not in wishes_dict:
            return {}
        return wishes_dict[userid]

    def add_item(self, userid: int, item: str):
        units = self.get_units(userid)
        if item[0] == "w":  # item is a weapon, add it to inven
            units.append(item)
        elif item[0] == "c":  # item is a character, check if already owned+constellation level then add
            clevel = self.get_character_constellation(userid, item[1:])
            if clevel == -1:
                units.append(item)
            elif clevel in range(0, 5):
                cindex = units.index(item[1:])
                del units[cindex]
                units.append(f"{item[1:]} C{clevel+1}")
        self.save_units(units)

    def get_character_constellation(self, userid: int, character: str):
        units = self.get_user_data(userid)["units"]
        clevel_int = -1
        for unit in units:
            if unit == character:
                clevel_int = 0
            elif unit[0:len(character)] == character:
                constellation_level = unit[-2:]
                if constellation_level[0] == 'C':
                    try:
                        clevel_int = int(constellation_level[1])
                    except ValueError:
                        pass
        return clevel_int

    def save_user_data(self, userid: int, data=None):
        if data is None:
            data = {"four_pity": 0, "five_pity": 0, "wishes":0, "primos": 0, "cooldown": "", "units": []}
        wishes_dict = self.get_all_data()
        wishes_dict[userid] = data
        with open("wishes.json", "w") as wishes_file:
            json.dump(wishes_dict, wishes_file, indent=2)

    def get_units(self, userid: int) -> list:
        data = self.get_user_data(userid)
        return data["units"]

    def save_units(self, userid: int, units: list):
        data = self.get_user_data(userid)
        data["units"] = units
        self.save_user_data(userid, data)

    def get_pity(self, userid: int) -> tuple[int, int]:
        data = self.get_user_data(userid)
        return data["four_pity"], data["five_pity"]

    def save_pity(self, userid: int, pity: list[int, int]):  # userid, [4pity, 5pity]
        data = self.get_user_data(userid)
        data["four_pity"] = pity[0]
        data["five_pity"] = pity[1]
        self.save_user_data(userid, data)

    def primo_transaction(self, userid: int, num: int):
        user_data = self.get_user_data(userid)
        if num > 0:  # add primos
            user_data["primos"] += num
            self.save_user_data(userid, user_data)
        elif num < 0:  # use primos
            primos = user_data["primos"]
            if (primos + num) >= 0:
                user_data["primos"] = primos + num
                self.save_user_data(userid, user_data)
            else:
                return False
        return True

    # single wish function with pity affecting weight
    def wishsingle_pity(self, userid):
        base_pity = 0.6
        soft_pity = 1.2
        hard_pity = 32
        fourstar_pity, fivestar_pity = self.pity_check(userid)

        # 5* unit guaranteed at 90 pulls
        if fivestar_pity == 90:
            rarity = ['5 star']
        # hard pity weight between 76 and 89 pulls for 5*
        elif 76 <= fivestar_pity <= 89:
            # 4* unit guaranteed every 10 pulls
            if fourstar_pity < 10:
                rarity = random.choices(self.rarity_pull, cum_weights=(hard_pity, 5.1, 94.3), k=1)
            else:
                rarity = ['4 star']
        # soft pity weight between 46 and 75 pulls for 5*
        elif 46 <= fivestar_pity <= 75:
            # 4* unit guaranteed every 10 pulls
            if fourstar_pity < 10:
                rarity = random.choices(self.rarity_pull, cum_weights=(soft_pity, 5.1, 94.3), k=1)
            else:
                rarity = ['4 star']
        # base pity weight under 46 pulls
        else:
            # 4* unit guaranteed every 10 pulls
            if fourstar_pity < 10:
                rarity = random.choices(self.rarity_pull, cum_weights=(base_pity, 5.1, 94.3), k=1)
            else:
                rarity = ['4 star']

        # grabs from parallel arrays if rarity is 3*
        if rarity[0] == '3 star':
            pull = []
            pull_emoji = []
            wish_rarity = []
            # random pull from list, grabs index
            index = random.choice(range(len(self.threestars_wep)))
            # uses index to grab unit name and emote from parallel arrays
            pull.append(self.threestars_wep[index])
            pull_emoji.append(self.wep_emote[index])
            # returns rarity for embed purposes
            wish_rarity.append('3')
            return pull_emoji, pull, wish_rarity

        # grabs from parallel arrays if rarity is 4*
        if rarity[0] == '4 star':
            pull = []
            pull_emoji = []
            wish_rarity = []
            # random pull from list, grabs index
            index = random.choice(range(len(self.fourstars_units)))
            # uses index to grab unit name and emote from parallel arrays
            pull.append(self.fourstars_units[index])
            pull_emoji.append(self.fourstar_emotes[index])
            # returns rarity for embed purposes
            wish_rarity.append('4')
            return pull_emoji, pull, wish_rarity

        # grabs from parallel arrays if rarity is 5*
        if rarity[0] == '5 star':
            pull = []
            pull_emoji = []
            wish_rarity = []
            # random pull from list, grabs index
            index = random.choice(range(len(self.fivestars_units)))
            # uses index to grab unit name and emote from parallel arrays
            pull.append(self.fivestars_units[index])
            pull_emoji.append(self.fivestar_emotes[index])
            # returns rarity for embed purposes
            wish_rarity.append('5')
            return pull_emoji, pull, wish_rarity

    # multi wish function with pity affecting weight
    def wishmulti_pity(self, userid, index):
        wish_result = []
        wish_result_emoji = []
        wish_rarity = []
        pull_rarity = []

        base_pity = 0.6
        soft_pity = 1.2
        hard_pity = 32
        # grabs current pity amount
        current_pulls = self.pity_check(userid)
        # adds +1 for each pity to account for the first pull
        fourstar_pity = int(current_pulls[0]) + 1
        fivestar_pity = int(current_pulls[1]) + 1

        # same as wishsingle, just does it 10 times
        for rarity in range(10):
            # 5* unit guaranteed at 90 pulls
            if fivestar_pity == 90:
                # resets pity if 5* is pulled
                pull_rarity.append('5 star')
                fivestar_pity = 0
                fourstar_pity = fourstar_pity + 1
            # hard pity weight between 76 and 89 pulls for 5*
            elif 76 <= fivestar_pity <= 89:
                # 4* unit guaranteed every 10 pulls
                if fourstar_pity < 10:
                    rarity = random.choices(self.rarity_pull, cum_weights=(hard_pity, 5.1, 94.3), k=1)
                    if rarity == '5 star':
                        # resets pity if 5* is pulled
                        pull_rarity.append('5 star')
                        fivestar_pity = 0
                        fourstar_pity = fourstar_pity + 1
                    elif rarity == '4 star':
                        # resets pity if 4* is pulled
                        pull_rarity.append('4 star')
                        fivestar_pity = fivestar_pity + 1
                        fourstar_pity = 0
                    else:
                        # adds to both pitys if 3* is pulled
                        pull_rarity.append('3 star')
                        fivestar_pity = fivestar_pity + 1
                        fourstar_pity = fourstar_pity + 1
                else:
                    pull_rarity.append('4 star')
                    fivestar_pity = fivestar_pity + 1
                    fourstar_pity = 0
            # soft pity weight between 46 and 75 pulls for 5*
            elif 46 <= fivestar_pity <= 75:
                # 4* unit guaranteed every 10 pulls
                if fourstar_pity < 10:
                    rarity = random.choices(self.rarity_pull, cum_weights=(soft_pity, 5.1, 94.3), k=1)
                    if rarity == '5 star':
                        # resets pity if 5* is pulled
                        pull_rarity.append('5 star')
                        fivestar_pity = 0
                        fourstar_pity = fourstar_pity + 1
                    elif rarity == '4 star':
                        # resets pity if 4* is pulled
                        pull_rarity.append('4 star')
                        fivestar_pity = fivestar_pity + 1
                        fourstar_pity = 0
                    else:
                        pull_rarity.append('3 star')
                        # adds to both pitys if 3* is pulled
                        fivestar_pity = fivestar_pity + 1
                        fourstar_pity = fourstar_pity + 1
                else:
                    pull_rarity.append('4 star')
                    fivestar_pity = fivestar_pity + 1
                    fourstar_pity = 0
            # base pity weight under 46 pulls
            else:
                # 4* unit guaranteed every 10 pulls
                if fourstar_pity < 10:
                    rarity = random.choices(self.rarity_pull, cum_weights=(base_pity, 5.1, 94.3), k=1)
                    if rarity == '5 star':
                        pull_rarity.append('5 star')
                        # resets pity if 5* is pulled
                        fivestar_pity = 0
                        fourstar_pity = fourstar_pity + 1
                    elif rarity == '4 star':
                        # resets pity if 4* is pulled
                        pull_rarity.append('4 star')
                        fivestar_pity = fivestar_pity + 1
                        fourstar_pity = 0
                    else:
                        pull_rarity.append('3 star')
                        # adds to both pitys if 3* is pulled
                        fivestar_pity = fivestar_pity + 1
                        fourstar_pity = fourstar_pity + 1
                else:
                    pull_rarity.append('4 star')
                    fivestar_pity = fivestar_pity + 1
                    fourstar_pity = 0

        # writes new pity values back to csv file
        contents = pd.read_csv('server_wishes.csv', dtype=str)
        contents.at[index, 'five_pity'] = fivestar_pity
        contents.at[index, 'four_pity'] = fourstar_pity
        contents.to_csv('server_wishes.csv', index=False)

        # loops through pulled rarities, grabs from parallel arrays based on rarity
        for i in pull_rarity:
            if i == '3 star':
                # random pull from 3* list, grabs index
                index = random.choice(range(len(self.threestars_wep)))
                # uses index to grab unit name and emote from parallel arrays
                wish_result_emoji.append(self.wep_emote[index])
                wish_result.append(self.threestars_wep[index])
            if i == '4 star':
                # random pull from 4* list, grabs index
                index = random.choice(range(len(self.fourstars_units)))
                # uses index to grab unit name and emote from parallel arrays
                wish_result_emoji.append(self.fourstar_emotes[index])
                wish_result.append(self.fourstars_units[index])
            if i == '5 star':
                # random pull from 5* list, grabs index
                index = random.choice(range(len(self.fivestars_units)))
                wish_result_emoji.append(self.fivestar_emotes[index])
                # uses index to grab unit name and emote from parallel arrays
                wish_result.append(self.fivestars_units[index])
                wish_rarity.append('5')
        return wish_result_emoji, wish_result, wish_rarity

    # multi wish function with no pity or tracking
    def wishmulti_nonpity(self):
        wish_result = []
        wish_result_emoji = []
        wish_rarity = []
        # grabs index of random 4* unit
        guarantee_index = random.choice(range(len(self.fourstars_units)))
        # appends one 4* result automatically, guaranteed one 4* per 10 pull
        wish_result.append(self.fourstars_units[guarantee_index])
        wish_result_emoji.append(self.fourstar_emotes[guarantee_index])
        # randomly grabs 9 rarities
        rarity_pull = random.choices(self.rarity_pull, cum_weights=(0.6, 5.1, 94.3), k=9)
        for i in rarity_pull:
            if i == '3 star':
                # random pull from 3* list, grabs index
                index = random.choice(range(len(self.threestars_wep)))
                # uses index to grab unit name and emote from parallel arrays
                wish_result_emoji.append(self.wep_emote[index])
                wish_result.append(self.threestars_wep[index])
            if i == '4 star':
                # random pull from 4* list, grabs index
                index = random.choice(range(len(self.fourstars_units)))
                # uses index to grab unit name and emote from parallel arrays
                wish_result_emoji.append(self.fourstar_emotes[index])
                wish_result.append(self.fourstars_units[index])
            if i == '5 star':
                # random pull from 5* list, grabs index
                index = random.choice(range(len(self.fivestars_units)))
                # uses index to grab unit name and emote from parallel arrays
                wish_result_emoji.append(self.fivestar_emotes[index])
                wish_result.append(self.fivestars_units[index])
                # appends 5 to wish_rarity for embed purposes
                wish_rarity.append('5')
        return wish_result_emoji, wish_result, wish_rarity

    # creates new user if they use .daily and are not in the csv file already
    def new_user(self, userid, cooldown):
        with open('server_wishes.csv', 'a', newline='') as server_wishes:
            fieldnames = ['userid', 'four_pity', 'five_pity', 'wishes', 'primos', 'cooldown', 'units']
            writer = csv.DictWriter(server_wishes, fieldnames=fieldnames)

            pity = 0
            # new user starts off with 1832 primos
            primos = 1832
            # had to put place holders for this to be put into the csv as an actual list instead of a str
            units = ['9', '0']
            wishes = 0

            writer.writerow({'userid': userid, 'four_pity': pity, 'five_pity': pity, 'wishes': wishes,
                             'primos': primos, 'cooldown': cooldown, 'units': units})
            return

    # parses csv file for pity amounts
    # def pity_check(self, userid):
    #     with open('server_wishes.csv', 'r', newline='') as server_wishes:
    #         reader = csv.DictReader(server_wishes)
    #         userids = []
    #         fourstarpity_vals = []
    #         fivestarpity_vals = []
    #         userid = str(userid)
    #         for row in reader:
    #             userids.append(row['userid'])
    #             fourstarpity_vals.append(row['four_pity'])
    #             fivestarpity_vals.append(row['five_pity'])
    #         # if userid exists in csv it will return the pity values
    #         if userid in userids:
    #             index = userids.index(userid)
    #             fourstarpity = fourstarpity_vals[index]
    #             fivestarpity = fivestarpity_vals[index]
    #             return fourstarpity, fivestarpity
    #         # userid not inside csv, returns NONE str for function
    #         else:
    #             user = 'NONE'
    #             return user

    # parses csv file for primogem count
    def primo_check(self, userid):
        with open('server_wishes.csv', 'r', newline='') as server_wishes:
            reader = csv.DictReader(server_wishes)
            userids = []
            primo_count = []
            userid = str(userid)
            for row in reader:
                userids.append(row['userid'])
                primo_count.append(row['primos'])
            # if userid exists in csv it will return current primos
            if userid in userids:
                index = userids.index(userid)
                primos = primo_count[index]
                return primos, index
            # userid not inside csv, returns NONE str for function
            else:
                user = 'NONE'
                return user

    # gives daily primos, creates new user if not in csv file already
    def daily_primo(self, userid, cooldown):
        # opens csv file
        with open('server_wishes.csv', 'r', newline='') as server_wishes:
            reader = csv.DictReader(server_wishes)
            userids = []
            primo_vals = []
            userid = str(userid)
            current_cooldown = []
            for row in reader:
                userids.append(row['userid'])
                primo_vals.append(row['primos'])
                current_cooldown.append(row['cooldown'])
            # if userid exists in csv it will handle process for adding daily primos
            if userid in userids:
                index = userids.index(userid)
                # have to use UTC as discord api returns time stamps in UTC
                # current time in UTC
                current_utc = dt.strptime(str(dt.utcnow()), '%Y-%m-%d %H:%M:%S.%f').date()
                # last time user used command in UTC
                last_cooldown = dt.strptime(str(current_cooldown[index]), '%Y-%m-%d %H:%M:%S.%f').date()
                # runs rest of function if it's been 24 hours
                if str(last_cooldown) < str(current_utc):
                    # current primos
                    primo_count = primo_vals[index]
                    # turns primos into integer
                    int_primo = int(primo_count)
                    # daily primo gain
                    primo_add = 458
                    primos = int_primo + primo_add
                    # stores new primos as str for return to discord
                    primo_return = str(primos)
                    # writes new cooldown and primos to csv file
                    contents = pd.read_csv('server_wishes.csv', dtype=str)
                    contents.at[index, 'primos'] = primos
                    contents.at[index, 'cooldown'] = cooldown
                    contents.to_csv('server_wishes.csv', index=False)
                    return primo_return
                else:
                    return
            # if userid does not exist in csv this will run new_user function to add them
            else:
                self.new_user(userid, cooldown)
                # returns primos in string for discord message
                primos = '1832'
                return primos

    # enters units into user's catalog and tracks duplicates
    def dupes(self, userid, index, namepull):
        with open('server_wishes.csv', 'r', newline='') as server_wishes:
            reader = csv.DictReader(server_wishes)
            userids = []
            catalog = []
            primos = []
            # tracks refund of primogems, if any
            total_refund = int()
            userid = str(userid)
            for row in reader:
                userids.append(row['userid'])
                pre_list = row['units']
                # the row from the csv still comes in as a bunch of separate strings
                # have to use ast.literal_eval for python to realize it's actually a list of strings
                post_list = ast.literal_eval(pre_list)
                catalog.append(post_list)
                primos.append(row['primos'])
            # checks to see if userid exists in the csv
            if userid in userids:
                user_catalog = catalog[index]
                user_primos = primos[index]
                # loops through the units pulled
                for unit in namepull:
                    # if unit already is in their catalog, will treat as a dupe
                    if unit in user_catalog:
                        # ignores the placeholders in the catalog row
                        if '9' in unit or '0' in unit:
                            continue
                        # refunds 160 primos since user already has max dupes of the unit
                        if 'C6' in unit:
                            refund = 160
                            total_refund = total_refund + refund
                        # refunds 160 primos and makes the unit C6 in the csv
                        if 'C5' in unit:
                            refund = 160
                            total_refund = total_refund + refund
                            split = unit.split(' ')
                            dupe_unit = f'{split[0]} C6'
                            user_catalog.remove(unit)
                            user_catalog.insert(0, dupe_unit)
                        # refunds 160 primos and makes the unit C5 in the csv
                        if 'C4' in unit:
                            refund = 160
                            total_refund = total_refund + refund
                            split = unit.split(' ')
                            dupe_unit = f'{split[0]} C5'
                            user_catalog.remove(unit)
                            user_catalog.insert(0, dupe_unit)
                        # refunds 160 primos and makes the unit C4 in the csv
                        if 'C3' in unit:
                            refund = 160
                            total_refund = total_refund + refund
                            split = unit.split(' ')
                            dupe_unit = f'{split[0]} C4'
                            user_catalog.remove(unit)
                            user_catalog.insert(0, dupe_unit)
                        # refunds 160 primos and makes the unit C3 in the csv
                        if 'C2' in unit:
                            refund = 160
                            total_refund = total_refund + refund
                            split = unit.split(' ')
                            dupe_unit = f'{split[0]} C3'
                            user_catalog.remove(unit)
                            user_catalog.insert(0, dupe_unit)
                        # refunds 160 primos and makes the unit C2 in the csv
                        if 'C1' in unit:
                            refund = 160
                            total_refund = total_refund + refund
                            split = unit.split(' ')
                            dupe_unit = f'{split[0]} C2'
                            user_catalog.remove(unit)
                            user_catalog.insert(0, dupe_unit)
                        # refunds 160 primos and makes the unit C1 in the csv
                        else:
                            refund = 160
                            total_refund = total_refund + refund
                            dupe_unit = f'{unit} C1'
                            user_catalog.remove(unit)
                            user_catalog.insert(0, dupe_unit)
                    # makes sure unit is a 4* or 5* unit, adds it to the catalog if it is
                    elif unit in self.fivestars_units or unit in self.fourstars_units:
                        user_catalog.insert(0, unit)
                # adds the initial primos with any refunds that were added
                updated_primos = int(user_primos) + total_refund
                # writes the new info to the csv file
                contents = pd.read_csv('server_wishes.csv', dtype=str)
                contents.at[index, 'units'] = user_catalog
                contents.at[index, 'primos'] = updated_primos
                contents.to_csv('server_wishes.csv', index=False)
                return

    # creates csv file with headers
    def create_csv(self):
        with open('server_wishes.csv', 'w', newline='') as server_wishes:
            fieldnames = ['userid', 'four_pity', 'five_pity', 'wishes', 'primos', 'cooldown', 'units']
            writer = csv.DictWriter(server_wishes, fieldnames=fieldnames)

            writer.writeheader()
            return

    # parses user's unit catalog
    # def catalog_parse(self, userid):
    #     with open('server_wishes.csv', 'r', newline='') as server_wishes:
    #         reader = csv.DictReader(server_wishes)
    #         userids = []
    #         catalog = []
    #         userid = str(userid)
    #         usercatalog_names = []
    #         usercatalog_emotes = []
    #         for row in reader:
    #             userids.append(row['userid'])
    #             pre_list = row['units']
    #             post_list = ast.literal_eval(pre_list)
    #             catalog.append(post_list)
    #         # if userid exists in csv their units will be parsed into lists
    #         if userid in userids:
    #             index = userids.index(userid)
    #             user_catalog = catalog[index]
    #             # loops through units in catalog
    #             for unit in user_catalog:
    #                 # have to parse the dupes in the catalog differently to grab the right index and emotes
    #                 if 'C' in unit:
    #                     # splits the unit dupe name so it uses just the actual unit name
    #                     nondupe_unit = unit.split(' ')
    #                     corrected_unit = nondupe_unit[0]
    #                     if corrected_unit in self.fourstars_units:
    #                         # uses the index to grab the correct emote from the parallel arrays
    #                         catalogindex = self.fourstars_units.index(corrected_unit)
    #                         usercatalog_emotes.append(self.fourstar_emotes[catalogindex])
    #                         usercatalog_names.append(unit)
    #                     if corrected_unit in self.fivestars_units:
    #                         # uses the index to grab the correct emote from the parallel arrays
    #                         catalogindex = self.fivestars_units.index(corrected_unit)
    #                         usercatalog_emotes.append(self.fivestar_emotes[catalogindex])
    #                         usercatalog_names.append(unit)
    #                 else:
    #                     if unit in self.fourstars_units:
    #                         # uses just the unit name since it's not a dupe
    #                         catalogindex = self.fourstars_units.index(unit)
    #                         usercatalog_emotes.append(self.fourstar_emotes[catalogindex])
    #                         usercatalog_names.append(self.fourstars_units[catalogindex])
    #                     if unit in self.fivestars_units:
    #                         # uses just the unit name since it's not a dupe
    #                         catalogindex = self.fivestars_units.index(unit)
    #                         usercatalog_emotes.append(self.fivestar_emotes[catalogindex])
    #                         usercatalog_names.append(self.fivestars_units[catalogindex])
    #             return usercatalog_emotes, usercatalog_names
    #         # returns NONE if userid is not in the csv
    #         else:
    #             return 'NONE'

    # parses user's total wish count
    def wishes_check(self, userid):
        with open('server_wishes.csv', 'r', newline='') as server_wishes:
            reader = csv.DictReader(server_wishes)
            userids = []
            wishes = []
            userid = str(userid)
            for row in reader:
                userids.append(row['userid'])
                wishes.append(row['wishes'])
            # if user exists in csv returns total wishes amount for message purposes
            if userid in userids:
                index = userids.index(userid)
                user_wishes = wishes[index]
                return user_wishes
            # user doesn't exist in csv, returns NONE
            else:
                return 'NONE'


# wish = Wish()
# wish.create_csv()
