from abc import ABC, abstractmethod
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.exceptions import NotFittedError
from keras import Sequential
from keras.layers import Conv2D, Flatten, Dense, BatchNormalization, Dropout


class DigitClassificationInterface(ABC):

    @abstractmethod
    def predict(self, image):
        pass


class CNNModel(DigitClassificationInterface):

    def __init__(self, input_shape=(28, 28, 1)):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=input_shape))
        model.add(BatchNormalization())
        model.add(Conv2D(32, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(Conv2D(32, kernel_size=5, strides=2, padding='same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))

        model.add(Conv2D(64, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(Conv2D(64, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(Conv2D(64, kernel_size=5, strides=2, padding='same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))

        model.add(Conv2D(128, kernel_size=4, activation='relu'))
        model.add(BatchNormalization())
        model.add(Flatten())
        model.add(Dropout(0.4))
        model.add(Dense(10, activation='softmax'))

        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])

        self.model = model

    def train(self, X_train, y_train):
        raise Exception("Not implemented")

    def evaluate(self, X_test, y_test):
        raise Exception("Not implemented")

    def predict(self, image):
        prediction = self.model.predict(image)
        return np.argmax(prediction)


class RFModel(DigitClassificationInterface):

    def __init__(self, n_estimators=10):
        self.model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)

    def train(self, X_train, y_train):
        raise Exception("Not implemented")

    def evaluate(self, X_test, y_test):
        raise Exception("Not implemented")

    def predict(self, image_flattened):
        try:
            prediction = self.model.predict([image_flattened])
            return prediction[0]
        except NotFittedError:
            print("Random Forest model is not trained")


class RandomModel(DigitClassificationInterface):

    def predict(self, crop_image):
        return np.random.randint(10)


class DigitClassifier:

    def __init__(self, algorithm_name):
        if algorithm_name == 'cnn':
            self.model = CNNModel()
            self.preprocessor = lambda x: np.expand_dims(x, axis=0)
        elif algorithm_name == 'rf':
            self.model = RFModel()
            self.preprocessor = lambda x: x.reshape(-1)
        elif algorithm_name == 'rand':
            self.model = RandomModel()
            self.preprocessor = lambda x: x[9:19, 9:19]
        else:
            raise ValueError(f"Unknown algorithm: {algorithm_name}")

    def predict(self, image):
        return self.model.predict(self.preprocessor(image))
