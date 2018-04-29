import os
import re

os.system("python HTMLparser.py | awk -F'<title>' '{print $1,$2,$3,$4,$5,$6,$7,$8,$9}'")