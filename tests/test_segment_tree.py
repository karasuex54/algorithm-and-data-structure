import unittest
import segment_tree

class TestSegmentTree(unittest.TestCase):
    def test_min(self):
        data = [5, 10, 15, 20, 25]
        ST = segment_tree.SegmentTree(data)
        query = [[2,0,6,5], [1,0,4], [2,0,6,4], [2,1,6,10]]
        for q in query:
            if q[0] == 1:
                ST.update(q[1], q[2])
            else:
                self.assertEqual(q[3], ST.query(q[1], q[2]))

    def test_max(self):
        data = [5, 10, 15, 20, 25]
        ST = segment_tree.SegmentTree(data, max, -float("inf"))
        query = [[2,0,6,25], [1,0,30], [2,0,6,30], [2,1,6,25]]
        for q in query:
            if q[0] == 1:
                ST.update(q[1], q[2])
            else:
                self.assertEqual(q[3], ST.query(q[1], q[2]))

if __name__ == '__main__':
    unittest.main()
