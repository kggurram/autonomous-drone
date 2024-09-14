# Line Detection with TensorFlow and OpenCV

This project implements a machine learning pipeline for detecting lines in images using TensorFlow and OpenCV. The core functionality includes training a model to detect lines in images and performing image processing tasks to visualize the results. The project leverages TensorFlow for model training and OpenCV for image manipulation and line detection.

## Features

- **Model Training**: A TensorFlow-based model is trained to detect lines from image data. The model architecture is loaded and saved using `Keras`.
- **Image Processing**: Images are pre-processed and post-processed using OpenCV to highlight detected lines.
- **Model Deployment**: Line detection can be run on new images with an inference script, demonstrating how the trained model generalizes to unseen data.
- **Python Integration**: Scripts for training (`train.py`), model inference (`play.py`, `test.py`), and data handling (`gather_images.py`) are included to ensure an end-to-end workflow.

## Technologies

- **TensorFlow**: For deep learning model training, utilizing `tensorflow-macos` and `tensorflow-metal` for hardware acceleration on Apple Silicon.
- **OpenCV**: For image processing and visualization tasks.
- **Keras**: Simplifies model creation and data handling, used for defining and training the model.
- **Scikit-learn**: Applied for model evaluation and performance metrics.
- **NumPy**: Utilized for efficient numerical operations and tensor manipulation.
- **Python**: General purpose programming language used for scripting the entire project pipeline.

## Installation

### Dependencies

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or use the additional `req2.txt` file for a similar environment setup:

```bash
pip install -r req2.txt
```

### Key Libraries:

- **TensorFlow 1.13.1** for deep learning capabilities.
- **OpenCV 4.1.0.25** for image processing.
- **Keras 2.1.1** for model definition and training.
- Other utilities like `numpy`, `scikit-learn`, `grpcio`, etc.

## How to Use

### Training the Model

To train the model, ensure that you have a dataset of images. You can use the provided `train.py` script to begin training:

```bash
python train.py
```

This script will train the model and save the weights in the `linedetect-model.h5` file.

### Running Inference

Once the model is trained, you can use `play.py` or `test.py` to detect lines in new images. For example:

```bash
python play.py --image path_to_image.jpg
```

This will load the trained model and process the given image for line detection.

## Model Structure

The model used for line detection is a custom convolutional neural network (CNN) that is built and trained using Keras. The architecture consists of convolutional layers followed by fully connected layers designed to identify straight lines in image data.

## File Overview

- `train.py`: Script for training the line detection model.
- `gather_images.py`: Script to gather and process images for the training dataset.
- `play.py`: Script to run inference on new images using the trained model.
- `test.py`: Another inference script for model testing.
- `linedetect-model.h5`: Pre-trained model file for line detection.
- `requirements.txt`: Lists the exact versions of dependencies used for the project.
- `req2.txt`: Alternative list of dependencies for the project.

## Acknowledgements

This project was developed using TensorFlow's Keras API for ease of experimentation and model deployment, combined with OpenCV for robust image processing.
