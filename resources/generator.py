from os import startfile

_TXTS_DIR = 'resources/partial'
_OUTPUT_FILE = 'resources\\turn_off.bat'

class Generator:

    @staticmethod
    def make_turn_off_bat(options):
        header, footer = _load_txts(
            ['header', 'footer']
        )
        cmd = (f"{header}"
               f"SHUTDOWN {options}"
               f"{footer}")
        with open(_OUTPUT_FILE, 'w') as file:
            file.writelines(cmd)

    @staticmethod
    def run_turn_off_bat():
        startfile(_OUTPUT_FILE)


def _load_txts(file_names: list):
    txts = []
    for name in file_names:
        txt_file = f'{_TXTS_DIR}/{name}.txt'
        with open(txt_file, 'r') as file:
            txts.append(file.read())
    return txts
