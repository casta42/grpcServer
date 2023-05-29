using System;
using Grpc.AspNetCore;
using Grpc.Core;
using GetCoordinate;

namespace Client
{
    /*! La clase program implementa un cliente al servidor grpc (implementado en python)*/
    class Program
    {
        static void Main(string[] args)
        {
                /** Se crea un canal para comunicarnos con el servidor grpc
                *  se tienen que incluir el namespace de los archivos de grpc generatos con protoc (using GetCoordinate)
                */
            Channel channel = new Channel("localhost:50058", ChannelCredentials.Insecure);
            var client = new coordinateService.coordinateServiceClient(channel);
            var request = new global::Google.Protobuf.WellKnownTypes.Empty();
            var reply = client.getCoordinate(request);
            Console.WriteLine("Server replied with coordinate ({0}, {1})", reply.X, reply.Y);
            channel.ShutdownAsync().Wait();
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();

    
        }
    }
}

