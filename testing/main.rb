require "google-cloud-vision"

ENV["VISION_CREDENTIALS"] = "top-chain-394711-7099022fdf51.json"

client = Google::Cloud::Vision.image_annotator

puts "x"

image = File.open("IMG_2713.jpg", 'rb') { |file| file.read }

requests = [
    {
      "features": [
        {
          "max_results": 5,
          "type": "LANDMARK_DETECTION"
        },
        {
          "max_results": 5,
          "type": "OBJECT_LOCALIZATION"
        },
        {
          "max_results": 5,
          "type": "LABEL_DETECTION"
        },
        {
          "max_results": 50,
          "type": "SAFE_SEARCH_DETECTION"
        },
      ],
      "image": {
        "content": image
      },
      "image_context": {
        "crop_hints_params": {
          "aspect_ratios": [
            0.8,
            1,
            1.2
          ]
        }
      }
    }
]

# requests = Hash.new

# requests = Google::Protobuf::Struct.from_hash(requests)

response = client.batch_annotate_images requests: requests

puts response

labels = response['responses'][0]['label_annotations']
objects = response['responses'][0]['']

for i in objects do 
  puts i
end

# https://vision.googleapis.com/v1/images:annotate