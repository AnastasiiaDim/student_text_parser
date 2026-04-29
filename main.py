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

# Compile Patterns
word_pattern = re.compile(r"\w+")
email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
date_pattern = re.compile(r"\b\d{2}[-./]\d{2}[-./]\d{4}\b")
sentence_pattern = re.compile(r"[A-Z].*?[\.!?](?=\s|$)", re.S)

# Process the files

student_folder = Path("C:\\Users\\Анастасия\\Desktop\\python_codes_in_txt\\student_texts")

#student_texts = {
#    file.name : file.read_text(encoding="utf-8")
#    for file in student_folder.iterdir()
#   if file.is_file() and file.suffix == ".txt"
#}

results = {}

for file_name in student_folder.iterdir():
    logging.info(f"Processing {file_name.name}")

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            text = f.read()
            words = word_pattern.findall(text)
            emails = email_pattern.findall(text)
            dates = date_pattern.findall(text)
            sentences = sentence_pattern.findall(text)

            results[file_name.name] = {
                "words_count": len(words),
                "emails": emails,
                "dates": dates,
                "sentences_count": len(sentences)
            }
            logging.info(f"--------Statistics for {file_name.name}--------")
            logging.info(f"Done: {len(words)} words found")
            logging.info(f"Done: {len(sentences)} sentences found")
            if emails:
                logging.info(f"Emails found:\n{'\n'.join(emails)}")
            if dates:
                logging.info(f"Dates found:\n{'\n'.join(dates)}")

    except FileNotFoundError:
        logging.warning(f"File not found: {file_name}")

with open("report.json", "w") as f:
    json.dump(results, f, indent=4)

logging.info("Report saved to report.json")

