import json

with open('C:\\Users\\momen\\Desktop\\json\\image1.txt', 'r') as txt_file:
    lines = txt_file.readlines()


json_data = {
    "annotations": [
        {
            "result": []
        }
    ]
}


for line in lines:
    values = line.strip().split()
    if len(values) == 5:
        x, y, width, height = map(float, values[1:])
        annotation = {
            "image_rotation": 0,
            "value": {
                "x": x ,
                "y": y ,
                "width": width ,
                "height": height,
                "rotation": 0,
                "rectanglelabels": ["object"]
            }
        }
        json_data["annotations"][0]["result"].append(annotation)



with open('image1.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
