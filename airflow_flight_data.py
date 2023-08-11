from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from FlightService import FlightService
from WeatherService import WeatherService


def read_flights(ds: str):
    flight_service = FlightService()
    return flight_service.read_open_sky_api()


def write_flights(flights):
    flight_service = FlightService()
    flight_service.writing(flights)


def read_weather(ds: str):
    weather_service = WeatherService()
    return weather_service.read_weather("2023-07-06", "2023-07-12", "temperature_2m,relativehumidity_2m,windspeed_10m")


def write_weather(weather_data):
    weather_service = WeatherService()
    weather_service.write_weather(weather_data)


def write_flights_to_sqlite(flights):
    flight_service = FlightService()
    flight_service.write_to_sqlite(flights)


default_args = {
    'owner': 'Your Name',
    'start_date': datetime(2022, 12, 1),
    'catchup': False
}

with DAG('open_sky_dag', default_args=default_args, schedule='0 1 * * *') as dag:
    read_flights_task = PythonOperator(
        task_id='read_flights',
        python_callable=read_flights,
        op_kwargs={'ds': '{{ ds }}'}
    )

    write_flights_task = PythonOperator(
        task_id='write_flights',
        python_callable=write_flights,
        op_args=[read_flights_task.output],
    )

    write_flights_to_sqlite_task = PythonOperator(
        task_id='write_flights_to_sqlite',
        python_callable=write_flights_to_sqlite,
        op_args=[read_flights_task.output],
    )

    read_weather_task = PythonOperator(
        task_id='read_weather',
        python_callable=read_weather,
        op_kwargs={'ds': '{{ ds }}'}
    )

    write_weather_task = PythonOperator(
        task_id='write_weather',
        python_callable=write_weather,
        op_args=[read_weather_task.output],
    )

    read_flights_task >> write_flights_task
    read_flights_task >> write_flights_to_sqlite_task
    read_weather_task >> write_weather_task
