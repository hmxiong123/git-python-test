import cv2
# 测试打印版本号，确认cv2正常加载
print(cv2.__version__)
import numpy as np
import easyocr

# 创建阅读器，中文+数字识别
reader = easyocr.Reader(['ch_sim','en'])

img_path = "car.jpg"
img = cv2.imread(img_path)

# 识别图片
result = reader.readtext(img_path)

print("===识别车牌结果===")
for box, text, score in result:
    print(f"车牌文字：{text}，置信度：{score:.2f}")
    # 画框
    pts = np.array([[int(p[0]), int(p[1])] for p in box])
    cv2.polylines(img, [pts], True, (0,255,0), 2)
    cv2.putText(img, text, pts[0], cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()