cd ../assets/courses-qr-codes
rename 's/\.jpeg/\.jpg/' *
rename 's/\.JPG/\.jpg/' *
cd ../members-photos
rename 's/\.jpeg/\.jpg/' *
rename 's/\.JPG/\.jpg/' *
cd ../departments-group-photos
rename 's/\.jpeg/\.jpg/' *
rename 's/\.JPG/\.jpg/' *
cd ../../utils
python3 get_courses_grouped_json.py
python3 get_department_json.py
