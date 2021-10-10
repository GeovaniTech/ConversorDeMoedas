import cx_Freeze

executables = [cx_Freeze.Executable('ConvertCoin - App.py', icon='View/QRC/LogoIco.ico', base='Win32GUI')]

cx_Freeze.setup(
    name="ConvertCoin",
    options={'build_exe': {'packages': ['PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'sys'],
                           'include_files': ['View/']}},
    executables=executables
)