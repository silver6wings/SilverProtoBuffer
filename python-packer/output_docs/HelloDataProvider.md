## This is a hello demo get

**GET /hello/{ID}/get?foo={foo}**




+ Response

```protobuf
message HelloResponse
{
    optional int64 ID = 1;
    optional string content = 2;
}
```


## This is a hello demo post

**POST /hello/post**



+ Request

```protobuf
message HelloRequest
{
    optional int64 ID = 1;
    optional string foo = 2;
    optional string bar = 3;
}
```


+ Response

```protobuf
message HelloResponse
{
    optional int64 ID = 1;
    optional string content = 2;
}
```


