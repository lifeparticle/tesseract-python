from PIL import Image
import pytesseract

def process_image(iamge_name, lang_code):
	return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)

def print_data(data):
	print(data)

def output_file(filename, data):
	file = open(filename, "w+")
	file.write(data)
	file.close()

def main():
	data_eng = process_image("test_eng.png", "eng")
	data_ben = process_image("test_ben.png", "ben")
	print_data(data_eng)
	print_data(data_ben)
	output_file("eng.txt", data_eng)
	output_file("ben.txt", data_ben)

if  __name__ == '__main__':
	main()