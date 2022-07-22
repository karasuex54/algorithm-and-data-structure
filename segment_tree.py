# Test SegmentTree file is tests/test_segment_tree.py.

# 0-index version segment tree.
class SegmentTree:
    def __init__(self, init_val, seg_func=min, ide_ele=float("inf")):
        n = len(init_val)
        self.seg_func = seg_func
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.seg_func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.seg_func(self.tree[k], self.tree[k^1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.seg_func(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.seg_func(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
