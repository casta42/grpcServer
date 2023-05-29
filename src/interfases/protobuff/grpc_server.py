#!/usr/bin/env python3
import grpc
from concurrent import futures
import time
import sys 
sys.path.insert(0,'/home/carbon/Documents/interfases_hw1/src/interfases/protobuff')
import getValue_pb2 
import getValue_pb2_grpc
import rclpy
from rclpy.node import Node 
from std_msgs.msg import Int32MultiArray


class CoordinateService(getValue_pb2_grpc.coordinateServiceServicer):

    """
    Esta clase implementa el servidor grpc, es clase hija que hereda de coordinateServiceServicer generada por grpc
    """

    def getCoordinate(self, request, context):
        """
        Esta funcion regresa la coordenada del centro del rectanglo cuando se hace una peticion al servidor
        """
        global res_x, res_y
        print("sending data")
        return getValue_pb2.coordinate(x = res_x, y= res_y)

##variable global donde se guarda el valor x de la coordenada
res_x = 0
##variable global donde se guarda el valor 7 de la coordenada
res_y = 0 

def serve():
    """
       Esta funcion inicializa un subscriber de ros para obtener los valores de las cordenadas y crea un servidor usando la clase correspondiente generada por grpc definida en el servicio protobuf
    """
    rclpy.init()

    node = Node("node_started")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    node.create_subscription(Int32MultiArray,'/coordinates',callback,10)

    while not res_x or not res_y:
        rclpy.spin_once(node)

    getValue_pb2_grpc.add_coordinateServiceServicer_to_server(CoordinateService(), server)

    server.add_insecure_port('[::]:50058')


    print("Server started. Listening on port 50058 :3")

    server.start()

    rclpy.spin(node)

    rclpy.shutdown()

    server.wait_for_termination()


def callback(msg):
    """
    Funcion del subscriber de ros que recibe los valores de la coordenada
    """
    global res_x, res_y
    res_x =  msg.data[0]
    res_y = msg.data[1]
    print(res_x,res_y)

if __name__ == '__main__':
    serve()