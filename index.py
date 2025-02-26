import tkinter as tk
from tkinter import messagebox
import requests

# Définition de la clé API DeepL
API_KEY = 'clé_API_Deepl'  # Remplace 'ta_clé_api_ici' par ta vraie clé API

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
            messagebox.showerror("Erreur", f"Erreur de traduction : {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erreur", f"Erreur de requête : {e}")
        return None

def translate():
    source_text = entry_source.get("1.0", tk.END).strip()
    if not source_text:
        messagebox.showwarning("Avertissement", "Veuillez entrer un texte à traduire.")
        return
    
    source_lang = 'FR'  # Langue source
    target_lang = target_lang_var.get()  # Langue cible choisie
    
    translation = translate_text(source_text, source_lang, target_lang)
    if translation:
        text_translated.config(state=tk.NORMAL)
        text_translated.delete("1.0", tk.END)
        text_translated.insert(tk.END, translation)
        text_translated.config(state=tk.DISABLED)

def clear_text():
    entry_source.delete("1.0", tk.END)
    text_translated.config(state=tk.NORMAL)
    text_translated.delete("1.0", tk.END)
    text_translated.config(state=tk.DISABLED)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Outil de Traduction DeepL")

# Cadre pour entrer du texte
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_source = tk.Label(frame_input, text="Entrez le texte à traduire (Français) :")
label_source.pack()

entry_source = tk.Text(frame_input, height=5, width=50)
entry_source.pack()

# Sélection de la langue cible
frame_lang = tk.Frame(root)
frame_lang.pack(pady=5)

target_lang_var = tk.StringVar(value='EN')
label_target = tk.Label(frame_lang, text="Langue cible :")
label_target.pack(side=tk.LEFT)

target_lang_menu = tk.OptionMenu(frame_lang, target_lang_var, 'EN', 'ES', 'DE', 'IT', 'NL', 'PT')
target_lang_menu.pack(side=tk.LEFT)

# Cadre pour afficher le texte traduit
frame_output = tk.Frame(root)
frame_output.pack(pady=10)

label_translated = tk.Label(frame_output, text="Texte traduit :")
label_translated.pack()

text_translated = tk.Text(frame_output, height=5, width=50, wrap=tk.WORD)
text_translated.config(state=tk.DISABLED)
text_translated.pack()

# Boutons pour traduire et effacer le texte
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_translate = tk.Button(frame_buttons, text="Traduire", command=translate)
button_translate.pack(side=tk.LEFT, padx=10)

button_clear = tk.Button(frame_buttons, text="Effacer", command=clear_text)
button_clear.pack(side=tk.LEFT, padx=10)

# Exécution de la fenêtre principale
root.mainloop()

