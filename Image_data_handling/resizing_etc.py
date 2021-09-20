""" 이미지 데이터 처리 - 2. Resizing """
from PIL import Image
import cv2

# PIL
# for문으로 모든 개별 파일에 접근
for f in files:
    img = Image.open(train_path + d + '/' + f, 'r')
    
		# 이미지를 128, 128로 일괄 리사이즈 한다.
    resize_img = img.resize((128, 128))


# OpenCV
img_astro3_gray_resized = cv2.resize(img_astro3_gray, dsize=(50, 50))


""" 이미지 데이터 처리 - 3. Read & Write & Copy """

# PIL
# open을 활용한 이미지 파일 열기
img_logo_png = Image.open("./logo.png")
img_logo_png.size

>> (601, 203)

# save를 활용한 이미지 저장
img_logo_png.save("./logo.bmp")

# 이미지 데이터 처리를 위해 Image클래스 => Numpy 배열로 변환
img_logo_array = np.array(img_logo_bmp)

# Numpy 배열 => Image클래스 변환
Image.fromarray(img_logo_array)

# Crop: 이미지를 잘라 특정 부분만 추출
# crop(좌, 상, 우, 하)
img_logo_cropped = img_logo_png.crop((10, 10, 200, 200))


# OpenCV
# imread: 이미지 읽기
img_astro3 = cv2.imread("./astronaut.png")

# 각 채널을 분리(OpenCV로 불러온 이미지는 BGR 순서라는 점에 유의!)
b, g, r = cv2.split(img_astro3)

# b, r을 서로 바꿔서 Merge
img_astro3_rgb = cv2.merge([r, g, b])

# imwrite: 이미지 파일 쓰기
cv2.imwrite("./gray_astronaut.png", img_astro3_gray)

# 이미지 자르기, 남기고 싶은 특정 부분을 행과 열 선택으로 자르기
image_cropped = image[:,:128]