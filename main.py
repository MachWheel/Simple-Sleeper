from controller import Controller
from view import MAIN_WINDOW


def main(app: Controller):
    while True:
        status = app.read_events()
        if status == 'done':
            break
    return 0


if __name__ == '__main__':
    main(Controller(MAIN_WINDOW()))
