import sys

def get_state(capital):
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

    reverse_capitals = {v: k for k, v in capital_cities.items()}
    initial = reverse_capitals.get(capital)
    reverse_states = {v:k for k, v in states.items()}
    print(reverse_states.get(initial, "unknown"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)
    get_state(sys.argv[1])
