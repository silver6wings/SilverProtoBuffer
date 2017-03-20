//
//  SILManager.m
//  SILProtobuffer
//
//  Created by JUNCHAO on 2017/3/14.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#import "SILManager.h"
#import "SILAPI.h"
#import "AFNetworking.h"

@interface SILManager ()

+ (AFHTTPSessionManager *)defaultSessionManager;

@end

@implementation SILManager

+ (instancetype)instance
{
    static SILManager *instance;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        instance = [[self alloc] init];
        instance.sessionManager = [SILManager defaultSessionManager];
    });
    return instance;
}

+ (AFHTTPSessionManager *)defaultSessionManager
{
    AFHTTPRequestSerializer *requestSerializer = [AFJSONRequestSerializer serializer];
    AFHTTPResponseSerializer *responseSerializer = [AFHTTPResponseSerializer serializer];
    
    requestSerializer.timeoutInterval = REQUEST_TIMOUT;
    [requestSerializer setValue:CONTENT_PROTOBUF forHTTPHeaderField:@"Content-Type"];
    [requestSerializer setValue:CONTENT_PROTOBUF forHTTPHeaderField:@"Accept"];
    
    responseSerializer.acceptableContentTypes = [NSSet setWithObjects:CONTENT_PROTOBUF, nil];
    
    AFHTTPSessionManager *manager = [AFHTTPSessionManager manager];
    manager.requestSerializer = requestSerializer;
    manager.responseSerializer = responseSerializer;
    return manager;
}


@end
