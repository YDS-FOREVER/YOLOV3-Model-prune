HAND Dataset
==== =======
A. Mittal, A. Zisserman and  P. H. S. Torr


Introduction
------------
We introduce a comprehensive dataset of hand images collected from various different public image data set sources as listed in [1]. A total of 13050 hand instances are annotated. Hand instances larger than a fixed area of bounding box (1500 sq. pixels) are considered 'big' enough for detections and are used for evaluation. This gives around 4170 high quality hand instances. While collecting the data, no restriction was imposed on the pose or visibility of people, nor was any constraint imposed on the environment.
In each image, all the hands that can be perceived clearly by humans are annotated. The annotations consist of a bounding rectangle, which does not have to be axis aligned, oriented with respect to the wrist. Please cite [1] if you use this dataset.


Contents
--------
This package contains:
- Training dataset (all the images with hand bounding-box annotations).
- Code to visualize annotations.
- Code to give statistics of data in the dataset.

Let PWD be the directory of the hand-dataset, then the structure of the containts is as follows:

PWD/training_data: Directory containing training data.

PWD/training_data/images: Directory containing training data images.

PWD/training_data/annotations: Annotations files for the training dataset.

counttraindata.m: Matlab function giving training data statistics.
displaydata.m :  Matlab function to visualize annotations over images.


Description of the annotation files
----------- -- --- ---------- -----
The annotation files are in standard matlab '.mat' format which contain annotations for the four end-points of the hand bounding box.
It has a structure 'boxes' having hand-boxes as different indices of cell array. Please refer to the visualization function (displaydata.m) for more clearification.


Evaluation Criteria
---------- --------
The performance is evaluated using average precision (AP) (the area under the Precision Recall curve). A hand detection is considered true or false according to its overlap with the ground-truth bounding box. 
A box is positive if the overlap score is more than 0.5. The overlap ratio is computed between the axis-aligned bounding rectangles around the ground-truth and the detected hand bounding box.


Support
-------
For any query/suggestions, please drop an email to the following addresses:
arpit@robots.ox.ac.uk
az@robots.ox.ac.uk
philiptorr@brookes.ac.uk


References
----------
[1] Hand detection using multiple proposals
A. Mittal, A. Zisserman, P.H.S. Torr
Proceedings of British Machine Vision Conference, 2011.