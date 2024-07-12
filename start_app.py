!ldconfig -v
!nvidia-smi
import subprocess
import os
print(subprocess.run(["python server.py"], shell=True))