from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
import requests


def get_definition(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    try:
        r = requests.get(url)
    except ConnectionError:
        return "No internet Connection"
    if r.status_code == 404:
        return "Non-existing word in Dictionary. Please try another word."
    content = r.json()
    meanings = content[0]['meanings']
    definitions = []
    for i in range(len(meanings)):
        definitions.append(f"{i + 1}. ({meanings[i]['partOfSpeech']}) {meanings[i]['definitions'][0]['definition']}")
    return "\n".join(definitions)


def convert():
    input_text = text.text()
    if input_text == "":
        output_label.setText("Try writing a word in English...")
        return
    definition = get_definition(input_text)
    output_label.setText(definition)


app = QApplication([])
window = QWidget()
window.setWindowTitle('English Dictionary')
layout = QVBoxLayout()

layout2 = QHBoxLayout()

text = QLineEdit()
layout2.addWidget(text)

btn = QPushButton('Convert')
layout2.addWidget(btn)
btn.clicked.connect(convert)

output_label = QLabel('')
window.setLayout(layout)
layout.addLayout(layout2)
layout.addWidget(output_label)
window.show()
app.exec()
