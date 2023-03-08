cd ../courses-qr-codes
rename 's/\.jpeg/\.jpg/' *
rename 's/\.JPG/\.jpg/' *
cd ../members-photos
rename 's/\.jpeg/\.jpg/' *
rename 's/\.JPG/\.jpg/' *
cd ../utils
python3 get_classes_grouped_json.py
