from app import index
import duties_controller


def test_get_duties_returns_at_least_one_duty(mocker):
    mocker.patch("duties_controller.get_duties",return_value=["duty1"])
    duties = duties_controller.get_duties()
    assert len(duties) > 0
    assert "duty1" in duties

def test_a_duty_works_as_it_should(mocker):
    mocker.patch("duties_controller.get_duties",return_value=[{'name': 'duty1'}])
    first_duty = duties_controller.get_duties()[0]
    assert first_duty['name']



