import sys
import os
import re

SETTINGS_FILE = "settings.py"

def error_exit(message, code=1):
    print(message, file=sys.stderr)
    sys.exit(code)

def validate_template(template):
    if not template.endswith(".template"):
        error_exit("Usage: python3 render.py <filename>.template")

def check_file_exists(filepath):
    if not os.path.exists(filepath):
        error_exit(f"Error: {filepath} not found")

def load_settings():
    check_file_exists(SETTINGS_FILE)
    namespace = {}
    exec(open(SETTINGS_FILE).read(), namespace)
    return namespace

def read_template(template):
    check_file_exists(template)
    with open(template) as f:
        return f.read()

def substitute_variables(content, namespace):
    def replace_var(match):
        var_name = match.group(1)
        return str(namespace.get(var_name, match.group(0)))
    return re.sub(r'\{(\w+)\}', replace_var, content)

def write_output(template, content):
    output_file = template.replace(".template", ".html")
    with open(output_file, "w") as f:
        f.write(content.strip())

def render(template):
    validate_template(template)
    namespace = load_settings()
    content = read_template(template)
    result = substitute_variables(content, namespace)
    write_output(template, result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        error_exit("Usage: python3 render.py <filename>.template")
    render(sys.argv[1])