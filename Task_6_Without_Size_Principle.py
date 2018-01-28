import Task_1
import Task_3


def give_non_size_principal_likelihood(h_index, x_list):
    count = 0
    for x in x_list:
        if h_index > 0:
            if -h_index <= x[0] <= h_index:
                if -h_index <= x[-1] <= h_index:
                    count += 1

    if count == len(x_list):
        return 1
    else:
        return 0


def give_posterior_probability(sig_12, x):
    posterior_x = {}
    for h in sig_12:
        area_h = give_non_size_principal_likelihood(h, x)
        posterior_x[h] = sig_12[h]*area_h
    return posterior_x


if __name__ == "__main__":

    x_data = ()
    h_values = (1, 10)
    y_values = (-10, 10)
    sigma_12 = Task_1.give_prior_distribution((1, 10), 12, 12)
    sigma_12 = {k: v / sum(sigma_12.values()) for k, v in sigma_12.items()}
    print(sum(sigma_12.values()))
    print(sigma_12)
    posterior = give_posterior_probability(sigma_12, [(1.5, 0.5)])
    print(posterior)
    print(sum(posterior.values()))
    Task_1.plot_bar(posterior, "(sigma = 12) Hypothesis", "Posterior probability")

    # part a
    posterior_3 = give_posterior_probability(sigma_12, [(2.2, -0.2)])
    print(posterior_3)
    gen_pred_3 = Task_3.give_general_prediction(y_values, h_values, posterior_3)
    print(gen_pred_3)
    Task_3.plot_contour(y_values, gen_pred_3, "Generalized Predictions with X = {(2.2, -2)}")
    # part b
    posterior_4 = give_posterior_probability(sigma_12, [(2.2, -0.2), (0.5, 0.5)])
    print(posterior_4)
    gen_pred_4 = Task_3.give_general_prediction(y_values, h_values, posterior_4)
    print(gen_pred_4)
    Task_3.plot_contour(y_values, gen_pred_4, "Generalized Predictions with X = {(2.2, -2),(0.5, 0.5)}")
    # part c
    posterior_5 = give_posterior_probability(sigma_12, [(2.2, -0.2), (0.5, 0.5), (1.5, 1)])
    print(posterior_5)
    gen_pred_5 = Task_3.give_general_prediction(y_values, h_values, posterior_5)
    print(gen_pred_5)
    Task_3.plot_contour(y_values, gen_pred_5, "Generalized Predictions with X = {(2.2, -2),(0.5, 0.5), (1.5, 1)}")




