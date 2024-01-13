import core


if __name__ == "__main__":
    game = core.Engine(7, 9)
    try:
        game.main()
    except KeyboardInterrupt:
        print("\nExit game.")
