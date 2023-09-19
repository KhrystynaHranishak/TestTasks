## Task 2: Regression on tabular data
The solution includes 
* the notebook with exploration data analysis and highlighted observation/conclusions
* script to train a model
* script to make a predictions

### Limitations
The train script duplicates a training of the best model chosen during exploration phase, so it does not include automatic feature selection and other experiments to find the best model.


### Requirements
* Python 3.10
* Jupyter Notebook
* IPython Kernel for Jupyter (`ipython kernel install --user --name=TestTasks`)
* `pip install -r requirements.txt`

### How to use
* To train a model run the `train.py` script from terminal (e.g. `python task2/train.py task2/data/train.csv task2/model/regression_model.pkl`)
* To calculate predictions run the `predict.py` script from terminal (e.g. `python task2/predict.py task2/data/hidden_test.csv task2/model/regression_model.pkl task2/data/hidden_test_predictions.csv`)


