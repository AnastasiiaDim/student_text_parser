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
    logging.info(f"--------Statistics for {file_name.name}--------")
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

            logging.info(f"Words: {len(words)} | Sentences: {len(sentences)} | Emails: {len(emails)} | Dates: {len(dates)}")
            if emails:
                logging.info(f"Emails found: {', '.join(emails)}")
            if dates:
                logging.info(f"Dates found: {', '.join(dates)}")

    except FileNotFoundError:
        logging.error(f"File not found: {file_name}")

summary = {
    "total_files": len(results),
    "total_words": sum(r["words_count"] for r in results.values()),
    "total_sentences": sum(r["sentences"] for r in results.values()),
    "files_with_emails": sum(1 for r in results.values() if r["emails"]),
    "files_with_dates": sum(1 for r in results.values() if r["dates"]),
}

output = {"summary": summary, "results": results}

with open("report.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4, ensure_ascii=False)

logging.info("Report saved to report.json")

