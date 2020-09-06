import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

#Training various images
image1 = face_recognition.load_image_file("Training Folder/Ben.jpg")
face_encoding_1 = face_recognition.face_encodings(image1)[0]

image2 = face_recognition.load_image_file("Training Folder/Ben1.jpeg")
face_encoding_2 = face_recognition.face_encodings(image2)[0]

image3 = face_recognition.load_image_file("Training Folder/ElonMusk.png")
face_encoding_3 = face_recognition.face_encodings(image3)[0]

image4 = face_recognition.load_image_file("Training Folder/Obama.jpg")
face_encoding_4 = face_recognition.face_encodings(image4)[0]

image6 = face_recognition.load_image_file("Training Folder/Jaspreet.jpeg")
face_encoding_6 = face_recognition.face_encodings(image6)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
	face_encoding_1,
	face_encoding_2,
	face_encoding_3,
	face_encoding_4,
	face_encoding_6
]
known_face_names = [
	"Ben Affleck",
	"Cool Ben",
	"Elon",
	"Barack Obama",
	"Me"
]

# Initialize these variables to pre allot space
face_encodings, face_locations, face_names, process_this_frame = [], [], [], True

# Run loop to capture and give output
while True:
	
	ret, frame = video_capture.read()
	small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) #Resizing captured frame
	rgb_small_frame = small_frame[:, :, ::-1] #BGR -> RGB

	if process_this_frame: # Processing only half the frames for speed
		face_locations = face_recognition.face_locations(rgb_small_frame)
		face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
		face_names = []
		for face_encoding in face_encodings:
			matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
			name = "Unknown"
			face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
			best_match_index = np.argmin(face_distances)
			if matches[best_match_index]:
				name = known_face_names[best_match_index]
			face_names.append(name)

	process_this_frame = not process_this_frame


	for (top, right, bottom, left), name in zip(face_locations, face_names): #Rescale
		top *= 4
		right *= 4
		bottom *= 4
		left *= 4
		
		#Style the Box
		cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
		cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

	cv2.imshow('Video', frame) #Display output box in video

	if cv2.waitKey(1) & 0xFF == ord('q'): # Quit if Q/q is pressed
		break

video_capture.release()
cv2.destroyAllWindows()