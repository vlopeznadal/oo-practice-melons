############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""
    musk = MelonType(
    "musk",
    1998,
    "green",
    True,
    True,
    "Muskmelon")
    musk.add_pairing("mint")

    cas = MelonType(
    "cas",
    2003,
    "orange",
    False,
    False,
    "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")

    yw = MelonType(
    "yw",
    2013,
    "yellow",
    True,
    True,
    "Yellow Watermelon")
    cas.add_pairing("ice cream")
    


    all_melon_types = []
    all_melon_types.append(musk)
    all_melon_types.append(cas)

    return all_melon_types
melon_list = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with {melon.pairings}")
print_pairing_info(melon_list)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}

    for melon in melon_types:
        if melon.code not in melon_dict:
            melon_dict[melon.code] = melon.name
  
    return melon_dict
make_melon_type_lookup(melon_list)
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, code, shape_rating, color_rating, field, harvester):
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester
    
    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False
    

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_list = []
    melons_by_id = make_melon_type_lookup(melon_types)
    print(melons_by_id)
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_list.append(melon_1)
    melon_list.append(melon_2)
    return melon_list
print(make_melons(melon_list))
def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



