import os
import pytest
from simple_db import SimpleDB

test_db = "test.db"

def test_init_new_db():
    sb = SimpleDB(test_db)
    result = sb.bytes_offset
    assert len(result) == 0

def test_init_db_exist_with_data():
    str_text = """1:{"name":"London","attractions":["Big Ben","London Eye"]}
12:{"name":"San Francisco","attractions":["Golden Gate Bridge"]}
"""
    byte_text = str.encode(str_text)
    with open(test_db, "wb") as bytefile:
        bytefile.write(byte_text)
    
    sb = SimpleDB(test_db)
    result = sb.bytes_offset
    assert len(result) == 2

def test_get_from_db():
    sb = SimpleDB(test_db)
    result = sb.get('12')
    should = '{"name":"San Francisco","attractions":["Golden Gate Bridge"]}\n'
    assert result == should

def test_add_to_db():
    sb = SimpleDB(test_db)
    key = "1234"
    value = '{"name":"Bankok", "attractions":["Wat Pho", "Wat Arun"]}'
    sb.add(key, value)
    should = b'1234:{"name":"Bankok", "attractions":["Wat Pho", "Wat Arun"]}\n'
    with open(test_db, "rb") as f:
        byte_start = list(sb.bytes_offset.values())[-1]
        f.seek(byte_start)
        result = f.readline()
        assert result == should

def test_teardown():
    os.remove(test_db)
    assert not os.path.isfile(test_db)