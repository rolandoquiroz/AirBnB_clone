#!/usr/bin/python3
"""
models/__init__.py updated to create a unique
FileStorage instance for hbnb application
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
