import unittest
import union_find

class TestUnionFind(unittest.TestCase):
    def test_same(self):
        N = 10
        T = union_find.UnionFind(N)
        query = [[1,2]]
        for x,y in query:
            T.unite(x, y)
        self.assertEqual(True, T.same(1,2))
        self.assertEqual(False, T.same(1,3))

    def test_size(self):
        N = 10
        T = union_find.UnionFind(N)
        query = [[1,2], [2,3], [3,4], [4,5], [5,6]]
        for x,y in query:
            T.unite(x, y)
        self.assertEqual(6, T.size(1))
        self.assertEqual(6, T.size(4))
        self.assertEqual(1, T.size(7))


if __name__ == '__main__':
    unittest.main()
