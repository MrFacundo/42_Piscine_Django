import sys

def get_state(search):
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
    
    search_items = search.split(",")
    if len(search_items) < 1 or len(search_items) > 10:
        return

    reverse_capitals = {v: k for k, v in capital_cities.items()}
    reverse_states = {v:k for k, v in states.items()}

    for item in search_items:
        state_match = states.get(item)
        if state_match:
            print(f"{state_match} is a state")
            return
        capital_match = reverse_capitals.get(item)
        if capital_match:
            print(f"{capital_match} is the capital of {reverse_states.get(reverse_capitals.get(capital_match))}")
            return
        print(f"{item} is neither a capital city nor a state")
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)
    get_state(sys.argv[1])
