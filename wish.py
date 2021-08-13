import json
import random
from datetime import date


class Wish:

    def __init__(self):
        with open("pullables.json", "r") as pullables_file:
            self.pullables = json.load(pullables_file)
            self.FIVE_STAR_START_INDEX = 16
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
        if pullable[0] == 'w':
            for i in self.pullables["weapons"]:
                if i == pullable[1:]:
                    emote = self.pullables[fl_to_type[pullable[0]]][i]
        elif pullable[0] == 'c':
            charArr = self.pullables["character_index"]
            for i in range(len(charArr)):
                if charArr[i] == pullable[1:]:
                    emote = self.pullables["characters"][i]
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
        catalog_response = []
        rarities  = self.pullables["rarities"]
        emoteList = self.pullables["characters"]
        for unit in unitData:
            five_stars = rarities[self.rarity_pull[0]]
            four_stars = rarities[self.rarity_pull[1]]
            for i in range(len(four_stars)):
                if four_stars[i][1:] in unit:
                    catalog_response.append(f"{emoteList[i]} {unit}")
                    continue

            for i in range(len(five_stars)):
                if five_stars[i][1:] in unit:
                    catalog_response.append(f"{emoteList[self.FIVE_STAR_START_INDEX + i]} {unit}")
                    continue

        return catalog_response
