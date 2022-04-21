from os import startfile

from generator._partial import HEADER, FOOTER

_TXTS_DIR = 'resources/partial'
_OUTPUT_FILE = 'resources\\turn_off.bat'


class Generator:
    @staticmethod
    def make_turn_off_bat(options):
        cmd = (f"{HEADER}"
               f"SHUTDOWN {options}"
               f"{FOOTER}")
        with open(_OUTPUT_FILE, 'w') as file:
            file.writelines(cmd)

    @staticmethod
    def run_turn_off_bat():
        startfile(_OUTPUT_FILE)
