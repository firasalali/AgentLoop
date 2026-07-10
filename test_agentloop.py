# test_agentloop.py
"""
Tests for AgentLoop module.
"""

import unittest
from agentloop import AgentLoop

class TestAgentLoop(unittest.TestCase):
    """Test cases for AgentLoop class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgentLoop()
        self.assertIsInstance(instance, AgentLoop)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgentLoop()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
