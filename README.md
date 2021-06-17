# normie - Python package for normal distribution functions

## Examples of use

```
>>> from normie import cdf, invcdf
>>> cdf(2.0)
0.9772498607635498
>>> invcdf(0.5)
0.0

```

## How it works.
The package uses C code, to be found in src/normie_impl.c

The code uses a built-in function for the cumulative distribution function, and a polynomial approximation for the inverse.
