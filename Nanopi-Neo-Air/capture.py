import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
	print("error")
	exit()
for i in range(3):
	ret, frame = cap.read()
	if not ret:
		print("error")
		break
	image_name = "captured_image"+str(i)+".jpg"
	cv2.imwrite(image_name, frame)
	print("success")
cap.release()
