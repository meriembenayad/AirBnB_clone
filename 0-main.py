#!/usr/bin/python3
from models.engine.file_storage import FileStorage

try:
    print(type(FileStorage._FileStorage__file_path))
except:
    fs = FileStorage()
    print(type(fs._FileStorage__file_path))
