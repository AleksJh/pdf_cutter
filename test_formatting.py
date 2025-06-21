# This is a test file to verify that black, flake8, and isort are working
# together with the configured line length of 88

from typing import Dict, List


def example_function_with_long_name_to_test_line_length(
    parameter1: str, parameter2: int, parameter3: List[str]
) -> Dict[str, any]:
    """This is an example function with a long name to test line length formatting.

    Args:
        parameter1: A string parameter
        parameter2: An integer parameter
        parameter3: A list of strings parameter

    Returns:
        A dictionary with the parameters
    """
    result = {
        "parameter1": parameter1,
        "parameter2": parameter2,
        "parameter3": parameter3,
        "very_long_key_name_to_test_line_wrapping": (
            "This is a very long string value that should be wrapped "
            "by black according to the 88 character limit we've set"
        ),
    }
    return result


if __name__ == "__main__":
    # This is a very long list that should be formatted by black
    # according to our line length setting
    long_list = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
    ]

    # This is a very long dictionary that should be formatted by black
    # according to our line length setting
    long_dict = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
        "key4": "value4",
        "key5": "value5",
        "key6": "value6",
    }

    print(
        example_function_with_long_name_to_test_line_length("test", 42, ["a", "b", "c"])
    )
