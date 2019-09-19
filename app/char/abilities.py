# Defining basic abilities
class Abilities(race=None, theme=None):

    """
    All operations with abilities define here
    """

    # Basic abilities value - 10 points
    base_abilities = {
        'strength': 10,
        'dexterity': 10,
        'constitution': 10,
        'intelligence': 10,
        'wisdom': 10,
        'charisma': 10,
        # Discretionary points
        'discret_points': 10
    }

    ability_modifiers = {
        'strength': 0,
        'dexterity': 0,
        'constitution': 0,
        'intelligence': 0,
        'wisdom': 0,
        'charisma': 0
    }

    # Adding race ability bonus
    def race_theme_ability_bonus(self, race: str = None, theme: str = None):

        """

        :param race: str, Race of character
        :param theme: str, Theme of character
        :return: abilities: dir with race values
        """

        if race is not None:
            if race == 'Android':
                self.base_abilities['dexterity'] += 2
                self.base_abilities['intelligence'] += 2
                self.base_abilities['charisma'] -= 2

            if race == 'Human':
                self.base_abilities['discret_points'] += 2

            if race == 'Kasatha':
                self.base_abilities['strength'] += 2
                self.base_abilities['intelligence'] -= 2
                self.base_abilities['wisdom'] += 2

            if race == 'Lashunta (Damaya)':
                self.base_abilities['constitution'] -= 2
                self.base_abilities['intelligence'] += 2
                self.base_abilities['charisma'] += 2

            if race == 'Lashunta (Korasha)':
                self.base_abilities['strength'] += 2
                self.base_abilities['wisdom'] -= 2
                self.base_abilities['charisma'] += 2

            if race == 'Shirren':
                self.base_abilities['constitution'] += 2
                self.base_abilities['wisdom'] -= 2
                self.base_abilities['charisma'] -= 2

            if race == 'Vesk':
                self.base_abilities['strength'] += 2
                self.base_abilities['constitution'] += 2
                self.base_abilities['intelligence'] -= 2

            if race == 'Ysoki':
                self.base_abilities['strength'] -= 2
                self.base_abilities['dexterity'] += 2
                self.base_abilities['intelligence'] += 2

            if race is None:
                pass  # TODO: Must rise error

        if theme is not None:
            if theme == 'Ace Pilot':
                self.base_abilities['dexterity'] += 1

            if theme == 'Bounty Hunter':
                self.base_abilities['constitution'] += 1

            if theme == 'Icon':
                self.base_abilities['charisma'] += 1

            if theme == 'Mercenary':
                self.base_abilities['strength'] += 1

            if theme == 'Outlaw':
                self.base_abilities['dexterity'] += 1

            if theme == 'Priest':
                self.base_abilities['wisdom'] += 1

            if theme == 'Scholar':
                self.base_abilities['intelligence'] += 1

            if theme == 'Spacefarer':
                self.base_abilities['constitution'] += 1

            if theme == 'Xenoseeker':
                self.base_abilities['charisma'] += 1

            if theme == 'Themeless':
                self.base_abilities['discret_points'] += 1

            if theme is None:
                pass  # TODO: Must rise error

    def add_discret_points(self, ability: str = None, amount: int = None):
        if ability and amount is not None:
            if self.base_abilities['discret_points'] > 0 and 0 < amount <= 10:
                self.base_abilities[ability] += amount
                self.base_abilities['discret_points'] -= amount

    def subtract_discret_points(self, ability: str = None, amount: int = None):
        pass

    def reset_discret_points(self):
        pass

    # Count ability modifiers
    def count_ability_modifiers(self, abilities: str = None):

        """
        The  right-hand  column  in  Table  2–1 (page 19)  shows  the  ability  modifier  corresponding to each ability score.
        This modifier is applied to die rolls related to your abilities, such as skill checks, attacks,
        and more. Nearly every roll is affected by your abilities in some way, often with additional modifiers from
        other sources, but they generally  involve  your  ability  modifier  rather  than  your  actual  ability
        score.  When  you  determine  your  ability  scores,  make  sure to note their respective ability modifiers
        on your character sheet. If a change to an ability score ever alters its modifier, be sure to adjust any
        statistics that rely on that modifier. Sometimes, a situation or ability might require you to attempt
        something  called  an  ability  check.  In  such  instances,  instead  of  attempting a check involving both
        your abilities and other factors (such  as  skills  or  saving  throws  that  reflect  your  training  and
        expertise),  you  attempt  a  check  using  just  1d20  +  your  ability  modifier.  This  represents  you
        trying  to  use  your  raw,  untrained  talent  for  that  particular  ability,  such  as  attempting  a
        Strength  check to kick down a door. See page 242 for more information.In  the  rare  instance  that  you
        need  to  determine  ability  modifiers  beyond  the  numbers  presented  in  the  table,  such  as  for
        extreme high-level play, ability modifiers can be determined by subtracting 10 from the ability score and
        dividing that result by 2, rounding down if the final result is a fraction. For example, an ability score of
        41 would have an ability modifier of +15 (since 41 – 10 = 31 and 31 ÷ 2 = 15-1/2, which rounds down to 15).
        :param abilities: :return:
        """

        for key, value in abilities.items:
            if value == 1:
                self.ability_modifiers[key] = -5
            elif value <= 3:
                self.ability_modifiers[key] = -4
            elif value <= 5:
                self.ability_modifiers[key] = -3
            elif value <= 7:
                self.ability_modifiers[key] = -2
            elif value <= 9:
                self.ability_modifiers[key] = -1
            elif value <= 11:
                self.ability_modifiers[key] = 0
            elif value <= 13:
                self.ability_modifiers[key] = 1
            elif value <= 15:
                self.ability_modifiers[key] = 2
            elif value <= 17:
                self.ability_modifiers[key] = 3
            elif value <= 19:
                self.ability_modifiers[key] = 4
            elif value <= 21:
                self.ability_modifiers[key] = 5
            elif value <= 23:
                self.ability_modifiers[key] = 6
            elif value <= 25:
                self.ability_modifiers[key] = 7
            elif value == 26:
                self.ability_modifiers[key] = 8

    def level_up_ability(self, abilities: str = None):

        """
        Every  5  levels  (at  5th,  10th,  15th,  and  20th  levels),  you  get  to  increase and customize your
        ability scores. Each time you reach one of these level thresholds, choose four of your ability scores to
        increase. If that ability score is 17 or higher (excluding any ability increases  from  personal  upgrades—see
        page  212),  it  increases  permanently  by  1.  If  it’s  16  or  lower,  it  increases  permanently  by  2.
        You  can’t  apply  more  than  one  of  these  increases  to  the  same ability score at a given level,
        but unlike at 1st level, these increases can make your ability scores go higher than 18.
        For   example,   let’s   say   you’re   leveling   up   your   android   technomancer with the following
        scores: STR 10, DEX 16, CON 10, INT 18, WIS 11, CHA 10
        You  might  decide  to  increase  your  Dexterity,  Constitution,  Intelligence,  and  Wisdom.
        Because  your  Intelligence  is  17  or  higher, it would increase by 1 to a score of 19. The other three scores
        would increase by 2, giving you these final scores: STR 10, DEX 18, CON 12, INT 19, WIS 13, CHA 10
        The next time you can increase your ability scores, you could decide to increase those same abilities again,
        or you could pick a different subset. For more details on leveling up, see page 26.
        :param abilities: str
        :return:
        """