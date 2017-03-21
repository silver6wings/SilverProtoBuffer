
Pod::Spec.new do |s|

    s.name         = "SILProtoBuffer"
    s.version      = "1.0.2"
    s.summary      = "A networking framework based on Google Protobuf v2.6 & AFNetworking that can help you pack APIs"
    s.cocoapods_version = '>= 1.0'
    s.homepage     = "https://github.com/silver6wings/SILProtoBuffer"
    s.license      = "MIT"
    s.author       = { "silver6wings" => "silver6wings@126.com" }
    s.platform     = :ios,'8.0'

    s.source       = { :git => "https://github.com/silver6wings/SILProtobuffer.git",
                       :tag => "#{s.version}" }

    s.requires_arc = true

    s.source_files    = 'objective-c/SILProtobuffer/SILProtobuffer.h',
                        'objective-c/SILProtobuffer/SILAPI.h',
                        'objective-c/SILProtobuffer/SILManager.{h,m}',
                        'objective-c/SILProtobuffer/SILParser.{h,m}',
                        'objective-c/SILProtobuffer/SILRequester.{h,m}'

    s.subspec 'AFNetworking' do |ss|
        ss.requires_arc = true
        ss.source_files = 'objective-c/AFNetworking/*.{h,m}'
    end

    s.subspec 'GoogleProtobuf' do |ss|

        ss.requires_arc = false
        ss.source_files = 'objective-c/GoogleProtobuf/*.{h,m}',
                          'objective-c/GoogleProtobuf/protobuf/Any.pbobjc.{h,m}',
                          'objective-c/GoogleProtobuf/protobuf/Api.pbobjc.{h,m}',
                          'objective-c/GoogleProtobuf/protobuf/Duration.pbobjc.{h,m}',
                          'objective-c/GoogleProtobuf/protobuf/Empty.pbobjc.{h,m}',
                          'objective-c/GoogleProtobuf/protobuf/FieldMask.pbobjc.{h,m}',
                          'objective-c/GoogleProtobuf/protobuf/SourceContext.pbobjc.{h,m}',
                          'objective-c/GoogleProtobuf/protobuf/Struct.pbobjc.{h,m}',
                          'objective-c/GoogleProtobuf/protobuf/Timestamp.pbobjc.{h,m}',
                          'objective-c/GoogleProtobuf/protobuf/Type.pbobjc.{h,m}',
                          'objective-c/GoogleProtobuf/protobuf/Wrappers.pbobjc.{h,m}'

        ss.exclude_files = 'objective-c/GoogleProtobuf/GPBProtocolBuffers.m'
        # ss.user_target_xcconfig = { 'GCC_PREPROCESSOR_DEFINITIONS' => '$(inherited) GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS=1' }
        # ss.pod_target_xcconfig = { 'GCC_PREPROCESSOR_DEFINITIONS' => '$(inherited) GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS=1' }

    end
end
