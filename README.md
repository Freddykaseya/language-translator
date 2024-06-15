import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = 'clé'  


def translate_text(text, source_lang, target_lang):
    url = 'https://api-free.deepl.com/v2/translate'
    params = {
        'auth_key': API_KEY,
        'text': text,
        'source_lang': source_lang,
        'target_lang': target_lang
    }

    try:
        response = requests.post(url, data=params)
        if response.status_code == 200:
            translation = response.json()['translations'][0]['text']
            return translation
        else:
            messagebox.showerror("Error", f"Translation Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Request error: {e}")
        return None

def translate():
    source_text = entry_source.get("1.0", tk.END).strip()

    if not source_text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    source_lang = 'FR'  # Langue source (FR pour français)
    target_lang = 'EN'  # Langue cible (EN pour anglais)

    translation_fr_en = translate_text(source_text, source_lang, target_lang)
    if translation_fr_en:
        text_translated.config(state=tk.NORMAL)
        text_translated.delete("1.0", tk.END)
        text_translated.insert(tk.END, translation_fr_en)
        text_translated.config(state=tk.DISABLED)

        translation_en_fr = translate_text(translation_fr_en, target_lang, source_lang)
        if translation_en_fr:
            text_original.config(state=tk.NORMAL)
            text_original.delete("1.0", tk.END)
            text_original.insert(tk.END, source_text)
            text_original.config(state=tk.DISABLED)

def clear_text():
    entry_source.delete("1.0", tk.END)
    text_original.config(state=tk.NORMAL)
    text_original.delete("1.0", tk.END)
    text_original.config(state=tk.DISABLED)
    text_translated.config(state=tk.NORMAL)
    text_translated.delete("1.0", tk.END)
    text_translated.config(state=tk.DISABLED)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Language Translation Tool")

# Cadre pour entrer du texte
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_source = tk.Label(frame_input, text="Enter text to translate (French):")
label_source.pack()

entry_source = tk.Text(frame_input, height=5, width=50)
entry_source.pack()

# Cadre pour afficher le texte original et traduit
frame_output = tk.Frame(root)
frame_output.pack(pady=10)

label_original = tk.Label(frame_output, text="Original Text (FR):")
label_original.pack()

text_original = tk.Text(frame_output, height=5, width=50, wrap=tk.WORD)
text_original.config(state=tk.DISABLED)
text_original.pack()

label_translated = tk.Label(frame_output, text="Translated Text (EN):")
label_translated.pack()

text_translated = tk.Text(frame_output, height=5, width=50, wrap=tk.WORD)
text_translated.config(state=tk.DISABLED)
text_translated.pack()

# Boutons pour traduire et effacer le texte
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_translate = tk.Button(frame_buttons, text="Translate", command=translate)
button_translate.pack(side=tk.LEFT, padx=10)

button_clear = tk.Button(frame_buttons, text="Clear", command=clear_text)
button_clear.pack(side=tk.LEFT, padx=10)

# Exécution de la fenêtre principale
root.mainloop()
