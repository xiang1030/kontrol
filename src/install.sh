#!/bin/bash

text_desktop="[Desktop Entry]
 
Type=Application
Version=1.0                                                                      
Name=Kontrol
Exec=kontrol
Icon=kontrol
StartupWMClass=kontrol.py"

text_bin="""#!/bin/bash
python3 /home/amr/Projects/kontrol/kontrol.py"""

sudo echo "$text_desktop" > /usr/share/applications/kontrol.desktop
sudo echo "$text_bin" > /usr/bin/kontrol
sudo chmod +x /usr/bin/kontrol

sudo cp "icons/png/kontrol_16.png" "/usr/share/icons/hicolor/16x16/apps/kontrol.png"
sudo cp "icons/png/kontrol_20.png" "/usr/share/icons/hicolor/20x20/apps/kontrol.png"
sudo cp "icons/png/kontrol_22.png" "/usr/share/icons/hicolor/22x22/apps/kontrol.png"
sudo cp "icons/png/kontrol_24.png" "/usr/share/icons/hicolor/24x24/apps/kontrol.png"
sudo cp "icons/png/kontrol_32.png" "/usr/share/icons/hicolor/32x32/apps/kontrol.png"
sudo cp "icons/png/kontrol_36.png" "/usr/share/icons/hicolor/36x36/apps/kontrol.png"
sudo cp "icons/png/kontrol_40.png" "/usr/share/icons/hicolor/40x40/apps/kontrol.png"
sudo cp "icons/png/kontrol_48.png" "/usr/share/icons/hicolor/48x48/apps/kontrol.png"
sudo cp "icons/png/kontrol_64.png" "/usr/share/icons/hicolor/64x64/apps/kontrol.png"
sudo cp "icons/png/kontrol_72.png" "/usr/share/icons/hicolor/72x72/apps/kontrol.png"
sudo cp "icons/png/kontrol_96.png" "/usr/share/icons/hicolor/96x96/apps/kontrol.png"
sudo cp "icons/png/kontrol_128.png" "/usr/share/icons/hicolor/128x128/apps/kontrol.png"
sudo cp "icons/png/kontrol_192.png" "/usr/share/icons/hicolor/192x192/apps/kontrol.png"
sudo cp "icons/png/kontrol_256.png" "/usr/share/icons/hicolor/256x256/apps/kontrol.png"
sudo cp "icons/png/kontrol_512.png" "/usr/share/icons/hicolor/512x512/apps/kontrol.png"
sudo cp "icons/png/kontrol_1024.png" "/usr/share/icons/hicolor/1024x1024/apps/kontrol.png"
sudo cp "icons/png/kontrol_256.png" "/usr/share/pixmaps/kontrol.png"
sudo cp "icons/png/kontrol_256.svg" "/usr/share/icons/hicolor/scalable/apps/kontrol.svg"
