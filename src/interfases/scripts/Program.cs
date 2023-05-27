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
            
            Channel channel = new Channel("localhost:50055", ChannelCredentials.Insecure);
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




 protoc api/v1/*.proto \
            --go_out=. \
            --go_opt=paths=source_relative \
            --go-grpc_out=. \
            --go-grpc_opt=paths=source_relative \
+            --grpc-gateway_out . \
+            --grpc-gateway_opt logtostderr=true \
+            --grpc-gateway_opt paths=source_relative \
+            --grpc-gateway_opt generate_unbound_methods=true \