package com.silver6wings.protobuffer;

import com.loopj.android.http.AsyncHttpClient;

public class SilverProtoManager
{
    // avoid using enum in android for better performance

    public static final int RequestMethodNULL       = 0;
    public static final int RequestMethodGET        = 1;
    public static final int RequestMethodPOST       = 2;
    public static final int RequestMethodPUT        = 3;
    public static final int RequestMethodPATCH      = 4;
    public static final int RequestMethodDELETE     = 5;

    public static final int ResponseCodeNull                = 0;
    public static final int ResponseCodeSuccess             = 1;
    public static final int ResponseCodeFailParse           = 2;
    public static final int ResponseCodeNetworkError        = 3;
    public static final int ResponseCodeParameterMissing    = 4;

    static volatile SilverProtoManager instance;
    static String contentType = "application/x-protobuf";
    static String accept = "application/x-protobuf";

    private AsyncHttpClient client;

    public SilverProtoListener delegate; // can be defined

    public static SilverProtoManager getInstance()
    {
        if (null == instance)
        {
            synchronized (SilverProtoManager.class)
            {
                if (null == instance)
                {
                    AsyncHttpClient client = new AsyncHttpClient();
                    client.addHeader("Accept", accept);

                    instance = new SilverProtoManager(client);
                }
            }
        }
        return instance;
    }

    public SilverProtoManager(AsyncHttpClient client)
    {
        this.client = client;
    }

    public AsyncHttpClient getClient()
    {
        return this.client;
    }

    public void setClient(AsyncHttpClient client)
    {
        this.client = client;
    }

    public void setBaseServerURL(String baseServerURL)
    {
        SilverProtoBaseProvider.serverURL = baseServerURL;
    }

}
