from application import Application
from view import MAIN_WINDOW


def main(app: Application):

    while True:
        status = app.read_events()
        if status == 'done':
            break
    return 0


if __name__ == '__main__':
    main(Application(MAIN_WINDOW()))
