# 🔥 Forest Fire Prediction Web App

This project is a **Flask-based web application** that predicts the likelihood of a forest fire based on environmental and weather-related parameters.  
The app uses a trained **Ridge Regression model** and a **StandardScaler** for preprocessing.

---

## 🚀 Features
- User-friendly web interface built with Flask.
- Takes multiple input features such as temperature, humidity, wind speed, etc.
- Scales the input data using a pre-trained scaler.
- Predicts output using a Ridge Regression model.
- Displays prediction results dynamically on the frontend.

---

## 🛠️ Tech Stack
- **Python**
- **Flask**
- **scikit-learn**
- **pandas / numpy**
- **HTML (Jinja2 templates)**

---

## 📂 Project Structure
```bash
├── app.py # Main Flask application
├── models/
│ ├── ridge.pkl # Pre-trained Ridge Regression model
│ ├── scaler.pkl # Pre-trained StandardScaler
├── templates/
│ ├── index.html # Landing page
│ ├── home.html # Prediction results page
├── requirements.txt # Dependencies
└── README.md # Project documentation
```

---

## ⚡ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <https://github.com/pranav-mahure/Test-forestfire.git>
   cd <Test-forestfire>
   ```
2. **Create & activate a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate       # Mac/Linux
    venv\Scripts\activate          # Windows
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Flask app**
    ```bash
    python app.py
    ```
5. **Open your browser at:**
    ```bash
    http://0.0.0.0:5000/   or   http://127.0.0.1:5000/
    ```
---

## 📊 Input Features

* Temperature 🌡️<br/>
* Relative Humidity (RH) 💧<br/>
* Wind Speed (Ws) 🌬️<br/>
* Rain 🌧️<br/>
* Fine Fuel Moisture Code (FFMC)<br/>
* Duff Moisture Code (DMC)<br/>
* Initial Spread Index (ISI)<br/>
* Classes<br/>
* Region<br/>

---

## 🖼️ Example Workflow
* User enters values in the web form.<br/>
* Data is scaled using the pre-trained StandardScaler.<br/>
* Ridge Regression model predicts fire risk.<br/>
* Prediction is shown on the results page.<br/>

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

This project is licensed under the MIT License.