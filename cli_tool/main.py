import os
import json
import subprocess
from cli_tool.handlers import python_handler, c_handler, cpp_handler, java_handler
from cli_tool.formatters import txt_formatter, latex_formatter, docx_formatter

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

def get_user_input():
    try:
        with open(CONFIG_PATH, 'r') as f:
            metadata = json.load(f)
            metadata["experiment_number"] = input("Experiment number: ")
    except FileNotFoundError:
        print(f"[ERROR] config.json not found at {CONFIG_PATH}")
        return None, None, None, None

    language = input("Programming Language (Python/C/C++/Java): ").strip()
    print("Enter your code (end with a single line containing only 'END'):")
    code_lines = []
    while True:
        line = input()
        if line.strip() == 'END':
            break
        code_lines.append(line)
    code = "\n".join(code_lines)

    output_format = input("Output format (txt/latex/docx): ").strip()

    # Return only if all required fields are filled
    if not (language and code and output_format and metadata):
        return None, None, None, None

    return language, code, metadata, output_format


def run():
    language, code, metadata, output_format = get_user_input()

    if not all([language, code, metadata, output_format]):
        print("[ERROR] Missing input. Exiting.")
        return

    # Code Language support
    lang = language.lower() # type: ignore
    if lang == "python":
        output = python_handler.execute(code)
    elif lang == "c":
        output = c_handler.execute(code)
    elif lang == "c++":
        output = cpp_handler.execute(code)
    elif lang == "java":
        output = java_handler.execute(code)
    else:
        print("Unsupported language")
        return

    # Code Output Formatters
    fmt = output_format.lower() # type: ignore
    if fmt == "txt":
        txt_formatter.generate(code, output, metadata)
    elif fmt == "latex":
        latex_formatter.generate(code, output, metadata) # type: ignore
    elif fmt == "docx":
        docx_formatter.generate(code, output, metadata)
    else:
        print("Unsupported format")


if __name__ == '__main__':
    run()
