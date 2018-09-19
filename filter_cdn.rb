require 'net/http'
require 'json'

query = ARGV[0]
uri = URI("https://api.cdnjs.com/libraries?search=#{query}")
response = JSON.parse(Net::HTTP.get(uri))
items = response['results'].map do |result|
  "<item arg='#{result['latest']} #{result['name']}'>\
    <title>#{result['name']}</title>\
   </item>\
  "
end

xml = <<EOS
<xml>
<items>
  #{items}
</items>
</xml>
EOS
puts xml
