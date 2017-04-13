
#import <Foundation/Foundation.h>
#import "SILManager.h"


#import "Hello.pbobjc.h"

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
// IIIIIIIIIIIIIIII
- (void)AAAAAWithCompletion:(void (^)(SILRRRRRRRR *response, YHJResponseCode code, NSError *error))handler
                 AndRequest:(SILRRRRRRR *)request
                AndPPPPPPPP:(NSUInteger)PPPPPPPP
;
@end
