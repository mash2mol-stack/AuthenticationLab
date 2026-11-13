class PasswordAuthenticator:
    """Проверка пары логин/пароль."""

    def authenticate(self, credentials):
        print("[PASSWORD] Проверка логина и пароля...")
        if (credentials.get("login") == "maria"
                and credentials.get("password") == "1234"):
            print("[PASSWORD] Аутентификация успешна.")
            return True
        print("[PASSWORD] Неверный логин или пароль.")
        return False


class FingerprintAuthenticator:
    """Имитация проверки отпечатка пальца."""

    def authenticate(self, credentials):
        print("[FINGERPRINT] Проверка отпечатка пальца...")
        if credentials.get("fingerprint") == "FP-001":
            print("[FINGERPRINT] Аутентификация успешна.")
            return True
        print("[FINGERPRINT] Отпечаток не распознан.")
        return False


class QrAuthenticator:
    """Проверка демонстрационного QR-кода."""

    def authenticate(self, credentials):
        print("[QR] Проверка QR-кода...")
        if credentials.get("qr_code") == "QR-2026":
            print("[QR] Аутентификация успешна.")
            return True
        print("[QR] QR-код недействителен.")
        return False


class TokenAuthenticator:
    """Проверка демонстрационного токена."""

    def authenticate(self, credentials):
        print("[TOKEN] Проверка токена...")
        if credentials.get("token") == "TOKEN-2026":
            print("[TOKEN] Аутентификация успешна.")
            return True
        print("[TOKEN] Токен недействителен.")
        return False
