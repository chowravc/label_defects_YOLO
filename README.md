# label_defects_YOLO
Pipeline to label defects on images with YOLO annotation format.

Start by dumping images into the images folder.
Next run the imageProcess.py file to darken these images.
Now go into the darkened_images folder and open each individual image with an application like paint and put a single white pixel at the defect location.
The Bounding box size is set to 11, 11, 12 but can be changed.
Run the createBounds.py file and your labels should also be generated. This will be the ground truth.