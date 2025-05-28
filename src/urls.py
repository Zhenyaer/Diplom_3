class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'  # Главная страница
    USER_CREATE = f'{BASE_URL}api/auth/register'  # POST, создание пользователя
    USER_DELETE = f'{BASE_URL}api/auth/user'  # DELETE, удаление пользователя
    URL_LOGIN_PAGE = f'{BASE_URL}login'  # Страница входа
    PASSWORD_FORGOT_PAGE = f'{BASE_URL}forgot-password'  # Страница восстановления пароля
    PASSWORD_RESET_PAGE = f'{BASE_URL}reset-password'  # Страница смены пароля
    ACCOUNT_PROFILE_PAGE = f'{BASE_URL}account/profile'  # Личный кабинет
    ACCOUNT_ORDER_HISTORY_PAGE = f'{BASE_URL}account/order-history'  # Страница истории заказов
    ORDER_FEED_PAGE = f'{BASE_URL}feed'  # Страница "Лента заказов"
