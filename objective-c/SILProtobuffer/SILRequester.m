//
//  SILRequestManager.m
//  SILProtobuffer
//
//  Created by JUNCHAO on 2017/3/14.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#import "SILRequester.h"
#import "SILManager.h"
#import "SILDataParser.h"
#import "AFNetworking.h"
#import "GPBProtocolBuffers.h"

@implementation SILRequester

+ (void)requestWithMethod:(NSString *)method
                   andTag:(NSString *)tag
                   andURL:(NSString *)url
            andGPBMessage:(__kindof GPBMessage *)gpb
          andResponseType:(Class)responseClass
        CompletionHandler:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler
{
    [SILRequester requestWithMethod:method
                                  andTag:tag
                                  andURL:url
                           andGPBMessage:gpb
                         andResponseType:responseClass
                       CompletionHandler:handler];
}

+ (void)requestWithMethod:(NSString *)method
                   andTag:(NSString *)tag
                   andURL:(NSString *)url
           andCachePolicy:(NSURLRequestCachePolicy)policy
            andGPBMessage:(__kindof GPBMessage *)gpb
          andResponseType:(Class)responseClass
               completion:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler;
{
    AFHTTPSessionManager *manager = [SILManager instance].sessionManager;
    manager.requestSerializer.cachePolicy = policy;
    
    [[SILManager instance].requestDelegate willRequestAPIwithURL:url withTag:tag];
    
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
             [SILRequester successFromRequestURL:url
                                               andTag:tag
                                          andResponse:responseObject
                                      andResponseType:responseClass
                                           completion:handler];
         }
             failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error)
         {
             [SILRequester failFromRequestURL:url
                                            andTag:tag
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
             [SILRequester successFromRequestURL:url
                                               andTag:tag
                                          andResponse:responseObject
                                      andResponseType:responseClass
                                           completion:handler];
         }
              failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error)
         {
             [SILRequester failFromRequestURL:url
                                            andTag:tag
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
             [SILRequester successFromRequestURL:url
                                               andTag:tag
                                          andResponse:responseObject
                                      andResponseType:responseClass
                                           completion:handler];
         }
               failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error)
         {
             [SILRequester failFromRequestURL:url
                                            andTag:tag
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
             [SILRequester successFromRequestURL:url
                                               andTag:tag
                                          andResponse:responseObject
                                      andResponseType:responseClass
                                           completion:handler];
         }
                failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error)
         {
             [SILRequester failFromRequestURL:url
                                            andTag:tag
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
                       andTag:(NSString *)tag
                  andResponse:(id)responseObject
              andResponseType:(Class)responseClass
              completion:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler
{
    [[SILManager instance].responseDelegate didResponsedFromAPIwithURL:url withTag:tag withResult:YES];
    
    __kindof GPBMessage *object = [SILDataParser dataToModel:responseObject withClassType:responseClass];
    handler(object, SILResponseCodeSuccess, nil);
}

+ (void)failFromRequestURL:(NSString *)url
                    andTag:(NSString *)tag
                  andError:(NSError *)error
              completion:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler
{
    [[SILManager instance].responseDelegate didResponsedFromAPIwithURL:url withTag:tag withResult:NO];
    handler(nil, SILResponseCodeFail, error);
}

@end
