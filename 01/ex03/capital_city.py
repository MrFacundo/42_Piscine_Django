import sys

def get_capital(state):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO",
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver",
    }


    print(capital_cities.get(states.get(state), "Unknown state"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)
    get_capital(sys.argv[1])
