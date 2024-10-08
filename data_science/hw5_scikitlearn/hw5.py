from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import interactive


if __name__ == '__main__':
    # Напишіть програму на Python:
    # a. щоб завантажити дані ірису з вказаного файлу csv у dataframe та надрукувати форму даних, тип даних та перші 3 рядки.

    iris_data = load_iris()
    species_dict = {i: name for i, name in enumerate(iris_data.target_names)}

    iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    iris_df['species_id'] = iris_data.target
    iris_df['species_name'] = iris_df['species_id'].map(species_dict)

    ### save *.csv file from sklearn.datasets:
    filename = 'iris_data.csv'
    iris_df.to_csv(filename, index=False)

    ### read *.csv file:
    df = pd.read_csv(filename)

    ### RESULT:
    print(f'Форма даних: {df.shape}')
    print(f'Тип даних: {type(df)}')
    print(f'Перші три рядки: \n{df.head(3)}')

    # b. за допомогою Scikit-learn, щоб надрукувати ключі, кількість рядків-стовпців, назви ознак та опис даних Ірису.
    print(f'\nКлючі набору: {iris_data.keys()}')
    print(f'\nКількість рядків і стовпців: {iris_data.data.shape}')
    print(f'\nНазви ознак: {iris_data.feature_names}')
    print(f'\nОпис даних:\n{iris_data.DESCR}')

    # c. щоб переглянути базові статистичні деталі, як-от перцентиль, середнє, стандартне відхилення тощо даних ірису.
    all_species_info = df.drop(columns=['species_id', 'species_name']).describe()
    print(all_species_info)

    # d. щоб отримати спостереження кожного виду (сетоза, версиколор, віргініка) з даних ірису
    species = df['species_name'].unique()

    for s in species:
        info = df[df['species_name'] == s].drop(columns=['species_id', 'species_name']).describe()
        print(f'\nAnalysis of {s.upper()}\n {info}')

    # e. щоб створити графік для отримання загальної статистики даних Ірис.

    ### check nullables:
    print(f'check nullables:')
    print(df.isnull().sum())

    f1 = plt.figure(1)
    sns.pairplot(data=df.drop(columns=['species_id']), hue='species_name', palette='Set1', markers=["o", "^", "D"])
    plt.title('Загальна статистика ірисів')

    # f. Напишіть програму на Python, щоб створити стовпчасту діаграму для визначення частоти трьох видів Ірис.
    f2 = plt.figure(2)
    sns.barplot(df['species_name'].value_counts())
    plt.title('Частота видів ірисів')

    # g. для розподілу набору даних ірисів на його атрибути (X) та мітки (y). Змінна X містить перші чотири стовпці (тобто атрибути), а y містить мітки набору даних
    x = iris_data.data
    y = iris_data.target

    # h. за допомогою Scikit-learn для розділення набору даних ірисів на 70% тренувальних даних та 30% тестових даних.
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, train_size=0.7, random_state=42)

    print(f'train x shape: {x_train.shape}')
    print(f'train y shape: {y_train.shape}')
    print(f'test x shape: {x_test.shape}')
    print(f'test y shape: {y_test.shape}')

    # З загальної кількості 150 записів, набір для тренування міститиме 120 записів, а тестовий набір - 30 з цих записів. Виведіть обидва набори даних.
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=30, train_size=120, random_state=42)

    print(f'train x shape: {x_train.shape}')
    print(f'train y shape: {y_train.shape}')
    print(f'test x shape: {x_test.shape}')
    print(f'test y shape: {y_test.shape}')

    # i. Напишіть програму на Python за допомогою Scikit-learn для перетворення стовпців видів у числовий стовпець набору даних ірисів. Для кодування цих даних кожне значення перетворіть на число. Наприклад, Iris-setosa:0, Iris-versicolor:1 та Iris-virginica:2. Тепер виведіть набір даних ірисів на 80% тренувальних даних і 20% тестових даних. З загальної кількості 150 записів, набір для тренування міститиме 120 записів, а тестовий набір - 30 з цих записів. Виведіть обидва набори даних.

    ### Encoding species column
    enc = LabelEncoder()
    df['encoded_species'] = enc.fit_transform(df['species_name']).reshape(-1, 1)

    x = df.drop(columns=['species_id', 'species_name', 'encoded_species']).to_numpy()
    y = df['encoded_species'].to_numpy()

    ### Data split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, random_state=42)
    print(f'\ntrain x {x_train.shape}:')
    print(x_train)

    print(f'\ntrain y {y_train.shape}:')
    print(y_train)
    print(f'\ntest x {x_test.shape}:')
    print(x_test)
    print(f'\ntest y {y_test.shape}:')
    print(y_test)

    # j. Напишіть програму на Python за допомогою Scikit-learn для розділення набору даних ірисів на 70% тренувальних даних та 30% тестових даних. З загальної кількості 150 записів, набір для тренування міститиме 105 записів, а тестовий набір - 45 з цих записів. Прогнозуйте відповідь для тестового набору даних (SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm) за допомогою алгоритму найближчих сусідів (K Nearest Neighbor Algorithm). Використовуйте 5 як кількість сусідів.¶
    x = iris_data.data
    y = iris_data.target
    # data split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(x_train, y_train)

    y_pred = knn.predict(x_test)

    print(y_test)
    print(y_pred)

    ### metrics
    score = knn.score(x_test, y_test)
    acc_score = accuracy_score(y_test, y_pred)

    print(f'Score: {score}')
    print(f'Accuracy score: {acc_score}')

    interactive(False)
    plt.show()