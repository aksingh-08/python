# Write a function classify_language(name) that returns the execution model for each language: "compiled", "interpreted", "bytecode-vm", or "jit-compiled".

def classify_language(name):
    categories = {
        "C": "compiled",
        "Rust": "compiled",
        "Go": "compiled",
        "Java": "bytecode-vm",
        "Python": "bytecode-vm",
        "C#": "bytecode-vm",
        "Bash": "interpreted",
        "JavaScript": "jit-compiled"
    }
    return categories.get(name, "unknown")
    
for lang in ["C", "Java", "Python", "Bash", "Rust", "JavaScript", "hindi"]:
    print(f"{lang}: {classify_language(lang)}")