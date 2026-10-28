# Iris Classification

A Python program that predicts the type of iris flower based on the length and width of the sepal and petal in centimeters using the K-Nearest Neighbors (KNN) algorithm.

## Overview

This project implements a simple machine learning classifier that takes four measurements as input:

- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

It then compares the input against a training dataset and predicts the iris species:

- Setosa
- Versicolor
- Virginica

## Files

- `Iris prediction.py` - main script containing the KNN classifier and input handling
- `iris.csv` - training dataset expected by the program (must be placed in the same directory as the script)

## Dataset Format

The program expects a CSV file named `iris.csv` with a header row in the following format:

```csv
sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,setosa
6.2,2.9,4.3,1.3,virginica
```

## How to Run

1. Make sure Python 3 is installed.
2. Place your `iris.csv` file in the same folder as `Iris prediction.py`.
3. Run the script:

```bash
python "Iris prediction.py"
```

4. Enter the four iris measurements in centimeters when prompted.
5. The program will print the predicted iris class.

## Example

```text
Please enter the measurements in centimeters:
Enter Sepal Length: 5.1
Enter Sepal Width: 3.5
Enter Petal Length: 1.4
Enter Petal Width: 0.2

Predicted Iris Class: setosa
```

## Notes

- The classifier uses Euclidean distance to find the closest neighbors.
- `k` is set to 3 by default to reduce tie situations.
- This project is a beginner-friendly example of KNN classification in Python.

## License

This project does not currently include a license file. Add one if you plan to share or distribute the project publicly.
