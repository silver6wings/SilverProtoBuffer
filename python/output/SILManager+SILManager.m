
#import "SILManager+ProtoDemo.h"

@implementation SILManager (ProtoDemo)

// This is the first sample api demo
- (void)getRandomStringWithCompletion:(void (^)(YHJGMessageCenterDTO *response, YHJResponseCode code, NSError *error))handler
                               AndNum:(NSUInteger)num
                               AndLen:(NSUInteger)len
                             AndIsnew:(NSString *)isnew
{
    NSString *URL = [NSString stringWithFormat:@"%@/strings/?num={num}&len={len}&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd={isnew}", [SILManager instance].serverURL];
    URL = [URL stringByReplacingOccurrencesOfString:@"{num}" withString:[NSString stringWithFormat:@"%lu", num]];
    URL = [URL stringByReplacingOccurrencesOfString:@"{len}" withString:[NSString stringWithFormat:@"%lu", len]];
    URL = [URL stringByReplacingOccurrencesOfString:@"{isnew}" withString:[NSString stringWithFormat:@"%@", isnew]];
    [YHJProtoUtils sendGPBWithMethod:@"GET"
                              AndTag:@"get_random_string"
                              AndURL:URL
                       AndGPBMessage:nil
                     AndResponseType:[YHJGMessageCenterDTO class]
                      AndCachePolicy:NSURLRequestUseProtocolCachePolicy
                   CompletionHandler:handler];
}

// This is the second sample api demo
- (void)testWithCompletion:(void (^)(YHJGMessageCenterDTO *response, YHJResponseCode code, NSError *error))handler
                AndRequest:(YHJGAddOption *)request
{
    NSString *URL = [NSString stringWithFormat:@"%@/www.random.org/", [SILManager instance].serverURL];
    [YHJProtoUtils sendGPBWithMethod:@"GET"
                              AndTag:@"get_random_string"
                              AndURL:URL
                       AndGPBMessage:request
                     AndResponseType:[YHJGMessageCenterDTO class]
                      AndCachePolicy:NSURLRequestUseProtocolCachePolicy
                   CompletionHandler:handler];
}

@end
