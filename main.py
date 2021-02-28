from PIL import Image
import pytesseract

def processImage(iamge_name, lang_code):
	return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)

def printData(data):
	print(data)

def output_file(filename, data):
	file = open(filename, "w+")
	file.write(data)
	file.close()

def main():
	data_eng = processImage("test_eng.png", "eng")
	data_ben = processImage("test_ben.png", "ben")
	printData(data_eng)
	printData(data_ben)
	output_file("eng.txt", data_eng)
	output_file("ben.txt", data_ben)

if  __name__ == '__main__':
	main()