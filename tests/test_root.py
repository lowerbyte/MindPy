from core.root import Root
from core.record import RecordOnScreen


TEST_FILE_PATH = 'tests/_resources/test.json'


def test_singleton():
    r1 = Root(0, 0)
    r2 = Root(1, 1)

    assert r1 is r2


def test_serialize(tmpdir):
    root = Root(0, 0)
    root.children = [RecordOnScreen()]

    f = tmpdir.join('output.txt')
    root.serialize(f.strpath)

    with open(TEST_FILE_PATH, 'r') as test_f:
        test_f_content = test_f.read()

    assert f.read() == test_f_content


def test_deserialize():
    tree_root = Root.deserialize(TEST_FILE_PATH)

    assert isinstance(tree_root, Root)
    assert len(tree_root.children) == 1
    assert len(tree_root.children[0].children) == 0
    assert tree_root.y == 0
    assert tree_root.x == 0
