from game import run_simulation
from time import monotonic

NUM_SIMULATIONS = 10000
STARTING_DICE_KURT = 1
STARTING_DICE_MATT = 6


def run():
    kurt_win_count = 0
    start = monotonic()
    for i in range(NUM_SIMULATIONS):
        kurt_win_count += run_simulation(STARTING_DICE_KURT,
                                         STARTING_DICE_MATT, False)
    duration = monotonic() - start
    print("Simulation Complete")
    print("-------------------")
    print("Num Simulations: {:,}".format(NUM_SIMULATIONS))
    print("Took:            {0:,.1f} seconds".format(duration))
    print("Kurt Wins:       {:,}".format(kurt_win_count))
    print("Win Percent:     {:.2%}".format(kurt_win_count / NUM_SIMULATIONS))
    print(
        "Wins 1 in {} times".format(
            "Infinite"
            if kurt_win_count == 0 else "{0:.2f}".format(
                NUM_SIMULATIONS / kurt_win_count)))

if __name__ == '__main__':
    run()
