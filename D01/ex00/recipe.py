class Recipe:
    def __init__(self, name="", cooking_lvl="", cooking_time="",
                 ingredients="", description="", recipe_type=""):
        valid = 1

        if name == "" or not name or not isinstance(name, str):
            valid = 0
        if cooking_lvl == "" or not isinstance(cooking_lvl, int) \
                or cooking_lvl < 1 or cooking_lvl > 5:
            valid = 0
            print("cooking_lvl must be a number declared between 1 and 5")
        if cooking_time == "" or not isinstance(cooking_time, int):
            valid = 0
            print("cooking_time must be the time declared in minutes")
        if ingredients == "" or not isinstance(ingredients, list):
            valid = 0
            print("ingredients must be a declared list of ingredients")
        if not isinstance(recipe_type, str) or (
                recipe_type != "starter" and
                recipe_type != "lunch" and
                recipe_type != "dessert"):
            print("recipe_type must be a chosen between "
                  "starter, lunch or dessert")
            valid = 0

        if valid == 1:
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
        else:
            exit()

    def __str__(self):
        """Return the string to print with the recipe info"""

        txt = ""
        """Your code goes here"""

        txt += "Name: " + str(self.name) + '\n' + \
               "cooking_lvl: " + str(self.cooking_lvl) + '\n' + \
               "cooking_time: " + str(self.cooking_time) + '\n' + \
               "ingredients: " + \
               ", ".join(str(n) for n in self.ingredients) + '\n' + \
               "description: " + str(self.description) + '\n' + \
               "recipe_type: " + str(self.recipe_type) + '\n' + \
               "------------ FIN DE LA RECETTE ------------"

        return txt
