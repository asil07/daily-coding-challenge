import numpy as np
import matplotlib.pyplot as plt

# Explanation
# - Alice and Bob are playing a fantasy game with Fire Dragon (F), Water Serpent (W), Earth Golem (E).
# - If they choose different creatures, one of them scores a point.
# - The task is to determine how many distinct sequences Bob can play to guarantee beating Alice's score.

# Let's write a function to solve the problem.
MOD = 10**9 + 7

# Mapping for points
points = {
    ('F', 'W'): 1,  # Water beats Fire
    ('W', 'E'): 1,  # Earth beats Water
    ('E', 'F'): 1,  # Fire beats Earth
}

def count_bob_sequences(s):
    n = len(s)
    # Define dynamic programming tables to hold the counts
    dp_win = np.zeros((n, 3), dtype=np.int64)  # Counts the winning sequences
    dp_all = np.zeros((n, 3), dtype=np.int64)  # Holds counts of all valid sequences
    
    # Initial round setup
    dp_all[0] = [1, 1, 1]  # Each type is possible at round 0
    dp_win[0] = [0, 0, 0]  # No winning score at round 0
    # Base conditions on how to beat
    if s[0] == 'F':
        dp_win[0][1] = 1  # Water beats Fire
    elif s[0] == 'W':
        dp_win[0][2] = 1  # Earth beats Water
    elif s[0] == 'E':
        dp_win[0][0] = 1  # Fire beats Earth

    # Iterate for each round
    for i in range(1, n):
        # Consider Bob's choices and the previous sequences
        for bob_move in range(3):  # F=0, W=1, E=2
            for prev_move in range(3):
                if bob_move != prev_move:  # Bob cannot play the same move consecutively
                    dp_all[i][bob_move] += dp_all[i-1][prev_move]
                    dp_all[i][bob_move] %= MOD
                    # Check if Bob wins this round
                    if (s[i], bob_move) in points:
                        dp_win[i][bob_move] += dp_all[i-1][prev_move]
                    else:
                        dp