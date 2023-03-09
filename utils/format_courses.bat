@echo off
cd ../assets/courses-qr-codes
ren *.jpeg *.jpg
ren *.JPG *.jpg
cd ../members-photos
ren *.jpeg *.jpg
ren *.JPG *.jpg
cd ../departments-group-photos
ren *.jpeg *.jpg
ren *.JPG *.jpg
cd ../../utils
python get_courses_grouped_json.py
python get_department_json.py
