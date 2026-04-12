# Examples of use

```
>>> from normie_alternatives.abram_steg import erf
>>> erf.erf_approx_7_1_2(0.0)
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    erf.erf_approx_7_1_2(0.0)
    ^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'normie_alternatives.abram_steg.erf' has no attribute 'erf_approx_7_1_2'. Did you mean: 'erf_approx_7_1_25'?
>>> erf.erf_approx_7_1_25(0.0)
0.0
>>> erf.erf_approx_7_1_25(1.0)
0.842716825727904
>>> erf.erf_approx_7_1_25(0.00001)
1.1290486131798616e-05

```