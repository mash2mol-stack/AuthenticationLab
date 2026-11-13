import json

from auth_service import AuthenticationService
from authenticators import (
    PasswordAuthenticator,
    FingerprintAuthenticator,
    QrAuthenticator,
    TokenAuthenticator,
)


def make_service(tmp_path, authenticator):
    return AuthenticationService(
        [authenticator],
        history_file=str(tmp_path / "history.json"),
        log_file=str(tmp_path / "logs" / "test.log"),
    )


def test_correct_password_is_accepted(tmp_path):
    service = make_service(tmp_path, PasswordAuthenticator())
    assert service.authenticate({"login": "maria", "password": "1234"}) is True


def test_incorrect_password_is_rejected(tmp_path):
    service = make_service(tmp_path, PasswordAuthenticator())
    assert service.authenticate({"login": "maria", "password": "bad"}) is False


def test_correct_fingerprint_is_accepted(tmp_path):
    service = make_service(tmp_path, FingerprintAuthenticator())
    assert service.authenticate({"fingerprint": "FP-001"}) is True


def test_incorrect_fingerprint_is_rejected(tmp_path):
    service = make_service(tmp_path, FingerprintAuthenticator())
    assert service.authenticate({"fingerprint": "wrong"}) is False


def test_correct_qr_is_accepted(tmp_path):
    service = make_service(tmp_path, QrAuthenticator())
    assert service.authenticate({"qr_code": "QR-2026"}) is True


def test_correct_token_is_accepted(tmp_path):
    service = make_service(tmp_path, TokenAuthenticator())
    assert service.authenticate({"token": "TOKEN-2026"}) is True


def test_invalid_token_is_rejected(tmp_path):
    service = make_service(tmp_path, TokenAuthenticator())
    assert service.authenticate({"token": "wrong"}) is False


def test_authentication_history_is_saved(tmp_path):
    service = make_service(tmp_path, PasswordAuthenticator())
    service.authenticate({"login": "maria", "password": "1234"})

    history_path = tmp_path / "history.json"
    records = json.loads(history_path.read_text(encoding="utf-8"))

    assert len(records) == 1
    assert records[0]["method"] == "PasswordAuthenticator"
    assert records[0]["success"] is True
