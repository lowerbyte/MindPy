from core.root import Root
from core.record import RecordOnScreen
import pytest


@pytest.fixture
def simple_tree():
    root = Root(0, 0)
    # list comprehenstion cannot be used with
    # current approach of assignig parent
    for i in range(5):
        root.add_child(RecordOnScreen())
    for child in root.children:
        for i in range(5):
            child.add_child(RecordOnScreen())

    return root
