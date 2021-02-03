# **Traffic Sign Recognition** 

## Writeup

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/visualization.jpg "Visualization"
[image2]: ./examples/grayscale.jpg "Grayscaling"
[image3]: ./examples/random_noise.jpg "Random Noise"
[image4]: ./examples/placeholder.png "Traffic Sign 1"
[image5]: ./examples/placeholder.png "Traffic Sign 2"
[image6]: ./examples/placeholder.png "Traffic Sign 3"
[image7]: ./examples/placeholder.png "Traffic Sign 4"
[image8]: ./examples/placeholder.png "Traffic Sign 5"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one. You can submit your writeup as markdown or pdf. You can use this template as a guide for writing the report. The submission includes the project code.

You're reading it! and here is a link to my [project code](https://github.com/bob800530/CarND-Traffic-Sign-Classifier-Project/blob/master/Traffic_Sign_Classifier.ipynb)

### Data Set Summary & Exploration

#### 1. Provide a basic summary of the data set. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

I used the numpy library to calculate summary statistics of the traffic
signs data set:

* The size of training set is ? Number of training examples = 34799
* The size of the validation set is ? Number of validation examples = 4410
* The size of test set is ? Number of testing examples = 12630
* The shape of a traffic sign image is ? Image data shape = (32, 32, 3)
* The number of unique classes/labels in the data set is ? Number of classes = 43

#### 2. Include an exploratory visualization of the dataset.

Here is an exploratory visualization of the data set. It is a bar chart showing how the data ...

[image1](https://github.com/bob800530/CarND-Traffic-Sign-Classifier-Project/blob/master/plots/bar_chart.png)

### Design and Test a Model Architecture

#### 1. Describe how you preprocessed the image data. What techniques were chosen and why did you choose these techniques? Consider including images showing the output of each preprocessing technique. Pre-processing refers to techniques such as converting to grayscale, normalization, etc. (OPTIONAL: As described in the "Stand Out Suggestions" part of the rubric, if you generated additional data for training, describe why you decided to generate additional data, how you generated the data, and provide example images of the additional data. Then describe the characteristics of the augmented training set like number of images in the set, number of images for each class, etc.)

As a first step, I decided to convert the images to grayscale because ...

Here is an example of a traffic sign image before and after grayscaling.

[image2](https://github.com/bob800530/CarND-Traffic-Sign-Classifier-Project/blob/master/plots/original_image.png)
[image3](https://github.com/bob800530/CarND-Traffic-Sign-Classifier-Project/blob/master/plots/grayscale_image.png)

As a last step, I normalized the image data because 

Normalization can reduce the effect of offset. For example, image captured in night would be darker than day time. 

So offset of image captured day time would be much higher than night.


#### 2. Describe what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

My final model consisted of the following layers:

| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| Input = 32x32x3.    							| 
| Convolution 5x5     	| 1x1 stride, Valid padding, outputs 28x28x6 	|
| RELU					| Activation												|
| Max pooling	      	| 2x2 stride,  outputs 14x14x6 				|
| Convolution 5x5	    | 1x1 stride, Valid padding, outputs 10x10x16      									|
| RELU		| Activation        									|
| Max pooling				| 2x2 stride,  outputs 5x5x16        									|
| Flatten						|Input = 5x5x16. Output = 400.												|
| Fully Connected.						|Input = 400. Output = 120.												|
| RELU						|Activation												|
| Dropout						|Activation												| 
| Fully Connected						|Input = 120. Output = 84.												|
| RELU						|Activation												|
| Dropout						|Activation												| 
| Fully Connected						|Input = 84. Output = 10.												|



#### 3. Describe how you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

To train the model, I used an Lenet algorithm mentioned in courses.
EPOCHS = 50
BATCH_SIZE = 128
rate = 0.001

#### 4. Describe the approach taken for finding a solution and getting the validation set accuracy to be at least 0.93. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

My final model results were:
* training set accuracy of ? 99.3%
* validation set accuracy of ? 95.5%
* test set accuracy of ? 94.2%

If a well known architecture was chosen:
* What architecture was chosen? Lenet architecture
* Why did you believe it would be relevant to the traffic sign application? It's first layer is 32x32x1, the same as my image's size.
* How does the final model's accuracy on the training, validation and test set provide evidence that the model is working well? High accurancy
 

### Test a Model on New Images

#### 1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are five German traffic signs that I found on the web:

[image4](https://github.com/bob800530/CarND-Traffic-Sign-Classifier-Project/blob/master/sign_images/1_Speed limit 60kmh)
[image5](https://github.com/bob800530/CarND-Traffic-Sign-Classifier-Project/blob/master/sign_images/2_Priority road) 
[image6](https://github.com/bob800530/CarND-Traffic-Sign-Classifier-Project/blob/master/sign_images/3_Stop) 
[image7](https://github.com/bob800530/CarND-Traffic-Sign-Classifier-Project/blob/master/sign_images/4_Turn right ahead)  
[image8](https://github.com/bob800530/CarND-Traffic-Sign-Classifier-Project/blob/master/sign_images/5_Roundabout mandatory) 

#### 2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

Here are the results of the prediction:

| Image			        |     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| Speed limit 60kmh      		| Speed limit 60kmh   									| 
| Priority road     			| Priority road 										|
| Stop					| Stop											|
| Turn right ahead	      		| Turn right ahead					 				|
| Roundabout mandatory			| Roundabout mandatory      							|


The model was able to correctly guess 5 of the 5 traffic signs, which gives an accuracy of 100%. 

#### 3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

The code for making predictions on my final model is located in the 11th cell of the Ipython notebook.

For the first image, the model is relatively sure that this is a stop sign (probability of 1.0), and the image does contain a stop sign. The top five soft max probabilities were

| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 1.00000000e+00			| Stop sign									| 
| 1.02689569e-12    				| Speed limit (80km/h) 										|
| 1.09374453e-15					| Speed limit (50km/h)											|
| 6.22115508e-18	      			| No vehicles					 				|
| 4.62154306e-20				    | Stop							|

For the second image ... 
| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 1.00000000e+00			| Priority road									| 
| 9.03371893e-26   				| Yield										|
| 9.49778130e-27					| Roundabout mandatory											|
| 2.78607066e-36	      			| Speed limit (100km/h)					 				|
| 8.22653115e-38				    | End of no passing by vehicles over 3.5 metric tons      							|

For the 3rd image ... 
| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 9.99999881e-01			|Stop									| 
| 9.55401447e-08   				|Speed limit (80km/h)										|
| 7.70135884e-08					|Speed limit (70km/h)											|
| 9.86797133e-09	      			|Speed limit (60km/h)					 				|
| 7.53576224e-09				    |Keep right							|

For the 4th image ... 
| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 9.99999881e-01			|Turn right ahead									| 
| 7.94856945e-08   				|Ahead only										|
| 1.15257857e-08					|Keep left											|
| 3.64971897e-09	      			|No vehicles					 				|
| 3.34919581e-09				    |Stop							|

For the 5th image ... 
| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 9.94439363e-01			|Roundabout mandatory									| 
| 3.58139514e-03   				|Speed limit (20km/h)										|
| 1.95297506e-03					|Go straight or left											|
| 1.88130907e-05	      			|Right-of-way at the next intersection					 				|
| 5.18936304e-06				    |Speed limit (100km/h) 							|

### (Optional) Visualizing the Neural Network (See Step 4 of the Ipython notebook for more details)
#### 1. Discuss the visual output of your trained network's feature maps. What characteristics did the neural network use to make classifications?


