#!/usr/local/bin/python3

import os
from datetime import datetime

hoy = datetime.now()

año = hoy.year
mes = hoy.month
día = hoy.day

fecha = f"#journal/{año}/{mes}/{día}"
os.system(f"echo '{fecha}' | pbcopy")
print(fecha)
print("y se copió al portapapeles")
