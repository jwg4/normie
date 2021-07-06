# Examples

```
>>> from normie import cdf
>>> cdf(0.1)
0.539827823638916
>>> cdf(100.0)
1.0
>>> cdf(-2.0)
0.0227501317858696

```

```
>>> from normie import invcdf
>>> invcdf(0.1)
-1.2815500497817993
>>> invcdf(0.5)
0.0
>>> invcdf(0.7)
0.5244004726409912
>>> invcdf(0.99)
2.326348066329956
>>> invcdf(0.0)
nan
>>> invcdf(-0.7)
nan
>>> invcdf(2.0)
nan

```
