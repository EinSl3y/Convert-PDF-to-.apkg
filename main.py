import csv
import pdfplumber
import genanki
import os

# === User Configuration ===
pdf_path = 'YourPDF.pdf'
exclude_keywords = ['BUỔI', 'SAT VOCABULARY', 'STT', 'Word']  
output_csv = 'vocabulary_table.csv'
output_apkg = 'vocabulary_deck.apkg'

# === Optional: Manually specify column indices (0-based) ===
use_manual_column_index = False  
word_index = 1
definition_index = 3
example_index = 4
flashcards = []
all_rows = []
column_indices_found = False

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if not table:
            continue
        for row_index, row in enumerate(table):
            if not row or len(row) < 3:
                continue
            if not use_manual_column_index and not column_indices_found:
                header = [cell.lower().strip() if cell else "" for cell in row]
                try:
                    word_index = header.index('word')
                    definition_index = header.index('definition')
                    example_index = header.index('example')
                    column_indices_found = True
                    continue 
                except ValueError:
                    continue
            if any(keyword.lower() in str(cell).lower() for keyword in exclude_keywords for cell in row if cell):
                continue
            if max(word_index, definition_index, example_index) >= len(row):
                continue
            word = row[word_index].strip()
            definition = row[definition_index].strip()
            example = row[example_index].strip()
            back = f"{definition}<br><br><i>{example}</i>"
            flashcards.append({'front': word, 'back': back})
            all_rows.append(row)

# === Export to CSV ===
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Definition', 'Example'])
    for row in all_rows:
        writer.writerow([row[word_index], row[definition_index], row[example_index]])

# === Create Anki Deck ===
model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[{'name': 'Front'}, {'name': 'Back'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '{{Front}}',
        'afmt': '{{Front}}<hr id="answer">{{Back}}',
    }]
)

deck = genanki.Deck(2059400110, 'Vocabulary Deck')
for card in flashcards:
    note = genanki.Note(model=model, fields=[card['front'], card['back']])
    deck.add_note(note)
genanki.Package(deck).write_to_file(output_apkg)
print(f"Created: {output_apkg}")

# === Delete CSV File ===
if os.path.exists(output_csv):
    os.remove(output_csv)
