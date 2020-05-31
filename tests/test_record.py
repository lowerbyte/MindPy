from core.record import RecordOnScreen
import curses
import pytest


def test_add_child():
    parent = RecordOnScreen()
    parent.add_child(RecordOnScreen())

    assert len(parent.children) == 1


def test_remove_child():
    parent = RecordOnScreen()
    child = RecordOnScreen()
    parent.add_child(child)
    parent.remove_child(child)

    assert len(parent.children) == 0


def test_delete(simple_tree):
    # delete child and it's children
    simple_tree.children[0].delete()

    assert len(simple_tree.children) == 4


def test_edit():
    rec = RecordOnScreen()
    rec.data = 'Test data'

    rec.edit('New test data')

    assert rec.data == 'New test data'


@pytest.mark.parametrize('key', [
    curses.KEY_RIGHT,
    curses.KEY_DOWN,
    curses.KEY_UP,
    curses.KEY_LEFT,
])
def test_select(simple_tree, key):
    test_rec = simple_tree.children[2]
    selected = RecordOnScreen.select(test_rec, key)

    if key == curses.KEY_RIGHT:
        assert selected == test_rec.children[0]
    elif key == curses.KEY_DOWN:
        assert selected == test_rec.parent.children[1]
    elif key == curses.KEY_UP:
        assert selected == test_rec.parent.children[3]
    elif key == curses.KEY_RIGHT:
        assert selected == test_rec.parent


def test_to_json():
    rec = RecordOnScreen(0, 0)
    rec.children = [RecordOnScreen()]

    json_dir = rec.toJSON()

    assert json_dir == {"data": "None", "y": 0, "x": 0, "children":
                        [{"data": "None", "y": 0, "x": 0, "children": []}]}
