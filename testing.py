from ultralytics import YOLO
import cv2
import os
model = YOLO("best.pt")


images = os.listdir("C:/Users/VANSH KHANEJA/PROJECTS/OBJECT DETECTION/CUSTOM DATA/RBC COUNT/BCCD_Dataset-master/BCCD/JPEGImages")
for i in images:

    img = cv2.imread("C:/Users/VANSH KHANEJA/Downloads/BCCD_Dataset-master/BCCD_Dataset-master/BCCD/JPEGImages/"+i)

    class_list = ['RBC', 'Platelets', 'WBC']
    results = model(img,stream=True)
    rbc = 0
    wbc = 0


    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            currentClass = class_list[int(box.cls[0])]

            #print(x1,y1,x2,y2)
            if currentClass == 'RBC':
                rbc+=1
                cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),1)
                cv2.putText(img,currentClass, (x1,y1-4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0),1, cv2.LINE_AA, False)

            elif currentClass == 'WBC':
                wbc+=1
                cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),1)
                cv2.putText(img,currentClass, (x1,y1-4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255),1, cv2.LINE_AA, False)

        cv2.putText(img,"RBC: "+str(rbc), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255),2, cv2.LINE_AA, False)
        cv2.putText(img,"WBC: "+str(wbc), (50,90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255),2, cv2.LINE_AA, False)
    cv2.imwrite("C:/Users/VANSH KHANEJA/PROJECTS/OBJECT DETECTION/CUSTOM DATA/RBC COUNT/outputs/"+i,img)


