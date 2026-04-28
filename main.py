import re
import json
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("parser.log"), logging.StreamHandler()],
)

#
# Process the files

student_folder = Path("C:\\Users\\Анастасия\\Desktop\\python_codes_in_txt\\student_texts")

student_texts = {
    file.name : file.read_text(encoding="utf-8")
    for file in student_folder.iterdir()
    if file.is_file() and file.suffix == ".txt"
}

print(student_texts)