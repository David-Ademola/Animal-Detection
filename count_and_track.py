import argparse
from pathlib import Path

import cv2
import numpy as np
import supervision as sv
from ultralytics import YOLO

# Path to the YOLOv8 weights file
WEIGHTS_PATH = "best.pt"


class Animal:
    """
    Base class for animal detection using YOLOv8.
    """

    def __init__(self) -> None:
        pass

    # Define a default zone polygon
    ZONE_POLYGON = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

    def parse_arguments(self) -> argparse.Namespace:
        """
        Parse command-line arguments for the YOLOv8 application.

        Returns:
            argparse.Namespace: Parsed arguments.
        """
        parser = argparse.ArgumentParser(description="YOLOv8 Live")
        parser.add_argument(
            "--video_resolution", default=[1280, 720], nargs=2, type=int
        )
        parser.add_argument("--video_path", default=None, type=Path)
        args = parser.parse_args()

        return args

    def setup_capture(self, args: argparse.Namespace) -> cv2.VideoCapture:
        """
        Set up the video capture from the webcam or video file

        Args:
            args (argparse.Namespace): Parsed command-line arguments.

        Returns:
            cv2.VideoCapture: Video capture object.
        """
        if args.video_path:
            capture = cv2.VideoCapture(str(args.video_path))
        else:
            frame_width, frame_height = args.video_resolution
            capture = cv2.VideoCapture(0)
            capture.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
            capture.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

        return capture

    def setup_model(self) -> YOLO:
        """
        Set up the YOLOv8 model.

        Returns:
            YOLO: YOLOv8 model.
        """
        return YOLO(WEIGHTS_PATH)

    def setup_zone_annotator(self, args: argparse.Namespace) -> sv.PolygonZoneAnnotator:
        """
        Set up the zone annotator for annotation overlay.

        Args:
            args (argparse.Namespace): Parsed command-line arguments.

        Returns:
            sv.PolygonZoneAnnotator: Zone annotator object.
        """
        zone_polygon = (self.ZONE_POLYGON * np.array(args.video_resolution)).astype(int)
        zone = sv.PolygonZone(
            polygon=zone_polygon, frame_resolution_wh=tuple(args.video_resolution)
        )
        return sv.PolygonZoneAnnotator(
            zone=zone,
            color=sv.Color.white(),
            thickness=1,
            text_scale=2,
            text_thickness=2,
        )

    def process_frame(self, frame, model, class_index) -> None:
        """
        Process a frame for object detection.

        Args:
            frame: Input frame.
            model: YOLOv8 model.
            class_index (int): Index of the class to detect.

        Returns:
            None
        """
        # Run YOLOv8 on the frame
        result = model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_yolov8(result)
        detections = detections[detections.class_id == class_index]

        # Format labels for detected objects
        labels = [
            f"{model.model.names[class_id]} {confidence:.2f}"
            for _, _, confidence, class_id, _ in detections
        ]

        # Annotate the frame with bounding boxes and labels
        box_annotator = sv.BoxAnnotator()
        frame = box_annotator.annotate(
            scene=frame, detections=detections, labels=labels
        )

        return frame, detections

    def run(self, class_index: int) -> None:
        """
        Run the animal detection application.

        Args:
            class_index (int): Index of the class to detect.

        Returns:
            None
        """
        args = self.parse_arguments()
        capture = self.setup_capture(args)
        model = self.setup_model()
        zone_annotator = self.setup_zone_annotator(args)

        while True:
            _, frame = capture.read()
            frame, detections = self.process_frame(frame, model, class_index)

            # Trigger the zone based on detections and annotate the frame
            zone_annotator.zone.trigger(detections=detections)
            frame = zone_annotator.annotate(scene=frame)

            # Display the annotated frame
            cv2.imshow("Animal Detection", frame)

            # Exit the loop if the 'Esc' key is pressed
            if cv2.waitKey(30) == 27:
                break

        # Release the video capture object and close the OpenCV windows
        capture.release()
        cv2.destroyAllWindows()


class Chicken(Animal):
    """
    Class for chicken detection
    """

    def __init__(self) -> None:
        pass

    def main(self, class_index: int = 0) -> None:
        super().run(class_index)


class Cow(Animal):
    """
    Class for cow detection.
    """

    def __init__(self) -> None:
        pass

    def main(self, class_index: int = 1) -> None:
        super().run(class_index)


class Goat(Animal):
    """
    Class for goat detection.
    """

    def __init__(self) -> None:
        pass

    def main(self, class_index: int = 2) -> None:
        super().run(class_index)


class Pig(Animal):
    """
    Class for pig detection.
    """

    def __init__(self) -> None:
        pass

    def main(self, class_index: int = 3) -> None:
        super().run(class_index)


class Sheep(Animal):
    """
    Class for sheep detection
    """

    def __init__(self) -> None:
        pass

    def main(self, class_index: int = 4) -> None:
        super().run(class_index)
