import csv
import json
import random
import ast
import pandas as pd
from datetime import date


class Wish:

    def __init__(self):
        with open("pullables.json", "r") as pullables_file:
            self.pullables = json.load(pullables_file)
        # {rarity: [(character/wep, emoji)]}

        # rarities for wish functions
        self.rarity_pull = ['5*', '4*', '3*']

    def wish(self, userid, pulls: int = 10, simulation: bool = True):
        # if a pull is a simulation, it does not require a real userid or primogems and does not affect a players pity
        fourstar_pity = 1
        fivestar_pity = 1
        if not simulation:
            fourstar_pity, fivestar_pity = self.get_pity(userid)
            if not self.primo_transaction(userid, 0-(pulls*160)):
                return False, False
        highest_rarity = None
        wish_pulls = []

        for pull in range(0, pulls):
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
            pulled = random.choice(self.pullables["rarities"][rarity])
            wish_pulls.append([pulled, self.get_emote_pullable(pulled)])
            if not simulation:
                self.save_pity(userid, [fourstar_pity, fivestar_pity])
                self.add_item(userid, pulled)
                self.add_wishes(userid, 1)
        return highest_rarity, wish_pulls

    def get_emote_pullable(self, pullable):
        emote = None
        fl_to_type = {"w": "weapons", "c": "characters"}
        for i in self.pullables[fl_to_type[pullable[0]]]:
            if i == pullable[1:]:
                emote = self.pullables[fl_to_type[pullable[0]]][i]
        return emote

    def get_all_data(self) -> dict:
        with open("wishes.json", "r") as wishes_file:
            wishes_dict = json.load(wishes_file)
        return wishes_dict

    def get_user_data(self, userid: int) -> dict:
        wishes_dict = self.get_all_data()
        if str(userid) not in wishes_dict:
            return {}
        return wishes_dict[str(userid)]

    def add_item(self, userid: int, item: str):
        units = self.get_units(userid)
        if item[0] == "w":  # item is a weapon, add it to inven
            units.append(item)
        elif item[0] == "c":  # item is a character, check if already owned+constellation level then add
            clevel = self.get_character_constellation(userid, item[1:], units)
            if clevel == -1:
                units.append(item[1:])
            elif clevel in range(0, 6):
                for i in range(len(units)):
                    if units[i].startswith(item[1:]):  # assumes no duplicates of same unit since only detects first one
                        units[i] = f"{item[1:]} C{clevel + 1}"
                        break
        self.save_units(userid, units)

    def get_character_constellation(self, userid: int, character: str, units: list):
        clevel_int = -1
        for unit in units:
            if unit == character:
                return 0
            elif unit[0:len(character)] == character:
                constellation_level = unit[-2:]
                if constellation_level[0] == 'C':
                    try:
                        clevel_int = int(constellation_level[1])
                        return clevel_int
                    except ValueError:
                        pass
        return clevel_int

    def save_user_data(self, userid: int, data=None):  # save user data or create new user if no data is provided
        if data is None:
            data = {"four_pity": 0, "five_pity": 0, "wishes": 0, "primos": 0, "cooldown": "", "units": []}
        wishes_dict = self.get_all_data()
        wishes_dict[str(userid)] = data
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
        return user_data["primos"]

    def get_cooldown(self, userid: int):
        data = self.get_user_data(userid)
        return data['cooldown']

    def set_cooldown(self, userid: int, cooldown: str):
        data = self.get_user_data(userid)
        data['cooldown'] = cooldown
        self.save_user_data(userid, data)

    def get_wishes(self, userid: int) -> int:
        data = self.get_user_data(userid)
        return data['wishes']

    def add_wishes(self, userid: int, wishes_to_add: int):
        data = self.get_user_data(userid)
        data['wishes'] += wishes_to_add
        self.save_user_data(userid, data)

    def check_user_exists(self, userid: int):
        if str(userid) in self.get_all_data():
            return True
        return False

    # gives daily primos, creates new user if not in json file already
    def daily_primo(self, userid: int):
        daily_valid = False
        if not self.check_user_exists(userid):
            self.save_user_data(userid)
            self.primo_transaction(userid, 1832)
            daily_valid = True
        primo_add = 458
        current_date = str(date.today())
        if not daily_valid:
            cooldown_date = self.get_cooldown(userid)
            if str(current_date) > str(cooldown_date):
                daily_valid = True
        if daily_valid:
            self.set_cooldown(userid, current_date)
            return self.primo_transaction(userid, primo_add)
        else:
            return False

    def get_catalog(self, userid):
        data = self.get_user_data(userid)
        return data['units']

    def catalog_parse(self, userid):
        catalog = self.get_catalog(userid)
        units_and_emojis = {}
        for unit in catalog:
            units_and_emojis[unit[1:]] = self.get_emote_pullable(unit)
        return units_and_emojis

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

    # parses user's unit catalog
    def catalog_parse(self, userid):
        # grab user data and check if user/units exist
        userData = self.get_user_data(userid)
        if userData == {}:
            return 'NONE'

        unitData = userData["units"]
        if unitData == {}:
            return {}

        # User exists and has units
        userCatalog_emotes = []
        userCatalog_names = []
        for unit in unitData:
            if unit in self.pullables[self.rarity_pull[2]]:
                break
            elif unit in self.pullables[self.rarity_pull[1]]:
                break
            elif unit in self.pullables[self.rarity_pull[0]]:
                break

        # for unit in user_catalog:
        #     # have to parse the dupes in the catalog differently to grab the right index and emotes
        #     if 'C' in unit:
        #         # splits the unit dupe name so it uses just the actual unit name
        #         nondupe_unit = unit.split(' ')
        #         corrected_unit = nondupe_unit[0]
        #         if corrected_unit in self.fourstars_units:
        #             # uses the index to grab the correct emote from the parallel arrays
        #             catalogindex = self.fourstars_units.index(corrected_unit)
        #             usercatalog_emotes.append(self.fourstar_emotes[catalogindex])
        #             usercatalog_names.append(unit)
        #         if corrected_unit in self.fivestars_units:
        #             # uses the index to grab the correct emote from the parallel arrays
        #             catalogindex = self.fivestars_units.index(corrected_unit)
        #             usercatalog_emotes.append(self.fivestar_emotes[catalogindex])
        #             usercatalog_names.append(unit)
        #     else:
        #         if unit in self.fourstars_units:
        #             # uses just the unit name since it's not a dupe
        #             catalogindex = self.fourstars_units.index(unit)
        #             usercatalog_emotes.append(self.fourstar_emotes[catalogindex])
        #             usercatalog_names.append(self.fourstars_units[catalogindex])
        #         if unit in self.fivestars_units:
        #             # uses just the unit name since it's not a dupe
        #             catalogindex = self.fivestars_units.index(unit)
        #             usercatalog_emotes.append(self.fivestar_emotes[catalogindex])
        #             usercatalog_names.append(self.fivestars_units[catalogindex])
        # return usercatalog_emotes, usercatalog_names

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
