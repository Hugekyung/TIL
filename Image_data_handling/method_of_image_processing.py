""" 이미지 처리를 위한 패키지 """

""" 1. PIL(pillow)

- JPEG, BPM, GIF, PNG, PPM, TIFF 등 다양한 포맷 지원
- BGR 형식으로 이미지를 가져옴
- torchvision 지원이 잘 됨
- numpy array와의 호환성이 안좋음
  (numpy array => image array 변환이 필요함)
"""

""" 2. OpenCV

- 이미지 처리, 컴퓨터 비전을 위한 라이브러리
- Window, Linux, Max OS, iOS, Android 등 다양한 플랫폼 지원
- 실시간 이미지 프로세싱에 중점을 둔 라이브러리(영상처리 알고리즘)

- RGB 형식으로 이미지를 가져옴
- torchvision과의 호환성이 안좋음
- PIL에 있는 거의 모든 기능이 OpenCV에 존재(PIL에 없는 기능 지원)
- numpy array와의 호환성이 좋음
- numpy array 인덱싱을 이용한 이미지 전처리 가능(자유로운 전처리)
- video capture 관련 기능이 잘 구성됨
"""