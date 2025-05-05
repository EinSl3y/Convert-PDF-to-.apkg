
# Convert-PDF-to-.apkg 

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
- After generating `.apkg`, the `.csv` file is automatically deleted.

---

## 📂 Expected Table Format

Each row in the PDF should follow this general format:

`No | Word | Word Type | Definition | Example Sentence | Meaning (optional)`

> **Note**: The script only requires **Word**,**Definition**, and **Example columns** (usually columns 2, 4, and 5 respectively). These columns are indexed starting from `0` in the script, so make sure your PDF aligns with this setup.


---

## 🚀 How to Use

1. **Install Requirements**

```bash
pip install pdfplumber genanki
```

2. **Edit Configuration in Script**

Modify these variables at the top of the script:

```python
pdf_path = 'YourPDF.pdf' 
exclude_keywords = ['BUỔI', 'STT', 'SAT VOCABULARY', 'Word'] 
use_manual_column_index = False  
word_index = 1 
definition_index = 3  
example_index = 4  
```
- `df_path`: Set this to the path of your PDF file containing the vocabulary list.
- `exclude_keywords`: This list contains keywords that will be used to filter out unwanted rows in the PDF. For example, you can skip rows containing headers or irrelevant information.
- `use_manual_column_index`: Set this to True if your PDF does not contain headers. Otherwise, the script will automatically detect the column positions.
- `word_index`, `definition_index`, `example_index`: These are the column indices for "Word", "Definition", and "Example" in the table, respectively. By default, these are set to 1, 3, and 4 based on the expected table format. If your table structure is different, you can update these values to match the correct columns.

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
- If the table structure in your PDF differs from the expected format, modify the column indices (`word_index`, `definition_index`, `example_index`) to fit your data layout.


