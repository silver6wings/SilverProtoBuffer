
#import "SILManager+HelloDemo.h"

@implementation SILManager (HelloDemo)

// This is a hello demo get
- (void)helloGetWithCompletion:(void (^)(SILHelloResponse *response, YHJResponseCode code, NSError *error))handler
                    AndRequest:(SILHelloRequest *)request
{
    NSString *URL = [NSString stringWithFormat:@"%@/hello", [SILManager instance].serverURL];
    [YHJProtoUtils sendGPBWithMethod:@"GET"
                              AndTag:@"hello_get"
                              AndURL:URL
                       AndGPBMessage:request
                     AndResponseType:[SILHelloResponse class]
                      AndCachePolicy:NSURLRequestUseProtocolCachePolicy
                   CompletionHandler:handler];
}

// This is a hello demo post
- (void)helloPostWithCompletion:(void (^)(SILHelloResponse *response, YHJResponseCode code, NSError *error))handler
                         AndNum:(NSUInteger)num
                         AndLen:(NSUInteger)len
                       AndIsnew:(NSString *)isnew
{
    NSString *URL = [NSString stringWithFormat:@"%@/hello", [SILManager instance].serverURL];
    URL = [URL stringByReplacingOccurrencesOfString:@"{num}" withString:[NSString stringWithFormat:@"%lu", num]];
    URL = [URL stringByReplacingOccurrencesOfString:@"{len}" withString:[NSString stringWithFormat:@"%lu", len]];
    URL = [URL stringByReplacingOccurrencesOfString:@"{isnew}" withString:[NSString stringWithFormat:@"%@", isnew]];
    [YHJProtoUtils sendGPBWithMethod:@"POST"
                              AndTag:@"hello_post"
                              AndURL:URL
                       AndGPBMessage:nil
                     AndResponseType:[SILHelloResponse class]
                      AndCachePolicy:NSURLRequestUseProtocolCachePolicy
                   CompletionHandler:handler];
}

// IIIIIIIIIIIIIIII
- (void)AAAAAWithCompletion:(void (^)(SILRRRRRRRR *response, YHJResponseCode code, NSError *error))handler
                 AndRequest:(SILRRRRRRR *)request
                AndPPPPPPPP:(NSUInteger)PPPPPPPP
{
    NSString *URL = [NSString stringWithFormat:@"%@UUUUUUUUUUU", [SILManager instance].serverURL];
    URL = [URL stringByReplacingOccurrencesOfString:@"{PPPPPPPP}" withString:[NSString stringWithFormat:@"%lu", PPPPPPPP]];
    [YHJProtoUtils sendGPBWithMethod:@"MMMMMMMMM"
                              AndTag:@"TTTTT"
                              AndURL:URL
                       AndGPBMessage:request
                     AndResponseType:[SILRRRRRRRR class]
                      AndCachePolicy:NSURLRequestUseProtocolCachePolicy
                   CompletionHandler:handler];
}

@end
