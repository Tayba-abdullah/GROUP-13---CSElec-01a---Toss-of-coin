import matplotlib.pyplot as plt

# ==============================
# INSERT YOUR GIVEN DATA
# ==============================

# 1 Peso Coin (1A) – Heads list (1 = Head, 0 = Tail)
coin_1A = [
1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,
1,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1,
1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,
1,1,1,0,0,0,0,0,1,0
]

# 10 Peso Coin (10A)
coin_10A = [
0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,
1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,
0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,
0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,
1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1
]

# ==============================
# FUNCTION
# ==============================

def calculate_cumulative(flips_list):
    heads_cum = []
    tails_cum = []
    h_count = 0
    t_count = 0

    for flip in flips_list:
        if flip == 1:
            h_count += 1
        else:
            t_count += 1
        
        heads_cum.append(h_count)
        tails_cum.append(t_count)

    attempts = list(range(1, len(flips_list) + 1))
    return attempts, heads_cum, tails_cum

# Calculate running totals
attempts_1A, heads_1A, tails_1A = calculate_cumulative(coin_1A)
attempts_10A, heads_10A, tails_10A = calculate_cumulative(coin_10A)

# ==============================
# GRAPH FOR 1 PESO (1A)
# ==============================

plt.figure("1 Peso Coin (1A)", figsize=(10,6))
plt.plot(attempts_1A, heads_1A, label="Heads", linewidth=2)
plt.plot(attempts_1A, tails_1A, label="Tails", linestyle="--", linewidth=2)

plt.title("1 Peso Coin (1A) - Cumulative Running Total", fontweight="bold")
plt.xlabel("Toss Number")
plt.ylabel("Running Total")
plt.legend()
plt.grid(True)

# ==============================
# GRAPH FOR 10 PESO (10A)
# ==============================

plt.figure("10 Peso Coin (10A)", figsize=(10,6))
plt.plot(attempts_10A, heads_10A, label="Heads", linewidth=2)
plt.plot(attempts_10A, tails_10A, label="Tails", linestyle="--", linewidth=2)

plt.title("10 Peso Coin (10A) - Cumulative Running Total", fontweight="bold")
plt.xlabel("Toss Number")
plt.ylabel("Running Total")
plt.legend()
plt.grid(True)

# ==============================
# COMBINED COMPARISON
# ==============================

plt.figure("Combined Comparison", figsize=(12,8))

plt.plot(attempts_1A, heads_1A, label="1A Heads", linewidth=2)
plt.plot(attempts_1A, tails_1A, label="1A Tails", linestyle="--", linewidth=2)

plt.plot(attempts_10A, heads_10A, label="10A Heads", linewidth=2)
plt.plot(attempts_10A, tails_10A, label="10A Tails", linestyle="--", linewidth=2)

plt.title("Cumulative Heads vs Tails Comparison (1A vs 10A)", fontweight="bold")
plt.xlabel("Toss Number")
plt.ylabel("Cumulative Count")
plt.legend()
plt.grid(True)

print("Displaying all 3 graphs...")
plt.show()
