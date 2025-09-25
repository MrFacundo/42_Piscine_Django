MAX_COLUMNS = 18
MAX_ROWS = 7
PERIOD_1_START = 1
PERIOD_1_END = 2
PERIOD_2_START = 3
PERIOD_2_END = 10
PERIOD_3_START = 11
PERIOD_3_END = 18
PERIOD_4_START = 19
PERIOD_4_END = 36
PERIOD_5_START = 37
PERIOD_5_END = 54
PERIOD_6_START = 55
PERIOD_6_END = 86
PERIOD_7_START = 87
PERIOD_7_END = 118

LANTHANIDE_START = 57
LANTHANIDE_END = 71
ACTINIDE_START = 89
ACTINIDE_END = 103

PERIOD_RANGES = [
    (PERIOD_1_START, PERIOD_1_END),
    (PERIOD_2_START, PERIOD_2_END),
    (PERIOD_3_START, PERIOD_3_END),
    (PERIOD_4_START, PERIOD_4_END),
    (PERIOD_5_START, PERIOD_5_END),
    (PERIOD_6_START, PERIOD_6_END),
    (PERIOD_7_START, PERIOD_7_END),
]

INPUT_FILE = "./periodic_table.txt"
CSS_FILE = "periodic.css"


def parse_line(line):
    name, rest = line.split("=", 1)
    fields = dict(part.split(":", 1) for part in rest.split(","))
    fields = {k.strip(): v.strip() for k, v in fields.items()}
    fields["name"] = name.strip()
    fields["number"] = int(fields["number"])
    fields["position"] = int(fields["position"])
    return fields


def period(n):
    for idx, (low, high) in enumerate(PERIOD_RANGES, start=1):
        if low <= n <= high:
            return idx
    return MAX_ROWS


def build_grid(elements):
    grid = [[None for _ in range(MAX_COLUMNS)] for _ in range(MAX_ROWS)]
    for e in elements:
        row = period(e["number"]) - 1
        col = e["position"]

        if LANTHANIDE_START <= e["number"] <= LANTHANIDE_END:
            continue
        elif ACTINIDE_START <= e["number"] <= ACTINIDE_END:
            continue

        if row < MAX_ROWS and col < MAX_COLUMNS:
            grid[row][col] = e
    return grid


def element_list(e):
    return (
        "<ul>"
        f"<li>No {e['number']}</li>"
        f"<li>{e['small']}</li>"
        f"<li>{e['molar']}</li>"
        f"<li>{e['electron']} electron</li>"
        "</ul>"
    )


def element_html(e):
    if not e:
        return "<td></td>"
    return f"<td class='element-cell'><h4>{e['name']}</h4>{element_list(e)}</td>"


def write_css():
    css_content = """
						.element-cell {
						border: 1px solid black;
						padding: 10px;
						vertical-align: top;
						}
						table {
						border-collapse: collapse;
						}
						h4 {
						margin: 0;
						}
						ul {
						margin: 5px 0;
						}
					"""
    with open(CSS_FILE, "w") as f:
        f.write(css_content.strip())


def build_html():
    write_css()
    with open(INPUT_FILE) as f:
        elements = [parse_line(l.strip()) for l in f if l.strip()]
    grid = build_grid(elements)
    with open("periodic_table.html", "w") as out:
        out.write(
            f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><title>Periodic Table</title><link rel='stylesheet' href='{CSS_FILE}'></head><body><table>"
        )
        for row in grid:
            out.write("<tr>" + "".join(element_html(c) for c in row) + "</tr>")
        out.write("</table></body></html>")


if __name__ == "__main__":
    build_html()
