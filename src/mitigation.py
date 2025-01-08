import unittest
from src.ddos_detector import block_ip_windows, unblock_ip

class TestMitigation(unittest.TestCase):
    def test_blocking_logic(self):
        ip = "192.168.1.1"
        # Simulate blocking an IP
        block_ip_windows(ip)
        self.assertIn(ip, block_ip_windows.__globals__["blocked_ips"])  # Check if IP is blocked

    def test_unblocking_logic(self):
        ip = "192.168.1.1"
        # Simulate unblocking an IP
        unblock_ip(ip)
        self.assertNotIn(ip, block_ip_windows.__globals__["blocked_ips"])  # Check if IP is unblocked
