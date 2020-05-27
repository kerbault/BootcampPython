from book import Book
from recipe import Recipe

quiche = Recipe("Quich", 2, 45, ["Oeuf", "Creme", "Lardons", "Pate brisee"],
                "On l'appelle aussi la ouiche", "lunch")

chips = Recipe("chips", 1, 30, ["Chips", "Moutarde"],
               "Des chipsaaaaaa a la saveur moutarde, C'est tout ce que ça te "
               "fait quand je te dis qu'on va manger des chips ?",
               "lunch")

the_book = Book("Necronomicon")

the_book.add_recipe(quiche)
the_book.add_recipe(chips)

the_book.get_recipes_by_types("lunch")
print("----------------Second test----------------")
the_book.get_recipe_by_name("chips")
