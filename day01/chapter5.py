def make_food(ingredients_needed, food_name):
    """make_food(ingredients_needed, food_name)
    Takes the ingredients from ingredients_needed and makes food_name"""
    for ingredient in ingredients_needed.keys():
        print("Adding %d of %s to make a %s" % (ingredients_needed[ingredient], ingredient))
    print("Made %s" % food_name)
    return food_name

def make_omlette(omlette_type):
    """This will make an omlette. You can either pass in a dictionary
    that contains all of the ingredients for your omlette, or provide
    a string to select a type of omlette this function already knows
    about"""
    if type(omlette_type) == type({}):
        print("omlette_type is a dictionary with ingredients")
        return make_food(omlette_type, "omlette")
    elif type(omlette_type) == type(""):
        omlette_ingredients = get_omlette_ingredients(omlette_type)
        return make_food(omlette_ingredients, omlette_type)
    else:
        print("I don't think I can make this kind of omlette: %s" % omlette_type)
