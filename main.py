import csv
import pdfplumber
import genanki

all_rows = []
with pdfplumber.open('(Chính thức) TỪ VỰNG VERBAL SAT - SAT Vocab.pdf') as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            for row in table:
                if not row or len(row) < 4:
                    continue
                if row[0] and ('STT' in row[0] or 'BUỔI' in row[0] or 'SAT VOCABULARY' in row[0]):
                    continue
                all_rows.append(row)

with open('vocabulary_table.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['No', 'Word', 'Word Type', 'Definition', 'Example', 'Topic'])
    writer.writerows(all_rows)

flashcards = []
for row in all_rows:
    word = row[1].strip()
    definition = row[3].strip() if len(row) > 3 else ''
    example = row[4].strip() if len(row) > 4 else ''
    back = f"{definition}<br><br><i>{example}</i>" if example else definition
    flashcards.append({'front': word, 'back': back})

model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[{'name': 'Front'}, {'name': 'Back'}],
    templates=[
        {'name': 'Card 1', 'qfmt': '{{Front}}', 'afmt': '{{Front}}<hr id="answer">{{Back}}'},
    ])

deck = genanki.Deck(2059400110, 'Vocabulary Deck')
for card in flashcards:
    note = genanki.Note(model=model, fields=[card['front'], card['back']])
    deck.add_note(note)

genanki.Package(deck).write_to_file('vocabulary_deck.apkg')
print("✅ Đã tạo xong file vocabulary_deck.apkg!")
