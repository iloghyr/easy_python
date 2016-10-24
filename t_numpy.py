#!/bin/env python
# encoding: utf-8
# vim: set tw=0 shiftwidth=4 tabstop=4 expandtab number:

class Predictor(object):
    """
    Predictor
    """
    def __init__(self, t, y, degree=3):
        """
        @param t: list t
        @param y: list y
        @note: len(t) == len(y) is required, t is odered and y is the same order with t
        
        The following is copied from numpy\lib\polynomial.py:
        `polyfit` issues a `RankWarning` when the least-squares fit is badly
        conditioned. This implies that the best fit is not well-defined due
        to numerical error. The results may be improved by lowering the polynomial
        degree or by replacing `x` by `x` - `x`.mean().
        """
        assert len(t) == len(y)
        
        # the reason for doing this plz ref the comment
        self.min_t = t[0]
        t = map(lambda x:x - self.min_t, t)
        
        # lazy import
        import numpy
        self._ploy1d = numpy.poly1d(numpy.polyfit(t, y, degree))

    def __call__(self, t):
        """
        predict the value at t
        """
        t = t - self.min_t
        return self._ploy1d(t)

if __name__ == "__main__":
    t = [1, 2, 3, 4, 5, 6]
    v = [55, 77, 88, 92, 80, 91]
    t = [1, 2, 3, 4, 5]
    v = [55, 77, 88, 92, 80]
    p = Predictor(t, v)
    print p(6)

