# Student Text Parser

_A robust Python-based utility designed to automate the analysis of student assignments.
It scans a directory of .txt files, extracts key metadata using regular expressions,
and generates a structured JSON report along with detailed execution logs._

## 🚀 Key Features
_Automated Extraction: Scans text for:_

- Word count.
- Sentence count (detecting English sentence structures).
- Email addresses (supporting complex domain formats).
- Dates (supporting multiple separators: ., -, or /).
- Dual-Stream Logging: Real-time console output plus a persistent parser.log file for auditing.
- Structured Output: Generates a comprehensive report.json containing both individual file statistics 
and a global summary.
- Modern Path Handling: Built using pathlib for cross-platform compatibility.

## 🛠 Project Structure
├── main.py: The core script containing the processing logic and Regex patterns.

├── student_texts/: Input directory where student .txt files should be placed.

├── report.json: The final analytical output.

├── parser.log: Execution history and error tracking.

## 🛠️ Tech Stack

_Language:_ Python 3.14