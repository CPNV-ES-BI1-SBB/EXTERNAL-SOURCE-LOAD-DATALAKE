````mermaid
classDiagram
    class ICloudService {
        <<Interface>>
        - connectionString : string
        - destinationName : string
        
        + connect(connectionString : string, destinationName : string) void
        + disconect() void
        + create(destination : string, source : string) void
    }
    
    ICloudService <|-- AwsService
    class AwsService {
        - connectionString : string
        - destinationName : string

        + AwsService(connectionString : string, destinationName : string)
        + connect(connectionString : string, destinationName : string) void 
        + disconect() void
        + create(destination : string, source : string) void        
    }
    
    
    ICloudService <-- Server 
    class Server {
        - host : string
        - port : int 
        - app : FastApi
        - service : ICloudService

        Server(host : string, port : int)
        + start() void
    }
    
    PermissionDeniedException <-- ICloudService
    class PermissionDeniedException {
        PermissionDeniedException()
        PermissionDeniedException(message : string)
        PermissionDeniedException(message : string, errorCode : int )
    }

    AwsService --() SdkAWS
    
````