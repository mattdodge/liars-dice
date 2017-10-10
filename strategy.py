def get_kurts_bid(dice, num_dice_matt_has, matts_bid=None):
    """ Get Kurt's bid given his dice and how many dice Matt has.

    Return a tuple of what your bid is or return 'CALL' to call Matt's bid

    Example:
        To bid three 5s, return (3, 5)
        To call Matt's bid return 'CALL'
    """

    # This is set to the value of your dice, assuming you have only one
    my_dice = dice[0]

    if my_dice == 1:
        if matts_bid is None:
            return (1, 2)
        else:
            return (matts_bid[0] + 1, matts_bid[1])

    else:
        if matts_bid is None:
            return (3, my_dice)  # Might as well try and trap him
        elif (matts_bid[0], my_dice) > matts_bid:
            return (matts_bid[0], my_dice)  # Hoping for [1, 1, 3] against [4]
        else:
            # Hope he has all 1s? Not sure this will matter
            return (matts_bid[0] + 1, my_dice)


def get_matts_bid(dice, num_dice_kurt_has, kurts_bid=None):
    """ Given some dice, return what should Matt bid.

    The strategy is fixed, bet the highest possible number guaranteed
    to succeed. If that bid is not higher than the current bid, then call

    Returns:
        (count, digit): "I bid <count> <digit>s"

    Example: dice = [1, 1, 3, 3, 5, 5] would bet four 5's (return (4, 5))
    """
    bids = [0] * 7  # we want a count for every digit (ignore 0)
    # see how many of each die we have
    for die in dice:
        bids[die] += 1

    # Find out which digit we should bid (which one has the most)
    digit_to_bid = 2  # start with 2s, we won't bid wildcards
    for i in range(3, 7):
        if bids[i] >= bids[digit_to_bid]:
            digit_to_bid = i

    # Bid the number of that digit plus the number of wild cards
    my_bid = (bids[digit_to_bid] + bids[1], digit_to_bid)

    if kurts_bid is None or my_bid > kurts_bid:
        return my_bid
    elif kurts_bid == my_bid:
        # In the case where Kurt bids exactly what I would have bid, I have
        # no choice but to go one higher
        return (my_bid[0] + 1, my_bid[1])
    else:
        return "CALL"
