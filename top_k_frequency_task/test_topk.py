import pytest

from top_k_freq import top_k_frequent_events


def test_example_1():
    events = [1, 2, 1, 3, 2, 1]
    k = 2

    assert top_k_frequent_events(events, k) == [1, 2]


def test_example_2_with_order_preservation_on_ties():
    events = [4, 4, 1, 2, 2, 3, 1, 3, 2]
    k = 3

    assert top_k_frequent_events(events, k) == [2, 4, 1]


def test_empty_events_returns_empty_list():
    events = []
    k = 3

    assert top_k_frequent_events(events, k) == []


def test_k_zero_returns_empty_list():
    events = [1, 2, 2, 3]
    k = 0

    assert top_k_frequent_events(events, k) == []


def test_k_greater_than_number_of_unique_events():
    events = [1, 1, 2, 3]
    k = 10

    assert top_k_frequent_events(events, k) == [1, 2, 3]


def test_all_elements_have_same_frequency_preserves_original_order():
    events = [5, 1, 3, 2]
    k = 3

    assert top_k_frequent_events(events, k) == [5, 1, 3]


def test_single_element_array():
    events = [99]
    k = 1

    assert top_k_frequent_events(events, k) == [99]


def test_duplicate_single_unique_event():
    events = [7, 7, 7, 7]
    k = 2

    assert top_k_frequent_events(events, k) == [7]


def test_negative_event_ids_are_supported():
    events = [-1, -2, -1, -3, -2, -1]
    k = 2

    assert top_k_frequent_events(events, k) == [-1, -2]


def test_frequency_tie_uses_first_appearance():
    events = [10, 20, 20, 10, 30, 30]
    k = 3

    assert top_k_frequent_events(events, k) == [10, 20, 30]


def test_negative_k_raises_value_error():
    events = [1, 2, 3]

    with pytest.raises(ValueError):
        top_k_frequent_events(events, -1)


def test_non_list_events_raises_type_error():
    events = "1,2,3"

    with pytest.raises(TypeError):
        top_k_frequent_events(events, 2)


def test_non_integer_k_raises_type_error():
    events = [1, 2, 3]

    with pytest.raises(TypeError):
        top_k_frequent_events(events, "2")


def test_non_integer_event_raises_type_error():
    events = [1, 2, "3"]

    with pytest.raises(TypeError):
        top_k_frequent_events(events, 2)