
# Convert-PDF-to-.apkg (Flexible Version)

This project extracts vocabulary words from a **tabular PDF file** and generates an Anki deck (`.apkg`) for effective SAT Verbal preparation or general vocabulary learning.

---

## ✅ Features

- Parses a vocabulary PDF file with table structure.
- **User-configurable** filtering: skip headers or unwanted rows based on keywords.
- Extracts essential fields:
  - **Front**: Vocabulary word
  - **Back**: Definition + Example sentence
- Generates `.apkg` file ready to import into Anki.
- Optionally exports a `.csv` file for backup or preview.

---

## 📂 Expected Table Format

Each row in the PDF should follow this general format:

`No | Word | Word Type | Definition | Example Sentence | Meaning (optional)`

> **Note:** The script only requires **Word**, **Definition**, and **Example** columns (usually columns 2, 4, and 5 respectively).

---

## 🚀 How to Use

1. **Install Requirements**

```bash
pip install pdfplumber genanki
```

2. **Edit Configuration in Script**

Modify these variables at the top of the script:

```python
pdf_path = 'your_file.pdf'  # Your actual PDF filename
exclude_keywords = ['BUỔI', 'STT', 'SAT VOCABULARY']  # Keywords to skip
```

3. **Run the Script**

```bash
python convert_to_apkg.py
```

4. **Output**

- `vocabulary_deck.apkg`: Import into Anki
- `vocabulary_table.csv`: (Optional) Cleaned vocabulary data

---

## 🧠 Flashcard Format

- **Front**: Word
- **Back**: Definition + _Example sentence_

---

## 🧹 Data Cleaning

The script automatically skips:

- Rows containing any keyword in `exclude_keywords`
- Duplicate or nested headers
- Rows with less than 5 columns

---

## ✨ Example

If a row in the PDF looks like this:

| 21 | **benevolent** | adj | kind and generous | She was a benevolent teacher. | Một giáo viên tử tế (Vietnamese or your native language) |

The flashcard will look like:

- **Front**: benevolent
- **Back**: kind and generous  
  _She was a benevolent teacher._

---

## 💡 Notes

- PDF must contain a **real table structure**, not plain text.
- Users can update `exclude_keywords` to match any unexpected headers or titles in their PDF.

