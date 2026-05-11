# IntelliWatt AI

IntelliWatt AI is an AI-based smart power monitoring dashboard that simulates appliance-wise electricity usage, detects overload conditions, estimates electricity cost, and predicts future power consumption using machine learning.

## Features

- Live appliance-based power monitoring
- AI-based future power usage prediction
- Real-time power usage graph
- Electricity cost estimation
- Overload detection
- Load status indication
- Live activity feed
- Environment selection for Home, Hostel, Office, and Factory

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn

## How It Works

1. The user turns appliances ON or OFF from the simulation panel.
2. Each appliance adds a realistic wattage value to total power usage.
3. The dashboard displays current power usage in watts.
4. A Linear Regression model predicts future power usage from recent power data.
5. The system calculates estimated electricity cost using real billing logic.
6. If usage crosses the overload limit, the dashboard displays an overload alert.
7. A live activity feed records current usage, prediction, cost, and environment.

## Cost Calculation

Electricity cost is calculated using:

```txt
Cost = Power in kW x Cost per Unit x Time in Hours
```

Since the dashboard updates approximately every second, each power reading is converted into kilowatt-hours before calculating cost.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

Open the local dashboard:

```txt
http://localhost:8501
```

## Project Structure

```txt
IntelliWatt-AI/
+-- app.py
+-- README.md
+-- requirements.txt
```
## Project Updates

- Blueprint / original idea: [LinkedIn Post 1](https://www.linkedin.com/posts/moses-chaitanya-981520282_python-streamlit-machinelearning-share-7459466381735153664-GVS5)
- Working dashboard screenshot: [LinkedIn Post 2](https://www.linkedin.com/posts/moses-chaitanya-981520282_python-streamlit-machinelearning-share-7459468881699672064-OPDH)
- Working demo video: [LinkedIn Post 3](https://www.linkedin.com/posts/moses-chaitanya-981520282_python-streamlit-machinelearning-ugcPost-7459471355265093632-sH8s)

## Future Scope

- Connect the dashboard with real hardware sensors
- Use Arduino or ESP32 for live power readings
- Store power history in a database
- Add appliance-wise monthly reports
- Send overload alerts through SMS or email
- Add user login and cloud dashboard support

## Conclusion

IntelliWatt AI provides a simple and intelligent way to monitor electricity usage. It helps users understand power consumption, estimate cost, detect overloads, and predict future usage. The project can be extended into a real IoT-based smart energy monitoring system using hardware sensors.
