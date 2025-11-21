"""
On a certain day the british pound was equivalent to $1.487 U.S., the french franc was $0.172,
The German deutschemark was $0.548, and the japanese yen was $0.00955.487
Write a program that allows the user to enter an amount in dollars, and then display these value converted,
in the above mentioned monetary units
"""

pound, franc, deutschemark, yen = 1.487, 0.172, 0.548, 0.009555

dollars = float(input("Please enter amount in dollars: "))

print("Converted Rates:\nBritish Pound: {:.3f}\nFrench Franc: {:.3f}\nGerman Deutschemark: {:.3f}\nJapanese Yen: {:.5f}".format(pound*dollars, franc*dollars,deutschemark*dollars,yen*dollars))
