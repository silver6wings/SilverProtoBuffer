//
//  SILProtobuffer.h
//  SILProtobuffer
//
//  Created by JUNCHAO on 2017/3/10.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#warning fill your domain URL here

#define BASE_URL @"http://api.zhushou.youhujia.com"

#define CONTENT_PROTOBUF @"application/x-protobuf"


typedef NS_ENUM(NSUInteger, YHJResponseCode)
{
    YHJResponseCodeSuccess,             // 请求成功，数据成功
    YHJResponseCodeFail,                // 请求成功，后端返回错误
    YHJResponseCodeProcess,             // 请求过程中
    YHJResponseCodeNetworkError,        // 请求失败网络错误
    YHJResponseCodeParameterError,      // 请求所需参数不合法
    YHJResponseCodeNeedTencentProfile,  // 请求所需参数需要腾讯云登录获得
    YHJResponseCodeNoPaid,              // 请求支付失败
};
