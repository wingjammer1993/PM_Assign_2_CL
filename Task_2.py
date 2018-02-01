import matplotlib.pyplot as plt
import math
import Task_1


def give_size_principal_likelihood(h_index, x_list):
    count = 0
    for x in x_list:
        if h_index > 0:
            if -h_index <= x[0] <= h_index:
                if -h_index <= x[-1] <= h_index:
                    count += 1

    if count == len(x_list):
        k = math.pow((4 * h_index * h_index), len(x_list))
        return 1/k
    else:
        return 0


def give_posterior_probability(sig_12, x):
    posterior_x = {}
    for h in sig_12:
        area_h = give_size_principal_likelihood(h, x)
        posterior_x[h] = sig_12[h]*area_h
    sum_post = sum(posterior_x.values())
    posterior_x = {k: v / sum_post for k, v in posterior_x.items()}
    return posterior_x


if __name__ == "__main__":

    x_data = ()
    sigma_12 = Task_1.give_prior_distribution((1, 10), 12, 12)
    sigma_12 = {k: v / sum(sigma_12.values()) for k, v in sigma_12.items()}
    print(sum(sigma_12.values()))
    print(sigma_12)
    posterior = give_posterior_probability(sigma_12, [(1.5, 0.5)])
    print(posterior)
    print(sum(posterior.values()))
    Task_1.plot_bar(posterior, "(sigma = 12) Hypothesis", "Posterior probability")


