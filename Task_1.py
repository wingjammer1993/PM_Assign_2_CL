import matplotlib.pyplot as plt
import math


def give_expected_size_prior(s1, s2, sig1, sig2):
    k = (s1/sig1) + (s2/sig2)
    prob = math.exp(-k)
    return prob


# Considering square hypothesis, s1 = s2 = 2k
def give_prior_distribution(h_range, sig1, sig2):
    i = h_range[0]
    j = h_range[-1]
    prior_dist = {}
    for k in range(i, j+1):
        prior_dist[k] = give_expected_size_prior(2*k, 2*k, sig1, sig2)
    return prior_dist


def plot_bar(prob_distribution, label_x, label_y):
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.bar(prob_distribution.keys(), prob_distribution.values())
    plt.show()


if __name__ == "__main__":

    # For sig = 6
    sigma_6 = give_prior_distribution((1, 10), 6, 6)
    # For sig = 12
    sigma_12 = give_prior_distribution((1, 10), 12, 12)
    sum_6 = sum(sigma_6.values())
    sum_12 = sum(sigma_12.values())
    print(sum_6)
    print(sum_12)
    print(sigma_6)
    print(sigma_12)
    plot_bar(sigma_6, "(Sigma = 6) Hypothesis", "Raw Expected Prior")
    plot_bar(sigma_12, "(Sigma = 12) Hypothesis", "Raw Expected Prior")
    sigma_6 = {k: v / sum_6 for k, v in sigma_6.items()}
    sigma_12 = {k: v / sum_12 for k, v in sigma_12.items()}
    plot_bar(sigma_6, "(Sigma = 6) Hypothesis", "Normalized Expected Prior Probability")
    plot_bar(sigma_12, "(Sigma = 12) Hypothesis", "Normalized Expected Prior Probability")
    print(sigma_6)
    print(sigma_12)
    print(sum(sigma_6.values()))
    print(sum(sigma_12.values()))



