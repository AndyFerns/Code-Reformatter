import os
import json
import subprocess
from cli_tool.handlers import python_handler, c_handler, cpp_handler, java_handler
from cli_tool.formatters import txt_formatter, latex_formatter, docx_formatter
from cli_tool.arg_cli import get_cli_args 

# Path to default config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

def load_metadata(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] Metadata file not found: {path}")
        return None
    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON format in: {path}")
        return None

def read_code_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERROR] Code file not found: {file_path}")
        return None

def execute_code(language, code):
    lang = language.lower()
    if lang == "python":
        return python_handler.execute(code)
    elif lang == "c":
        return c_handler.execute(code)
    elif lang == "c++":
        return cpp_handler.execute(code)
    elif lang == "java":
        return java_handler.execute(code)
    else:
        print("[ERROR] Unsupported language.")
        return None

def generate_output(format, code, output, metadata):
    fmt = format.lower()
    if fmt == "txt":
        txt_formatter.generate(code, output, metadata)
    elif fmt == "latex":
        latex_formatter.generate(code, output, metadata)
    elif fmt == "docx":
        docx_formatter.generate(code, output, metadata)
    else:
        print("[ERROR] Unsupported output format.")

def interactive_mode():
    metadata = load_metadata(CONFIG_PATH)
    if metadata is None:
        return

    metadata["experiment_number"] = input("Experiment number: ")
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

    output = execute_code(language, code)
    if output is not None:
        generate_output(output_format, code, output, metadata)

def main():
    args = get_cli_args(CONFIG_PATH)

    if args.interactive:
        interactive_mode()
        return

    # Non-interactive mode requires all these
    if not (args.language and args.code_file and args.format):
        print("[ERROR] Missing required arguments. Use --help for usage.")
        return

    metadata = load_metadata(args.input)
    if metadata is None:
        return

    metadata["experiment_number"] = input("Experiment number: ")

    code = read_code_from_file(args.code_file)
    if code is None:
        return

    output = execute_code(args.language, code)
    if output is not None:
        generate_output(args.format, code, output, metadata)

if __name__ == '__main__':
    main()