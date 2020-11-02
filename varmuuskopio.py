import os
from pathlib import Path
from dirsync import sync

try:

	drives = [ chr(x) + ":/" for x in range(65,91) if x != 43 and os.path.exists(chr(x) + ":") ]

	varmuuskopio_path = None
	arkisto_path = None

	for drive in drives:

		if not varmuuskopio_path:
			varmuuskopio_path = Path(drive, 'arkisto_varmuuskopio')
			if not varmuuskopio_path.is_dir():
				varmuuskopio_path = None

		if not arkisto_path:
			arkisto_path = Path(drive, 'arkisto')
			if not arkisto_path.is_dir():
				arkisto_path = None

		if arkisto_path and varmuuskopio_path:
			sync(arkisto_path, varmuuskopio_path, 'sync')

	if not varmuuskopio_path:
		input("Varmuuskopiomuistitikku puuttuu! Paina enter poistuaksesi...")

	if not arkisto_path:
		input("Arkistomuistitikku puuttuu! Paina enter poistuaksesi...")


except Exception as e:
	print(e)
	input("\n\n\nEi onnistunut. Pyydä Rami apuun!")


