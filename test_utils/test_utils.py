from develop import utils

def test_get_data():
    assert len(utils.get_data('operations.json')) is not None

def test_get_operations_executed(test_data):
    assert len(utils.get_operations_executed(test_data)) == 2

def test_get_last_num_operations(test_data):
    pass