from constants import RESOLUTION
from func_utils import get_ISO_times
import pandas as pd
import numpy as np
import time
from pprint import pprint

# Get relevant time periods ofr ISO from and to
ISO_TIMES = get_ISO_times()
pprint(ISO_TIMES)

# Constract prices
def constract_prices(client):
    pass