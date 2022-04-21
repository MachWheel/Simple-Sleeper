import PySimpleGUI as sg

from ._elements import TITLE, TIME_SLIDER, MODE_SELECTOR, APP_BTNS
from ._labels import APP_TITLE


def MAIN_WINDOW():
    return sg.Window(
        APP_TITLE,
        [
            *TITLE,
            [TIME_SLIDER(kind='hours', min_max=(0, 24), starts_at=0)],
            [TIME_SLIDER(kind='min', min_max=(0, 60), starts_at=15)],
            [*MODE_SELECTOR, sg.Push(), *APP_BTNS],
        ],
        size=(380, 230),
        element_justification='center',
        text_justification='center',
        finalize=True
    )
