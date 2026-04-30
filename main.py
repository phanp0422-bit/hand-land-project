#!/usr/bin/env python3
"""
MiAI Hand Language - Main Entry Point
Hệ thống nhận diện ký hiệu tay cho người khuyết tật
"""

import sys
import os
from pathlib import Path

# Add MiAI_Hand_Lang to path
sys.path.insert(0, str(Path(__file__).parent / 'MiAI_Hand_Lang'))

def print_menu():
    print("\n" + "="*60)
    print("  MiAI Hand Language Recognition System")
    print("  Hệ thống nhận diện ký hiệu tay")
    print("="*60)
    print("\n  Menu Options:")
    print("  1. Train Model (train_model.py)")
    print("  2. Run Demo/Recognition (demo.py)")
    print("  3. Run Detection (detection.py)")
    print("  0. Exit")
    print("\n" + "="*60)


def check_data():
    """Check if training data exists"""
    data_path = Path('MiAI_Hand_Lang/data')
    if not data_path.exists():
        print("\n✗ WARNING: Training data folder not found!")
        print(f"  Expected: {data_path}")
        return False
    
    files = list(data_path.glob('*/*'))
    if not files:
        print("\n✗ WARNING: No training images found in data folder!")
        return False
    
    print(f"✓ Found {len(files)} training images")
    return True


def check_model():
    """Check if trained model exists"""
    model_paths = [
        'models/saved_model.keras',
        'MiAI_Hand_Lang/models/saved_model.keras'
    ]
    
    for path in model_paths:
        if os.path.exists(path):
            print(f"✓ Model found: {path}")
            return True
    
    print("\n✗ WARNING: No trained model found!")
    print("  Run option 1 (Train Model) first")
    return False


def main():
    print("\n" + "="*60)
    print("  MiAI Hand Language Recognition System")
    print("  Hệ thống nhận diện ký hiệu tay")
    print("="*60)
    
    while True:
        print_menu()
        choice = input("\nSelect option (0-3): ").strip()
        
        if choice == '1':
            print("\n" + "="*60)
            print("  OPTION 1: Train Model")
            print("="*60)
            
            if not check_data():
                print("\n  Cannot train without data!")
                continue
            
            print("\n  Starting training...")
            print("  This may take a while...\n")
            
            try:
                os.system('python MiAI_Hand_Lang/train_model.py')
            except Exception as e:
                print(f"\n✗ Error: {e}")
        
        elif choice == '2':
            print("\n" + "="*60)
            print("  OPTION 2: Run Demo")
            print("="*60)
            
            if not check_model():
                continue
            
            print("\n  Starting demo...")
            print("  Controls:")
            print("    'b' = Capture background")
            print("    'r' = Reset background")
            print("    'q' = Quit\n")
            
            try:
                os.system('python MiAI_Hand_Lang/demo.py')
            except Exception as e:
                print(f"\n✗ Error: {e}")
        
        elif choice == '3':
            print("\n" + "="*60)
            print("  OPTION 3: Run Detection")
            print("="*60)
            
            if not check_model():
                continue
            
            print("\n  Starting detection (legacy version)...")
            print("  Controls:")
            print("    'b' = Capture background")
            print("    'r' = Reset background")
            print("    'q' = Quit\n")
            
            try:
                os.system('python MiAI_Hand_Lang/detection.py')
            except Exception as e:
                print(f"\n✗ Error: {e}")
        
        elif choice == '0':
            print("\n✓ Goodbye!")
            sys.exit(0)
        
        else:
            print("\n✗ Invalid option! Please select 0-3")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✓ Program interrupted")
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()

