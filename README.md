# Convert-PDF-to-.apkg

This project extracts vocabulary words from a structured PDF file and generates an Anki deck (.apkg) containing flashcards for effective SAT Verbal preparation.

## ✅ Features

- Parses a SAT vocabulary PDF file with tabular format.  
- Cleans unwanted rows (e.g., headers).  
- Extracts key fields:  
  - **Front**: *Vocabulary word*  
  - **Back**: *Definition + example sentence*  
- Generates an `.apkg` file ready for import into Anki.  
- Optionally exports a `.csv` for preview or backup.  

---

## 📂 PDF Table Structure (Expected Format)

Each row in the PDF should follow this format:  
**No | Word | Word Type | Definition | Example Sentence | Meaning**  

---

## 🚀 How to Use

**1. Install requirements**  
```bash
pip install pdfplumber genanki
```

**2. Run the script**  

Make sure you update the PDF filename in the script to match your actual file name.  
By default, the code is set to:  

```python
pdfplumber.open('Your_PDF.pdf')
```

Then run the script:  

```bash
python generate_apkg.py
```

**3. Output**  
- `vocabulary_deck.apkg`: Import this into Anki.  
- `vocabulary_table.csv`: *(optional)* A clean table of extracted data.  

---

## 🧠 Flashcard Format

- **Front**: *Word*  
- **Back**: *Definition + Example sentence*  

---

## 🧹 Data Cleaning

During extraction, the script automatically skips:  
- Page headers and Duplicate headers  
- Rows with fewer than 4 valid columns
