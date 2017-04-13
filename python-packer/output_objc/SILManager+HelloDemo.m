
#import "SILManager+HelloDemo.h"
#import "SILRequester.h"

@implementation SILManager (HelloDemo)

// This is a hello demo get
+ (void)helloGetWithCompletion:(void (^)(SILHelloResponse *response, SILResponseCode code, NSError *error))handler
                    AndContent:(NSString *)content
                         AndId:(NSUInteger)id
{
    NSString *URL = [NSString stringWithFormat:@"%@/hello?id={id}&content={content}", [SILManager instance].serverURL];
    URL = [URL stringByReplacingOccurrencesOfString:@"{content}" withString:[NSString stringWithFormat:@"%@", content]];
    URL = [URL stringByReplacingOccurrencesOfString:@"{id}" withString:[NSString stringWithFormat:@"%lu", id]];
    [SILRequester requestWithMethod:SILRequestMethodGET
                             andTag:@"helloGet"
                             andURL:URL
                      andGPBMessage:nil
                    andResponseType:[SILHelloResponse class]
                  completionHandler:handler];
}

// This is a hello demo post
+ (void)helloPostWithCompletion:(void (^)(SILHelloResponse *response, SILResponseCode code, NSError *error))handler
                     AndRequest:(SILHelloRequest *)request
{
    NSString *URL = [NSString stringWithFormat:@"%@/hello", [SILManager instance].serverURL];
    [SILRequester requestWithMethod:SILRequestMethodPOST
                             andTag:@"helloPost"
                             andURL:URL
                      andGPBMessage:request
                    andResponseType:[SILHelloResponse class]
                  completionHandler:handler];
}

@end
