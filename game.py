from strategy import get_matts_bid, get_kurts_bid
from random import randint


def get_random_dice(num_dice):
    """ Get a list of <num_dice> random dice rolls """
    return [randint(1, 6) for _ in range(num_dice)]


def run_simulation(num_kurt_dice, num_matt_dice, kurts_turn=True):
    """ Run a simulation with a number of dice for Kurt and Matt

    Returns True if Kurt wins the game
    """
    while num_kurt_dice and num_matt_dice:
        kurt = get_random_dice(num_kurt_dice)
        matt = get_random_dice(num_matt_dice)
        kurt_wins = play_turn(kurt, matt, kurts_turn)

        # It's the losers turn now
        kurts_turn = not kurt_wins

        # Remove a dice from the loser
        if kurt_wins:
            num_matt_dice -= 1
        else:
            num_kurt_dice -= 1

    return num_kurt_dice > 0


def play_turn(kurt, matt, kurts_turn=True):
    """ Play a turn.

    Go back and forth on the strategies until someone calls.

    Returns:
       kurt_is_winner (True if Kurt wins)
    """
    current_bid = None
    while True:
        if kurts_turn:
            next_bid = get_kurts_bid(kurt, len(matt), current_bid)
        else:
            next_bid = get_matts_bid(matt, len(kurt), current_bid)

        if next_bid == "CALL":
            break

        assert(current_bid is None or next_bid > current_bid)

        # Set the current bid to the most recent and roll the turn over
        current_bid = next_bid
        kurts_turn = not kurts_turn

    bid_satisfied = check_bid(current_bid, matt + kurt)
    # Turn variable indicates the person who made the call
    # Kurt wins if he called (his turn) and bid not satisfied or vice versa
    return kurts_turn != bid_satisfied


def check_bid(bid, dice):
    """ Return true if a bid has been satisfied given some dice """
    total = 0
    for die in dice:
        if die == 1 or die == bid[1]:
            total += 1
    return total >= bid[0]
