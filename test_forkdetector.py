# test_forkdetector.py
"""
Tests for ForkDetector module.
"""

import unittest
from forkdetector import ForkDetector

class TestForkDetector(unittest.TestCase):
    """Test cases for ForkDetector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ForkDetector()
        self.assertIsInstance(instance, ForkDetector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ForkDetector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
