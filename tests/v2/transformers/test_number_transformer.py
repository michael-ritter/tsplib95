import pytest

from tsplib95.v2 import exceptions
from tsplib95.v2 import transformers as T


@pytest.fixture
def tf():
    return T.NumberT()


@pytest.mark.parametrize('text,value,error', [
    ('42', 42, None),
    ('-2', -2, None),
    ('0', 0, None),
    ('3.14', 3.14, None),
    ('', None, exceptions.ParsingError),
])
def test_transformer_parse(tf, text, value, error):
    if error is None:
        assert tf.parse(text) == value
    else:
        with pytest.raises(error):
            tf.parse(text)


@pytest.mark.parametrize('value,text,error', [
    (42, '42', None),
    (-2, '-2', None),
    (0, '0', None),
    (3.14, '3.14', None),
    (None, 'None', None),
])
def test_transformer_render(tf, value, text, error):
    if error is None:
        assert tf.render(value) == text
    else:
        with pytest.raises(error):
            tf.render(value)
