import core


if __name__ == "__main__":
    game = core.Engine(7, 7)
    try:
        game.main()
    except KeyboardInterrupt:
        print("\nExit game.")
