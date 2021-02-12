import maze
import pytest

@pytest.mark.parametrize("test_file, expected_result", 
    [("maze1.txt", (0,5)),
    ("maze2.txt", (8,13)),
    ("maze3.txt", (2,1)),
    ("maze4.txt", (10,22)),
    ("maze5.txt", (0,5))]
    )

def test_maze(test_file, expected_result):
    mazeRef = maze.Maze(test_file)
    mazeRef.solve()
    assert mazeRef.goal == expected_result