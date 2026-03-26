🏭 Manufacturing Prediction System
📌 Project Overview
This project is a **Machine Learning-based Manufacturing Prediction System** that predicts output based on input parameters using a trained model.
It includes:
* Backend for prediction
* Frontend interface
* Dataset for training
* Pre-trained ML model
  🚀 Features
* Predict manufacturing output using ML
* Simple and interactive interface
* Uses real dataset (1000 samples)
 🛠️ Tech Stack

Python
Flask (Backend)
Machine Learning (Linear Regression)
HTML/CSS(Frontend)

📂 Project Structure

Manufacturing_Project/
│── Backend/
│   └── backend.py
│
│── Frontend/
│   └── app.py
│
│── Data/
│   └── manufacturing_dataset_1000_samples.csv
│
│── Model/
│   ├── linear_regression_model.pkl
│   └── scaler.pkl
⚙️ How to Run the Project

 1️⃣ Clone the Repository


git clone https://github.com/adharsh801/manufacturing-project.git
cd manufacturing-project
2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Backend
python Backend/backend.py
4️⃣ Run Frontend
python Frontend/app.py
 📊 Dataset

The dataset contains 1000 samples of manufacturing data used to train the model.
🤖 Model

Algorithm: Linear Regression
Includes preprocessing using a scaler
Saved using `.pkl` files
🎯 Future Improvements

* Add advanced ML models
* Improve UI design
* Deploy as a web application
* Add real-time data input
👨‍💻 Author
Adharsh
GitHub: https://github.com/adharsh801
If you like this project, give it a ⭐ on GitHub!
