#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 
import numpy as np 
import ctypes
from ctypes.util import find_library
from std_msgs.msg import Int32MultiArray



rclpy.init()
##Nodo de ros 
nh = Node("coordinate_publisher_initiated")
##Publisher de ros 
publisher = nh.create_publisher(Int32MultiArray, '/coordinates',10)

def timer_callback(array):

  """Funcion deonde se publica al topico /coordinates la cordenada del centro del rectangulo usando el publisher de ros
"""
  
  msg = Int32MultiArray()
  msg.data = array
  print(msg.data)
  publisher.publish(msg)
  print(array)


def main():

  """En el archivo main de image.py se obtiene el centro de un rectangulo azul, se llama la funcion multiplicarpor100 de la 
  libreria multiplicador y se llama la funcion timer callback (a esta funcion se pasan como parametros el componente x y y de la cordenada de centro del rectangulo ) 

  """

  nh.create_timer(0.5, timer_callback)
  cap = cv2.VideoCapture(0)
  font = cv2.FONT_HERSHEY_COMPLEX 
  library = ctypes.cdll.LoadLibrary(find_library("multiplicador"))
  
  while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    """
    l_h = cv2.getTrackbarPos("L-H", "trackbar")
    l_s = cv2.getTrackbarPos("L-S", "trackbar")
    l_v = cv2.getTrackbarPos("L-V", "trackbar")
    u_h = cv2.getTrackbarPos("U-H", "trackbar")
    u_s = cv2.getTrackbarPos("U-S", "trackbar")
    u_v = cv2.getTrackbarPos("U-V", "trackbar")
    """

    low_blue = np.array([86, 191, 118])
    high_blue = np.array([133, 255, 255])
    mask = cv2.inRange(hsv, low_blue, high_blue)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
      aprox = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt,True),True)
      area = cv2.contourArea(cnt)

      if area> 400:
        cv2.drawContours(frame,[cnt],0,(0,0,0),5)

        if len(aprox) == 4:
            M = cv2.moments(cnt)
            if M['m00'] != 0:
              cx = int(M['m10']/M['m00'])
              cy = int(M['m01']/M['m00'])
              cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
              cv2.circle(frame, (cx, cy), 7, (0, 0, 255), -1)
              cv2.putText(frame, "center", (cx - 20, cy - 20),
              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
              result_x = library.multiplicar_por_100(cx)
              result_y = library.multiplicar_por_100(cy)
              coor_array = [result_x,result_y]
              timer_callback(coor_array)
              

              #print(result)


    cv2.imshow("mask", mask)
    cv2.imshow("video",frame)

    if (cv2.waitKey(30) == 27):
       break
    
  cap.release()
  cv2.destroyAllWindows()
  rclpy.spin(nh)
  nh.destroy_node()
  rclpy.shutdown()

  
if __name__ == '__main__':
  main()