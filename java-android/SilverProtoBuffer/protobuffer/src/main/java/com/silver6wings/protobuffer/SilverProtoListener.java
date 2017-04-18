package com.silver6wings.protobuffer;

public interface SilverProtoListener
{
    void onRequest(String url, String tag);

    void onResponse(String url, String tag, byte[] bytes, int responseCode);
}
