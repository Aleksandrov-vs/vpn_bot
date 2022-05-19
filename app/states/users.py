from aiogram.dispatcher.filters.state import State, StatesGroup


class AuthUserInstFSM(StatesGroup):
    link = State()


class AuthUserVkFSM(StatesGroup):
    link = State()


class AuthUserTokenFSM(StatesGroup):
    link = State()


class AuthUserRequestAccessFSM(StatesGroup):
    link = State()


class AuthUserPhNumberFSM(StatesGroup):
    link = State()


class AuthUserFSM(StatesGroup):
    inst = AuthUserInstFSM()
    token = AuthUserTokenFSM()
    vk = AuthUserVkFSM()
    request_access = AuthUserRequestAccessFSM()
    phNumber = AuthUserPhNumberFSM()
