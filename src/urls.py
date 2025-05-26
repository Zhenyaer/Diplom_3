class Urls:
    base_url = 'https://stellarburgers.nomoreparties.site/'  # Главная страница
    user_create = f'{base_url}api/auth/register'  # POST, создание пользователя
    user_delete = f'{base_url}api/auth/user'  # DELETE, удаление пользователя
    url_login_page = f'{base_url}login'  # Страница входа
    password_forgot_page = f'{base_url}forgot-password'  # Страница восстановления пароля
    password_reset_page = f'{base_url}reset-password'  # Страница смены пароля
    account_profile_page = f'{base_url}account/profile'  # Личный кабинет
    account_order_history_page = f'{base_url}account/order-history'  # Страница истории заказов
    order_feed_page = f'{base_url}feed'  # Страница "Лента заказов"
