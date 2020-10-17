import json
import difflib

DATA = json.load(open("data.json"))
text = ""
END = "/exit"


def find_word(search_term):
    search_term = search_term.lower()

    if search_term in DATA:
        result = DATA[search_term]

        if type(result) == list:
            for r in result:
                print(r)
        else:
            print(result)
    elif len(difflib.get_close_matches(search_term, DATA.keys())) > 0:
        find_closest_match(search_term)
    else:
        print("This word does not exist. Please check again.")


def find_closest_match(search_term):
    closest_result = difflib.get_close_matches(search_term, DATA.keys())

    decision = input(
        f"Did you mean {closest_result[0]}, {closest_result[1]} or {closest_result[2]}? "
        f"Type the suitable word or N for none.")

    if decision == "Y":
        find_word(closest_result)
    elif len(decision) > 1:
        find_word(decision)
    else:
        return None


while text != END:
    text = input("Enter a word: ")
    if text != END:
        find_word(text)
