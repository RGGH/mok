from unittest.mock import patch
from app.fetch_www import parse


@patch("..app.fetch_www")
def test_parse_from_fetch_net(mock_get):
    """meh"""
    mock_get.return_value = "def"
    assert parse() == "abc123"
