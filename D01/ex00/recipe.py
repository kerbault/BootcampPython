class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        valid = 1

        if not name:
            valid = 0
        if not cooking_lvl or cooking_lvl < 1 or cooking_lvl > 5:
            valid = 0
            print("cooking_lvl must be a number declared between 1 and 5")
        if not cooking_time:
            valid = 0
            print("cooking_time must be a declared number between 1 and 5")
        if not ingredients:
            valid = 0
        if not description:
            valid = 0
        if not recipe_type:
            valid = 0
        if valid == 1:
            self.name = ""
            self.cooking_lvl = 1
            self.cooking_time = 0
            self.ingredients = []
            self.description = ""
            self.recipe_type = ""
