from typing import List, Tuple
import os
import face_recognition


def get_face_encodings_from_folder(folder_path: str) -> Tuple[List, List]:
    face_encodings = []
    nume_knownFaces = []
    for file_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, file_name)
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        if len(face_locations) == 0:
            print("No face detected in image:", file_name)
            continue
        encoding = face_recognition.face_encodings(image)[0]
        face_encodings.append(encoding)
        nume_knownFaces.append(file_name.split(".")[0])
    return face_encodings, nume_knownFaces
