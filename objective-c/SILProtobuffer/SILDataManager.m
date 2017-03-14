//
//  SILDataManager.m
//  SILProtobuffer
//
//  Created by JUNCHAO on 2017/3/14.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#import "SILDataManager.h"
#import "GPBProtocolBuffers.h"

@implementation SILDataManager

+ (GPBMessage *)dataToProto:(NSData *)data WithClassType:(Class)classType
{
    __kindof GPBMessage *object = nil;
    
    @try
    {
        object = [classType parseFromData:data error:nil];
    }
    @catch (NSException *exception)
    {
        NSLog(@"解析Protobuf数据时出错");
    }
    
    return object;
}

@end
