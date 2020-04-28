import json
from sudachipy import config
from sudachipy import dictionary

print(config.DEFAULT_SETTINGFILE)
# /Users/ohke/src/sudachipy/sudachipy/../resources/sudachi.json

print("-------------\n-------------\n\n")
with open(config.DEFAULT_SETTINGFILE, 'r', encoding='utf-8') as f:
    settings = json.load(f)
    
print(settings)
# {'systemDict': 'system.dic',
#  'characterDefinitionFile': 'char.def',
#  'inputTextPlugin': [{'class': 'com.worksap.nlp.sudachi.DefaultInputTextPlugin'}],
#  'oovProviderPlugin': [{'class': 'com.worksap.nlp.sudachi.MeCabOovProviderPlugin',
#    'charDef': 'char.def',
#    'unkDef': 'unk.def'},
#   {'class': 'com.worksap.nlp.sudachi.SimpleOovProviderPlugin',
#    'oovPOS': ['補助記号', '一般', '*', '*', '*', '*'],
#    'leftId': 5968,
#    'rightId': 5968,
#    'cost': 3857}],
#  'pathRewritePlugin': [{'class': 'com.worksap.nlp.sudachi.JoinNumericPlugin',
#    'joinKanjiNumeric': True},
#   {'class': 'com.worksap.nlp.sudachi.JoinKatakanaOovPlugin',
#    'oovPOS': ['名詞', '普通名詞', '一般', '*', '*', '*']}]}