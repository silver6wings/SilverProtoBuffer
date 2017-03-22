package com.silver6wings.silverprotobuffer.silverprotobuffer;

public interface SilverProtoListener
{
    void onRequest(String url, String tag);

    void onResponse(String url, String tag, byte[] bytes, int responseCode);
}
