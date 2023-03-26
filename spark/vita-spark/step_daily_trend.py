import pandas as pd
import datetime

# csv 파일 읽기
def readCsv(csvName):
    df = pd.read_csv(csvName, header=0, 
                     names=['binning_data', 'update_time', 'create_time', 'source_pkg_name', 'source_type', 'count', 'speed', 'distance', 'calorie', 'deviceuuid', 'pkg_name', 'datauuid', 'day_time', ''], 
                     skiprows=1)
    return df

# 일 데이터 처리
def dayDF(df):
    df.rename(columns = {'count':'daily_wearable_step', 'day_time':'date'}, inplace=True)
    df = df[['daily_wearable_step', 'date']]
    df['date'] = df['date'].apply(lambda d: datetime.date.fromtimestamp((float)(d)/1000.0)).astype(str) # 날짜 형식 변환
    df2 = df.groupby('date', as_index=False).max() # 날짜별 최대값   
    return df2