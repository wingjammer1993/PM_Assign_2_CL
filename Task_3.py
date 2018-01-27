import numpy as np
import matplotlib.pyplot as plt
import Task_2
import Task_1


def give_point_prediction(y, h_range, h_x_probability):
    y_prediction = {}
    for h_index in range(h_range[0], h_range[-1]+1):
        if h_index > 0:
            if -h_index <= y[0] <= h_index:
                if -h_index <= y[-1] <= h_index:
                    y_prediction[h_index] = h_x_probability[h_index]
                else:
                    y_prediction[h_index] = 0
            else:
                y_prediction[h_index] = 0

    return y_prediction


def give_general_prediction(y_range, h_range, h_x_probability):
    general_prediction = np.zeros((21, 21))
    for row in range(y_range[0], y_range[-1]+1):
        for col in range(y_range[0], y_range[-1]+1):
            prediction = give_point_prediction((row, col), h_range, h_x_probability)
            probability = sum(prediction.values())
            general_prediction[row+10][col+10] = probability

    return general_prediction


def plot_contour(y_range, gen_prediction, label):
    x = np.arange(y_range[0], y_range[-1]+1)
    y = np.arange(y_range[0], y_range[-1]+1)
    X, Y = np.meshgrid(x, y)
    plt.title(label)
    k = plt.contourf(X, Y, gen_prediction)
    plt.colorbar(k)
    plt.show()


if __name__ == "__main__":
    h_values = (1, 10)
    sigma = 10
    y_values = (-10, 10)
    sigma_10 = Task_1.give_prior_distribution(h_values, sigma, sigma)
    sigma_10 = {k: v / sum(sigma_10.values()) for k, v in sigma_10.items()}
    print(sum(sigma_10.values()))
    print(sigma_10)
    posterior_1 = Task_2.give_posterior_probability(sigma_10, [(1.5, 0.5)])
    print(posterior_1)
    gen_pred_1 = give_general_prediction(y_values, h_values, posterior_1)
    print(gen_pred_1)
    plot_contour(y_values, gen_pred_1, "Generalized Predictions with X = {(1.5,0.5)}")
    plt.show()
    posterior_2 = Task_2.give_posterior_probability(sigma_10, [(4.5, 2.5)])
    print(posterior_2)
    gen_pred_2 = give_general_prediction(y_values, h_values, posterior_2)
    print(gen_pred_2)
    plot_contour(y_values, gen_pred_2, "Generalized Predictions with X = {(4.5,2.5)}")


