import json

DATA = json.load(open("data.json"))
text = ""
END = "/exit"


def find_word(search_term):
    result = DATA[search_term]

    if not result:
        print("This word does not exist. Please check again.")
    elif type(result) == list:
        for r in result:
            print(r)
    else:
        print(result)


while text != END:
    text = input("Enter a word: ")
    find_word(text)
