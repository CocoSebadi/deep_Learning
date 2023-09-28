import streamlit as st
import pickle
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

# Define your model
def create_model():
    model = keras.Sequential([
        layers.Dense(units=64, input_shape=[9]),
        layers.Dense(units=32, activation='relu'),
        layers.Dense(units=32, activation='relu'),
        layers.Dense(units=32, activation='relu'),
        layers.Dense(units=32, activation='relu'),
        layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
    return model

# Function to load the selected model
def load_model():
    model_path = '/Users/da_m1_47/Desktop/Wines/Wine.pkl'
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


def main():
    # Title of the web app
    st.title('Wine Quality Prediction')

    # Subheader
    st.subheader('Welcome! Select a model and input features for prediction.')
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url('https://www.paintnite.com/blog/content/images/size/w1600/2021/04/pexels-jonathan-borba-5359802.jpg');
        background-size: cover;
    }
    </style>
    ''' 
   
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Load the selected model
    model = load_model()
    
    # User input for features
    volatile_acidity = st.number_input('Volatile Acidity', min_value=0.0, max_value=2.0, step=0.01, value=0.5)
    citric_acid = st.number_input('Citric Acid', min_value=0.0, max_value=1.0, step=0.01, value=0.3)
    residual_sugar = st.number_input('Regular Sugar', min_value=0.0, max_value=20.0, step=0.1, value=2.0)
    chlorides = st.number_input('Chlorides', min_value=0.0, max_value=1.0, step=0.01, value=0.08)
    free_sulfur_dioxide = st.number_input('Free Sulfur Dioxide', min_value=0, max_value=100, step=3, value=30)
    total_sulfur_dioxide = st.number_input('Total Sulfur Dioxide', min_value=0, max_value=300, step=3, value=100)
    density = st.number_input('Density', min_value=0.85, max_value=1.5, step=0.05, value=0.995)
    sulphates = st.number_input('Sulphates', min_value=0.0, max_value=2.0, step=0.01, value=0.5)
    alcohol = st.number_input('Alcohol', min_value=8.0, max_value=16.0, step=1.0, value=10.0)

# Button for predictions
    clicked = st.button('Get Predictions')

    # Perform predictions when the button is clicked
    if clicked:
        # Create a feature vector from user inputs
        features = np.array([[volatile_acidity, citric_acid, residual_sugar, chlorides,
                              free_sulfur_dioxide, total_sulfur_dioxide, density, sulphates, alcohol]])

        # Perform predictions using the selected model
        prediction = model.predict(features)

        # Display the prediction result
        st.header('Prediction')
        st.write(f'The predicted quality is: {prediction[0]}')

if __name__ == '__main__':
    main()


