# 🧾 Code Formatter CLI

A simple command-line tool to generate well-formatted **experiment reports** from your code in **Python, C, C++, or Java**, along with its **compiled output**.  
Built out of absolute laziness and the compulsion to **save time** and focus on the really important work at hand (writing the code).

Output formats include: **DOCX**, **LaTeX** and **Plain Text**. (In the order of usage priority)

---

## ✨ Features

- ✅ Supports **Python**, **C**, **C++**, and **Java** code
- 🧠 Custom metadata:
  - Student Name
  - Class
  - Roll Number
  - Experiment Number
- 📄 Formats the code and its output into:
  - Microsoft Word (.docx)
  - Plain text (.txt)
  - LaTeX (.tex)
- ⚙️ CLI options for:
  - Custom config path
  - Interactive mode
  - Version display
  - Script-based automation
  
---

## 📦 Installation

1. Clone the git repository

    ```bash
    git clone https://github.com/AndyFerns/Code-Reformatter
    cd Code-Reformatter
    pip install .
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Usage

```console
formatcode 
[-h] 
[--input INPUT] 
[--language LANGUAGE] 
[--code-file CODE_FILE] 
[--format FORMAT] 
[--interactive] 
[--version]
```

--code-file: Path to the source code file

--language: Programming language (python, c, cpp, java)

--format: Output format (docx, txt, latex)

--interactive: Launch an interactive session (prompts for code, language, and format)

--input: Path to custom metadata JSON config

--version: Display version info

---

## Output Examples

```docx
                                        Name: Alice Doe              
                                        Class: SE-A            
                                        Roll No: 42

                EXPERIMENT 03

Code:
[Code block here]

Output:
[Compiled output here]

```

---

## Contributions

Contributions are welcome! If you'd like to contribute, please:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add feature description"
   ```

4. Push to your forked repository and create a pull request.

---

## Contact

If you have any questions or suggestions, feel free to reach out:

- Email: <write2andrew.important@gmail.com>
