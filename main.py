import csv
import pdfplumber
import genanki

# === Customize here ===
pdf_path = '(Chính thức) TỪ VỰNG VERBAL SAT - SAT Vocab.pdf'
exclude_keywords = ['BUỔI', 'SAT VOCABULARY', 'STT', 'Word']  # Exclude any row containing any of these keywords
output_csv = 'vocabulary_table.csv'
output_apkg = 'vocabulary_deck.apkg'

# === Read and filter from PDF file ===
flashcards = []
all_rows = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if not table:
            continue
        for row in table:
            # Skip if row is empty, too short, or contains unwanted keywords
            if not row or len(row) < 5:
                continue
            if any(keyword.lower() in str(cell).lower() for keyword in exclude_keywords for cell in row if cell):
                continue
            all_rows.append(row)
            word = row[1].strip()
            definition = row[3].strip()
            example = row[4].strip()
            back = f"{definition}<br><br><i>{example}</i>"
            flashcards.append({'front': word, 'back': back})

# === Write to CSV (optional) ===
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Definition', 'Example'])
    for row in all_rows:
        writer.writerow([row[1], row[3], row[4]])

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
