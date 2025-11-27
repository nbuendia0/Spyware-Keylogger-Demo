# Educational Spyware Demonstration

This repository contains a Python-based demonstration designed for cybersecurity education.  
The project showcases how spyware-like programs can collect and organize system information in a controlled, ethical, and fully permitted academic environment.  
It is intended to help students understand the technical concepts behind data collection, analysis, and defensive countermeasures.

---

## Important Disclaimer

This project is provided strictly for educational and research purposes.

- I will not deploy or run this software on systems I do not own.
- I have explicit permission from my academic institution to develop and study this material.
- The code is not intended, designed, or optimized for malicious use.
- Users are fully responsible for following all applicable laws, institutional rules, and ethical guidelines.
- The author assumes no liability for misuse.

Use this only in controlled environments for legitimate cybersecurity learning.

---

## Project Overview

This demonstration models several data-gathering mechanisms commonly discussed in malware and spyware research.  
The purpose is to give cybersecurity students hands-on exposure to:

- How information-gathering tools function at a basic level
- What types of data can be exposed on compromised systems
- How defensive tools detect and analyze suspicious activity
- The importance of system hardening and user awareness

This project does **not** include persistence, evasion, or network exfiltration features, keeping it aligned with academic safety practices.

---

## Project Structure

```
spyware-demo/
├── spyware_demo.py         # Main demonstration script
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
└── output/                 # Auto-generated output directory
    ├── keystrokes.txt      # Logged keystrokes (demo)
    ├── system_info.xlsx    # Collected system information
    └── screenshot.png      # Screenshot of display
```

---

## File Descriptions

### `spyware_demo.py`
The core Python script containing the demonstration class.  
It manages:

- System information collection  
- Timed keystroke recording  
- Screenshot capture  
- Automatic output directory creation  
- File organization and timestamped saving  

### `requirements.txt`
Lists Python packages used by the demonstration.  
Install them using:

```
pip install -r requirements.txt
```

### `output/`
A folder automatically generated during runtime that stores all collected demonstration data.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher  
- `pip` package manager  
- A local environment you fully control  

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd spyware-demo
   ```

2. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate          # Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Platform Notes
- Windows: fully supported  
- Linux/macOS: may require additional permissions for certain features  
- Administrator privileges: not required for basic demonstration functions  

---

## Running the Demonstration

1. Start the program:
   ```
   python spyware_demo.py
   ```

2. Read the disclaimer that appears on launch.  
   You must type `yes` to continue.

3. The demonstration performs the following (in sequence):
   - Collects system information  
   - Records keystrokes (press `ESC` to stop early)  
   - Captures a screenshot  
   - Saves all data into the `output/` directory  

---

## Features Demonstrated

### 1. System Information Collection
- IP address  
- Hostname  
- Operating system details  
- Processor architecture  
- Timestamped metadata  
- Exported to `system_info.xlsx`

### 2. Keystroke Recording
- Captures user keystrokes in real-time  
- Logs both character keys and special keys  
- Saves results to `keystrokes.txt`  
- Recording ends automatically after the configured timer or by pressing `ESC`

### 3. Screenshot Capture
- Full-screen PNG image  
- Saved as `screenshot.png`  
- Timestamped naming for organization  

---

## Example Output

### `keystrokes.txt`
```
[Key.shift] H e l l o [Key.space] W o r l d [Key.enter]
```

### `system_info.xlsx`
```
Metric        Value
Timestamp     2024-01-15 10:30:00
IP Address    192.168.1.100
Hostname      DESKTOP-ABC123
OS            Windows
```

### `screenshot.png`
A full-screen PNG image showing the display at the end of the demonstration.

---

## Educational Value

This project provides hands-on insight into:

- How data collection mechanisms function
- The impact of insecure systems on privacy
- Defensive monitoring and detection strategies
- Basic digital forensics and log interpretation
- Ethical considerations in cybersecurity research

It is an effective teaching tool for courses on system security, malware analysis, and digital forensics.

---

## Learning Extensions

Students may explore further by:

- Adding local log analysis features  
- Visualizing collected data with charts  
- Implementing safe detection mechanisms  
- Studying behavioral signatures  
- Creating defensive scripts for identifying suspicious activity  

All extensions should remain within ethical and legal guidelines.

---

## Legal and Ethical Notes

- Only operate this software on systems you own or have explicit permission to test.  
- Follow all institutional cybersecurity and research guidelines.  
- Use for academic learning, demonstrations, and controlled research only.  
- Never attempt unauthorized data collection.

---

## Contributing

Contributions that expand the educational and defensive value of this demonstration are welcome, including:

- Documentation improvements  
- Cross-platform enhancements  
- Additional safe, non-invasive learning modules  
- Detection and analysis tools

---

## License

This project is provided for educational purposes under academic fair use principles.

**Status: Complete**

