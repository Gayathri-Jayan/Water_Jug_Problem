
import pytest
from solver import bfs_solve


@pytest.mark.parametrize(
    "capacity_a, capacity_b, target, expected",
    [
        (4, 3, 2, True),
        (3, 5, 4, True),
        (4, 6, 3, False),
        (3, 5, 6, False),
        (4, 3, 0, True),
        (2, 3, 1, True),
        (5, 7, 6, True),
    ],
)
def test_bfs_solve(capacity_a, capacity_b, target, expected):
    result = bfs_solve(capacity_a, capacity_b, target)

    assert (result is not None) == expected

    if result is not None:
        path = result["path"]

        assert result["operations"] == len(path) - 1
        assert path[0]["state"] == (0, 0)

        final_a, final_b = path[-1]["state"]
        assert final_a == target or final_b == target

        for item in path:
            a, b = item["state"]
            assert 0 <= a <= capacity_a
            assert 0 <= b <= capacity_b



def test_zero_target():
    result = bfs_solve(4, 3, 0)

    assert result is not None
    assert result["operations"] == 0
    assert result["path"][0]["state"] == (0, 0)


def test_target_equal_to_jug_capacity():
    result = bfs_solve(4, 3, 4)

    assert result is not None
    final_a, final_b = result["path"][-1]["state"]
    assert final_a == 4 or final_b == 4


def test_impossible_target():
    result = bfs_solve(6, 4, 3)

    assert result is None


def test_target_exceeds_both_capacities():
    result = bfs_solve(4, 3, 5)

    assert result is None
