
#import <Foundation/Foundation.h>
#import "SILManager.h"
#import "Hello.pbobjc.h"

@interface SILManager (HelloDataProvider)

// This is a hello demo get
+ (void)helloGetWithCompletion:(void (^)(SILHelloResponse *response, SILResponseCode code, NSError *error))handler
                        AndFoo:(NSString *)foo
                         AndID:(NSUInteger)ID
;
// This is a hello demo post
+ (void)helloPostWithCompletion:(void (^)(SILHelloResponse *response, SILResponseCode code, NSError *error))handler
                 AndCachePolicy:(NSURLRequestCachePolicy)policy
                     AndRequest:(SILHelloRequest *)request
;
@end
