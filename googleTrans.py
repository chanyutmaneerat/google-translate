from googletrans import Translator
def translate() :
    while True :
        translater = Translator()
        user_input = input('กรอกข้อความที่เราต้องการแปล =')
        translation = translater.translate(user_input,dest= 'th') #'en' หมายถึงให้แปลงค่าเป็นภาษาอังกฤษ
        print(translation.origin,'=',translation.text)

translate()
#สามารถหาข้อมูลเพิ่มเติมได้ที่ https://pypi.org/project/googletrans/ 
# สามารถเปลี่ยนให้แปลงเป็นภาษาอื่นได้



