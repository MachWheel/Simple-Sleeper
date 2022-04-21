from os import startfile, remove
from time import sleep

from ._partial import HEADER, FOOTER

_TXTS_DIR = 'resources/partial'
_OUTPUT_FILE = 'turn_off.bat'


class Application:
    def __init__(self, options: str):
        self._options = options

    def execute_shutdown(self):
        self._make_bat_file()
        startfile(_OUTPUT_FILE)
        sleep(3)
        remove(_OUTPUT_FILE)

    def _make_bat_file(self):
        options = self._options
        cmd = (
            f"{HEADER}"
            f"SHUTDOWN {options}"
            f"{FOOTER}"
        )
        with open(_OUTPUT_FILE, 'w') as bat:
            bat.writelines(cmd)
