import face_recognition
from listaFaces.getFaces import get_face_encodings_from_folder


def recunoastere():
    matches = []
    knownFaces, name_knownFaces = get_face_encodings_from_folder(
        r"D:\NASA\CAM_p\Cam_p\src\known_faces")
    unknown_image = face_recognition.load_image_file(r"D:\NASA\CAM_p\win.png")
    unknown_face_encodings = face_recognition.face_encodings(unknown_image)
    for face_encoding in unknown_face_encodings:
        matches = face_recognition.compare_faces(knownFaces, face_encoding)
        name = "Necunoscut"
    if True in matches and len(matches) > 0:
        first_match_index = matches.index(True)
        name = name_knownFaces[first_match_index]
        print("Am detectat pe cineva în această imagine: {}".format(name))
        return True
    else:
        print("Persoana necunoscuta detectata")
        return False
