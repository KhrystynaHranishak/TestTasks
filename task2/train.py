import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import sys


def train_and_save_model(data_path, model_path):

    data = pd.read_csv(data_path)

    # Feature generation
    data['6_square'] = data['6'].apply(lambda x: x ** 2)

    X = data['6_square'].values.reshape(-1, 1)
    y = data['target']

    # Training
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)

    # Testing
    y_pred = lin_reg.predict(X_test)
    # MSE
    mse_error_test = mean_squared_error(y_pred, y_test)
    # R_square
    R_square_test = lin_reg.score(X_test, y_test)
    print('The Mean Square Error(MSE) on Test Set: ', mse_error_test)
    print('R square on Test Set:', R_square_test)

    # Save the trained model to the specified path
    joblib.dump(lin_reg, model_path)
    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:  task2/train.py <path_to_data> <path_to_store_model>")
        sys.exit(1)

    data_path = sys.argv[1]
    model_path = sys.argv[2]

    train_and_save_model(data_path, model_path)
