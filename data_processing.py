import os
import xml.etree.ElementTree as ET

def convert_annotation(annotation_path, txt_path, class_list):
    tree = ET.parse(annotation_path)
    root = tree.getroot()

    with open(txt_path, "w") as f:
        for obj in root.findall('object'):
            cls = obj.find('name').text
            if cls not in class_list:
                continue
            xmin = int(obj.find('bndbox').find('xmin').text)
            ymin = int(obj.find('bndbox').find('ymin').text)
            xmax = int(obj.find('bndbox').find('xmax').text)
            ymax = int(obj.find('bndbox').find('ymax').text)
            width = xmax - xmin
            height = ymax - ymin
            f.write(f"{class_list.index(cls)} {xmin} {ymin} {width} {height}\n")

def main(input_dir, output_dir, class_list):
    os.makedirs(output_dir, exist_ok=True)
    for file in os.listdir(input_dir):
        annotation_path = os.path.join(input_dir, file)
        txt_path = os.path.join(output_dir, file.replace('.xml', '.txt'))
        convert_annotation(annotation_path, txt_path, class_list)

if __name__ == '__main__':
    # TODO: Change these values to match your directory structure and class names
    input_dir = 'data/annotations'
    output_dir = 'data/labels'
    class_list = ['RBC', 'Platelets', 'WBC']
    main(input_dir, output_dir, class_list)