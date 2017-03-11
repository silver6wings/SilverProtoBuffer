
Pod::Spec.new do |s|

s.name         = "SILProtobuffer"
s.version      = "1.0.0"
s.summary      = "Google Protobuffer v2.6 pods"

s.cocoapods_version = '>= 1.0'

s.homepage     = "https://github.com/silver6wings/SILProtoBuffer"
s.license      = "MIT"
s.author       = { "silver6wings" => "silver6wings@126.com" }
s.platform     = :ios,'8.0'

s.source       = { :git => "https://github.com/silver6wings/SILProtobuffer.git",
                   :tag => "#{s.version}" }

s.source_files = 'GoogleProtoBuffer/*.{h,m}',
                 'GoogleProtoBuffer/protobufAny.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobufApi.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobufDuration.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobufEmpty.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobufFieldMask.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobufSourceContext.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobufStruct.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobufTimestamp.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobufType.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobufWrappers.pbobjc.{h,m}'

s.exclude_files = 'GoogleProtoBuffer/GPBProtocolBuffers.m'

s.user_target_xcconfig = { 'GCC_PREPROCESSOR_DEFINITIONS' => '$(inherited) GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS=1' }
s.pod_target_xcconfig = { 'GCC_PREPROCESSOR_DEFINITIONS' => '$(inherited) GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS=1' }

s.requires_arc = false

end
