import re

import ghoststructure


def test_version_is_a_semantic_version_string() -> None:
    assert re.fullmatch(r"\d+\.\d+\.\d+", ghoststructure.__version__) is not None
