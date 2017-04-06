
#import <Foundation/Foundation.h>

@interface SILManager (ProtoDemo)

// 添加公告
- (void)addAnnouncementWithCompletion:(void (^)(YHJGAnnouncementEventAddDTO *response, YHJResponseCode code, NSError *error))handler
                           AndRequest:(YHJGAnnouncementEventAddOption *)request
;
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
