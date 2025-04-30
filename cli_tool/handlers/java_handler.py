import subprocess
import tempfile
import os

def execute(code):
    with tempfile.TemporaryDirectory() as temp_dir:
        java_file_path = os.path.join(temp_dir, "Main.java")

        with open(java_file_path, "w") as java_file:
            java_file.write(code)

        compile_result = subprocess.run(
            ["javac", java_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if compile_result.returncode != 0:
            return compile_result.stderr

        run_result = subprocess.run(
            ["java", "-cp", temp_dir, "Main"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )

        return run_result.stdout + run_result.stderr
