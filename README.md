# Face-Recognition

A programming for detecting a face or multiple faces from either an image or real time cam through the PC.

This program is written in PYTHON and uses openCV mostly for capturing images.

It also uses an algorithm know as Haar Cascade to feed the data into software.

Haar Cascade is an algorithm of chain of machine learning events that looks at every square of image and passes each of those squares through the machine learning process and cascades it down.

This algorithm uses Haar Features (rudimentary building blocks) such as edge features, line features, and four-rectangle features to determine if each square corresponds to any of Haar features. When we chain these blocks ogether over and over, it will form a combination of layers that look like a shape of face, which is then used to detect face. It will try every Haar Feature of every type, size, and location to find which feature matches.

It is important to note that color is irrelevant in this algorithm because haar features are consisted of dark sides and bright sides, and this algorithm looks at the brightness of an image by comparing each square of image to blocks.

Before we apply this algorithm, we first need to convert images into greyscale so that we can compare brightness of an image.

Once images are converted into greyscale, we run the Haar Cascade on an image to detect a face.

This is possible because OpenCV provides a pre-trained classifier that has the chain of haar features that best match a frontal face, and we only need to pass a sliding window of the image into the classifier to detect a face.
