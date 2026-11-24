import os

ENTRY = "I'm so sorry for your loss. Your grandfather was a wonderful man, and he will be deeply moose."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
