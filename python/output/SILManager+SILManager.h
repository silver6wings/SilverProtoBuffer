
#import <Foundation/Foundation.h>

@interface SILManager (ProtoDemo)

// This is the first sample api demo
- (void)getRandomStringWithCompletion:(void (^)(YHJGMessageCenterDTO *response, YHJResponseCode code, NSError *error))handler
                               AndNum:(NSUInteger)num
                               AndLen:(NSUInteger)len
                             AndIsnew:(NSString *)isnew
;
// This is the second sample api demo
- (void)testWithCompletion:(void (^)(YHJGMessageCenterDTO *response, YHJResponseCode code, NSError *error))handler
                AndRequest:(YHJGAddOption *)request
;
@end
