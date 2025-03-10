# Animal Classification Using Deep Learning 

This project implements a deep learning-based image classification model to classify animals into various categories using **Convolutional Neural Networks (CNN)**, **ResNet50V2**, and **MobileNet** for feature extraction.
## 🚀 Features
- **Custom CNN Model** trained for image classification
- **MobileNet Transfer Learning** model for improved accuracy
- **Jupyter Notebook for Model Training (`dl-image-classification-final.ipynb`)**
- **Saved Models (`CNN.h5`, `MobileNet.h5`)**
- **Python Homepage (`Homepage.py`) for Model Inference**
- **Test Images (`test_image` folder)**

## 📊 Model Performance  
We trained three different models on the dataset and obtained the following accuracies:  

| Model        | Accuracy |
|-------------|---------|
| **CNN**         | **67%**  |
| **MobileNet**   | **94%**  |
| **ResNet50V2**  | **90%**  |

- **MobileNet performed the best** due to **transfer learning**, achieving **94% accuracy**.  
- **ResNet50V2** also showed strong performance with **90% accuracy**.  
- The **CNN model**, trained from scratch, achieved **67% accuracy**.  


## ResNet50V2 Model and Presentation Links

Due to the large size of the ResNet50V2 model and presentation file, they are hosted on Google Drive. You can access them using the links below:

- **ResNet50V2 Model:** [Download Here](https://drive.google.com/file/d/1BfKY86KVhM5c_DJO7kVbWx8MA7WuYf0v/view?usp=sharing)  
- **Presentation:** [Download Here](https://drive.google.com/file/d/1qpbPCvsmpaZzQkDsFlibKUy8XOAGepJQ/view?usp=sharing)


## 📂 Project Structure  
📦 Deep Learning Animal Classifier
│-- 📜 README.md - Project documentation
│-- 📜 Homepage.py - Main script for running the app
│-- 📜 dl-image-classification-final.ipynb - Jupyter Notebook with training code
│-- 📜 CNN.h5 - Trained CNN model
│-- 📜 MobileNet.h5 - Trained MobileNet model
│-- 📂 test_image/ - Sample images for testing
