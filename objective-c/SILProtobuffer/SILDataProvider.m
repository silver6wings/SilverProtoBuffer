//
//  SILManager+Sample.m
//  SILProtobuffer
//
//  Created by Junchao Yu on 2017/3/19.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#import "SILDataProvider.h"
#import "SILProtobuffer.h"
#import "Galaxy.pbobjc.h"
#import "Common.pbobjc.h"

@implementation SILDataProvider

// put generated code here

+ (void)announcementAddWithRequest:(YHJGAnnouncementEventAddOption *)request
                 CompletionHandler:(void(^)(SAFSimpleResponse *response, SILResponseCode code, NSError *error))handler
{
    NSString *URL = @"http://api.zhushou.youhujia.com/api/nurses/signup/phone-captcha";
    
    [SILRequester requestWithMethod:SILRequestMethodPOST
                             andTag:@""
                             andURL:URL
                      andGPBMessage:request
                    andResponseType:[SAFSimpleResponse class]
                  CompletionHandler:handler];
}

@end
