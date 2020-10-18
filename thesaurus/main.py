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

        elif closest_matches := difflib.get_close_matches(search_term, self.data.keys()):
            # closest_matches always has 3 suggestions
            self.handle_matches(closest_matches)

        else:
            print("This word does not exist. Please check again.")

    def create_response(self, search_term):
        result = self.data[search_term]

        if type(result) == list:
            for r in result:
                print(r)
        else:
            print(result)

    def handle_matches(self, closest_matches):
        decision = input(
            f"Did you mean {closest_matches[0]}, {closest_matches[1]} or {closest_matches[2]}? "
            f"Type the suitable word or N for none.")

        if len(decision) > 1:
            self.find_word(decision)


word_finder = WordFinder()


while text != END:
    text = input("Enter a word: ")
    if text != END:
        word_finder.find_word(text)
