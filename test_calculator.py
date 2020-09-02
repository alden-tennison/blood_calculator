import pytest
n = "normal."
bl = "borderline low."
l = "low."
@pytest.mark.parametrize("number,expected",[
    (100,n),
    (59,bl),
    (38,l),
    ])


def test_check_HDL_norm(number,expected):
    from calculator import check_HDL
    result = check_HDL(number)
    assert result == expected
