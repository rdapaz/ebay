#generateAuctions.py

from pathlib import Path
from markdown import markdown
import os
import re

cwd = Path.cwd()

for subdir, dirs, files in os.walk(cwd):
	for my_file in files:
		if re.search(r'\.md$', my_file):
			with open(os.path.join(cwd, my_file),'r') as fin:
				raw_text = fin.read()
			with open(os.path.join(cwd, 'html', f'{my_file}.html'),'w') as fout:
				html_text = markdown(raw_text)
				fout.write(html_text)