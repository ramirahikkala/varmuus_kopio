import os
from pathlib import Path
from dirsync import sync

try:

	arkisto_path = Path(os.environ['USERPROFILE'], 'Desktop', 'Arkisto') 

	drives = [ chr(x) + ":/" for x in range(65,91) if x != 43 and os.path.exists(chr(x) + ":") ]

	for drive in drives:
		varmuus_kopio_path = Path(drive, 'arkisto_varmuuskopio')
		if varmuus_kopio_path.is_dir():
			sync(arkisto_path, varmuus_kopio_path, 'sync')

except Exception as e:
	print(e)
	input("\n\n\nEi onnistunut. Pyydä Rami apuun!")


