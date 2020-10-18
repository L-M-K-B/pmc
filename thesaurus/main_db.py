import mysql.connector
import difflib

word = ""
END = "/exit"

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()


class WordFinder:
    def __init__(self):
        query_alt = cursor.execute("SELECT Expression FROM Dictionary")
        expressions = cursor.fetchall()

        self.exp_list = self.clean_expressions(expressions)

    def clean_expressions(self, exp):
        clean_exp = []

        for e in exp:
            clean_exp.append(e[0])

        return clean_exp

    def handle_query(self, search_term):
        query = cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = '{search_term}'")
        definitions = cursor.fetchall()

        return definitions

    def handle_results(self, results):
        for r in results:
            print(r[0])

    def handle_no_results(self):
        if closest_matches := difflib.get_close_matches(word, self.exp_list):
            # closest_matches always has 3 suggestions
            self.handle_closest_match(closest_matches[0])

        else:
            print("This word does not exist. Please check again.")

    def handle_closest_match(self, match):
        decision = input(
            f"Did you mean {match}? Type Y for yes or N for no.")

        if decision == 'Y':
            alt = self.handle_query(match)
            self.handle_results(alt)

        else:
            return None


word_finder = WordFinder()

while word != END:
    word = input("Enter a word: ")

    if word != END:
        result = word_finder.handle_query(word)

        if result:
            word_finder.handle_results(result)

        else:
            word_finder.handle_no_results()

