@echo off
cd ../courses-qr-codes
ren *.jpeg *.jpg
ren *.JPG *.jpg
cd ../members-photos
ren *.jpeg *.jpg
ren *.JPG *.jpg
cd ../departments-group-photos
ren *.jpeg *.jpg
ren *.JPG *.jpg
cd ../utils
python get_classes_grouped_json.py
python get_members_grouped_json.py
