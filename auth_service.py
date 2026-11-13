import json
import logging
from datetime import datetime
from pathlib import Path


class AuthenticationService:
    def __init__(self, authenticators, history_file="authentication.json",
                 log_file="logs/authentication.log"):
        self.authenticators = authenticators
        self.history_file = Path(history_file)
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

        self.logger = logging.getLogger("AuthenticationLab")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        # Не добавляем повторные обработчики при повторном создании сервиса.
        if not self.logger.handlers:
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )
            file_handler = logging.FileHandler(
                self.log_file, encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def authenticate(self, credentials):
        print("\n=== НАЧАЛО АУТЕНТИФИКАЦИИ ===")
        self.logger.info("Начало аутентификации")

        success = False
        method = "Не определён"

        for authenticator in self.authenticators:
            if authenticator.authenticate(credentials):
                success = True
                method = authenticator.__class__.__name__
                break

        if success:
            print("=== АУТЕНТИФИКАЦИЯ УСПЕШНА ===")
            self.logger.info("Аутентификация успешна: %s", method)
        else:
            print("=== АУТЕНТИФИКАЦИЯ НЕ ПРОЙДЕНА ===")
            self.logger.warning("Аутентификация не пройдена")

        self._save_record(method, success)
        return success

    def _save_record(self, method, success):
        records = []
        if self.history_file.exists():
            try:
                records = json.loads(
                    self.history_file.read_text(encoding="utf-8")
                )
            except (json.JSONDecodeError, OSError):
                records = []

        records.append({
            "method": method,
            "success": success,
            "time": datetime.now().isoformat(timespec="seconds"),
        })
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
        self.history_file.write_text(
            json.dumps(records, ensure_ascii=False, indent=4),
            encoding="utf-8",
        )
