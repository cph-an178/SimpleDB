import os
import pytest
from simple_db import SimpleDB

test_db = "test.db"

def test_class_init_db_doesnt_exist():
    SimpleDB(test_db)
    assert os.path.isfile(test_db)

def test_class_init_db_exist_without_data():
    sb = SimpleDB(test_db)
    result = sb.bytes_offset
    assert len(result) == 0 

def test_class_init_db_exist_with_data():
    str_text = """1,{"name":"London","attractions":["Big Ben","London Eye"]}
12,{"name":"San Francisco","attractions":["Golden Gate Bridge"]}
"""
    byte_text = str.encode(str_text)
    with open(test_db, "wb") as bytefile:
        bytefile.write(byte_text)
    
    sb = SimpleDB(test_db)
    result = sb.bytes_offset
    assert len(result) == 2

def test_get_from_db():
    sb = SimpleDB(test_db)
    result = sb.get('1')
    should = '{"name":"London","attractions":["Big Ben","London Eye"]}\n'
    assert result == should

def test_add_to_db():
    sb = SimpleDB(test_db)

def test_teardown():
    os.remove(test_db)
    assert not os.path.isfile(test_db)