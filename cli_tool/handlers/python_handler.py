import subprocess
import tempfile
import os

def execute(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as tmp_file:
        tmp_file.write(code)
        tmp_file_path = tmp_file.name

    try:
        result = subprocess.run(
            ["python", tmp_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )
        output = result.stdout + result.stderr
    except Exception as e:
        output = str(e)
    finally:
        os.remove(tmp_file_path)

    return output
