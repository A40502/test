# -*- coding: utf-8 -*-
"""test.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M4cKmOhP2Ht2DYv9UdgIrwAcBfzrRM9R
"""

import os
import requests
import zipfile
import pandas as pd

def download_file_from_google_drive(url, file_name, data_dir):
  # Tạo thư mục dữ liệu nếu chưa có
  if not os.path.exists(data_dir):
    os.makedirs(data_dir)

  # Lấy ID file từ URL
  file_id = url.split('=')[1]

  # Tạo URL tải file
  download_url = f'https://drive.google.com/uc?export=download&id={file_id}'

  # Gửi yêu cầu tải file
  response = requests.get(download_url, stream=True)

  # Kiểm tra trạng thái yêu cầu
  if response.status_code == 200:
    # Lưu file
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, 'wb') as f:
      for chunk in response.iter_content(chunk_size=1024):
        if chunk:
          f.write(chunk)

    print(f'File {file_name} đã được tải xuống thành công!')
    return file_path
  else:
    print(f'Lỗi tải file: {response.status_code}')
    return None

url = 'https://drive.google.com/uc?id=1yyL20BNKv3PxJRJVjJ_2Q-HidvIUis45&export=download'
file_name = 'data.zip'
data_dir = './data'

file_path = download_file_from_google_drive(url, file_name, data_dir)

if file_path:
  print(f'Đường dẫn file: {file_path}')

#giải nén file zip
with zipfile.ZipFile('/content/data/data.zip', 'r') as zip_ref:
    zip_ref.extractall('./data')

customer_data=pd.read_csv("/content/data/customers-100.csv")
customer_data.head(10)

#lấy số dòng số cột của file dữ liêu
customer_data.shape

#trích xuất các cột cụ thể trong file dữ liệu
result_data=customer_data[['Index','Customer Id','First Name','Last Name','Phone 1']]
result_data.to_csv("./data/result_data")