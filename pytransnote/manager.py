
from deep_translator import MyMemoryTranslator

class my_translator():
    def __init__(self):
        self._user_name="Guest"
        self._from_lang="english"
        self._to_lang="spanish"
    def set_user_name(self,name):
        self._user_name=name
    def set_to_lang(self,language):
        self._to_lang=language
    def set_from_lang(self,language):
        self._from_lang=language
    def translation(self,from_str):
        text_to_translate = from_str
        ts= MyMemoryTranslator(source=self._from_lang, target=self._to_lang)
        return ts.translate(text_to_translate)
    def display_user(self):
        return self._user_name

            

