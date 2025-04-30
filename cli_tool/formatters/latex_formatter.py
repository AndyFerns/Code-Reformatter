def generate(code: str, output: str, metadata: dict):
    language_map = {
        'python': 'Python',
        'c': 'C',
        'cpp': 'C++',
        'java': 'Java'
    }
    lang = metadata.get('lang', 'text').lower()
    latex_lang = language_map.get(lang, '')

    latex_content = f"""
\\documentclass[12pt]{{article}}
\\usepackage[margin=1in]{{geometry}}
\\usepackage{{fancyhdr}}
\\usepackage{{listings}}
\\usepackage{{xcolor}}
\\pagestyle{{fancy}}
\\fancyhf{{}}
\\rhead{{Name: {metadata['name']} \\ Class: {metadata['class']} \\ Roll No: {metadata['roll_number']}}}
\\begin{{document}}
\\begin{{center}}
    \\section*{{EXPERIMENT {metadata['experiment_number']}}}
\\end{{center}}

\\textbf{{Code:}}
\\begin{{lstlisting}}[language={latex_lang}, basicstyle=\ttfamily\small, breaklines=true, frame=single]
{code}
\\end{{lstlisting}}

\\textbf{{Output:}}
\\begin{{lstlisting}}[basicstyle=\ttfamily\small, breaklines=true, frame=single]
{output}
\\end{{lstlisting}}

\\end{{document}}
"""

    with open("output.tex", "w") as f:
        f.write(latex_content)

    print("[✔] LaTeX file 'output.tex' has been generated.")
