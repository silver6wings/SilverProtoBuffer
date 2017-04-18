package com.silver6wings;

import android.content.Context;
import com.silver6wings.protobuffer.SilverProtoBaseProvider;
import com.silver6wings.protobuffer.SilverProtoHandler;
import com.silver6wings.protobuffer.SilverProtoManager;
import com.silver6wings.protobuffer.SilverProtoRequester;
import com.silver6wings.MyHello;

public class HelloDemoProvider extends SilverProtoBaseProvider
{
	public static interface HelloResponseHandler extends SilverProtoHandler <MyHello.HelloResponse> {}

	// This is a hello demo get
	public static void helloGet(Context context,
								String foo, Integer ID,
								HelloDemoProvider.HelloResponseHandler handler)
	{
		String URL = serverURL + "/hello/{ID}/get?foo={foo}";
		URL = URL.replace("{foo}", foo.toString());
		URL = URL.replace("{ID}", ID.toString());
		SilverProtoRequester.request(
				SilverProtoManager.getInstance().getClient(),
				context,
				SilverProtoManager.RequestMethodGET,
				"helloGetTag",
				URL,
				null,
				MyHello.HelloResponse.class,
				handler
		);
	}

	// This is a hello demo post
	public static void helloPost(Context context,
								 MyHello.HelloRequest.Builder requestBody,
								 HelloDemoProvider.HelloResponseHandler handler)
	{
		String URL = serverURL + "/hello/post";
		SilverProtoRequester.request(
				SilverProtoManager.getInstance().getClient(),
				context,
				SilverProtoManager.RequestMethodPOST,
				"helloPostTag",
				URL,
				requestBody,
				MyHello.HelloResponse.class,
				handler
		);
	}

}
