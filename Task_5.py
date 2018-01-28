import Task_2
import Task_1
import Task_3

if __name__ == "__main__":
    h_values = (1, 10)
    sigma = 30
    y_values = (-10, 10)
    sigma_30 = Task_1.give_prior_distribution(h_values, sigma, sigma)
    sigma_30 = {k: v / sum(sigma_30.values()) for k, v in sigma_30.items()}
    print(sum(sigma_30.values()))
    Task_1.plot_bar(sigma_30, "(Sigma = 30) Hypothesis", "Normalized Expected Prior Probability")
    print(sigma_30)
    # part a
    posterior_3 = Task_2.give_posterior_probability(sigma_30, [(2.2, -0.2)])
    print(posterior_3)
    gen_pred_3 = Task_3.give_general_prediction(y_values, h_values, posterior_3)
    print(gen_pred_3)
    Task_3.plot_contour(y_values, gen_pred_3, "Generalized Predictions with X = {(2.2, -2)}")
    # part b
    posterior_4 = Task_2.give_posterior_probability(sigma_30, [(2.2, -0.2), (0.5, 0.5)])
    print(posterior_4)
    gen_pred_4 = Task_3.give_general_prediction(y_values, h_values, posterior_4)
    print(gen_pred_4)
    Task_3.plot_contour(y_values, gen_pred_4, "Generalized Predictions with X = {(2.2, -2),(0.5, 0.5)}")
    # part c
    posterior_5 = Task_2.give_posterior_probability(sigma_30, [(2.2, -0.2), (0.5, 0.5), (1.5, 1)])
    print(posterior_5)
    gen_pred_5 = Task_3.give_general_prediction(y_values, h_values, posterior_5)
    print(gen_pred_5)
    Task_3.plot_contour(y_values, gen_pred_5, "Generalized Predictions with X = {(2.2, -2),(0.5, 0.5), (1.5, 1)}")

