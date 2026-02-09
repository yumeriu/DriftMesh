# test_driftmesh.py
"""
Tests for DriftMesh module.
"""

import unittest
from driftmesh import DriftMesh

class TestDriftMesh(unittest.TestCase):
    """Test cases for DriftMesh class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DriftMesh()
        self.assertIsInstance(instance, DriftMesh)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DriftMesh()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
