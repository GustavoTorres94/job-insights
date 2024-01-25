from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "python") == 1639
    assert count_ocurrences("data/jobs.csv", "java") == 676
    assert count_ocurrences("data/jobs.csv", "sql") == 1748
    assert count_ocurrences("data/jobs.csv", "aws") == 860
    assert count_ocurrences("data/jobs.csv", "spark") == 870
