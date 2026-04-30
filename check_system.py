#!/usr/bin/env python3
"""
System Check Script - Verify all dependencies and setup
"""

import sys
import os

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("⚠️  WARNING: Python 3.7+ is recommended")
        return False
    print("✓ Python version OK")
    return True


def check_packages():
    """Check required packages"""
    packages = {
        'cv2': 'opencv-python',
        'numpy': 'numpy',
        'PIL': 'pillow',
        'sklearn': 'scikit-learn',
        'keras': 'keras',
        'tensorflow': 'tensorflow'
    }
    
    print("\nChecking packages:")
    all_ok = True
    for import_name, package_name in packages.items():
        try:
            __import__(import_name)
            print(f"  ✓ {package_name}")
        except ImportError:
            print(f"  ✗ {package_name} NOT INSTALLED")
            all_ok = False
    
    if not all_ok:
        print("\nInstall missing packages with:")
        print("  pip install -r MiAI_Hand_Lang/setup.txt")
    
    return all_ok


def check_model():
    """Check if model exists"""
    print("\nChecking model files:")
    model_paths = [
        'models/saved_model.keras',
        'MiAI_Hand_Lang/models/saved_model.keras'
    ]
    
    for path in model_paths:
        if os.path.exists(path):
            size_mb = os.path.getsize(path) / (1024 * 1024)
            print(f"  ✓ Found: {path} ({size_mb:.1f} MB)")
            return True
    
    print("  ⚠️  No trained model found")
    print("  Run: python main.py -> Option 1 (Train Model)")
    return False


def check_camera():
    """Check if camera is accessible"""
    print("\nChecking camera:")
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print("  ✓ Camera accessible")
            cap.release()
            return True
        else:
            print("  ✗ Camera not available")
            return False
    except Exception as e:
        print(f"  ✗ Error accessing camera: {e}")
        return False


def check_data():
    """Check training data"""
    print("\nChecking training data:")
    data_path = 'MiAI_Hand_Lang/data'
    if os.path.isdir(data_path):
        files = []
        for root, dirs, filenames in os.walk(data_path):
            files.extend(filenames)
        print(f"  ✓ Data folder found ({len(files)} files)")
        return True
    else:
        print(f"  ⚠️  Data folder not found: {data_path}")
        return False


def main():
    print("\n" + "="*60)
    print("  MiAI Hand Language - System Check")
    print("="*60 + "\n")
    
    results = []
    
    # Run all checks
    results.append(("Python Version", check_python_version()))
    results.append(("Packages", check_packages()))
    results.append(("Camera", check_camera()))
    results.append(("Model", check_model()))
    results.append(("Training Data", check_data()))
    
    # Summary
    print("\n" + "="*60)
    print("  Summary")
    print("="*60)
    
    for check_name, result in results:
        status = "✓ OK" if result else "⚠️  ISSUE"
        print(f"{check_name:.<30} {status}")
    
    # Recommendations
    print("\n" + "="*60)
    print("  Next Steps")
    print("="*60)
    
    if results[0][1] and results[1][1]:
        if results[2][1]:  # Camera OK
            if results[2][1]:  # Model OK
                print("\n✓ System ready! Run:")
                print("  python main.py")
                print("  (Select option 2: Run Demo)")
            else:
                print("\n⚠️  System setup incomplete. Need:")
                print("  1. Train a model: python main.py -> Option 1")
        else:
            print("\n⚠️  Camera not detected. Make sure:")
            print("  - Webcam is connected")
            print("  - No other app is using the camera")
            print("  - Camera permissions are granted")
    else:
        print("\n✗ System not ready. Install:")
        print("  pip install -r MiAI_Hand_Lang/setup.txt")
    
    print("\n" + "="*60 + "\n")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
