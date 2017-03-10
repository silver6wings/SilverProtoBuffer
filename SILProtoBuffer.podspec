
Pod::Spec.new do |s|

s.name         = "SILProtobuffer"
s.version      = "1.0.0"
s.summary      = "Google Protobuffer v2.6 pods"
s.description  = <<-DESC
Google Protobuffer v2.6 pods easy to import
DESC

s.homepage     = "https://github.com/silver6wings/SILProtoBuffer"
s.license      = "MIT"
s.author       = { "silver6wings" => "silver6wings@126.com" }
s.platform     = :ios,'8.0'
s.source       = { :git => "https://github.com/silver6wings/SAFProtobuffer.git", :tag => "#{s.version}" }

s.source_files = "GoogleProtoBuffer/*.{h,m}"

end
