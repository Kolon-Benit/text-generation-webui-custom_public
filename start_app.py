import subprocess
import os
print(subprocess.run(["python server.py --port " + str(os.environ['CDSW_APP_PORT'])], shell=True))