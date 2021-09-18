""" 이미지 데이터 처리 - 1. Normalizatoin """

"""
RGB 채널은 Red, Green, Blue 채널로 나뉘는데 , 각각의 채널은 0~255 사이의 좌표값을 갖는다. 
따라서 효과적인 데이터 활용을 위해 RGB채널값을 255로 나눠주는 정규화 작업을 수행한다.

각 채널 값이 0~255 사이의 숫자이므로 정규화를 진행하면 0~1사이의 값으로 숫자가 작아지는 효과가 있다. 
이를 통해 데이터별 숫자 크기에 따른 문제 발생을 방지하고 모든 데이터가 균일한 중요도로 모델에 투입되도록 할 수 있다.
"""
import numpy as np

r, g, b = resize_img.split()

# 각 쪼갠 이미지를 255로 나눠서 0~1 사이의 값이 나오도록 정규화 한다.
r_resize_img = np.asarray(np.float32(r) / 255.0)
b_resize_img = np.asarray(np.float32(g) / 255.0)
g_resize_img = np.asarray(np.float32(b) / 255.0)


""" (참고)np.array() VS np.asarray()  
np.array는 ndarray(배열)을 만드는 클래스이고, 
np.asarray는 배열의 데이터타입이 설정된 경우 데이터타입이 기존과 다른 경우에만 복사하는 클래스다.
"""