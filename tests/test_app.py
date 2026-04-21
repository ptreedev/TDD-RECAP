from app import index

# def test_index_returns_a_list_of_duties():
#     result = index()
#     duty_list = ['duty1', 'duty2', 'duty3', 'duty4']
#     for duty in duty_list:
#         assert duty in result

def test_index_returns_a_list_of_duty_dictionaries():
    result = index()
    duty_dict_list = [{
        'name': 'duty1',
        'description': 'Description of duty1',
    }, {
        'name': 'duty2',
        'description': 'Description of duty2',
    }, {
        'name': 'duty3',
        'description': 'Description of duty3',
    }, {
        'name': 'duty4',
        'description': 'Description of duty4',
    }]
    assert isinstance(result[0], dict)

    assert result == duty_dict_list