
Pod::Spec.new do |s|

    s.name         = "SILProtoBuffer"
    s.version      = "1.0.3"
    s.summary      = "A networking framework based on Google Protobuf v2.6 & AFNetworking that can help you pack APIs"
    s.cocoapods_version = '>= 1.0'
    s.homepage     = "https://github.com/silver6wings/SILProtoBuffer"
    s.license      = "MIT"
    s.author       = { "silver6wings" => "silver6wings@126.com" }
    s.platform     = :ios,'8.0'

    s.source       = { :git => "https://github.com/silver6wings/SILProtobuffer.git",
                       :tag => "#{s.version}" }

    s.subspec 'SILProtobuffer' do |ss|
        s.requires_arc = true
        s.source_files    = 'objc-ios/SILProtobuffer/SILProtobuffer.h',
                            'objc-ios/SILProtobuffer/SILAPI.h',
                            'objc-ios/SILProtobuffer/SILManager.{h,m}',
                            'objc-ios/SILProtobuffer/SILParser.{h,m}',
                            'objc-ios/SILProtobuffer/SILRequester.{h,m}'
    end

    s.subspec 'SilverAFNetworking' do |ss|
        ss.requires_arc = true
        ss.source_files = 'objc-ios/AFNetworking/*.{h,m}'
    end

    s.subspec 'Protobuf260' do |ss|

        ss.requires_arc = false
        ss.source_files = 'objc-ios/GoogleProtobuf/*.{h,m}',
                          'objc-ios/GoogleProtobuf/protobuf/Any.pbobjc.{h,m}',
                          'objc-ios/GoogleProtobuf/protobuf/Api.pbobjc.{h,m}',
                          'objc-ios/GoogleProtobuf/protobuf/Duration.pbobjc.{h,m}',
                          'objc-ios/GoogleProtobuf/protobuf/Empty.pbobjc.{h,m}',
                          'objc-ios/GoogleProtobuf/protobuf/FieldMask.pbobjc.{h,m}',
                          'objc-ios/GoogleProtobuf/protobuf/SourceContext.pbobjc.{h,m}',
                          'objc-ios/GoogleProtobuf/protobuf/Struct.pbobjc.{h,m}',
                          'objc-ios/GoogleProtobuf/protobuf/Timestamp.pbobjc.{h,m}',
                          'objc-ios/GoogleProtobuf/protobuf/Type.pbobjc.{h,m}',
                          'objc-ios/GoogleProtobuf/protobuf/Wrappers.pbobjc.{h,m}'

        ss.exclude_files = 'objc-ios/GoogleProtobuf/GPBProtocolBuffers.m'
        # ss.user_target_xcconfig = { 'GCC_PREPROCESSOR_DEFINITIONS' => '$(inherited) GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS=1' }
        # ss.pod_target_xcconfig = { 'GCC_PREPROCESSOR_DEFINITIONS' => '$(inherited) GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS=1' }

    end
end
