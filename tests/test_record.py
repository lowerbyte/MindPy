from core.record import Record, RecordOnScreen
from tests.test_visitor import simple_tree

def test_add_child():
    parent = RecordOnScreen()
    parent.add_child(RecordOnScreen())

    assert len(p.children) == 1


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
