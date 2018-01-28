import matplotlib.pyplot as plt
import Task_2
import Task_3


def give_uninformative_prior(s1, s2):
    k = s1*s2
    prob = 1/k
    return prob


# Considering square hypothesis, s1 = s2 = 2k
def give_prior_distribution(h_range):
    i = h_range[0]
    j = h_range[-1]
    prior_dist = {}
    for k in range(i, j+1):
        prior_dist[k] = give_uninformative_prior(2*k, 2*k)
    return prior_dist


def plot_bar(prob_distribution, label_x, label_y):
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.bar(prob_distribution.keys(), prob_distribution.values())
    plt.show()


if __name__ == "__main__":

    prior = give_prior_distribution((1, 10))
    y_values = (-10, 10)
    h_values = (1, 10)
    summation = sum(prior.values())
    print(summation)
    print(prior)
    plot_bar(prior, "Hypothesis", "Raw Uninformative Prior")
    sigma = {k: v / summation for k, v in prior.items()}
    plot_bar(sigma, "Hypothesis", "Normalized Uninformative Prior Probability")
    print(sigma)
    print(sum(sigma.values()))

    posterior_3 = Task_2.give_posterior_probability(sigma, [(2.2, -0.2)])
    print(posterior_3)
    gen_pred_3 = Task_3.give_general_prediction(y_values, h_values, posterior_3)
    print(gen_pred_3)
    Task_3.plot_contour(y_values, gen_pred_3, "Generalized Predictions with X = {(2.2, -2)}")
    # part b
    posterior_4 = Task_2.give_posterior_probability(sigma, [(2.2, -0.2), (0.5, 0.5)])
    print(posterior_4)
    gen_pred_4 = Task_3.give_general_prediction(y_values, h_values, posterior_4)
    print(gen_pred_4)
    Task_3.plot_contour(y_values, gen_pred_4, "Generalized Predictions with X = {(2.2, -2),(0.5, 0.5)}")
    # part c
    posterior_5 = Task_2.give_posterior_probability(sigma, [(2.2, -0.2), (0.5, 0.5), (1.5, 1)])
    print(posterior_5)
    gen_pred_5 = Task_3.give_general_prediction(y_values, h_values, posterior_5)
    print(gen_pred_5)
    Task_3.plot_contour(y_values, gen_pred_5, "Generalized Predictions with X = {(2.2, -2),(0.5, 0.5), (1.5, 1)}")






