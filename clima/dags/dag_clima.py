from datetime import timedelta, datetime, timezone
from tempfile import NamedTemporaryFile
import pandas as pd
import requests
import csv
import pendulum

from airflow.decorators import dag, task
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook

default_args = {
    'owner':'val',
    'retries': 2,
    'retry_delay':timedelta(minutes=2)
}

@dag(
    dag_id='dag_clima_v01',
    default_args=default_args,
    description='dag dados clima usando taskflow API',
    start_date=pendulum.datetime(2024,6,25,tz="UTC"),
    schedule_interval='0 6 * * *'
)


def clima_etl():
    def save_temp_file(df):
        """
        Save DataFrame data to a temporary CSV file.

        Parameters
        ----------
        df : DataFrame
            The df DataFrame object to be saved.

        Returns
        -------
        temp_file_path : str
            The csv file path.
        """
        with NamedTemporaryFile(mode='w',suffix="tempfile", delete=False) as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(df.columns)
            csv_writer.writerows(df.values)
            temp_file_path = f.name
        print(f"Arquivo CSV temporário salvo em {temp_file_path}")
        return temp_file_path
    
    @task()
    def get_data():
        """
        Retrieve data from the weather API.

        Returns
        -------
        data : dict
            The data retrieved from the API.
        """
        conn = HttpHook.get_connection('openweather')
        apikey = conn.extra_dejson.get('apikey')
        url = f'{conn.host}?q=Brasília&units=metric&appid={apikey}'
        response = requests.get(url)
        data = response.json()
        return data

    @task()
    def transform_data(data):
        """
        Transform API data and save it to a temporary CSV file.

        Parameters
        ----------
        data : dict
            The data to be transformed.

        Returns
        -------
        path : str
            The temporary CSV file path.
        """
        df_data = {
            'lon': [data['coord']['lon']],
            'lat': [data['coord']['lat']],
            'weather_description': [data['weather'][0]['description']],
            'temp': [data['main']['temp']],
            'feels_like': [data['main']['feels_like']],
            'temp_min': [data['main']['temp_min']],
            'temp_max': [data['main']['temp_max']],
            'pressure': [data['main']['pressure']],
            'humidity': [data['main']['humidity']],
            'wind_speed': [data['wind']['speed']],
            'wind_deg': [data['wind']['deg']],
            'clouds_all': [data['clouds']['all']],
            'dt': [datetime.fromtimestamp(data['dt'],tz=timezone(timedelta(hours=int(data['timezone'])/3600)))],
            'sys_country': [data['sys']['country']],
            'sunrise': [datetime.fromtimestamp(data['sys']['sunrise'],tz=timezone(timedelta(hours=int(data['timezone'])/3600)))],
            'sunset': [datetime.fromtimestamp(data['sys']['sunset'],tz=timezone(timedelta(hours=int(data['timezone'])/3600)))],
            'timezone': [int(data['timezone'])/3600],
            'city_name': [data['name']],
        }

        df = pd.DataFrame(df_data)
        path = save_temp_file(df)
        return path

    @task()
    def load_data(path):
        """
        Load data from a CSV file into the database.

        Parameters
        ----------
        path : str
            The CSV file path.

        """
        with open(path, 'r') as f:
            data = pd.read_csv(f)

        sql_query = """
        INSERT INTO weather (longitude, latitude, weather_description, temperature, feels_like, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, dt_collected, sys_country, dt_sunrise, dt_sunset, timezone, city_name)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        records = data.to_records(index=False).tolist()[0]

        pg_hook = PostgresHook(postgres_conn_id='postgres_localhost')
        pg_hook.run(sql_query,parameters=records)

    dados = get_data()
    df = transform_data(dados)
    load_data(df)

clima_dag = clima_etl()