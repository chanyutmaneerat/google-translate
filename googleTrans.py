from googletrans import Translator
def translate() :
    while True :
        translater = Translator()
        user_input = input('Enter the message =')
        translation = translater.translate(user_input,dest= 'th') #'en' mean to translate into english
        print(translation.origin,'=',translation.text)

translate()
#can file more information https://pypi.org/project/googletrans/ 
# can chaing to anater language



