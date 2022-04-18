### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:

# Self was missed out of parameters boolean values needed capital lettes
# Colon needed after if and else

  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:
      return False
   
# def was spelled as dif. Colons missing. First return statement needed card1

  def highest_card(self, card1, card2):
    if card1.value > card2.value:
      return card1
    else:
      return card2
    
# Self missing as parameter. Colons were missing. String was not interpolated correctly
# added f to start interpolation, + was removed and curly brackets round total was missing

  def cards_total(self, cards):
    total = 0
    for card in cards:
      total += card.value
    return f"You have a total of {total}"