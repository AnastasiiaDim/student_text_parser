import re
import json
import logging
import os

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("parser.log"), logging.StreamHandler()],
)

#
# Process the files

student_folder = "C:\\Users\\Анастасия\\Desktop\\python_codes_in_txt\\student_texts"
student_files = []
student_contents = []

if not os.path.exists(student_folder):
    raise FileNotFoundError(f"Check your path: {student_folder}")

for file_name in os.listdir(student_folder):
    full_path = os.path.join(student_folder, file_name)

    if os.path.isfile(full_path):
        student_files.append(file_name)

        with open(full_path, "r") as f:
            student_contents.append(f.read())

student_texts = dict(zip(student_files, student_contents))
print(student_texts)