//
//  SILAPI.h
//  SILProtobuffer
//
//  Created by JUNCHAO on 2017/3/14.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#define CONTENT_PROTOBUF    @"application/x-protobuf"
#define CONTENT_JSON        @"application/json"
#define REQUEST_TIMOUT      (10.0f)

typedef NS_ENUM(unsigned long, SILResponseCode)
{
    SILResponseCodeSuccess,             // 请求成功，数据成功
    SILResponseCodeFail,                // 请求失败，网络错误
    SILResponseCodeProcess,             // 请求过程中
};

@protocol SILRequestDelegate <NSObject>

- (void)willRequestToURL:(NSString *)URL withTag:(NSString *)tag;

@end

@protocol SILResponseDelegate <NSObject>

- (void)didResponsedFromURL:(NSString *)URL withTag:(NSString *)tag withResult:(BOOL)success;

@end
