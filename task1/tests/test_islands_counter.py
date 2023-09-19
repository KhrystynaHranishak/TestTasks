from task1.islands_counter import parse_file_input, count_islands

TEST_CASES = 'test_cases.txt'


def test_count_islands():

    test_data = parse_file_input(TEST_CASES)
    for example in test_data:
        assert count_islands(example[0], example[1], example[2]) == example[3]
