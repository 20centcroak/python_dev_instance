# this may be called from parent folder of module1 with python -m module1

from module2 import scriptb

from . import scripta
from . import another_script

if __name__ == "__main__":
    print("launch module1")
    another_script.reprint(scripta.script + scriptb.script)
