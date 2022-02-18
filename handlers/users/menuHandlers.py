from aiogram.types import Message, CallbackQuery
from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu, booksMenu,python_keyboard
from keyboards.inline.callback_data import course_callback,book_callback
from loader import dp
import logging

@dp.message_handler(text_contains="Maxsulotlar")
async def select_category(message:Message):
    await message.answer(f"Mahsulotni tanlang",reply_markup=categoryMenu)

#kurslar javoni
@dp.callback_query_handler(text="courses")
async def buy_courses(call:CallbackQuery):
    await call.message.answer(f"Kursni tanlang",reply_markup=coursesMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

#detail kurs
@dp.callback_query_handler(course_callback.filter(item_name="python"))
async def buying_course(call:CallbackQuery,callback_data:dict):
    logging.info(f"{callback_data}")
    await call.message.answer(f"Siz Python kursini sotib olmoqchimisiz",reply_markup=python_keyboard)
    await call.answer(cache_time=60)
    
  #kitoblar javoni  
@dp.callback_query_handler(text="books")
async def buy_book(call:CallbackQuery):
    await call.message.answer("Kitobni tanlang",reply_markup=booksMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

#kitob detail
@dp.callback_query_handler(book_callback.filter(item_name='python_book'))
async def order_access(call:CallbackQuery,callback_data:dict):
    logging.info(f"{callback_data}")
    await call.answer("Buyurtmangiz qabul qilindi",cache_time=60,show_alert=True)
    
@dp.callback_query_handler(text="close")
async def close(call:CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer(cache_time=60)
    