import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.set_palette('bright')

    penguins = sns.load_dataset('penguins')
    cs = penguins.columns
    params_size = [cs[cs.size - 2], cs[cs.size - 3], cs[0]]

    plt.figure()
    plot_size = sns.scatterplot(data=penguins, x=params_size[0], y=params_size[1], hue=params_size[2])
    plot_size.set_xlabel('body mass, g')
    plot_size.set_ylabel('flipper length, mm')
    plot_size.set_title('Visualizing Penguin Size: Weight and Flipper Length')

    plt.figure()
    plot_size_spec = sns.boxplot(data=penguins,
                                 x=params_size[2], y=params_size[1],
                                 hue=params_size[2],
                                 legend=False, fliersize=5, linewidth=1.5)
    plot_size_spec.set(ylabel='flipper length, mm', title='Flipper Length by Penguin Species')

    numeric_data = penguins.select_dtypes(include='float64')
    plt.figure()
    sns.heatmap(data=numeric_data.corr(), annot=True, fmt='.3f', square=True, linewidths=0.75, cmap='coolwarm')

    plt.show()