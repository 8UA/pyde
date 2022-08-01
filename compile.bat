@echo off
CALL nuitka --onefile --low-memory --enable-plugin=tk-inter --output-dir="src" --windows-icon-from-ico="src\resources\icon.ico" "src\pyde.py"
CALL echo "Creating bin folder... in (src\bin)"
CALL mkdir "src\bin"
CALL echo "Moving binary inside bin folder..."
CALL move /Y "src\pyde.exe" "src\bin"
CALL echo "Eating Leftovers..."
CALL rmdir /s /q "src\pyde.build" "src\pyde.dist" "src\pyde.onefile-build"
CALL echo "Done!"
