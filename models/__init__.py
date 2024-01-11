#!/usr/bin/env python
"""Initialize the FileStorage instance"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
