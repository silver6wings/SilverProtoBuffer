//
//  ViewController.m
//  SilverProtoBufferDemo
//
//  Created by JUNCHAO on 2017/4/13.
//  Copyright © 2017年 silver6wings. All rights reserved.
//

#import "ViewController.h"
#import "SILProtobuffer.h"
#import "SILManager+HelloDataProvider.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    [SILManager instance].isDebugging = NO;
    [SILManager instance].onlineServerURL = @"http://localhost:8080";
    
    UIButton *btGet = [UIButton buttonWithType:UIButtonTypeCustom];
    btGet.frame = CGRectMake(60, 100, 200, 50);
    btGet.backgroundColor = [UIColor redColor];
    [btGet setTitle:@"HelloGet" forState:UIControlStateNormal];
    [btGet addTarget:self action:@selector(requestGet:) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:btGet];
    
    
    UIButton *btPost = [UIButton buttonWithType:UIButtonTypeCustom];
    btPost.frame = CGRectMake(60, 200, 200, 50);
    btPost.backgroundColor = [UIColor blueColor];
    [btPost setTitle:@"HelloPost" forState:UIControlStateNormal];
    [btPost addTarget:self action:@selector(requestPost:) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:btPost];
    
}

- (void)requestGet:(id)sender
{
    [SILManager helloGetWithCompletion:^(SILHelloResponse *response, SILResponseCode code, NSError *error)
     {
         if (code == SILResponseCodeSuccess)
         {
             NSLog(@"id:%lu", (unsigned long)response.id_p);
             NSLog(@"content:%@", response.content);
         }
     }
                                AndFoo:@"qqq"
                                 AndID:111];
}

- (void)requestPost:(id)sender
{
    SILHelloRequest *helloRequest = [[SILHelloRequest alloc] init];
    helloRequest.id_p = 1;
    helloRequest.foo = @"AA";
    helloRequest.bar = @"BB";
    
    [SILManager helloPostWithCompletion:^(SILHelloResponse *response, SILResponseCode code, NSError *error)
     {
         if (code == SILResponseCodeSuccess)
         {
             NSLog(@"id:%lu", (unsigned long)response.id_p);
             NSLog(@"content:%@", response.content);
         }
     }
                         AndCachePolicy:NSURLRequestReloadIgnoringLocalCacheData
                             AndRequest:helloRequest
     ];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
}

@end
