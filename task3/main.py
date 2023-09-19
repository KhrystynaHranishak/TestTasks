import numpy as np
from task3.digit_classifier import DigitClassifier

algorithm_name = 'cnn'  # possible values: 'cnn', 'rf', 'rand'
classifier = DigitClassifier(algorithm_name=algorithm_name)
result = classifier.predict(np.random.rand(28, 28, 1))
print(result)
