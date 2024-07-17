# AE_automation_gui

## Description

AE_automation_gui is a graphical user interface application for automating Power over Line (PoL) testing. It provides an interface for setting up and running efficiency and transient tests on electronic components.

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
2. **Create and activate a virtual environment:**
3. **Install the required packages:**


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

## Contributing

We welcome contributions to AE_automation_gui. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a new Pull Request

## License

[Insert your license information here]

## Contact

For queries or support, please contact [Your Name] at [your.email@example.com].