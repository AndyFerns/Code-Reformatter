import subprocess
import tempfile
import os

def execute(code):
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, "program.cpp")
        binary_path = os.path.join(temp_dir, "program.out")

        with open(source_path, "w") as src_file:
            src_file.write(code)

        compile_result = subprocess.run(
            ["g++", source_path, "-o", binary_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if compile_result.returncode != 0:
            return compile_result.stderr

        run_result = subprocess.run(
            [binary_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )

        return run_result.stdout + run_result.stderr
