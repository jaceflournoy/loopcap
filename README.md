# Screenshot to PDF Converter

This script captures a series of screenshots of a selected area on the screen, and then has the option to convert the screenshots into a PDF document.

## Prerequisites

Before you can use this script, you need to install the following dependencies:

- [pyscreenshot](https://pypi.org/project/pyscreenshot/)
- [pynput](https://pypi.org/project/pynput/)
- [img2pdf](https://pypi.org/project/img2pdf/)

To install these dependencies, run the following command:
```pip install pyscreenshot pynput img2pdf```

## Using the script

To use the script, follow these steps:

1. Run the script using Python 3.
2. Click on the top-left corner of the area you want to capture.
3. Click on the bottom-right corner of the area you want to capture.
4. Click on the location of the button that advances to the next slide.
5. Enter the total number of slides you want to capture.
6. Enter the name of the directory where you want to save the screenshots.
7. Wait for the countdown to complete, and then click on the button that advances to the next slide to begin the capture session.
8. When the capture session is complete, the script will prompt you to decide whether to generate a PDF document from the screenshots. If you choose to do so, enter a file name for the PDF and the script will create the PDF.

## Tips

- Make sure that the button that advances to the next slide is visible and not covered by any other windows when you start the capture session.
- If you are capturing slides from a presentation, it might be helpful to enable presenter view so that the button that advances to the next slide is always visible.
- You can adjust the delay between captures by modifying the `time.sleep` call in the script.
