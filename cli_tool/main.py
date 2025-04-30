import os
import subprocess
from cli_tool.handlers import python_handler, c_handler, cpp_handler, java_handler
from cli_tool.formatters import txt_formatter, latex_formatter, docx_formatter

def get_user_input():
    print("Enter your details:")
    name = input("Name: ")
    class_name = input("Class: ")
    roll_number = input("Roll Number: ")
    experiment_number = input("Experiment Number: ")
    
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

    metadata = {
        "name": name,
        "class": class_name,
        "roll_number": roll_number,
        "experiment_number": experiment_number
    }
    return language, code, metadata, output_format

def run():
    language, code, metadata, output_format = get_user_input()

    if language.lower() == "python":
        output = python_handler.execute(code)
    elif language.lower() == "c":
        output = c_handler.execute(code)
    elif language.lower() == "c++":
        output = cpp_handler.execute(code)
    elif language.lower() == "java":
        output = java_handler.execute(code)
    else:
        print("Unsupported language")
        return

    if output_format == "txt":
        txt_formatter.generate(code, output, metadata)
    elif output_format == "latex":
        latex_formatter.generate(code, output, metadata)
    elif output_format == "docx":
        docx_formatter.generate(code, output, metadata)
    else:
        print("Unsupported format")

if __name__ == '__main__':
    run()
