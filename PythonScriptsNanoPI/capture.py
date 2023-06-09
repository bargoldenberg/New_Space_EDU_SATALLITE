import cv2





def capture_image(num):

	cap = cv2.VideoCapture(0)
	if not cap.isOpened():
		print("error")
		exit()

	files = []

	for i in range(num):
		ret, frame = cap.read()
		if not ret:
			print("error")
			break
		image_name = "captured_image"+str(i)+".jpg"
		cv2.imwrite(image_name, frame)
		print("success")
		files.append(image_name)
	cap.release()

	return files



if __name__ == '__main__':
	files = capture_image(1)
	print(files)
