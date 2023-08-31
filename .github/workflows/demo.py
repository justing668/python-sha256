name: pyinstaller
on: workflow_dispatch

jobs:
  build-on-windows:
    run-on: windows-2022
    steps:
      - name: checkout code
        uses: actions/checkout@v3
      - name: install pyinstaller
        run: pip install pyinstaller
      - name: build exe
        run: pyinstaller sha256.py -F
