import numpy as np


class NeuralNetwork:

    def __init__(self, input_layer_size, hidden_layer_size, output_layer_size):
        #np.random.seed(1)

        self.W1 = np.random.randn(input_layer_size, hidden_layer_size)
        self.W2 = np.random.randn(hidden_layer_size, output_layer_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoidPrime(self, z):
        return np.exp(-z) / ((1 + np.exp(-z)) ** 2)

    def forward(self, X):
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)

        return yHat

    def costFunctionPrime(self, X, y):
        yHat = self.forward(X)

        delta3 = np.multiply(-(y - yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)

        delta2 = np.multiply(np.dot(delta3, self.W2.T), self.sigmoidPrime(self.z2))
        dJdW1 = np.dot(X.T, delta2)

        return dJdW1, dJdW2

    def train(self, training_set_inputs, training_set_outputs, number_of_iterations):
        for i in range(number_of_iterations):
            dJdW1, dJdW2 = self.costFunctionPrime(training_set_inputs, training_set_outputs)

            self.W1 -= dJdW1
            self.W2 -= dJdW2


if __name__ == "__main__":
    neural_network = NeuralNetwork(2, 20, 2)

    print("Random starting synaptic weights 1: ")
    print(neural_network.W1)

    print("Random starting synaptic weights 2: ")
    print(neural_network.W2)

    training_set_raw_inputs = np.array([[3, 5], [1, 6], [4, 7]]).astype(float)
    training_set_raw_outputs = np.sqrt(training_set_raw_inputs.astype(float))

    raw_input_max = np.max(training_set_raw_inputs)
    raw_output_max = np.max(training_set_raw_outputs)

    training_set_inputs = training_set_raw_inputs / raw_input_max
    training_set_outputs = training_set_raw_outputs / raw_output_max

    neural_network.train(training_set_inputs, training_set_outputs, 200000)

    print("Post training synaptic weights 1: ")
    print(neural_network.W1)

    print("Post training synaptic weights 2: ")
    print(neural_network.W2)

    output = neural_network.forward(training_set_inputs)


    print("Input values")
    print(training_set_raw_inputs)

    print("Expected output")
    print(training_set_raw_outputs)

    print("Calculated Output")
    print(output * raw_output_max)
