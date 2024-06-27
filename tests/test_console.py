#!/usr/bin/python3
"""Defines the HBNB Test console."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """Test the console."""
    def setUp(self):
        """Set up the test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up."""
        self.console = None

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            self.assertTrue(f.getvalue() != "")

    def test_show(self):
        """Test the show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show State")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show City")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Amenity")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Place")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Review")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
