# FFU_automation_gui

## Description

FFU_automation_gui is a graphical user interface application for automating Power over Line (PoL) testing. It provides an interface for setting up and running efficiency and transient tests on electronic components.

## Features

- Graphical user interface for test configuration
- Support for efficiency and transient testing
- Integration with various test instruments
- Real-time test progress and results display
- Excel report generation

## Installation

### Prerequisites

- Python 3.7 or higher
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository:**
3. **Install the required packages:** pip install -r requirements.txt


## Usage

### Launching the Application

1. Ensure all test instruments are properly connected to your computer.
2. Run the main application:

### Configuring Settings

1. In the Setting Frame:
- Select the IC to test
- Choose the test type (Efficiency or Transient)
- Configure power supply, DAQ, and load settings
- Set protection parameters
2. Click the "Set" button to validate and apply the settings.

### Running Tests

1. In the Testing Frame:
- Select the appropriate test tab (Efficiency or Transient)
- Click "Start Test" to begin the test
- Monitor the test progress and view results in real-time

### Viewing Results

- View the test log and results in the GUI
- Find the generated Excel report in the `results` folder

## Troubleshooting

If you encounter issues:
- Ensure all devices are properly connected and powered on
- Check the console output for error messages or exceptions
- Verify that the correct drivers for your test instruments are installed

## Contact

For queries or support, please contact ChenYu(ChenYu.Hsieh@infineon) and MingYue(Mingyue.Zhao@infineon.com)