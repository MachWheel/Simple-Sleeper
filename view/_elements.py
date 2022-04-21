import PySimpleGUI as sg

from . import _icons
from ._labels import *

sg.theme('DarkBlue')

TITLE = (
    [
        sg.Text(
            APP_TITLE,
            font="Default 14 bold",
            p=((0, 5), (20, 3)),
        ),
        sg.Text(
            APP_VERSION,
            font="Default 10 italic",
            p=((0, 0), (20, 3)),
        ),
    ],
    [sg.Text(
        APP_SUBTITLE,
        font="Default 11 italic",
    )]
)

HEADINGS_STYLE = {
    'font': 'Default 12 bold'
}


def TIME_SLIDER(kind: str, min_max: tuple, starts_at: int):
    prefix = kind.upper()
    DISPLAY = sg.Text(
        f"{starts_at} {kind}",
        **HEADINGS_STYLE,
        key=f"-{prefix}_DISPLAY-",
        text_color='gold'
    )
    SLIDER = sg.Slider(
        range=min_max,
        default_value=starts_at,
        resolution=1,
        orientation='horizontal',
        disable_number_display=True,
        key=f"-{prefix}_SLIDER-",
        enable_events=True,
        size=(35, 20)
    )
    return DISPLAY, sg.Push(), SLIDER, sg.VPush()


BTN_STYLE = {
    'button_color': (sg.theme_background_color(),
                     sg.theme_background_color()),
    'border_width': 0,
}

APP_BTNS = (
    sg.Button(
        image_data=_icons.START(),
        **BTN_STYLE,
        tooltip=START_TOOLTIP,
        key="-START_BTN-"
    ),
    sg.Button(
        image_data=_icons.ABORT(),
        **BTN_STYLE,
        tooltip=ABORT_TOOLTIP,
        key="-ABORT_BTN-"
    )
)

MODE_SELECTOR = (
    sg.Text(MODE_HEADING, **HEADINGS_STYLE),
    sg.Combo(
        MODE_OPTIONS,
        MODE_OPTIONS[0],
        background_color=sg.theme_background_color(),
        readonly=True,
        text_color='yellow',
        font='Default 10 bold',
        size=(11, 1),
        key='-MODE_COMBO-'
    )
)
