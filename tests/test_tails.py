from normie import cdf

 # List of bold numbers 
bold_numbers = [ 
    3.075, 3.105, 3.138, 3.174, 3.215, 3.263, 3.320, 3.389, 3.480, 
    3.615, 3.731, 3.759, 3.791, 3.826, 3.867, 3.916, 3.976, 4.055, 
    4.173, 4.417 
] 
 
# List of non-bold numbers (boundaries) 
non_bold_numbers = [ 
    0.9990,
    0.9991, 0.9992, 0.9993, 0.9994, 0.9995, 0.9996, 0.9997, 0.9998, 0.9999,
    0.99991, 0.99992, 0.99993, 0.99994, 0.99995, 0.99996, 0.99997, 0.99998, 0.99999, 
    1.00000 
] 
 
 
def test_tail_bounds():
    # Assert that f(bold) is between the corresponding boundaries 
    for i in range(1, len(bold_numbers)): 
        bold = bold_numbers[i] 
        lower_bound = non_bold_numbers[i - 1] 
        upper_bound = non_bold_numbers[i] 
        f_value = cdf(bold) 
        assert lower_bound <= f_value <= upper_bound, f"Assertion failed for bold number {bold}: f({bold}) = {f_value}, not in [{lower_bound}, {upper_bound}]" 

 