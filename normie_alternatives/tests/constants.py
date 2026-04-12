# error function of 5.921587... is 1 - 2^(-54)
# But the largest number less than and distinct from 1
# which can be represent in 64-bit floating point, is 1 - 2^(-53)
# Thus for a input x greater than 5.921.., the erf(x) appears 
# as 1 in 64 bit floats. 
ERF_IS_64_BIT_ONE = 5.93
ERF_IS_64_BIT_MINUS_ONE = 0 - ERF_IS_64_BIT_ONE

TEST_ERF_MAX = ERF_IS_64_BIT_ONE * 2
TEST_ERF_MIN = ERF_IS_64_BIT_MINUS_ONE * 2
