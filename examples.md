# Examples

```
>>> from normie import cdf
>>> cdf(0.1)  # doctest: +ELLIPSIS
0.5398278...
>>> cdf(100.0)
1.0
>>> cdf(-2.0)  # doctest: +ELLIPSIS
0.022750131...

```

```
>>> from normie import invcdf
>>> invcdf(0.1)  # doctest: +ELLIPSIS
-1.28155...
>>> invcdf(0.5)
0.0
>>> invcdf(0.7)  # doctest: +ELLIPSIS
0.524400...
>>> invcdf(0.99)  # doctest: +ELLIPSIS
2.32634...
>>> invcdf(0.0)
nan
>>> invcdf(-0.7)
nan
>>> invcdf(2.0)
nan

```
