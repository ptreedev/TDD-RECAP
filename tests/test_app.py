from app import index

def test_index_returns_a_list_of_duties():
    result = index()
    assert result == ['duty1', 'duty2', 'duty3']
