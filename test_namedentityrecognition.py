# test_namedentityrecognition.py
"""
Tests for NamedEntityRecognition module.
"""

import unittest
from namedentityrecognition import NamedEntityRecognition

class TestNamedEntityRecognition(unittest.TestCase):
    """Test cases for NamedEntityRecognition class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NamedEntityRecognition()
        self.assertIsInstance(instance, NamedEntityRecognition)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NamedEntityRecognition()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
