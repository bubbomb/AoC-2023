from challenge8 import get_steps_to_z

TEST_INPUT="""
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip()


def test_get_steps_to_z():
    assert get_steps_to_z(TEST_INPUT) == 6