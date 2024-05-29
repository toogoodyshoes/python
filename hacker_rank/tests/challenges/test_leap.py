from challenges.leap import leap


def test_is_leap_year():
    num = 2400

    result = leap(num)

    assert result is True


def test_is_not_leap_year():
    num = 2500

    result = leap(num)

    assert result is False
