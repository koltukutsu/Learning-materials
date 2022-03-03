import numpy as np
import cv2
import pandas as pd

##################################33
label = pd.read_csv("labels.csv", encoding="ISO-8859-1")
frameWidth = 640
frameHeight = 480
brightness = 180
threshold = 0.75
font = cv2.FONT_HERSHEY_SIMPLEX
# Setup the video camera

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, brightness)

# import the trannined model
import keras

model = keras.models.load_model("MY_h5_model_5.h5")


def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def equalize(img):
    img = cv2.equalizeHist(img)
    return img


def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    return img


def getCalssName(classNo):
    labels = pd.read_csv("labels.csv", encoding="ISO-8859-1")
    a = labels[labels["Classid"] == classNo]["Name"]
    return a


cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow("frame", frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
while True:

    # READ IMAGE
    success, imgOrignal = cap.read()

    # PROCESS IMAGE
    img = np.asarray(imgOrignal)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)

    cv2.imshow("showed", img)
    img = img.reshape(1, 32, 32, 1)

    cv2.putText(
        imgOrignal, "CLASS: ", (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA
    )
    cv2.putText(
        imgOrignal, "PROBABILITY: ", (20, 75), font, 0.75, (255, 0, 0), 2, cv2.LINE_AA
    )

    # PREDICT IMAGE
    predictions = model.predict(img)
    probabilityValue = np.amax(predictions)
    classIndex = np.where(predictions == probabilityValue)[1][0]

    if probabilityValue > threshold:
        # print(getCalssName(classIndex))
        cv2.putText(
            imgOrignal,
            str(classIndex) + " " + str(getCalssName(classIndex)),
            (120, 35),
            font,
            0.75,
            (0, 0, 255),
            2,
            cv2.LINE_AA,
        )
        cv2.putText(
            imgOrignal,
            str(round(probabilityValue * 100, 2)) + "%",
            (180, 75),
            font,
            0.75,
            (255, 0, 0),
            2,
            cv2.LINE_AA,
        )
    cv2.imshow("deneme", imgOrignal)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
