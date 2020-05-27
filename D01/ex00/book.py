import datetime

from recipe import Recipe

dt = datetime.datetime


class Book:
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
            self.last_update = dt.now()
            self.creation_date = dt.now()
            self.recipes_list = {"starter": {}, "lunch": {}, "dessert": {}}
        else:
            exit()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for i in self.recipes_list:
            if name in self.recipes_list[i]:
                print(self.recipes_list[i][name])
                return
        print("recipe not found")
        return

    pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list:
            for i in self.recipes_list[recipe_type]:
                print(self.recipes_list[recipe_type][i])
        else:
            print("Invalid type of dish")

    pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""

        if type(recipe) is Recipe:
            self.recipes_list[recipe.recipe_type][recipe.name] = recipe
            self.last_update = dt.now()
        else:
            print("ERROR")

    pass
