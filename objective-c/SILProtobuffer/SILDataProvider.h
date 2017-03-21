//
//  SILManager+Sample.h
//  SILProtobuffer
//
//  Created by Junchao Yu on 2017/3/19.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#import "SILManager.h"

@class YHJGAnnouncementEventAddOption, YHJGAnnouncementEventAddDTO, SAFSimpleResponse;

@interface SILDataProvider : NSObject

// put generated code here

+ (void)announcementAddWithRequest:(YHJGAnnouncementEventAddOption *)request
                 CompletionHandler:(void(^)(SAFSimpleResponse *response, SILResponseCode code, NSError *error))handler;

@end
