package io.dcloud.service.protobuf;

import android.content.Context;
import io.dcloud.service.protobuf.params.ProtoBufferBaseHandler;
import io.dcloud.service.protobuf.params.RequestModel;
import io.dcloud.service.protobuf.params.RequestType;
import com.example.Hello;

public class HelloDemoProvider extends SILDataProvider
{
	public static interface HelloResponseHandler extends ProtoBufferBaseHandler<Hello.HelloResponse> {}

	// This is a hello demo get
	public static void helloGet(Context context, String token, CacheType cacheType,
		String content, Integer id, 
		HelloDemoProvider.HelloResponseHandler handler)
	{
		String URL = serverURL + "/hello?id={id}&content={content}";
		URL = URL.replace("{content}", content.toString());
		URL = URL.replace("{id}", id.toString());
		RequestModel requestModel = new RequestModel();
		requestModel.cacheType = cacheType;
		requestModel.requestType = RequestType.GET;
		requestModel.url = URL;
		requestModel.sensorTag = "helloGet";
		ProtoBufferRequester.request(context, token, requestModel, null, Hello.HelloResponse.class, handler);
	}

	// This is a hello demo post
	public static void helloPost(Context context, String token, CacheType cacheType,
		Hello.HelloRequest.Builder requestBody,
		HelloDemoProvider.HelloResponseHandler handler)
	{
		String URL = serverURL + "/hello";
		RequestModel requestModel = new RequestModel();
		requestModel.cacheType = cacheType;
		requestModel.requestType = RequestType.POST;
		requestModel.url = URL;
		requestModel.sensorTag = "helloPost";
		ProtoBufferRequester.request(context, token, requestModel, requestBody, Hello.HelloResponse.class, handler);
	}

}
