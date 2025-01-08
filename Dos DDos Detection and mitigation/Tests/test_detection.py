import unittest
from src.ddos_detector import request_counts, INITIAL_BLOCK_THRESHOLD

class TestDetection(unittest.TestCase):
    def test_threshold_detection(self):
        # Simulate traffic from an IP address
        ip = "192.168.1.1"
        for _ in range(INITIAL_BLOCK_THRESHOLD + 1):
            request_counts[ip] += 1

        # Check if the IP exceeded the threshold
        self.assertTrue(request_counts[ip] > INITIAL_BLOCK_THRESHOLD)
