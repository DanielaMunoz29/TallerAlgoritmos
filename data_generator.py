import os
import random

SIZES = [10000, 100000, 1000000]
DATA_DIR = "data"

def generate_file(size: int):
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, f"data_{size}.txt")

    if os.path.exists(path):
        print(f"Ya existe: {path}")
        return

    with open(path, "w", encoding="utf-8") as f:
        for _ in range(size):
            number = random.randint(10_000_000, 99_999_999)
            f.write(f"{number}\n")

    print(f"Archivo generado: {path}")

def main():
    for size in SIZES:
        generate_file(size)

if __name__ == "__main__":
    main()