#!/usr/bin/python3
# coding: utf-8
import os
import json
from pathlib import Path

current_path = os.path.abspath(__file__).removesuffix("data.py")

V_PATH = str(Path(f"{current_path}resources/voice").absolute()) + "/"
T_PATH = str(Path(f"{current_path}resources/text").absolute()) + "/"


with open(f"{T_PATH}atri.json", "r", encoding="utf-8") as file:
    atri_text = json.load(file)
