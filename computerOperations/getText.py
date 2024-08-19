from PIL import Image
import pytesseract
import pyautogui

def takeScreenAndGetText(region=(0,0,1920,1080)):
    # Take a screenshot
    screenshot = pyautogui.screenshot(region=region)
    # If needed, specify the Tesseract-OCR installation path
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    screenshot.save("screenshot.png")

    # Open an image file
    image = Image.open('screenshot.png')

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(text)

takeScreenAndGetText()