from randnd.randomizer import Randomizer


def main():
    r = Randomizer()
    r.generate_gender()
    print(r.character.gender)


if __name__ == "__main__":
    main()
