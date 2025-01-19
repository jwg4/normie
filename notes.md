# Technical notes

NCST refers to the book 'New Cambridge Statistical Tables, Second Edition', by D. V. Lindley and W. F. Scott, published 1984 by Cambridge University Press, ISBN 0-521-48485-5.

## Validation
- Wichura 1988 has a method for checking the algo which uses random values drawn from the real line. (It seems more sensible to transform evenly spaced uniform variates, than random uniform variates.)
- we could check the derivative of the cdf quite easily it seems, and generate pdf values to compare to.