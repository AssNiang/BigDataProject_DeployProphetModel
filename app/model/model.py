import pickle
from datetime import datetime, timedelta
from pandas import DataFrame, to_datetime
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/model-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


def predict_next_3_hours_temp():
    current_time = datetime.now().replace(microsecond=0,second=0,minute=0)
    timestamps_list = []

    for i in range(3):
        timestamp = current_time + timedelta(hours=i+1)
        timestamps_list.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))

    future = DataFrame(timestamps_list)
    future.columns = ['ds']
    future['ds']= to_datetime(future['ds'])
    forecast = model.predict(future)
    forecast = forecast[['ds', 'yhat']].rename(columns={'ds': 'datetime', 'yhat': 'predicted_temp'})
    forecast["datetime"] = forecast["datetime"].dt.strftime("%Y-%m-%d %H:%M:%S")
    json_result = forecast[['datetime', 'predicted_temp']].to_json(orient='records')
    return json_result
