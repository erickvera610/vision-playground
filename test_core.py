import unittest
from core import transform,convolve
class Tests(unittest.TestCase):
    def test_constant_edges(self): self.assertEqual(transform([[50]*4 for _ in range(4)],'edges'),[[0.]*4 for _ in range(4)])
    def test_blur_preserves_constant(self): self.assertAlmostEqual(transform([[90]*3 for _ in range(3)],'blur')[1][1],90)
    def test_edge_detected(self): self.assertGreater(transform([[0,0,255]]*3,'edges')[1][1],0)
    def test_shape(self): self.assertEqual(len(transform([[1]*5 for _ in range(3)],'blur')),3)
    def test_invalid(self):
        with self.assertRaises(ValueError): convolve([[1],[1,2]],[[1]*3]*3)
