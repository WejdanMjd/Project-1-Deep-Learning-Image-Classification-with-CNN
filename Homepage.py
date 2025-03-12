import streamlit as st  
import tensorflow as tf  
from PIL import Image  
import numpy as np  
import matplotlib.pyplot as plt  


model_cnn1 = tf.keras.models.load_model("C:/Users/HUAWI/Multipage/Models/Model1.h5")
model_cnn2 = tf.keras.models.load_model("C:/Users/HUAWI/Multipage/Models/Model2.h5")
model_cnn3 = tf.keras.models.load_model("C:/Users/HUAWI/Multipage/Models/Model3.h5")

class_names = ['butterfly', 'cat', 'chicken', 'cow', 'dog', 
               'elephant', 'horse', 'sheep', 'spider', 'squirrel']

def predict(image, model):
    img_array = np.array(image) / 255.0
    img_array = tf.image.resize(img_array, [model.input_shape[1], model.input_shape[2]])
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    class_id = np.argmax(prediction)
    return class_id, prediction  

def run_homepage():
    st.title("Welcome to the Image Classification App using AI")
    
   
    st.write("**Neural Vision:**")
    st.write("Ranwah sadik")
    st.write("Razan alkhamisi")
    st.write("Wejdan alharthi")
    st.write(" ")
    st.write("In this app, our team developed 3 models for image classification.")
    st.write("Here are the available models:")
    st.write("- **CNN Model 1 : MobileNet**")
    st.write("The **MobileNet model** achieves high accuracy (95% on training, 94% on validation and test sets), showcasing its effective learning and generalization capabilities through transfer learning.")
    st.write("- **CNN Model 2 : ResNet**")
    st.write("We use the **ResNet model** in transfer learning to leverage pre-trained features, improving our model’s accuracy by adapting it to a new task with fewer data.")
    st.write("- **CNN Model 3 : Our First CNN Model**")
    st.write("The **CNN first model** achieves 67% accuracy")
    st.write(" ")
    st.write("**Choose a model from the sidebar to start**")
    

    page = st.sidebar.selectbox("Choose a model", ["Mobilenet Model", "ResNet Model", "CNN Model"])


    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file) 
        st.image(image, caption="Uploaded Image", use_column_width=True)  
        
        if page == "Mobilenet Model":
            st.title("CNN Model 1")
            class_id, probabilities = predict(image, model_cnn1)  
            st.write(f"Predicted class: {class_names[class_id]}")  
            

            fig, ax = plt.subplots()
            ax.bar(class_names, probabilities[0])  
            ax.set_xlabel('Class')  
            ax.set_ylabel('Probability')  
            ax.set_title('Class Probabilities')  
            plt.xticks(rotation=90)  
            st.pyplot(fig)  

        elif page == "ResNet Model":
            st.title("CNN Model 2")
            class_id, probabilities = predict(image, model_cnn2)  
            st.write(f"Predicted class: {class_names[class_id]}")  
            

            fig, ax = plt.subplots()
            ax.bar(class_names, probabilities[0]) 
            ax.set_xlabel('Class')  
            ax.set_ylabel('Probability')  
            ax.set_title('Class Probabilities')  
            plt.xticks(rotation=90)  
            st.pyplot(fig)  


        elif page == "CNN Model":
           st.title("CNN Model 3")
           class_id, probabilities = predict(image, model_cnn3)  
           st.write(f"Predicted class: {class_names[class_id]}")  
           


           fig, ax = plt.subplots()
           ax.bar(class_names, probabilities[0])  
           ax.set_xlabel('Class')  
           ax.set_ylabel('Probability')  
           ax.set_title('Class Probabilities')  
           plt.xticks(rotation=90)  
           st.pyplot(fig)  

if __name__ == "__main__":
    run_homepage()  
