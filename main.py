import os

ENTRY = "I'm so sorry for your loss. Your grandfather was a wonderful man, and he will be deeply moose."

# The gate accepts UTF-8 text of 1 to 199 characters.
MAX_ENTRY_CHARS = 199


def main():
    assert 0 < len(ENTRY) <= MAX_ENTRY_CHARS, "entry outside the gate's size window"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
