import sys

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

def get_state(search):
    items = [s.strip() for s in search.split(",") if s.strip()]
    if not (1 <= len(items) <= 10):
        return

    states_lu = {name.lower(): name for name in states}
    capitals_lu = {cap.lower(): code for code, cap in capital_cities.items()}
    reverse_states = {code: name for name, code in states.items()}

    for item in items:
        key = item.lower()
        if key in states_lu:
            state = states_lu[key]
            capital = capital_cities[states[state]]
            print(f"{capital} is the capital of {state}")
        elif key in capitals_lu:
            code = capitals_lu[key]
            capital = capital_cities[code]
            state = reverse_states[code]
            print(f"{capital} is the capital of {state}")
        else:
            print(f"{item} is neither a capital city nor a state")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)
    get_state(sys.argv[1])
