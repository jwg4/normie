# Technical notes

NCST refers to the book 'New Cambridge Statistical Tables, Second Edition', by D. V. Lindley and W. F. Scott, published 1984 by Cambridge University Press, ISBN 0-521-48485-5.

## number theory of normal dist integration

The sequence of even-numbered (central) moments of a Gaussian is given by 

> 1, 1, 3, 15, 105, 945, ...

This is OEIS A001147:

> Double factorial of odd numbers: a(n) = (2\*n-1)!! = 1\*3\*5\*...\*(2n-1).

What is the connection between the combinatoric significance of this sequence and the Gaussian? Does expansion of the Gaussian integral through integration by parts illuminate this?

The formula given in NCST for approximating tail values of erf is given in test/helpers.py. It contains the expansion:

> 1 - 1/x^2 + 3/x^4 - 15/x^6 + 105/x^8

and quotes a relative error based on this truncation of less than 945/x^10. This seems to imply that the sequence converges for small 1/x (whereas it seems to have radius of convergence 0) and that the truncation error is approximated by the next term (but the terms increase eventually since sooner or later 2n-1 / x^2 will be bigger than 1). Check the analysis of this, they probably know what they are talking about.

Does it rely on a Taylor expansion for exp(1/x^2)??

A comment from the OEIS entry:

> From Tom Copeland, Nov 13 2007, clarified in first and extended in second paragraph, Jun 12 2021: (Start)

> a(n) has the e.g.f. (1-2x)^(-1/2) = 1 + x + 3\*x^2/2! + ..., whose reciprocal is (1-2x)^(1/2) = 1 - x - x^2/2! - 3\*x^3/3! - ... = b(0) - b(1)\*x - b(2)\*x^2/2! - ... with b(0) = 1 and b(n+1) = -a(n) otherwise. By the formalism of A133314, Sum_{k=0..n} binomial(n,k)\*b(k)\*a(n-k) = 0^n where 0^0 := 1. In this sense, the sequence a(n) is essentially self-inverse. See A132382 for an extension of this result. See A094638 for interpretations.

> This sequence aerated has the e.g.f. e^(t^2/2) = 1 + t^2/2! + 3\*t^4/4! + ... = c(0) + c(1)\*t + c(2)\*t^2/2! + ... and the reciprocal e^(-t^2/2); therefore, Sum_{k=0..n} cos(Pi k/2)\*binomial(n,k)\*c(k)\*c(n-k) = 0^n; i.e., the aerated sequence is essentially self-inverse. Consequently, Sum_{k=0..n} (-1)^k*binomial(2n,2k)\*a(k)\*a(n-k) = 0^n. (End)

This suggests that the derivation does rely on a Taylor expansion for the Gaussian pdf, and that the sequence of derivatives has meaning in the integration by parts expansion?

Is there a Gamma-type function which corresponds to this? Is this a decomposition of Gamma as the quotient of two functions based on the above sequence?

## testing the NCST approximation

How is this different from the current implementation for large values? Should we adopt it?

## Behavior when cdf(x) is close to 0.

The smallest positive double is very small. Experimentally our current implementation seems to show that cdf(8.0) > 0 but that cdf(9.0) is indistinguishable from 0 as a double. Don't have any way of verifying this at the moment

## Behavior when cdf(x) is close to 1.

It is straightforward to identify the max relative error in double representation ~= the closest number to 1 which isn't 1. This is about 1 - 2**(-53) or 1 - 10**(-16). Back of envelope calculations (to check) gives this as cdf(8.49).

Verifying this relies on being able to use either the complex approximation from NCST above, or the much simpler approximation for large x

> 1 - erf(x) ~ exp(-x**2) / (x sqrt(pi))

(Can we reconcile at least the first term of the above with this? )


