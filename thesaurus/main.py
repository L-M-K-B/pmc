import json
import difflib

text = ""
END = "/exit"


class WordFinder:
    def __init__(self):
        raw_data = json.load(open("data.json"))
        self.data = {}

        for key in raw_data:
            self.data[key.lower()] = raw_data[key]

    def find_word(self, search_term):
        search_term = search_term.lower()

        if search_term in self.data:
            self.create_response(search_term)

        elif len(difflib.get_close_matches(search_term, self.data.keys())) > 0:
            # creates 3 suggestions
            self.find_closest_match(search_term)

        else:
            print("This word does not exist. Please check again.")

    def create_response(self, search_term):
        result = self.data[search_term]

        if type(result) == list:
            for r in result:
                print(r)
        else:
            print(result)

    def find_closest_match(self,search_term):
        closest_result = difflib.get_close_matches(search_term, self.data.keys())

        decision = input(
            f"Did you mean {closest_result[0]}, {closest_result[1]} or {closest_result[2]}? "
            f"Type the suitable word or N for none.")

        if decision == "Y":
            self.find_word(closest_result)
        elif len(decision) > 1:
            self.find_word(decision)
        else:
            return None


word_finder = WordFinder()


while text != END:
    text = input("Enter a word: ")
    if text != END:
        word_finder.find_word(text)
