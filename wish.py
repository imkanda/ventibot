import csv
import random
import ast
import pandas as pd
from datetime import datetime as dt


class Wish:

    # list of all 4* units (parallel array)
    fourstars_units = ['Amber', 'Barbara', 'Beidou', 'Bennett', 'Chongyun', 'Diona', 'Fischl', 'Kaeya', 'Lisa',
                       'Ningguang', 'Noelle', 'Razor', 'Sucrose', 'Xiangling', 'Xingqiu', 'Xinyan']

    # list of all 4* unit emotes (parallel array)
    fourstar_emotes = ['<:amber:779443715713400883>', '<:barbara:779443715806199889>',
                       '<:beidou:779443715910795324>', '<:bennett:779443715293970503>',
                       '<:chongyun:779443715738566657>', '<:diona:779443715709337681>',
                       '<:fischl:779443715696623626>', '<:kaeya:779443715688235068>', '<:lisa:779443715885367336>',
                       '<:ningguang:779443715449946144>', '<:noelle:779443715709337630>',
                       '<:razorgenshin:779443715768844318>', '<:sucrose:779443715542351903>',
                       '<:xiangling:779443715625320478>', '<:xingqiu:779443715511943218>',
                       '<:xinyan:779443715508535326>']

    # list of all 5* units (parallel array)
    fivestars_units = ['Diluc', 'Jean', 'Keqing', 'Klee', 'Mona', 'Qiqi', 'Tartaglia',
                       'Venti', 'Xiao', 'Zhongli']

    # list of all 5* unit emotes (parallel array)
    fivestar_emotes = ['<:diluc:779443715882221578>', '<:jean:779443715675521024>', '<:keqing:779443715717857320>',
                       '<:klee:779443715768057976>', '<:mona:779443715395026955>', '<:qiqi:779443715727032330>',
                       '<:childe:779443715155820595>', '<:venti:779443715382050858>', '<:xiao:779443715437232128>',
                       '<:zhongli:779443715809738763>']

    # list of all 3* weapons (parallel array)
    threestars_wep = ['Ebony Bow', 'Messenger', 'Raven Bow', 'Recurve Bow', 'Sharpshooters Oath', 'Slingshot',
                      'Amber Catalyst', 'Emerald Orb', 'Magic Guide', 'Otherwordly Story', 'Thrilling Tales of Dragon '
                                                                                           'Slayers', 'Twin Nephrite',
                      'Bloodtainted Greatsword', 'Debate Club', 'Ferrous Shadow',
                      'Quartz', 'Skyrider Greatsword', 'White Iron Greatsword', 'Black Tassel', 'Halberd',
                      'White Tassel', 'Cool Steel', 'Dark Iron Greatsword', 'Fillet Blade', 'Harbringer of Dawn',
                      'Skyrider Sword', 'Travelers Handy Sword']

    # list of all 3* weapon emotes (parallel array)
    wep_emote = ['<:ebony_bow:784915675932131388>', '<:messenger:784915675847589959>',
                 '<:raven_bow:784915675457650749>', '<:recurve_bow:784915675662516264>',
                 '<:sharpshooters_oath:784915675277164565>', '<:slingshot:784915676015886376>',
                 '<:amber_catalyst:784915674904395837>', '<:emerald_orb:784915675633811467>',
                 '<:magic_guide:784915675553464342>', '<:otherworldly_story:784915675331821569>',
                 '<:thrilling_tales:784915675675361291>', '<:twin_nephrite:784915675835531305>',
                 '<:bloodtainted_greatsword:784915674924711956>', '<:debate_club:784915675814035546>',
                 '<:ferrous_shadow:784915675961098260>', '<:quartz:784915675641544704>',
                 '<:skyrider_greatsword:784915675734343741>', '<:white_iron_greatsword:784915675448606751>',
                 '<:black_tassel:784915674912260176>', '<:halberd:784915675990327296>',
                 '<:white_tassel:784915675532754964>', '<:cool_steel:784915675042283522>',
                 '<:dark_iron_sword:784915675838676997>', '<:fillet_blade:784915675336540171>',
                 '<:harbringer_of_dawn:784915675629879336>', '<:skyrider_sword:784915675860303882>',
                 '<:traverlers_handy_sword:784915675378352179>']

    # rarities for wish functions
    rarity_pull = ['5 star', '4 star', '3 star']

    # single wish function with pity affecting weight
    def wishsingle_pity(self, userid):
        base_pity = 0.6
        soft_pity = 1.2
        hard_pity = 32
        current_pulls = self.pity_check(userid)
        fourstar_pity = int(current_pulls[0])
        fivestar_pity = int(current_pulls[1])

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
    def pity_check(self, userid):
        with open('server_wishes.csv', 'r', newline='') as server_wishes:
            reader = csv.DictReader(server_wishes)
            userids = []
            fourstarpity_vals = []
            fivestarpity_vals = []
            userid = str(userid)
            for row in reader:
                userids.append(row['userid'])
                fourstarpity_vals.append(row['four_pity'])
                fivestarpity_vals.append(row['five_pity'])
            # if userid exists in csv it will return the pity values
            if userid in userids:
                index = userids.index(userid)
                fourstarpity = fourstarpity_vals[index]
                fivestarpity = fivestarpity_vals[index]
                return fourstarpity, fivestarpity
            # userid not inside csv, returns NONE str for function
            else:
                user = 'NONE'
                return user

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
    def catalog_parse(self, userid):
        with open('server_wishes.csv', 'r', newline='') as server_wishes:
            reader = csv.DictReader(server_wishes)
            userids = []
            catalog = []
            userid = str(userid)
            usercatalog_names = []
            usercatalog_emotes = []
            for row in reader:
                userids.append(row['userid'])
                pre_list = row['units']
                post_list = ast.literal_eval(pre_list)
                catalog.append(post_list)
            # if userid exists in csv their units will be parsed into lists
            if userid in userids:
                index = userids.index(userid)
                user_catalog = catalog[index]
                # loops through units in catalog
                for unit in user_catalog:
                    # have to parse the dupes in the catalog differently to grab the right index and emotes
                    if 'C' in unit:
                        # splits the unit dupe name so it uses just the actual unit name
                        nondupe_unit = unit.split(' ')
                        corrected_unit = nondupe_unit[0]
                        if corrected_unit in self.fourstars_units:
                            # uses the index to grab the correct emote from the parallel arrays
                            catalogindex = self.fourstars_units.index(corrected_unit)
                            usercatalog_emotes.append(self.fourstar_emotes[catalogindex])
                            usercatalog_names.append(unit)
                        if corrected_unit in self.fivestars_units:
                            # uses the index to grab the correct emote from the parallel arrays
                            catalogindex = self.fivestars_units.index(corrected_unit)
                            usercatalog_emotes.append(self.fivestar_emotes[catalogindex])
                            usercatalog_names.append(unit)
                    else:
                        if unit in self.fourstars_units:
                            # uses just the unit name since it's not a dupe
                            catalogindex = self.fourstars_units.index(unit)
                            usercatalog_emotes.append(self.fourstar_emotes[catalogindex])
                            usercatalog_names.append(self.fourstars_units[catalogindex])
                        if unit in self.fivestars_units:
                            # uses just the unit name since it's not a dupe
                            catalogindex = self.fivestars_units.index(unit)
                            usercatalog_emotes.append(self.fivestar_emotes[catalogindex])
                            usercatalog_names.append(self.fivestars_units[catalogindex])
                return usercatalog_emotes, usercatalog_names
            # returns NONE if userid is not in the csv
            else:
                return 'NONE'

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
