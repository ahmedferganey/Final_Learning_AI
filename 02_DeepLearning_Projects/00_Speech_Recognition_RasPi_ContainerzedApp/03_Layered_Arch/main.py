from app import AppController


def main():
    try:
        controller = AppController()
        controller.run()
    except KeyboardInterrupt:
        print("\nStopped by user.")


if __name__ == "__main__":
    main()
