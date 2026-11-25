import pytest

from sum_def import f, func


def test_answer():
    assert func(3)


def test_answer_multples():
    with pytest.raises(SystemExit):
        f()
