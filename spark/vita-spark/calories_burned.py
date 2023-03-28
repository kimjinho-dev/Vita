import pandas as pd
import datetime

# csv 파일 읽기
def readCsv(csvName):
    df = pd.read_csv(csvName, header=0, 
                     names=['active_calories_goal', 'version', 'extra_data', 'com.samsung.shealth.calories_burned.tef_calorie', 'com.samsung.shealth.calories_burned.active_time', 'com.samsung.shealth.calories_burned.rest_calorie', 'com.samsung.shealth.calories_burned.update_time', 'com.samsung.shealth.calories_burned.create_time', 'com.samsung.shealth.calories_burned.active_calorie', 'com.samsung.shealth.calories_burned.deviceuuid', 'com.samsung.shealth.calories_burned.pkg_name', 'com.samsung.shealth.calories_burned.datauuid', 'com.samsung.shealth.calories_burned.day_time', ''], 
                     skiprows=1)
    return df

# 일 데이터 처리
def dayDF(df):
    df.rename(columns={'com.samsung.shealth.calories_burned.day_time':'date', 'com.samsung.shealth.calories_burned.active_calorie':'daily_wearable_energy'}, inplace=True)
    df = df[['daily_wearable_energy', 'date']]
    df['date'] = df['date'].apply(lambda d: datetime.date.fromtimestamp((float)(d)/1000.0)).astype(str) # 날짜 형식 변환
    df = df.groupby('date', as_index=False).mean().round(0) # 날짜별 평균
    return df