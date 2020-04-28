import json
from sudachipy import config
from sudachipy import dictionary
from expression_trans import expressionTranslate

with open(config.DEFAULT_SETTINGFILE, "r", encoding="utf-8") as f:
    sudachi_settings = json.load(f)
    
dict = dictionary.Dictionary()
sudachi_instance = dict.create()
input_text = '私が惚れたら困ります。'
ex_trans = expressionTranslate(False, 'holo', sudachi_instance)
translated_text = ex_trans.translateText(input_text).translated_text
print(translated_text)