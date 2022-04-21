from PySimpleGUI import read_all_windows, WIN_CLOSED
from application import Application


class Controller:
    def __init__(self, window):
        self.window = window

    @staticmethod
    def read_events():
        window, event, values = read_all_windows()
        state = window, event, values

        if event and '_SLIDER-' in event:
            return _update_display(state)

        if event == '-START_BTN-':
            options = _read_options(state)
            Application(options).execute_shutdown()
            return 'done'

        if event == '-ABORT_BTN-':
            Application('/a').execute_shutdown()
            return 'done'

        if event == WIN_CLOSED:
            return 'done'


def _update_display(state: tuple):
    window, event, values = state
    selected = event.split('_SLIDER-')[0].strip('-')
    display = window[f'-{selected}_DISPLAY-']
    value = int(values[f'-{selected}_SLIDER-'])
    display.update(f"{value} {selected.lower()}")
    return


def _read_options(state: tuple):
    window, event, values = state
    time = _get_time(values)
    mode = _get_mode(values)
    return f"{mode} {time}"


def _get_time(values):
    hours = int(values[f'-HOURS_SLIDER-'])
    minutes = int(values[f'-MIN_SLIDER-'])
    seconds = (hours * 3600) + (minutes * 60)
    return f"/t {seconds}"


def _get_mode(values):
    shutdown_modes = {
        'Shut down': '/s /f',
        'Restart': '/r /f'
    }
    selected = values['-MODE_COMBO-']
    return shutdown_modes[selected]
