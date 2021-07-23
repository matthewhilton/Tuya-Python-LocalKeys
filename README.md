# Tuya-Python-LocalKeys

Easily get your Localkeys to control Tuya devices locally. 

Simple python script, portable and easy to use.

## Setup
If you already have a preferences.xml file, skip to step 7
1. Download [Bluestacks](https://www.bluestacks.com/) and [Bluestacks Tweaker](https://bstweaker.tk/)
2. Install Smart Life 3.6.1 (version is important!) onto the Bluestacks emulator. [APK Link](https://www.apkmirror.com/apk/volcano-technology-limited/smart-life-smart-living/smart-life-smart-living-3-6-1-release/smart-life-smart-living-3-6-1-android-apk-download/)
3. Sign up or Login to Smart Life and pair Tuya devices to an account (this is only needed temporarily, and can be deleted later).
4. Once devices are associated, load Blue Stacks Tweaker and select the running Bluestacks instance
5. Open File Mananger and navigate to data/data/com.tuya.smartlife/shared_prefs
6. Locate the file preferences_global_key\<account id\>.xml. (E.g. preferences_global_keyag4622356265159tBQwp.xml) and copy it somewhere onto your computer
7. Run the python script LocalTuyaKeys.py and select the preferences file that you just copied.
8. Done! A CSV file with devices and keys will be generated in the same directory as the python script.
