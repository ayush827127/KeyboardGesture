import cv2
import mediapipe
import pyautogui

capture_hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
x1 = y1 = x2 = y2 = x3 = y3 = x4 = y4 = x5 = y5 = 0

while True:
    _,image = camera.read()
    image_height, image_width, _ = image.shape
    image = cv2.flip(image,1)
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image,hand)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * image_width)
                y =  int(lm.y * image_height)

                if id == 8:
                    mouse_x = int(screen_width / image_width *x )
                    mouse_y = int(screen_height / image_height *y )
                    cv2.circle(image,(x,y),10,(0,255,255))
                    # pyautogui.moveTo(mouse_x,mouse_y)
                    x1 = x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y
                    cv2.circle(image,(x,y),10,(0,255,255))
                if id == 12:
                    x3 = x
                    y3 = y
                    cv2.circle(image,(x,y),10,(0,255,255))
                if id == 16:
                    x4 = x
                    y4 = y
                    cv2.circle(image,(x,y),10,(0,255,255))
                if id == 20:
                    x5 = x
                    y5 = y
                    cv2.circle(image,(x,y),10,(0,255,255))
        Upkey = y2 - y1
        print(Upkey)
        if(Upkey<40):
            pyautogui.keyDown('up')
        else:
            pyautogui.keyUp('up')
        DownKey = y2 -  y3
        if(DownKey<40):
            pyautogui.keyDown('down')
        else:
            pyautogui.keyUp('down')
        RihgtKey = y2 -  y4
        if(RihgtKey<40):
            pyautogui.keyDown('right')
        else:
            pyautogui.keyUp('right')
        LeftKey = y2 -  y5
        if(LeftKey<40):
            pyautogui.keyDown('left')
        else:
            pyautogui.keyUp('left')
        
    cv2.imshow("hand movement video capture", image)
    key = cv2.waitKey(100)
    if key == 27:
        break
camera.release()
cv2.destroyAllWindows()


