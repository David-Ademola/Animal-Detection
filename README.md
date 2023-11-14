# Animal Detection with YOLOv8

This project uses YOLOv8 for real-time animal detection. It supports multiple animal classes, including chickens, cows, goats, pigs, and sheep. The application allows users to choose the type of animal they want to detect.

![cow](https://github.com/David-Ademola/Animal-Detection/assets/cow.jpg)

### Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- OpenCV
- Ultralytics YOLO library

You can install the required Python packages using the provided `requirements.txt` file:

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/David-Ademola/Animal-Detection.git
    cd Animal-Detection
    ```

2. Install dependencies:

    ```bash
    ⠀
    pip install -r requirements.txt
    ⠀
    ```

3. Run the application:

- To run from a live webcam:
    ```bash
    ⠀
    python main.py --video_resolution (resolution of your webcam)
    ⠀
    ```
- To run on a video:
  ```bash
  ⠀
  python main.py --video_path (path to your video)
  ⠀
  ```

Upon running `main.py`, you will be prompted to enter the type of animal you want to detect. Choose from the supported animals, and the application will start real-time detection using YOLOv8.

Press 'Esc' to exit the application.

## Supported Animals

- Chicken
- Cow
- Goat
- Pig
- Sheep

## Customization

You can customize the application by modifying the `count_and_track.py` file. Adjust the YOLOv8 weights, default zone polygon, and other parameters as needed.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub flow:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## Acknowledgments

- YOLOv8: [Link to YOLOv8 repository](https://github.com/ultralytics/yolov8)
- Supervision: [Link to Supervision library](https://github.com/roboflow/supervision)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Akinwande David Ademola

Feel free to contribute or report issues!
