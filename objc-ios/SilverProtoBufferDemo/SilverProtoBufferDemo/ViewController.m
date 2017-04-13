//
//  ViewController.m
//  SilverProtoBufferDemo
//
//  Created by JUNCHAO on 2017/4/13.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#import "ViewController.h"
#import "SILProtoBuffer.h"
#import "SILManager+HelloDemo.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    [SILManager instance].isDebugging = NO;
    [SILManager instance].onlineServerURL = @"http://localhost:8080";
    
    [SILManager helloGetWithCompletion:^(SILHelloResponse *response, SILResponseCode code, NSError *error)
    {
        NSLog(@"%@", response.helloContent);
    }
                            AndContent:@"qqq"
                                 AndId:111];
}


- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
}


@end
