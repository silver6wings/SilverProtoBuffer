//
//  SILDataManager.m
//  SILProtobuffer
//
//  Created by JUNCHAO on 2017/3/14.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#import "SILParser.h"
#import "GPBMessage.h"

@implementation SILParser

+ (GPBMessage *)dataToModel:(id)data
              withClassType:(Class)classType
{
    if (![data isKindOfClass:[NSData class]]) return nil;
    
    __kindof GPBMessage *object = nil;
    
    @try
    {
        object = [classType parseFromData:data error:nil];
    }
    @catch (NSException *exception)
    {
        NSLog(@"Parsing protobuf data error");
        @throw NSGenericException;
    }
    
    return object;
}

@end
