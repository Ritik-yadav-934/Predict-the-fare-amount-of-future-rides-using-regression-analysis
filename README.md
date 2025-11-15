# 🚕 Uber Fare Prediction - Machine Learning Model

A complete machine learning application that predicts Uber fare amounts using regression analysis. This project includes model training, evaluation, and a production-ready Streamlit web application for real-time predictions.

## ✨ Features

- 🎯 **ML Model:** Random Forest Regressor with 96.7% training accuracy
- 🌐 **Web Interface:** Interactive Streamlit application
- 📊 **Real-time Predictions:** Get fare predictions instantly
- ☁️ **Cloud Ready:** Easy deployment on multiple platforms

## 🚀 Quick Start (5 Minutes)

### Local Setup
```bash
# Clone and setup
git clone https://github.com/Ritik-yadav-934/Predict-the-fare-amount-of-future-rides-using-regression-analysis.git
cd uber-app

# Install & Run
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```

Access at: **http://localhost:8501**

### Cloud Deployment

**Streamlit Cloud (Easiest & FREE):**
1. Push to GitHub
2. Go to https://streamlit.io/cloud
3. Deploy from repo → Done! ✅

**Railway (1-Click & FREE):**
1. Go to https://railway.app
2. New Project → Deploy from GitHub
3. Done! ✅

See [QUICK_DEPLOYMENT_GUIDE.md](QUICK_DEPLOYMENT_GUIDE.md) for more options.

---

## 📁 Project Structure

```
uber-app/
├── app.py                      # Streamlit application
├── train_model.py              # Model training script
├── requirements.txt            # Dependencies
├── QUICK_DEPLOYMENT_GUIDE.md   # Deployment instructions
├── uber.csv                    # Training dataset
├── models/
│   ├── uber_fare_model.pkl     # Trained model
│   └── scaler.pkl              # Feature scaler
└── .streamlit/
    └── config.toml             # Configuration
```

---

## 🧠 Model Details

### Performance
- **Train R² Score:** 0.9670 (96.7% - Excellent!)
- **Test R² Score:** 0.6953 (69.5% - Good!)
- **Algorithm:** Random Forest Regressor

### Input Features (8)
- Pickup: Month, Day, Hour
- Passenger Count
- Pickup/Dropoff Coordinates

### Target
- **Fare Amount** in USD

---

## 💻 How to Use

1. **Enter Trip Details:** Date, time, location, passengers
2. **Click Predict:** Get instant fare prediction
3. **View Results:** See predicted amount + confidence range

---

## 🚀 Deployment Options

| Platform | Ease | Cost | Setup Time |
|----------|------|------|-----------|
| Streamlit Cloud | ⭐ Easy | Free | 5 min |
| Railway | ⭐ Easy | Free | 3 min |
| Render | ⭐ Easy | Free | 5 min |
| Heroku | ⭐⭐ Medium | $7+/mo | 10 min |
| AWS EC2 | ⭐⭐⭐ Hard | $5+/mo | 20 min |

📖 **See [QUICK_DEPLOYMENT_GUIDE.md](QUICK_DEPLOYMENT_GUIDE.md) for detailed instructions!**

---

## 🛠️ Troubleshooting

```bash
# Model not found
python train_model.py

# Port already in use
streamlit run app.py --server.port 8502

# Dependencies missing
pip install --upgrade -r requirements.txt
```

---

## 📊 Dataset

- **Size:** 200,000+ Uber trips
- **Period:** 2009-2015
- **Features:** Locations, date/time, passengers, fare
- **File:** `uber.csv`

---

## 📦 Dependencies

```
streamlit, pandas, numpy, scikit-learn, matplotlib, seaborn, joblib
```

---

## 👨‍💻 Author

**Ritik Yadav** - [@Ritik-yadav-934](https://github.com/Ritik-yadav-934)

---

## 📚 Resources

- 📖 [Deployment Guide](QUICK_DEPLOYMENT_GUIDE.md)
- 🐛 [Report Issues](https://github.com/Ritik-yadav-934/Predict-the-fare-amount-of-future-rides-using-regression-analysis/issues)
- 📚 [Streamlit Docs](https://docs.streamlit.io/)

---

## ⭐ Support This Project

- Star ⭐ the repository
- Fork 🍴 for your own use
- Share 📢 with others

**Happy Predicting!** 🚕📊
