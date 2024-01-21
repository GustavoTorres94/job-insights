from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "python") == 89
    assert count_ocurrences("data/jobs.csv", "java") == 85
    assert count_ocurrences("data/jobs.csv", "sql") == 76
    assert count_ocurrences("data/jobs.csv", "aws") == 60
    assert count_ocurrences("data/jobs.csv", "spark") == 37
