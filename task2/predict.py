import pandas as pd
import joblib
import sys


def predict_and_save_results(data_path, model_path, results_path):

    model = joblib.load(model_path)
    data = pd.read_csv(data_path)

    # preprocessing
    data['6_square'] = data['6'].apply(lambda x: x ** 2)

    predictions = model.predict(data['6_square'].values.reshape(-1, 1))
    predictions_df = pd.DataFrame(predictions, columns=['Prediction'])

    predictions_df.to_csv(results_path, index=False)
    print(f"Predictions saved to {results_path}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: task2/predict.py <path_to_data> <path_to_model> <path_to_store_results>")
        sys.exit(1)

    data_path = sys.argv[1]
    model_path = sys.argv[2]
    results_path = sys.argv[3]

    predict_and_save_results(data_path, model_path, results_path)