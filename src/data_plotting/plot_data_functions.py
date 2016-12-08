import matplotlib.pyplot as plt

def plot_data_n_classes(data, x_lim=[-1.5, 1.5], y_lim=[-1.0, 1.0], colors = ['r', 'b', 'g']):

    axes = plt.gca()
    axes.set_xlim(x_lim)
    axes.set_ylim(y_lim)

    class_index = 0
    for data_class in data:
        for data_pair in data_class:
            plt.scatter(data_pair[0], data_pair[1], color=colors[min(class_index, len(colors)-1)])
        class_index += 1

    plt.show()
