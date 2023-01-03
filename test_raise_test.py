import pytest


def raise_exception():
    raise Exception("Error!")


def return_no_exception():
    return 1

def raise_assertion_error():
    assert 1 == 0

def test_use_pytest_raise():
    with pytest.raises(Exception):
        raise_exception()


def test_use_pytest_raises_error():
    with pytest.raises(Exception):
        return_no_exception()

def test_without_raise():
    raise_exception()

def test_check_exception_type():
    # Assertion Error가 나야 함
    with pytest.raises(ZeroDivisionError):
        raise_assertion_error()

def test_err_message():
    with pytest.raises(Exception) as error_info:
        raise_exception()

    assert str(error_info.value) == "Error!"
    assert error_info.value.args[0] == "Error! No"
    print("Assert문 통과!")
