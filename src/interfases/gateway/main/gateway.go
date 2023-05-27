package main

import (
  "context"
  "flag"
  "net/http"
  "fmt"

  "github.com/golang/glog"
  "github.com/grpc-ecosystem/grpc-gateway/runtime"
  "google.golang.org/grpc"
  "google.golang.org/grpc/credentials/insecure"

  gw "gateway/grpc"  
)

var (
  grpcServerEndpoint = flag.String("grpc-server-endpoint",  "[::]:50056", "gRPC server endpoint")
)


func run() error {
  ctx := context.Background()
  ctx, cancel := context.WithCancel(ctx)
  defer cancel()


  mux := runtime.NewServeMux()
  opts := []grpc.DialOption{grpc.WithTransportCredentials(insecure.NewCredentials())}
  err := gw.RegisterCoordinateServiceHandlerFromEndpoint(ctx, mux,  *grpcServerEndpoint, opts)
  if err != nil {
    return err
  }

  fmt.Print("Starting http server on port 8083")
  return http.ListenAndServe(":8083", mux)
}

func main() {
  flag.Parse()
  defer glog.Flush()

  if err := run(); err != nil {
    glog.Fatal(err)
  }
}