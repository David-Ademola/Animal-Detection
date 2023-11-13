# Animal Detection with YOLOv8

This project utilizes YOLOv8 for real-time animal detection. It supports the detection of multiple animal classes, including chickens, cows, goats, pigs, and sheep. The application allows you to choose the specific animal class you want to detect.

## Requirements

- Python 3.x
- OpenCV
- Ultralytics
- Supervision

Install the required dependencies using:

```pip install opencv-python ultralytics supervision```

## Usage

### Run the main script:

- To run from live webcam, run ```python main.py --video_resolution <width of your webcam, height of your webcam>```
- To run it on a video, run ```python main.py --video_path <path to your video>```

### Enter the type of animal you want to detect when prompted.

## Configuration

- The YOLOv8 weights file (`best.pt`) is required for the model. Ensure it is available in the project directory.

## Customization

To extend or customize the project, you can create additional animal classes by inheriting from the `Animal` base class. Each animal class should implement the `main` method, specifying the class index for the desired animal.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- YOLOv8: [Link to YOLOv8 repository](https://github.com/ultralytics/yolov8)
- Supervision: [Link to Supervision library](https://github.com/oughtinc/supervision)

## Author

[Ademola David]

Feel free to contribute or report issues!
