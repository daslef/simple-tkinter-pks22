
"""Импорт разнообразных приблуд, дополнений, фич"""
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import requests

YA_TOKEN = 'trnsl.1.1.20200228T124248Z.23d3f30fe1bc309f.8c9ccda6143f22ccb6fb89bef10fbdec79b24dca'


def translate_api_call(text, direction):
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={'key': YA_TOKEN, 'text': text, 'lang': direction})
    if r.status_code != 200:
        raise requests.HTTPError
    return r.json()['text'][0]

"""Создадим функцию"""
def translate_text():
  """"""
    current_tab_index = notebook.index(notebook.select())
    current_tab_object = notebook.winfo_children()[current_tab_index]
    required_tab_object = notebook.winfo_children()[not(current_tab_index)]

    required_tab_object.children['!text'].delete(1.0, tk.END)

    if str(current_tab_object) == '.!notebook.!frame':
        current_lang, required_lang = 'en', 'ru'
        required_tab_name = '.!notebook.!frame2'
    else:
        current_lang, required_lang = 'ru', 'en'
        required_tab_name = '.!notebook.!frame'

    text = current_tab_object.children['!text'].get(1.0, tk.END).rstrip()

    try:
        result = translate_api_call(text, f'{current_lang}-{required_lang}')
    except requests.HTTPError:
        messagebox.showwarning('Warning', 'Yandex.API is not available. Check your network connection')
    else:
        notebook.select(required_tab_name)
        required_tab_object.children['!text'].insert(1.0, result)
    

root = tk.Tk()
root.title('Ya.Translator')
root.geometry('500x300')
root.resizable(False, False)

notebook = ttk.Notebook(root)
frame_en = tk.Frame(notebook) """"Здесь родитель не корень а нотебук"""
frame_ru = tk.Frame(notebook)
text_en = tk.Text(frame_en) """А хдесь вообще фрейм"""
text_ru = tk.Text(frame_ru)
button = tk.Button(root, text='Translate!', command=translate_text)"""Это мы создаем кнопку,
                                                                   ее родитель корень, она содержит в себе выполнение функции, 
                                                                   которую мы самостоятельно создали выше"""

button.pack(side=tk.BOTTOM, fill=tk.X, expand=True)"""Пакуем кнопку, делаем заполнение"""
frame_en.pack(fill=tk.BOTH)
frame_ru.pack(fill=tk.BOTH)  """Пакуем все на свете"""
text_en.pack(fill=tk.BOTH)
text_ru.pack(fill=tk.BOTH)

notebook.add(frame_en, text='English')
notebook.add(frame_ru, text='Russian')
notebook.pack(fill=tk.BOTH)

text_en.focus_set() """Делаем так чтобы можно бло сразу вводить текст без всяких кликов"""

root.mainloop()
