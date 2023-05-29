using System;
using Grpc.AspNetCore;
using Grpc.Core;
using GetCoordinate;

namespace Client
{
    class Program
    {
        static void Main(string[] args)
        {
            
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

