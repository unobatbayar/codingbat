"""

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True

@author unobatbayar

"""

def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  elif weekday == True or vacation == False:
    return False