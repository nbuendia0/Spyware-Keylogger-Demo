# Educational Spyware Demonstration

This repository contains a Python-based demonstration designed for cybersecurity education. The project showcases how spyware-like programs can collect and organize system information in a controlled, ethical, and fully permitted academic environment. It is intended to help users understand: 

- the technical concepts behind data collection, analysis, and defensive countermeasures.
- How information-gathering tools function at a basic level
- What types of data can be exposed on compromised systems
- How defensive tools detect and analyze suspicious activity
- The importance of system hardening and user awareness


### Platform Notes
- Windows: fully supported  
- Linux/macOS: may require additional permissions for certain features  
- Administrator privileges: not required for basic demonstration functions  

---

## Important Disclaimer ⚠️

This project is provided strictly for educational and research purposes.

- Do not deploy or run this software on systems you do not own.
- The code is not intended, designed, or optimized for malicious use.
- Users are fully responsible for following all applicable laws, institutional rules, and ethical guidelines.
- I assume no liability for misuse.

Use this only in controlled environments for legitimate cybersecurity learning.

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

## Project Structure

```
spyware-demo/
├── spyware_demo.py         # Main demonstration script
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
└── output/                 # Auto-generated output directory
    ├── keystrokes.txt      # Logged keystrokes
    ├── system_info.xlsx    # Collected system information
    └── screenshot.png      # Screenshot of display
```

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
   
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
   
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

## Example Output

### `keystrokes.txt`
```
[Key.shift] H e l l o [Key.space] W o r l d [Key.enter]
```

### `system_info.xlsx`
```
| Metric      | Value                |
|-------------|----------------------|
| Timestamp   | 2024-01-15 10:30:00  |
| IP Address  | 192.168.1.100        |
| Hostname    | DESKTOP-ABC123       |
| OS          | Windows              |
| Processor   | Intel(R) Core(TM)…   |
```

### `screenshot.png`
A full-screen PNG image showing the display at the end of the demonstration.

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

**Status: ✅Complete**

