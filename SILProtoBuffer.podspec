
Pod::Spec.new do |s|

s.name         = "SILProtoBuffer"
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
                 'GoogleProtoBuffer/protobuf/Any.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobuf/Api.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobuf/Duration.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobuf/Empty.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobuf/FieldMask.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobuf/SourceContext.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobuf/Struct.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobuf/Timestamp.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobuf/Type.pbobjc.{h,m}',
                 'GoogleProtoBuffer/protobuf/Wrappers.pbobjc.{h,m}'

s.exclude_files = 'GoogleProtoBuffer/GPBProtocolBuffers.m'

# s.user_target_xcconfig = { 'GCC_PREPROCESSOR_DEFINITIONS' => '$(inherited) GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS=1' }
# s.pod_target_xcconfig = { 'GCC_PREPROCESSOR_DEFINITIONS' => '$(inherited) GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS=1' }

s.requires_arc = false

end
