#!"c:\users\zakaria abdessamed\desktop\mindset-master\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'python-card-me==0.9.3','console_scripts','ics_diff'
__requires__ = 'python-card-me==0.9.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('python-card-me==0.9.3', 'console_scripts', 'ics_diff')()
    )