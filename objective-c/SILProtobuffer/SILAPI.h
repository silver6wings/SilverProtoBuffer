//
//  SILAPI.h
//  SILProtobuffer
//
//  Created by JUNCHAO on 2017/3/14.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

typedef NS_ENUM(NSUInteger, SILResponseCode)
{
    SILResponseCodeSuccess,             // 请求成功，数据成功
    SILResponseCodeFail,                // 请求失败，网络错误
    SILResponseCodeProcess,             // 请求过程中
};

@protocol SILRequestDelegate <NSObject>

- (void)willRequestAPIwithURL:(NSString *)URL withTag:(NSString *)tag;

@end

@protocol SILResponseDelegate <NSObject>

- (void)didResponsedFromAPIwithURL:(NSString *)URL withTag:(NSString *)tag withResult:(BOOL)success;

@end
