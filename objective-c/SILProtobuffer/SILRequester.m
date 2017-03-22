//
//  SILRequestManager.m
//  SILProtobuffer
//
//  Created by JUNCHAO on 2017/3/14.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#import "SILManager.h"
#import "SILParser.h"
#import "SILRequester.h"
#import "GPBMessage.h"

@implementation SILRequester

+ (void)requestWithMethod:(SILRequestMethod)method
                   andTag:(NSString *)tag
                   andURL:(NSString *)url
            andGPBMessage:(__kindof GPBMessage *)gpb
          andResponseType:(Class)responseClass
        CompletionHandler:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler
{
    [SILRequester requestWithMethod:method
                             andTag:tag
                             andURL:url
                     andCachePolicy:NSURLRequestUseProtocolCachePolicy
                      andGPBMessage:gpb
                    andResponseType:responseClass
                         completion:handler];
}

+ (void)requestWithMethod:(SILRequestMethod)method
                   andTag:(NSString *)tag
                   andURL:(NSString *)url
           andCachePolicy:(NSURLRequestCachePolicy)policy
            andGPBMessage:(__kindof GPBMessage *)gpb
          andResponseType:(Class)responseClass
               completion:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler;
{
    AFHTTPSessionManager *manager = [SILManager instance].sessionManager;
    manager.requestSerializer.cachePolicy = policy;
    
    [[SILManager instance].requestDelegate willRequestToURL:url withTag:tag];
    
    switch (method)
    {
        case SILRequestMethodGET:
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
            break;
            
        case SILRequestMethodPOST:
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
            break;
            
        case SILRequestMethodPUT:
        {
            [manager PUT:url
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
            break;
            
        case SILRequestMethodPATCH:
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
            break;
            
        case SILRequestMethodDELETE:
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
            break;
            
        default:
        {
            NSLog(@"Not supported HTTP method:%lu %@", method, url);
            @throw NSGenericException;
        }
            break;
    }
}

+ (void)successFromRequestURL:(NSString *)url
                       andTag:(NSString *)tag
                  andResponse:(id)responseObject
              andResponseType:(Class)responseClass
              completion:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler
{
    [[SILManager instance].responseDelegate didResponsedFromURL:url withTag:tag withResult:YES];
    __kindof GPBMessage *object = [SILParser dataToModel:responseObject withClassType:responseClass];
    
    handler(object, object ? SILResponseCodeSuccess : SILResponseCodeFailParse, nil);
}

+ (void)failFromRequestURL:(NSString *)url
                    andTag:(NSString *)tag
                  andError:(NSError *)error
              completion:(void(^)(__kindof GPBMessage *response, SILResponseCode code, NSError *error))handler
{
    [[SILManager instance].responseDelegate didResponsedFromURL:url withTag:tag withResult:NO];
    handler(nil, SILResponseCodeNetworkError, error);
}

@end
