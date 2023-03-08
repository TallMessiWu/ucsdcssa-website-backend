cd ../courses-qr-codes
rename 's/\.jpeg/\.jpg/' *
rename 's/\.JPG/\.jpg/' *
cd ../members-photos
rename 's/\.jpeg/\.jpg/' *
rename 's/\.JPG/\.jpg/' *
cd ../departments-group-photos
rename 's/\.jpeg/\.jpg/' *
rename 's/\.JPG/\.jpg/' *
cd ../utils
python3 get_classes_grouped_json.py
python3 get_members_grouped_json.py
