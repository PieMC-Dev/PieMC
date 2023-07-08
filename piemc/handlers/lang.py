import json
import os
import time
from pathlib import Path

from piemc import config


class LangHandler:
    @staticmethod
    def initialize_language():
        current_dir = Path(__file__).resolve().parent.parent
        lang_dirname = "lang"
        lang_fullpath = os.path.join(current_dir, lang_dirname)
        lang_file_path = os.path.join(lang_fullpath, f"{config.LANG}.json")
        fallback_lang_file_path = os.path.join(lang_fullpath, "en.json")

        if not os.path.exists(lang_file_path):
            print(f"Language file not found for language: {config.LANG}")
            lang = {}
        else:
            with open(lang_file_path, 'r', encoding='utf-8') as lang_file:
                lang = json.load(lang_file)

        if os.path.exists(fallback_lang_file_path):
            with open(fallback_lang_file_path, 'r', encoding='utf-8') as fallback_lang_file:
                fallback_lang = json.load(fallback_lang_file)
                lang = {**fallback_lang, **lang}

        return lang
