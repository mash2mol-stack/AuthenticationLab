from auth_service import AuthenticationService
from authenticators import (
    PasswordAuthenticator,
    FingerprintAuthenticator,
    QrAuthenticator,
    TokenAuthenticator,
)


def main():
    service = AuthenticationService([
        PasswordAuthenticator(),
        FingerprintAuthenticator(),
        QrAuthenticator(),
        TokenAuthenticator(),
    ])

    scenarios = [
        ("Аутентификация по паролю", {
            "login": "maria", "password": "1234"
        }),
        ("Аутентификация по отпечатку", {
            "fingerprint": "FP-001"
        }),
        ("Аутентификация по QR-коду", {
            "qr_code": "QR-2026"
        }),
        ("Аутентификация по токену", {
            "token": "TOKEN-2026"
        }),
        ("Проверка неверных данных", {
            "login": "wrong", "password": "wrong",
            "fingerprint": "wrong", "qr_code": "wrong",
            "token": "wrong"
        }),
    ]

    for title, credentials in scenarios:
        print(f"\n=== {title} ===")
        result = service.authenticate(credentials)
        print("Результат:", "УСПЕШНО" if result else "ОТКАЗАНО")

    print("\nИстория сохранена в authentication.json")
    print("Журнал сохранён в logs/authentication.log")


if __name__ == "__main__":
    main()
