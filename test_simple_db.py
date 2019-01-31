import pytest
import pickle
import simple_db as sd

class TestSimpleDB(object):

    # TODO Use monkey patch and setup/teardown for propper tests


    def test_save_dict(self):
       test_dict = {0:"text", 1:"more text", 2:"even more text"}
       sd.save_dict(test_dict)
       
       with open("db_dump.pkl", "rb") as f:
           rs = pickle.load(f)
           assert test_dict == rs

    def test_load_dict(self):
        test_dict = {0:"text", 1:"more text", 2:"even more text"}
        rs = sd.load_dict()
        assert test_dict == rs
