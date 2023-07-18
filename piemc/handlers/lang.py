# -*- coding: utf-8 -*-

#  ____  _      __  __  ____
# |  _ \(_) ___|  \/  |/ ___|
# | |_) | |/ _ \ |\/| | |
# |  __/| |  __/ |  | | |___
# |_|   |_|\___|_|  |_|\____|
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# @author PieMC Team
# @link http://www.PieMC-Dev.github.io/

import yaml
import os

from pathlib import Path
from piemc import config


class LangHandler:
    @staticmethod
    def initialize_language():
        current_dir = Path(__file__).resolve().parent.parent
        lang_dirname = "lang"
        lang_fullpath = os.path.join(current_dir, lang_dirname)
        lang_file_path = os.path.join(lang_fullpath, f"{config.LANG}.yml")
        fallback_lang_file_path = os.path.join(lang_fullpath, "en.yml")

        if not os.path.exists(lang_file_path):
            print(f"Language file not found for language: {config.LANG}")
            lang = {}
        else:
            with open(lang_file_path, 'r', encoding='utf-8') as lang_file:
                lang = yaml.safe_load(lang_file)

        if os.path.exists(fallback_lang_file_path):
            with open(fallback_lang_file_path, 'r', encoding='utf-8') as fallback_lang_file:
                fallback_lang = yaml.safe_load(fallback_lang_file)
                lang = {**fallback_lang, **lang}

        return lang