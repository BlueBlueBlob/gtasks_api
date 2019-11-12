from unittest import TestCase
from unittest.mock import patch, mock_open
from datetime import datetime
import responses
from gtasks_api import GtasksAPI


class TestGtasksAPI(TestCase):
    def setUp(self):
        self.gtasks_api = None

    def test_init_valid(self):
        with patch("os.path.exists" ) as m_exist:
            with patch("builtins.open", mock_open()) as m_open:
                m_exist.return_value = True
                self.gtasks_api = GtasksAPI('/path/credentials.json', '/path/token.pickle')
        assert isinstance(self.gtasks_api, GtasksAPI)

