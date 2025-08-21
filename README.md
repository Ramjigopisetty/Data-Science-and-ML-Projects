# 🧠 AI Task Manager  

An intelligent task management system powered by **machine learning** and **data-driven analytics**.  
This project helps assign, prioritize, and track tasks for users automatically using AI models, dashboards, and performance trackers.  

---

## 🚀 Features  
- 📊 **Task Dashboard** – Interactive dashboard to visualize tasks and performance.  
- 🤖 **Smart Task Assignment** – Automatically assigns tasks based on user performance and workload.  
- 🧹 **EDA & Cleaning** – Preprocessing and exploratory data analysis of task datasets.  
- 🏆 **Priority Model** – Machine learning model (`priority_model.pkl`) to classify and prioritize tasks.  
- 📈 **Performance Tracking** – Monitors user productivity with historical data.  
- 🔍 **Prediction System** – Predicts task categories using trained ML models (`vectorizer.pkl`).  

---

## 📂 Project Structure  

```
AI_Task_Manager_Project/
│── assign_tasks.py              # Assign tasks to users
│── dashboard.py                 # Main dashboard for visualization
│── eda_analysis.py              # Exploratory data analysis
│── eda_cleaning.py              # Dataset cleaning script
│── predict_task.py              # Predict tasks using ML model
│── smart_assigner.py            # AI-powered task assigner
│── task_classifier.py           # ML model for task classification
│── task_dashboard.py            # Dashboard for task insights
│── task_dataset.py              # Dataset preparation script
│── task_predictor.py            # Task prediction logic
│── track_performance.py         # Track user performance
│── update_user_performance.py   # Update and manage user performance
│── user_tracker.py              # User activity tracking
│
├── tasks.csv                    # Raw task dataset
├── tasks_cleaned.csv            # Cleaned dataset
├── users.csv                    # User details
├── user_data.csv                # User activity data
├── model_predictions.csv        # Model output
│
├── priority_model.pkl           # Trained ML model for prioritization
├── vectorizer.pkl               # Feature vectorizer for text
│
├── config.json                  # Project configurations
├── requirements.txt             # Dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # Project documentation
```

---

## ⚙️ Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/AI_Task_Manager_Project.git
   cd AI_Task_Manager_Project
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up configuration in `config.json`.  

---

## ▶️ Usage  

Run scripts as needed:  

- **Launch Dashboard**  
  ```bash
  python dashboard.py
  ```

- **Assign Tasks Automatically**  
  ```bash
  python assign_tasks.py
  ```

- **Predict Task Category**  
  ```bash
  python predict_task.py
  ```

- **Track User Performance**  
  ```bash
  python track_performance.py
  ```

---

## 📊 Example Workflows  
- Clean dataset → Train model → Predict tasks → Assign automatically → Track performance.  

---

## 📜 License  
This project is open-source. You can use and modify it under the terms of your chosen license.  

---

## 🙌 Contributions  
Feel free to fork the repo, open issues, and submit pull requests.  
