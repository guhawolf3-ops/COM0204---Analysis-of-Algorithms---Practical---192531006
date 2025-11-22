import random
import statistics

# -------------------------------
# 1️⃣ Simulate tossing n coins
# -------------------------------
def simulate_coin_tosses(n, trials=1000):
    heads_counts = []

    for _ in range(trials):
        # Each toss: 1 = Head, 0 = Tail (Indicator variable)
        tosses = [1 if random.random() < 0.5 else 0 for _ in range(n)]
        heads_counts.append(sum(tosses))  # Sum of indicators = number of heads

    expected_value = statistics.mean(heads_counts)
    variance = statistics.variance(heads_counts)
    return expected_value, variance


# -------------------------------
# 2️⃣ Hiring problem simulation
# -------------------------------
def simulate_hiring_problem(n, trials=1000):
    hires_counts = []

    for _ in range(trials):
        best = 0
        hires = 0
        # Randomly order candidates
        candidates = [random.random() for _ in range(n)]
        for score in candidates:
            # Indicator variable: hire if score is best so far
            if score > best:
                hires += 1
                best = score
        hires_counts.append(hires)

    expected_value = statistics.mean(hires_counts)
    variance = statistics.variance(hires_counts)
    return expected_value, variance


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    n = 10  # number of coins/candidates
    trials = 1000

    print("---- Using Indicator Random Variables ----\n")

    # Coin toss simulation
    exp_heads, var_heads = simulate_coin_tosses(n, trials)
    print(f"Coin Toss Simulation (n={n}, trials={trials})")
    print(f"  Expected number of Heads ≈ {exp_heads:.2f}")
    print(f"  Variance ≈ {var_heads:.2f}\n")

    # Hiring problem simulation
    exp_hires, var_hires = simulate_hiring_problem(n, trials)
    print(f"Hiring Problem Simulation (n={n}, trials={trials})")
    print(f"  Expected number of Hires ≈ {exp_hires:.2f}")
    print(f"  Variance ≈ {var_hires:.2f}")
