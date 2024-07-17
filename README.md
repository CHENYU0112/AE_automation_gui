# FFU_automation_gui

## Description

FFU_automation_gui is a graphical user interface application for setting up and running tests on the PoL Buck Converter.

## Features

- Support for multiple test types, including:
  - Efficiency testing
  - Transient testing
  - [New test types can be added here]
- Integration with various test instruments
- Real-time test progress and results display
- Excel report generation

## Installation

### Prerequisites

- Python 3.7 or higher
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository:**
2. **Install the required packages:** `pip install -r requirements.txt`

## Usage

### Launching the Application

1. Ensure all test instruments are properly connected to your computer.
2. Run the main application: `main.py`
   
### Configuring Settings

1. In the Setting Frame:
- Select the IC to test
- Choose the test type from the available options
- Configure test-specific parameters
2. Click the "Set" button to validate and apply the settings.

**Note:** Before running the GUI, you can set the default parameters in the `config.py` file.

### Running Tests

1. In the Testing Frame:
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

For queries or support, please contact:
- ChenYu Hsieh(ChenYu.Hsieh@infineon.com)
- MingYue Zhao(Mingyue.Zhao@infineon.com)
