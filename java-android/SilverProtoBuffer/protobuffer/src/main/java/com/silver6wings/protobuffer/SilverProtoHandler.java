package com.silver6wings.protobuffer;

import com.google.protobuf.GeneratedMessage;

public interface SilverProtoHandler<T extends GeneratedMessage>
{
    void onResponse(T response, int responseCode, int httpCode, Throwable throwable);
}
