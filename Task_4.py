import Task_2
import Task_1
import Task_3

if __name__ == "__main__":
    h_values = (1, 10)
    sigma = 10
    y_values = (-10, 10)
    sigma_10 = Task_1.give_prior_distribution(h_values, sigma, sigma)
    sigma_10 = {k: v / sum(sigma_10.values()) for k, v in sigma_10.items()}
    print(sum(sigma_10.values()))
    print(sigma_10)
    posterior_2 = Task_2.give_posterior_probability(sigma_10, [(4.5, 2.5)])
    print(posterior_2)
    gen_pred_2 = Task_3.give_general_prediction(y_values, h_values, posterior_2)
    print(gen_pred_2)
    Task_3.plot_contour(y_values, gen_pred_2, "Generalized Predictions with X = {(4.5,2.5)}")


    