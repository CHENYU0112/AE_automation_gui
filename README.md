AE_automation_gui
Description
AE_automation_gui is a graphical user interface application for automating Power over Line (PoL) testing. It provides an interface for setting up and running efficiency and transient tests on electronic components.
Features

Graphical user interface for test configuration
Support for efficiency and transient testing
Integration with various test instruments
Real-time test progress and results display
Excel report generation

Installation
Prerequisites

Python 3.7 or higher
Virtual environment (recommended)

Setup Steps

Clone the repository:
Copygit clone https://github.com/your-username/AE_automation_gui.git
cd AE_automation_gui

Create and activate a virtual environment:
Copypython -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:
Copypip install -r requirements.txt


Usage

Preparation: Ensure all test instruments are properly connected to your computer.
Launch the application:
Copypython main.py

Main Window: The application will open with two main sections:

Setting Frame: For configuring test parameters
Testing Frame: For running tests and viewing results


Configuring Settings:

Select the IC to test
Choose the test type (Efficiency or Transient)
Configure power supply, DAQ, and load settings
Set protection parameters
Click the "Set" button to validate and apply the settings


Running Tests:

Select the appropriate test tab (Efficiency or Transient)
Click "Start Test" to begin the test
Monitor the test progress and view results in real-time


Viewing Results:

Check the test log and results in the GUI
Find the generated Excel report in the results folder



Troubleshooting
If you encounter issues:

Ensure all devices are properly connected and powered on
Check the console output for error messages or exceptions
Verify that the correct drivers for your test instruments are installed

Contributing
We welcome contributions to AE_automation_gui. Please follow these steps:

Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Make your changes
Commit your changes (git commit -am 'Add some feature')
Push to the branch (git push origin feature/your-feature)
Create a new Pull Request

License
[Insert your license information here]
Contact
For queries or support, please contact [Your Name] at [your.email@example.com].