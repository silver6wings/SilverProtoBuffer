package com.silver6wings.protobuffer;

import android.content.Context;
import android.util.Log;

import com.google.protobuf.GeneratedMessage;
import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import cz.msebera.android.httpclient.Header;
import cz.msebera.android.httpclient.entity.ByteArrayEntity;

public class SilverProtoRequester
{
    static String contentType = SilverProtoManager.contentType;

    public static <T extends GeneratedMessage> void request(AsyncHttpClient client,
                                                            Context context,
                                                            int requestMethod,
                                                            final String tag,
                                                            final String url,
                                                            GeneratedMessage.Builder requestBuilder,
                                                            final Class<T> responseType,
                                                            final SilverProtoHandler handler)
    {
        if (null == handler)
        {
            return;
        }

        if (null == client || null == context || null == url)
        {
            handler.onResponse(null, SilverProtoManager.ResponseCodeParameterMissing, -1, null);
            return;
        }

        final SilverProtoListener delegate = SilverProtoManager.getInstance().delegate;

        ByteArrayEntity entity = null;
        if (null != requestBuilder)
        {
            entity = new ByteArrayEntity(requestBuilder.build().toByteArray());
        }

        AsyncHttpResponseHandler httpHandler = new AsyncHttpResponseHandler()
        {
            @Override
            public void onSuccess(int code, Header[] headers, byte[] bytes)
            {
                try
                {
                    Method method = responseType.getDeclaredMethod("parseFrom", byte[].class);
                    Object obj = method.invoke(responseType, bytes);
                    T response = (T) obj;

                    handler.onResponse(response, SilverProtoManager.ResponseCodeSuccess, code, null);
                    if (null != delegate) delegate.onResponse(url, tag, bytes, SilverProtoManager.ResponseCodeSuccess);
                }
                catch (NoSuchMethodException e)
                {
                    SilverProtoRequester.handlerResponseException(delegate, handler, url, tag, SilverProtoManager.ResponseCodeFailParse, code, e);
                }
                catch (IllegalAccessException e)
                {
                    SilverProtoRequester.handlerResponseException(delegate, handler, url, tag, SilverProtoManager.ResponseCodeFailParse, code, e);
                }
                catch (InvocationTargetException e)
                {
                    SilverProtoRequester.handlerResponseException(delegate, handler, url, tag, SilverProtoManager.ResponseCodeFailParse, code, e);
                }
                catch (Exception e)
                {
                    SilverProtoRequester.handlerResponseException(delegate, handler, url, tag, SilverProtoManager.ResponseCodeFailParse, code, e);
                }
            }

            @Override
            public void onFailure(int code, Header[] headers, byte[] bytes, Throwable throwable)
            {
                SilverProtoRequester.handlerResponseException(delegate, handler, url, tag, SilverProtoManager.ResponseCodeNetworkError, code, throwable);
            }
        };

        if (null != delegate) delegate.onRequest(url, tag);
        switch (requestMethod)
        {
            case SilverProtoManager.RequestMethodGET:
                client.get(context, url, entity, contentType, httpHandler);
                break;

            case SilverProtoManager.RequestMethodPOST:
                client.post(context, url, entity, contentType, httpHandler);
                break;

            case SilverProtoManager.RequestMethodPUT:
                client.put(context, url, entity, contentType, httpHandler);
                break;

            case SilverProtoManager.RequestMethodPATCH:
                client.patch(context, url, entity, contentType, httpHandler);
                break;

            case SilverProtoManager.RequestMethodDELETE:
                client.delete(context, url, entity, contentType, httpHandler);
                break;

            default:
                Log.e("Exception", "Not supprted request method");
        }
    }

    private static void handlerResponseException(SilverProtoListener delegate,
                                                 SilverProtoHandler handler,
                                                 String url,
                                                 String tag,
                                                 int responseCode,
                                                 int httpCode,
                                                 Throwable throwable)
    {
        if (null != delegate) delegate.onResponse(url, tag, null, responseCode);
        handler.onResponse(null, responseCode, httpCode, throwable);
        throwable.printStackTrace();
    }

}
