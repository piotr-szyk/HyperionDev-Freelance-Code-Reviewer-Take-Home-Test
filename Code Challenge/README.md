#### International Standard Book Numbers
Instructions for the Code Challenge can be found here: https://edabit.com/challenge/DpFmDxcyesPfPoFMn

The "International Standard Book Number" task description on
https://edabit.com/challenge/DpFmDxcyesPfPoFMn for how the ISBN-13
is calulated in not correct. The statement: "If the sum is divisible by 10,
the ISBN-13 is valid" is not true. It seems that the procedure is missing
one important step. According to the Appendix 1 (Check digit calculation)
of the ISBN International Users Manual - 7th edition, this is Step 2,
which only renders the reminder. In the missing Step 3, that reminder is
substracted from 10. Also, when we line up the digits with alternating
1s and 3s only first 12 digits should be considered, not 13.
The last digit is the check digit. The correct procedure is as follows:
Each of the first 12 digits of the ISBN is alternately multiplied by 1 and 3.
The check digit is equal to 10 minus the remainder resulting from dividing the
sum of the weighted products of the first 12 digits by 10 with one exception.
If this calculation results in an apparent check digit of 10,
the check digit is 0. I have assumed the correct procedure in the program.
