input_file = '../image_text.txt'
output_image = 'images/image_file.png'

try:
    with open(input_file, 'rb') as inp_file:
        image_bytes = inp_file.read()

    with open(output_image, 'wb') as output_file:
        output_file.write(image_bytes)
    print("Image Created Successfully!!")
except Exception as e:
    print(e)

def image_generate(image_bytes, output_image):
    try:
        with open(output_image, 'wb') as output_file:
            output_file.write(image_bytes)
        print("Image Created Successfully!!")
    except Exception as e:
        print(e)