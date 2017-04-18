
#import <Foundation/Foundation.h>
#import "SilverProtoBaseProvider.h"
#import "Hello.pbobjc.h"

@interface SilverProtoBaseProvider (HelloDemo)

// This is a hello demo get
+ (void)helloGetWithCompletion:(void (^)(SILHelloResponse *response, SILResponseCode code, NSError *error))handler
                        AndFoo:(NSString *)foo
                         AndID:(NSUInteger)ID
;
// This is a hello demo post
+ (void)helloPostWithCompletion:(void (^)(SILHelloResponse *response, SILResponseCode code, NSError *error))handler
                     AndRequest:(SILHelloRequest *)request
;
@end
