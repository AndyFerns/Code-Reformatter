def generate(code, output, metadata):
    filename = f"experiment_{metadata['experiment_number']}.txt"

    with open(filename, "w") as f:
        # Header
        f.write(f"{metadata['name']:>50}\n")
        f.write(f"{metadata['class']:>50}\n")
        f.write(f"{metadata['roll_number']:>50}\n")
        f.write("\n")
        f.write(f"{'EXPERIMENT ' + metadata['experiment_number']:^50}\n")
        f.write("\n")

        # Code
        f.write("Code:\n")
        f.write("" + code + "\n")
        f.write("\n")

        # Output
        f.write("Output:\n")
        f.write(output + "\n")

    print(f"Text file generated: {filename}")
