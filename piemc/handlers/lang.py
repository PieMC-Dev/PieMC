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

from pathlib import Path

import yaml

from piemc import config


class LangHandler:
    lang_cache = None

    @staticmethod
    def initialize_language():
        if LangHandler.lang_cache is not None:
            return LangHandler.lang_cache

        current_dir = Path(__file__).resolve().parent.parent
        lang_dirname = "lang"
        lang_fullpath = current_dir / lang_dirname
        lang_file_path = lang_fullpath / f"{config.LANG}.yml"
        fallback_lang_file_path = lang_fullpath / "en.yml"

        lang = {}
        if lang_file_path.exists():
            with lang_file_path.open("r", encoding="utf-8") as lang_file:
                lang = yaml.safe_load(lang_file)
        else:
            print(f"Language file not found for language: {config.LANG}")

        if fallback_lang_file_path.exists():
            with fallback_lang_file_path.open("r", encoding="utf-8") as fallback_lang_file:
                fallback_lang = yaml.safe_load(fallback_lang_file)
                lang = {**fallback_lang, **lang}

        LangHandler.lang_cache = lang
        return lang
