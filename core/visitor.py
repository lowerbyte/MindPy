from core.record import Record
from box import Box, RootBox
import core.tree
import logging

class Visitor:
    """ Visitor class - mainly used to print the tree
    """
    y, x, s = 0, 0, 0
    def visit(self, rec: Record):
        #print(rec.__class__.__name__, rec.data)
        if isinstance(rec, core.tree.Tree):
            logging.warning('RootBox')
            rb = RootBox(rec)
            rb.print()
            Visitor.y, Visitor.x, Visitor.s = rb.get_win_pos_and_size()
            Visitor.x = Visitor.x + Visitor.s + 1
        else:
            Box(rec, Visitor.y, Visitor.x).print()
        for child in rec.children:
            child.accept(self)