import argparse
import json

parser = argparse.ArgumentParser(description='Construct the input json file for the image rekognition experiment.')
parser.add_argument('input_configuration',
                    help='a file containing configuration (AWS lambda uris, number of executions, s3 uri)')
parser.add_argument('image_names_file',
                    help='a file containing the output of `aws s3 ls` on the uploads directory')
parser.add_argument('output_file',
                    help='a name for the output file containing the complete json')

args = parser.parse_args()

with open(args.input_configuration) as input_config_file:
    input_config_data = input_config_file.read()

with open(args.image_names_file) as image_names_file:
    image_names_lines = image_names_file.readlines()

def clean_image_name_line(line):
    clean_line = " ".join(line.rstrip().split())
    image_name = clean_line.split()[3]
    image_id = image_name.split(".")[0]
    return (image_name, image_id)

clean_image_names_ids = [clean_image_name_line(line) for line in image_names_lines]


input_config_json = json.loads(input_config_data)
# print(input_config_json)

s3Bucket = input_config_json['s3Bucket']
s3Prefix = input_config_json['s3Prefix']
images_json = []
for image_name, image_id in clean_image_names_ids:
    image_json = {}
    image_json['s3Bucket'] = s3Bucket
    image_json['s3Key'] = "{}/{}".format(s3Prefix, image_name)
    image_json['objectID'] = image_id
    images_json.append(image_json)

output_json = input_config_json
output_json['images'] = images_json

output_json_data = json.dumps(output_json, indent=2)
# print(output_json_data)

with open(args.output_file, "w") as output_file:
    output_file.write(output_json_data)