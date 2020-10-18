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


def handle_query(search_term):
    query = cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = '{search_term}'")
    definitions = cursor.fetchall()

    return definitions


def handle_results(results):
    for r in results:
        print(r[0])


def handle_no_results():
    query_alt = cursor.execute("SELECT Expression FROM Dictionary")
    expressions = cursor.fetchall()

    exp_list = clean_expressions(expressions)

    if closest_matches := difflib.get_close_matches(word, exp_list):
        # closest_matches always has 3 suggestions
        handle_closest_match(closest_matches[0])

    else:
        print("This word does not exist. Please check again.")


def handle_closest_match(match):
    decision = input(
        f"Did you mean {match}? Type Y for yes or N for no.")

    if decision == 'Y':
        alt = handle_query(match)
        handle_results(alt)

    else:
        return None


def clean_expressions(exp):
    clean_exp = []

    for e in exp:
        clean_exp.append(e[0])

    return clean_exp


while word != END:
    word = input("Enter a word: ")

    if word != END:
        result = handle_query(word)

        if result:
            handle_results(result)

        else:
            handle_no_results()

