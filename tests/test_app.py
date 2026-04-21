from app import index

def test_index_returns_a_list_of_duties():
    result = index()
    duty_list = ['duty1', 'duty2', 'duty3', 'duty4']
    for duty in duty_list:
        assert duty in result

