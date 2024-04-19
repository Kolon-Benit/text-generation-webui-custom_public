import subprocess
import os
print(subprocess.run(["python server.py --port=${CDSW_APP_PORT}"], shell=True))