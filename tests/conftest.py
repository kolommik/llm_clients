"""conftest.py

This module provides configuration and fixtures for pytest.
"""
import sys
from pathlib import Path

# Adding the src directory to the Python path
SRC_DIR = str(Path(__file__).parent.parent.joinpath("src").resolve())
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
