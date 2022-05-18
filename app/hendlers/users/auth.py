from aiogram import types, Dispatcher
from app.keyboards.auth_kbd import welcome_kbd, choice_auth_method


async def process_callback_want_vpn(callback_query: types.CallbackQuery):
    await callback_query.answer(callback_query.id)
    # await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer(text='выберите способ подтвержения личности', reply_markup=choice_auth_method())


async def process_callback_choice_auth_method(callback_query: types.CallbackQuery):
    if callback_query.data == "auth_inst":
        await callback_query.message.answer(text='отправь ссылку на инст')
    elif callback_query.data == "auth_vk":
        await callback_query.message.answer(text='отправь ссылку на вк')
    elif callback_query.data == "auth_ph_nmb":
        await callback_query.message.answer(text='номер телефона')
    elif callback_query.data == "auth_token":
        await callback_query.message.answer(text='введите токен')
    elif callback_query.data == "auth_request_access":
        await callback_query.message.answer(text='запросить доступ')

async def cmd_start(message: types.Message):
    chat_id: int = message.chat.id
    user_id: int = message['from']['id']

    keyboard = welcome_kbd()
    await message.answer(
        text="привет! я бот от Васи. Я выдаю его друзьям доступ к VPN.",
        parse_mode="HTML",
        reply_markup=keyboard
    )


def register_handlers_auth(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_callback_query_handler(process_callback_want_vpn, lambda cb: cb.data == "want_vpn", state="*")
    dp.register_callback_query_handler(process_callback_choice_auth_method, lambda cb: cb.data[:5] == "auth_", state="*")