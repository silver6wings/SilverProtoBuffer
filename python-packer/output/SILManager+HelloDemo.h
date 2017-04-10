
#import <Foundation/Foundation.h>

@interface SILManager (HelloDemo)

// This is a hello demo get
- (void)helloGetWithCompletion:(void (^)(SILHelloResponse *response, YHJResponseCode code, NSError *error))handler
                    AndRequest:(SILHelloRequest *)request
;
// This is a hello demo post
- (void)helloPostWithCompletion:(void (^)(SILHelloResponse *response, YHJResponseCode code, NSError *error))handler
                         AndNum:(NSUInteger)num
                         AndLen:(NSUInteger)len
                       AndIsnew:(NSString *)isnew
;
@end
