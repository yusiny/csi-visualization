import argparse
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def data_preprocess(csi_df):

    # Min-Max Normalization
    scaler = MinMaxScaler()
    scaler.fit(csi_df)
    scaled_df = scaler.transform(csi_df)
    csi_df = scaled_df

    return csi_df


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 'True', 'TRUE', 'T', 'Y', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'False', 'FALSE', 'F', 'N', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def complexToAmp(comp_df):

    comp_df = comp_df.astype('complex')
    amp_df = comp_df.apply(np.abs, axis=1)

    return amp_df

'''
    Configuration of Extractor and plot parameters
'''

import pandas as pd
import glob
import datetime
import pytz

def getTime(df):
    # 한국 시간대 설정
    kor_tz = pytz.timezone('Asia/Seoul')

    # 첫 번째 패킷 시간
    first_packet_time = df['time'].iloc[0]
    
    # 마지막 패킷 시간
    last_packet_time = df['time'].iloc[-1]

    # 첫 번째 패킷 시간을 datetime 객체로 변환 및 한국 시간대로 변환
    first_dt_object = datetime.datetime.fromtimestamp(first_packet_time, pytz.utc)
    first_kor_time = first_dt_object.astimezone(kor_tz)
    
    # 마지막 패킷 시간을 datetime 객체로 변환 및 한국 시간대로 변환
    last_dt_object = datetime.datetime.fromtimestamp(last_packet_time, pytz.utc)
    last_kor_time = last_dt_object.astimezone(kor_tz)

    first_kor_time =  first_kor_time.strftime("%Y-%m-%d %H:%M:%S")
    last_kor_time = last_kor_time.strftime("%Y-%m-%d %H:%M:%S")
    
    # 파일 이름과 함께 결과 출력
    print(f"  첫 번째 패킷 시간 (한국 시간대): {first_kor_time}")
    print(f"  마지막 패킷 시간 (한국 시간대): {last_kor_time}")
    print()

    return first_kor_time,last_kor_time

  