def ncst_tail_approximation(x):
    if -3.3 < x < 3.3:
        return None
    if x > 0.0:
        return 1.0 - ncst_tail_approximation(-x)
    
    sq = x ** 2

    exp_term = exp(-sq/2.0)
    denom_term = -x * sqrt(2 * pi)
    polynomial_term = 1 - 1 / sq + 3 / sq ** 2 - 15 / sq ** 3 + 105 / sq ** 4

    return exp_term / denom_term * polynomial_term