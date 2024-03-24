import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def input_fn(x):
    val=x/5
    
    return model(val)
# Sample data (replace with your dataset)
def model(val):
    data = np.array([
    [0.75, 1],  # Test score of 0.75, course: Newbie (Class 0)
    [0.80, 1],  # Test score of 0.80, course: Intermediate (Class 1)
    [0.90, 2], 
    [0.30, 0],
    [0.42, 0],
    [0.99, 2],
    [0.23, 0]# Test score of 0.90, course: Pro (Class 2)
    # Add more data points
    ])

    # Split data into features (test scores) and labels (course classes)
    X = data[:, 0:1]  # Test scores
    y = data[:, 1]    # Course classes

    # Normalize test scores to zero mean and unit variance
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # One-hot encode course classes
    y = tf.keras.utils.to_categorical(y, num_classes=3)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build a simple feedforward neural network model
    model = Sequential([
    Dense(32, activation='relu', input_dim=1),
    Dense(16, activation='relu'),
    Dense(3, activation='softmax')  # Output layer with 3 classes (3 courses)
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=2)

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test loss: {loss}, Test accuracy: {accuracy}")

    # Make course recommendations for a new student
    new_student_score = np.array([[val]])  # Replace with the test score of the new student
    normalized_score = scaler.transform(new_student_score)
    predicted_probabilities = model.predict(normalized_score)
    predicted_course_index = np.argmax(predicted_probabilities)
    courses = ["Newbie", "Intermediate", "Pro"]
    recommended_course = courses[predicted_course_index]
    
    return recommended_course

input_fn(5)