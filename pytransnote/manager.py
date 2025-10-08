
from deep_translator import GoogleTranslator

class my_translator():
    def __init__(self):
        self.__user_name="Guest"
        self.__from_lang=None
        self.__to_lang=None
    def set_user_name(self,name):
        self.__user_name=name
    def set_to_lang(self,language):
        self.__to_lang=language
    def set_from_lang(self,language):
        self.__from_lang=language
    def translation(self,from_str):
        text_to_translate = from_str
        ts= GoogleTranslator(source=self.__from_lang, target=self.__to_lang)
        return ts.translate(text_to_translate)
    def display_user(self):
        return self.__user_name

            

