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

    def getCoordinate(self, request, context):
        global res_x, res_y
        print("sending data")
        return getValue_pb2.coordinate(x = res_x, y= res_y)

res_x = 0
res_y = 0 

def serve():

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
    
    global res_x, res_y
    res_x =  msg.data[0]
    res_y = msg.data[1]
    print(res_x,res_y)

if __name__ == '__main__':
    serve()