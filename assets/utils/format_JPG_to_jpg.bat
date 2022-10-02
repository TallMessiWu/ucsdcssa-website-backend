@echo off
cd ../courses-qr-codes
ren *.JPG *.jpg
cd ../utils
python3 get_classes_grouped_json.py
