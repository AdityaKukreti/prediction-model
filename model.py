from prophet import Prophet
import pandas as pd

class Model:

    def __inti__(self):
        pass
        
    def predictor(self,user_month,user_year,wool_type):
        
        data = pd.read_csv('10years data - Sheet1.csv')
        df = data[["Date", wool_type]]
        df.columns=['ds','y']

        m = Prophet()
        m.fit(df)
        future = m.make_future_dataframe(periods=120, freq='M')

        df['ds'] = pd.to_datetime(df['ds'])
        forecast = m.predict(future)
        forecast= forecast[['ds','yhat']]

        filtered_data = forecast[(forecast['ds'].dt.year == user_year) & (forecast['ds'].dt.month == user_month)]
        user_yhat_values = filtered_data['yhat'].values

        return {"month":user_month,"year":user_year,"type":wool_type,"prediction":user_yhat_values[0]}

