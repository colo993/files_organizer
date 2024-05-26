import os
import json

EXTENSIONS_DATA = None
def get_extensions_data():
    """Read file with the list of supported extensions."""
    global EXTENSIONS_DATA
    if EXTENSIONS_DATA is None:
        EXTENSIONS_DATA = json.load(open("%s/extensions_data.json"%(os.path.dirname(__file__))))
    return EXTENSIONS_DATA
