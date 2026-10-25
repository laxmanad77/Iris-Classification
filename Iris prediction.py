import csv
import math
from collections import Counter


def euclidean_distance(point1, point2):
    """Calculates the Euclidean distance between two data points."""
    distance = 0.0
    # The first 4 elements are the numeric features (sepal/petal dimensions)
    for i in range(4):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)


def knn_predict(filename, test_data, k):
    # 1. Load the data
    training_data = []
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                if row:  # Ensure the row is not empty
                    # Convert the first 4 columns to floats, keep the 5th as the string label
                    features = [float(val) for val in row[:4]]
                    label = row[4]
                    training_data.append(features + [label])
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found. Please ensure it is in the same directory."

    # 2. Initialize the value of k (handled via the function parameter 'k')
    distances = []

    # 3. Iterate from 1 to the total number of training data points
    for train_row in training_data:
        # 4. Calculate the distance between the test data and each row of training data
        dist = euclidean_distance(test_data, train_row)
        distances.append((train_row, dist))

    # 5. Sort the calculated distances in ascending order based on distance values
    # distances is a list of tuples: (training_row_data, distance_value)
    distances.sort(key=lambda tup: tup[1])

    # 6. Get top k rows from the sorted array
    top_k_rows = []
    for i in range(k):
        top_k_rows.append(distances[i][0])

    # 7. Get the most frequent class of these rows
    top_k_labels = [row[-1] for row in top_k_rows]
    most_frequent_class = Counter(top_k_labels).most_common(1)[0][0]

    # 8. Return the predicted class
    return most_frequent_class


if __name__ == "__main__":
    print("--- Iris KNN Classifier ---")
    print("Please enter the measurements in centimeters:")

    try:
        # Accepts input of 4 floating point numbers
        sepal_length = float(input("Enter Sepal Length: "))
        sepal_width = float(input("Enter Sepal Width:  "))
        petal_length = float(input("Enter Petal Length: "))
        petal_width = float(input("Enter Petal Width:  "))

        test_instance = [sepal_length, sepal_width, petal_length, petal_width]

        # Initialize k (commonly set to an odd number like 3 or 5 to prevent ties)
        k_value = 3

        # Run the classifier using "iris.csv"
        prediction = knn_predict("iris.csv", test_instance, k_value)

        print("\n--------------------------------")
        print(f"Predicted Iris Class: {prediction}")
        print("--------------------------------")

    except ValueError:
        print("\nInvalid input. Please enter valid numbers (e.g., 5.1).")