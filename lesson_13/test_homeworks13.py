import unittest
import logging
from homework_13_1 import log_event

class TestLogging(unittest.TestCase):

    def test_log_success(self):
        """Перевірка логування успішного входу (INFO)"""
        with self.assertLogs('log_event', level='INFO') as cm:
            log_event("user1", "success")
        
        # Перевіряємо, що в логах з'явився потрібний запис
        self.assertIn("INFO:log_event:Login event - Username: user1, Status: success", cm.output)

    def test_log_expired(self):
        """Перевірка логування застарілого пароля (WARNING)"""
        with self.assertLogs('log_event', level='WARNING') as cm:
            log_event("user2", "expired")
        
        self.assertIn("WARNING:log_event:Login event - Username: user2, Status: expired", cm.output)

    def test_log_failed(self):
        """Перевірка логування помилки входу (ERROR)"""
        with self.assertLogs('log_event', level='ERROR') as cm:
            log_event("user3", "failed")
        
        self.assertIn("ERROR:log_event:Login event - Username: user3, Status: failed", cm.output)

    def test_log_invalid_status_defaults_to_error(self):
        """Перевірка, що будь-який інший статус логується як ERROR (згідно з else у функції)"""
        with self.assertLogs('log_event', level='ERROR') as cm:
            log_event("user4", "unknown_status")
        
        self.assertIn("ERROR:log_event:Login event - Username: user4, Status: unknown_status", cm.output)

if __name__ == '__main__':
    unittest.main()
