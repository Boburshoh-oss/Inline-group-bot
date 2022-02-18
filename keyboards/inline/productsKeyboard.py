from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callback_data import course_callback, book_callback
import logging

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kurslar",callback_data="courses"),
            InlineKeyboardButton(text="Kitoblar",callback_data="books")
        ],
        [
            InlineKeyboardButton(text="Boburbek bilan bog'lanish",url="https://t.me/INTILLEGENT")
        ],
        [
            InlineKeyboardButton(text="Qidirish",switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="Ulash",switch_inline_query="Zo'r bot ekan"),
        ]
    ]
)

#kurslar uchun keyboard
coursesMenu = InlineKeyboardMarkup(row_width=1)
python = InlineKeyboardButton(text="Python dasturlash asoslari",callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)
java = InlineKeyboardButton(text="Java dasturlash asoslari",callback_data=course_callback.new(item_name="java"))
coursesMenu.insert(java)
php = InlineKeyboardButton(text="Php dasturlash asoslari",callback_data=course_callback.new(item_name="php"))
coursesMenu.insert(php)
cpp = InlineKeyboardButton(text="C++ dasturlash asoslari",callback_data=course_callback.new(item_name="c++"))
coursesMenu.insert(cpp)
#ikkinchi usul
django = InlineKeyboardButton(text="django asoslari",callback_data="course:django")
coursesMenu.insert(django)
flask = InlineKeyboardButton(text="flask asoslari",callback_data="course:flask")
coursesMenu.insert(flask)
back_button = InlineKeyboardButton(text="🔙 Ortga",callback_data="close")
coursesMenu.insert(back_button)
#for books 
# booksMenu = InlineKeyboardMarkup(row_width=2)
# sariq = InlineKeyboardButton(text="Sariq devni minib",callback_data=book_callback.new(item_name="sariq"))
# yulduz = InlineKeyboardButton(text="Yulduzli tunlar",callback_data=book_callback.new(item_name="tunlar"))
# ozlik = InlineKeyboardButton(text="O'zlikni anglash",callback_data=book_callback.new(item_name="o'zlik"))
# booksMenu.insert(sariq)
# booksMenu.insert(yulduz)
# booksMenu.insert(ozlik)


books = {
    "Python kitobi":"python_book",
    "C++ dasturlash asoslari":"cpp_book",
    "Mukammal Dasturlash. asoslari":"js_book",
    "Telegram Dasturlash. asoslari":"tg",
}

booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key,callback_data=book_callback.new(item_name=value)))
booksMenu.insert(back_button)

#Har bir kurs uchun tugma
python_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Xarid qilish", url="https://mohirdev.uz/courses/telegram/")]
    ]
)

algoritm_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ko'rish",url="https://mohirdev.uz/courses/algortimlar/")]
    ]
)