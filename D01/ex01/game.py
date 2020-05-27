class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
        self.kill_count = 0

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

    def kill(self, kill_count=1):
        if isinstance(kill_count, int):
            self.kill_count += kill_count
        else:
            print("Give me a number !")
