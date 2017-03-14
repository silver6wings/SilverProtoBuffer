//
//  SILRequestManager.m
//  SILProtobuffer
//
//  Created by JUNCHAO on 2017/3/14.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#import "SILRequestManager.h"
#import "SILManager.h"
#import "SILDataManager.h"
#import "AFNetworking.h"
#import "GPBProtocolBuffers.h"

@interface SILRequestManager ()

@end

@implementation SILRequestManager

+ (void)sendGPBWithMethod:(NSString *)method
                   andTag:(NSString *)urlTag
                   andURL:(NSString *)url
            andGPBMessage:(__kindof GPBMessage *)gpb
          andResponseType:(Class)responseClass
        CompletionHandler:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler
{
    [SILRequestManager sendGPBWithMethod:method
                                  andTag:urlTag andURL:url
                           andGPBMessage:gpb
                         andResponseType:responseClass
                       CompletionHandler:handler];
}

+ (void)sendGPBWithMethod:(NSString *)method
                   andTag:(NSString *)urlTag
                   andURL:(NSString *)url
           andCachePolicy:(NSURLRequestCachePolicy)policy
            andGPBMessage:(__kindof GPBMessage *)gpb
          andResponseType:(Class)responseClass
               completion:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler;
{
    AFHTTPSessionManager *manager = [SILManager instance].sessionManagerHTTP;
    manager.requestSerializer.cachePolicy = policy;
    
    [[SILManager instance].requestDelegate willRequestAPIwithURL:url withTag:urlTag];
    
    if ([method isEqualToString:@"GET"])
    {
        [manager GET:url
          parameters:[gpb data]
            progress:^(NSProgress * _Nonnull downloadProgress)
         {
             handler(nil, SILResponseCodeProcess, nil);
         }
             success:^(NSURLSessionDataTask * _Nonnull task, id  _Nullable responseObject)
         {
             [SILRequestManager successFromRequestURL:url
                                               andTag:urlTag
                                          andResponse:responseObject
                                      andResponseType:responseClass
                                           completion:handler];
         }
             failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error)
         {
             [SILRequestManager failFromRequestURL:url
                                            andTag:urlTag
                                          andError:error
                                        completion:handler];
         }];
    }
    else if ([method isEqualToString:@"POST"])
    {
        [manager POST:url
           parameters:[gpb data]
             progress:^(NSProgress * _Nonnull downloadProgress)
         {
             handler(nil, SILResponseCodeProcess, nil);
         }
              success:^(NSURLSessionDataTask * _Nonnull task, id  _Nullable responseObject)
         {
             [SILRequestManager successFromRequestURL:url
                                               andTag:urlTag
                                          andResponse:responseObject
                                      andResponseType:responseClass
                                           completion:handler];
         }
              failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error)
         {
             [SILRequestManager failFromRequestURL:url
                                            andTag:urlTag
                                          andError:error
                                        completion:handler];
         }];
    }
    else if ([method isEqualToString:@"PATCH"])
    {
        [manager PATCH:url
            parameters:[gpb data]
               success:^(NSURLSessionDataTask * _Nonnull task, id  _Nullable responseObject)
         {
             [SILRequestManager successFromRequestURL:url
                                               andTag:urlTag
                                          andResponse:responseObject
                                      andResponseType:responseClass
                                           completion:handler];
         }
               failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error)
         {
             [SILRequestManager failFromRequestURL:url
                                            andTag:urlTag
                                          andError:error
                                        completion:handler];
         }];
    }
    else if ([method isEqualToString:@"DELETE"])
    {
        [manager DELETE:url
             parameters:[gpb data]
                success:^(NSURLSessionDataTask * _Nonnull task, id  _Nullable responseObject)
         {
             [SILRequestManager successFromRequestURL:url
                                               andTag:urlTag
                                          andResponse:responseObject
                                      andResponseType:responseClass
                                           completion:handler];
         }
                failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error)
         {
             [SILRequestManager failFromRequestURL:url
                                            andTag:urlTag
                                          andError:error
                                        completion:handler];
         }];
    }
    else
    {
        NSLog(@"不支持HTTP方法名:%@ %@", method, url);
        @throw NSGenericException;
    }
}

+ (void)successFromRequestURL:(NSString *)url
                       andTag:(NSString *)urlTag
                  andResponse:(id)responseObject
              andResponseType:(Class)responseClass
              completion:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler
{
    [[SILManager instance].responseDelegate didResponsedFromAPIwithURL:url withTag:urlTag withResult:YES];
    
    __kindof GPBMessage *object = [SILDataManager dataToProto:responseObject WithClassType:responseClass];
    handler(object, SILResponseCodeSuccess, nil);
}

+ (void)failFromRequestURL:(NSString *)url
                    andTag:(NSString *)urlTag
                  andError:(NSError *)error
              completion:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler
{
    [[SILManager instance].responseDelegate didResponsedFromAPIwithURL:url withTag:urlTag withResult:NO];
    handler(nil, SILResponseCodeFail, error);
}

@end
