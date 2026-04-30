================================================================================
   MiAI HAND LANGUAGE - HAND GESTURE RECOGNITION SYSTEM
   Hệ thống nhận diện ký hiệu tay cho người khuyết tật
================================================================================

PROJECT OVERVIEW:
================================================================================
This project is a hand gesture recognition system that can identify sign language
gestures in real-time using a webcam and a trained neural network model.

Supported Gestures (5 classes):
  - E: Yes/OK gesture
  - L: Love gesture
  - F: Peace/Victory gesture
  - V: Victory/Peace gesture
  - B: Fist gesture

================================================================================
QUICK START GUIDE:
================================================================================

1. INSTALLATION
   Prerequisites: Python 3.7+, pip

   Install dependencies:
   $ pip install -r MiAI_Hand_Lang/setup.txt
   
   Or manually:
   $ pip install opencv-python keras tensorflow pillow scikit-learn

2. TRAIN MODEL (if needed)
   $ python main.py
   Select option 1 (Train Model)
   
   Note: This requires training data in MiAI_Hand_Lang/data/ folder
   organized as:
   data/
     L_*/  (Love gesture images)
     fi*/  (Fist gesture images)
     ok*/  (OK gesture images)
     pe*/  (Peace gesture images)
     pa*/  (... other gesture images)

3. RUN DEMO (Recommended)
   $ python main.py
   Select option 2 (Run Demo)
   
   OR directly:
   $ python MiAI_Hand_Lang/demo.py

4. CONTROLS IN DEMO:
   - 'b' = Capture background (do this first!)
   - 'r' = Reset background
   - 'q' = Quit

================================================================================
USAGE INSTRUCTIONS:
================================================================================

When you run the demo:

1. The camera window shows:
   - Green rectangle: Detection region (right half of screen)
   - Red text: Status and help messages
   - Green text: Recognized gesture and confidence score

2. Steps to recognize:
   a) Press 'b' to capture the background (background without hand)
   b) Wait for "Background captured" message
   c) Place your hand in the green detection box
   d) The system will recognize the gesture in real-time
   e) Press 'q' to quit

3. Tips for better recognition:
   - Good lighting is important
   - Place hand clearly in detection region
   - Move hand slowly for consistent detection
   - Confidence must be > 70% for recognition

================================================================================
FILE STRUCTURE:
================================================================================

Hand_land/
├── main.py                          # Main entry point menu
├── MiAI_Hand_Lang/
│   ├── demo.py                      # Main demo script (RECOMMENDED)
│   ├── detection.py                 # Alternative detection script
│   ├── train_model.py               # Model training script
│   ├── setup.txt                    # Dependencies list
│   ├── models/
│   │   └── saved_model.keras        # Trained model (main)
│   ├── data/                        # Training data (if available)
│   └── README.md                    # Project info
├── models/
│   └── saved_model.keras            # Copy of trained model

================================================================================
TROUBLESHOOTING:
================================================================================

Q: "ERROR: Could not load any model file!"
A: Model file not found. Ensure MiAI_Hand_Lang/models/saved_model.keras exists.
   If not, train the model first using option 1.

Q: Camera window shows "BG: NOT CAPTURED"
A: Press 'b' to capture background first. The system needs to learn the
   background before recognizing hand gestures.

Q: Gestures not being recognized
A: 
   - Check lighting conditions
   - Make sure background is captured
   - Keep hand clearly in the green detection box
   - Move hand slower and more deliberately
   - The confidence threshold is 70% - try clearer gestures

Q: Camera not opening
A: 
   - Check if webcam is connected
   - Ensure no other app is using the camera
   - Try restarting the application
   - On Linux/Mac, you may need to grant camera permissions

================================================================================
TECHNICAL DETAILS:
================================================================================

Model Architecture:
  - Base: VGG16 (pre-trained on ImageNet)
  - Input: 224x224 RGB images
  - Output: 5 gesture classes
  - Framework: TensorFlow/Keras

Image Processing Pipeline:
  1. Bilateral filter (smoothing)
  2. Horizontal flip
  3. Grayscale conversion
  4. Gaussian blur
  5. Threshold (binary)
  6. Background subtraction
  7. ROI extraction
  8. Resize to 224x224

Recognition Process:
  1. Capture background once
  2. Remove background from live frames
  3. Extract hand region of interest (ROI)
  4. Convert to threshold image
  5. Normalize and resize
  6. Feed to trained model
  7. Get probability scores
  8. Display result if confidence > threshold

================================================================================
IMPROVEMENTS MADE:
================================================================================

✓ Fixed model loading with multiple path fallbacks
✓ Added comprehensive error handling
✓ Created intuitive demo.py with better UI
✓ Added info panel showing status and controls
✓ Improved detection region visualization
✓ Better frame processing and validation
✓ Consistent model file naming
✓ Added help text and instructions
✓ Fixed undefined variable issues
✓ Added documentation and comments
✓ Created main menu system

================================================================================
CREDITS:
================================================================================

Original Project: MiAI Hand Language
Link: http://ainoodle.tech/2019/09/30/

Technology Stack:
- OpenCV: Computer vision library
- TensorFlow/Keras: Deep learning framework
- NumPy: Numerical computing
- PIL: Image processing

================================================================================
NOTES:
================================================================================

- This system works best with clear, well-lit conditions
- Background should be simple and consistent
- Hand gestures should be within the green detection region
- The model achieves best results with consistent hand poses
- Real-time performance depends on system resources

For questions or improvements, refer to the project documentation.

================================================================================
Last Updated: 2026-04-30
Version: 2.0 (Improved & Fixed)
================================================================================
