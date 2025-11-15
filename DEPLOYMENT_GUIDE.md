# 🚕 Uber Fare Prediction - Streamlit Deployment

A machine learning application that predicts Uber fare amounts using regression analysis.

## 📋 Features

- ✅ Real-time fare prediction
- ✅ Interactive UI with Streamlit
- ✅ Random Forest ML model
- ✅ Feature scaling with StandardScaler
- ✅ Easy to deploy on cloud platforms

## 📦 Project Structure

```
uber-app/
├── app.py                 # Main Streamlit application
├── train_model.py         # Model training script
├── requirements.txt       # Python dependencies
├── uber.csv              # Training dataset
├── Uber.ipynb            # Original notebook
├── .streamlit/
│   └── config.toml       # Streamlit configuration
└── models/               # Trained model directory (created after training)
    ├── uber_fare_model.pkl
    └── scaler.pkl
```

## 🚀 Quick Start (Local Setup)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model
```bash
python train_model.py
```

### 3. Run Streamlit App
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## ☁️ Cloud Deployment Options

### Option 1: Deploy on Streamlit Cloud (RECOMMENDED - FREE)

1. **Push code to GitHub:**
   ```bash
   git add .
   git commit -m "Add Streamlit deployment"
   git push
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to https://streamlit.io/cloud
   - Click "Deploy an app"
   - Select your GitHub repo and branch
   - Enter app command: `app.py`
   - Click Deploy

### Option 2: Deploy on Heroku

1. **Install Heroku CLI** from https://devcenter.heroku.com/articles/heroku-cli

2. **Create Procfile:**
   ```
   web: streamlit run --server.port=$PORT --server.address=0.0.0.0 app.py
   ```

3. **Create setup.sh:**
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]" > ~/.streamlit/config.toml
   echo "headless = true" >> ~/.streamlit/config.toml
   echo "port = $PORT" >> ~/.streamlit/config.toml
   echo "enableCORS = false" >> ~/.streamlit/config.toml
   ```

4. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku open
   ```

### Option 3: Deploy on AWS (EC2)

1. **Launch EC2 instance** (Ubuntu 20.04)

2. **SSH into instance:**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Install dependencies:**
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip python3-venv git
   ```

4. **Clone and setup:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd uber-app
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python train_model.py
   ```

5. **Run with Nginx (optional):**
   ```bash
   streamlit run app.py --server.port=8501 &
   ```

### Option 4: Deploy on Railway

1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Select your repository
4. Set environment: `PORT=8501`
5. Click Deploy

### Option 5: Deploy on Render

1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Select GitHub repository
4. Build command: `pip install -r requirements.txt && python train_model.py`
5. Start command: `streamlit run app.py --server.port=$PORT`
6. Deploy

## 🔧 Model Details

- **Algorithm:** Random Forest Regressor
- **Features Used:** 8 features
  - Pickup Month
  - Pickup Day
  - Pickup Hour
  - Passenger Count
  - Pickup Latitude/Longitude
  - Dropoff Latitude/Longitude
- **Target:** Fare Amount (USD)
- **Training Set Size:** 80%
- **Test Set Size:** 20%

## 📊 Input Parameters

| Parameter | Range | Description |
|-----------|-------|-------------|
| Month | 1-12 | Month of trip |
| Day | 1-31 | Day of month |
| Hour | 0-23 | Hour of day (24-hour format) |
| Passengers | 1-6 | Number of passengers |
| Pickup Latitude | -90 to 90 | Starting location latitude |
| Pickup Longitude | -180 to 180 | Starting location longitude |
| Dropoff Latitude | -90 to 90 | Destination latitude |
| Dropoff Longitude | -180 to 180 | Destination longitude |

## 🛠️ Troubleshooting

### Model files not found
**Solution:** Run `python train_model.py` to train and save the model

### Port already in use
**Solution:** 
```bash
streamlit run app.py --server.port 8502
```

### Dependency issues
**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

## 📝 License

This project is open source. Feel free to use and modify as needed.

## 👨‍💻 Author

Ritik Yadav - [GitHub](https://github.com/Ritik-yadav-934)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Happy Deploying!** 🚀
