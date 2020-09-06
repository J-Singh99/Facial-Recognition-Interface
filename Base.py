import face_recognition
import cv2
import numpy as np
from csv import writer
from csv import DictWriter
import PrebuiltBill


db, bill = 0, 0

print("If you want to use a prebuilt model, type in 'Y'.")
print("The model is trained on Obama, Elon Musk, Scarlet Johansen, and The Creator!")
a = input()
if a == 'Y':
	import PrebuiltDB
	db = PrebuiltDB.DB
	print('Importing data from pre-built model...')
else:
	import DataStore
	db = DataStore.DB

n = len(db)



# Preparing CSV file for people spotted on the camera
field_names = ['ID', 'Name', 'Age', 'Gender', 'Number', 'Balance', 'FileName']
file_name = 'PeoplesList.csv'

with open(file_name, 'a+', newline='') as write_obj:
	csv_writer = writer(write_obj)
	csv_writer.writerow(field_names)




# What to do if a face is spotted
checklist = [False]*n
BigCheck = True
def ExtractInfo(mathes):
	if not False in checklist: BigCheck = False
		
	if not True in matches: 
		pass #print('Unknown')
	else:
		for i in range(n):
			if (checklist[i] == False) and (matches[i] == True):
			   checklist[i] = True



# Preparing the data to be manipulated
known_face_encodings = []
known_face_names =[]

for j in db:
	i = str(db[j]['ID'])
	known_face_names.append(db[j]['Name'])
	ImCode = 'image' + i + ' = face_recognition.load_image_file("' + db[j]['FileName'] + '")'
	exec(ImCode)
	EnCode = 'face_encoding_' + i + '= face_recognition.face_encodings(image' + i + ')[0]'
	exec(EnCode)
	ApCode = 'known_face_encodings.append(face_encoding_' + i + ')'
	exec(ApCode)



# Initialize these variables to pre-allot space
face_encodings, face_locations, face_names, process_this_frame = [], [], [], True

# Run loop to capture and give output
video_capture = cv2.VideoCapture(0)
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
			if BigCheck: ExtractInfo(matches)
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


#Build the billing system
print("If you want to use a automatic billing mechanism, type in 'Y'.")
b = input()
if b == 'Y':
	bill = PrebuiltBill.BILL
	print('Importing bill...')
	print()
	print()
else:
	import BillMaker
	bill = BillMaker.Billing(checklist, known_face_names, db)

def HandleFace(name):
	for j in db:
		if name == db[j]['Name']:
		
			with open(file_name, 'a+', newline='') as write_obj:
				dict_writer = DictWriter(write_obj, fieldnames=field_names)
				dict_writer.writerow(db[j])
				
				ID = db[j]['ID']
				print('Calculating bill for ' + db[j]['Name'])
				if b == 'Y':
					PrebuiltBill.DoCalc(ID, bill)
				else:
					BillMaker.DoCalc(ID, bill)
				print()
				print()
				
def FinalBilling(checklist):
	for i in range(n):
		if checklist[i] == True:
			HandleFace(known_face_names[i])

# Printing the Bill
FinalBilling(checklist)

print('You can check out who came into the store using the "PeoplesList" file generated.')
print('It gives all the information stored about the person.')