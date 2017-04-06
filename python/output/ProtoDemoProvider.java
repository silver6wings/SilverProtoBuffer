import test.sample.Galaxy;

public class ProtoDemoProvider
{
	// 添加公告
	public static interface AnnouncementEventAddDTOHandler extends ProtoBufferBaseHandler<Galaxy.AnnouncementEventAddDTO> {}
	public static void addAnnouncement(Context context, String token, CacheType cacheType,
		Galaxy.AnnouncementEventAddOption.Builder requestBody,
		ProtoDemoProvider.AnnouncementEventAddDTOHandler handler)
	{
		String URL = serverURL + "/api/addAnnouncement";
		RequestModel requestModel = new RequestModel();
		requestModel.cacheType = cacheType;
		requestModel.requestType = RequestType.POST;
		requestModel.url = URL;
		requestModel.sensorTag = "addAnnouncement";
		ProtoBufferRequester.request(context, token, requestModel, requestBody, Galaxy.AnnouncementEventAddDTO.class, handler);
	}

	// This is the first sample api demo
	public static interface MessageCenterDTOHandler extends ProtoBufferBaseHandler<Galaxy.MessageCenterDTO> {}
	public static void getRandomString(Context context, String token, CacheType cacheType,
		Integer num, Integer len, String isnew, 
		ProtoDemoProvider.MessageCenterDTOHandler handler)
	{
		String URL = serverURL + "/strings/?num={num}&len={len}&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd={isnew}";
		URL = URL.replace("{num}", num.toString());
		URL = URL.replace("{len}", len.toString());
		URL = URL.replace("{isnew}", isnew.toString());
		RequestModel requestModel = new RequestModel();
		requestModel.cacheType = cacheType;
		requestModel.requestType = RequestType.GET;
		requestModel.url = URL;
		requestModel.sensorTag = "get_random_string";
		ProtoBufferRequester.request(context, token, requestModel, null, Galaxy.MessageCenterDTO.class, handler);
	}

	// This is the second sample api demo
	public static interface MessageCenterDTOHandler extends ProtoBufferBaseHandler<Galaxy.MessageCenterDTO> {}
	public static void test(Context context, String token, CacheType cacheType,
		Galaxy.AddOption.Builder requestBody,
		ProtoDemoProvider.MessageCenterDTOHandler handler)
	{
		String URL = serverURL + "/www.random.org/";
		RequestModel requestModel = new RequestModel();
		requestModel.cacheType = cacheType;
		requestModel.requestType = RequestType.GET;
		requestModel.url = URL;
		requestModel.sensorTag = "get_random_string";
		ProtoBufferRequester.request(context, token, requestModel, requestBody, Galaxy.MessageCenterDTO.class, handler);
	}

}
