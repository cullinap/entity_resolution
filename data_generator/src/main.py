from data_generators.name_generator import NameGenerator

def main():
    name_gen = NameGenerator()

    names = name_gen.generate(10)

    for name in names:
        print(f"Name {name}")

if __name__ == "__main__":
    main()