import pytest
from core.root import Root
from core.record import RecordOnScreen
from core.visitor import Visitor
from unittest.mock import Mock, patch


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


@patch('core.canvas.Canvas')
@patch('core.path.Path')
def test_visit(mock_path, mock_canvas, simple_tree):
    ''' Well test of this function is very hacky.
    First of all Canvas and Path are patched, to not be
    considered in scope of this test.
    Later pad.addstr is replaced with lamda (callable was needed)
    to return None and finally refresh method of Canvas id mocked
    to get call_count. Because this function is allways called
    whenever Visitor.visit method is called we can calculate
    how many time visit was called for our simple tree.
    '''
    mock_canvas.pad.addstr = lambda x, y, z: None
    mock_canvas.refresh = Mock()
    v = Visitor(mock_canvas)
    simple_tree.accept(v)

    # visit shloud be called 31 times - one for each record
    assert mock_canvas.refresh.call_count == 31
