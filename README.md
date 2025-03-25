# Animal Classification Using Deep Learning 🦁  

This project implements a deep learning-based image classification model to classify animals into various categories using **Convolutional Neural Networks (CNN)**, **ResNet50V2**, and **MobileNet** for feature extraction.

## 📌 Dataset  

We used the **Animals-10 Dataset**, a publicly available dataset on **Kaggle** that contains images of 10 different animal species.  

📌 **Dataset Source:** [Animals-10 Dataset on Kaggle](https://www.kaggle.com/datasets/alessiocorrado99/animals10)  

### 📂 Dataset Overview  

The dataset consists of **~26,000 images** categorized into **10 animal classes**, originally labeled in **Italian**.  
We renamed them to **English** for consistency.  

## 🚀 Features
- **Custom CNN Model** trained for image classification
- **MobileNet Transfer Learning** model for improved accuracy
- **ResNet50V2** for high-performance classification
- **Multi-class classification** with 10 animal categories
- Handles a dataset of **26,000+ images**

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

📦 **Deep Learning Animal Classifier**  
│-- 📜 `README.md` - Project documentation  
│-- 📜 `Homepage.py` - Main script for running the app  
│-- 📜 `Deep Learning Animal classifier.ipynb` - Jupyter Notebook with training code  
│-- 📜 `CNN.h5` - Trained CNN model  
│-- 📜 `MobileNet.h5` - Trained MobileNet model  
│-- 📂 `test_image/` - Sample images for testing  

## Team members
- Ranwah Sadik
- Razan Alkhamisi
- Wejdan Alharthi

