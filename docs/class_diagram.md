````mermaid
classDiagram
    class CloudService {
        <<Interface>>        
        + connect() void
        + disconect() void
        + load(destination : string, source : string) void
    }
    
    CloudService <|-- GcpService
    class GcpService {
        - connectionString : string
        - destinationName : string

        + GcpService(connectionString : string, destinationName : string)
        + connect() void 
        + disconect() void
        + load(destination : string, source : string) void        
    }
    
    
    CloudService <-- Server
    class Server {
        - host : string
        - port : int 
        - app : FastApi
        - service : CloudService

        Server(host : string, port : int)
        + start(service : CloudService) void
        + stop() void
        + load(content : any) void
    }
    
    DestinationNotFoundException <-- CloudService
    class DestinationNotFoundException {
        DestinationNotFoundException()
    }
    
    ObjectAlreadyExistException <-- CloudService
    class ObjectAlreadyExistException {
        ObjectAlreadyExistException()
    }
    
    AuthenticationFailedException <-- CloudService
    class AuthenticationFailedException {
        AuthenticationFailedException()
    }

    GcpService --() SdkGcp
    Server --() FastApi
    
````