def slugify(sentence):
    words = sentence.strip().lower().split()
    return "_".join(words)


def analyze(text):
    clean = text.strip()
    words = clean.split()

    print(f"Characters (with spaces): {len(clean)}")
    print(f"Characters (no spaces): {len(clean.replace(' ', ''))}")
    print(f"Words: {len(words)}")
    print(f"Upper: {clean.upper()}")
    print(f"Reversed: {clean[::-1]}")
    print(f"Count of 'a': {clean.lower().count('a')}")
    print(f"Slug: {slugify(clean)}")
    print(f"First word: {words[0] if words else '-'}")
    print(f"Last word: {words[-1] if words else '-'}")
    print(f"Has 'python': {'python' in clean.lower()}")


english = "  Python is the Language of Agentic AI  "
persian = "  سلام دنیا من پایتون یاد میگیرم  "

print("--- English ---")
analyze(english)

print()
print("--- Persian ---")
analyze(persian)