# DCGAN

Authors : Ançay Rémi & Charbonnier Lucas

## Questions 1.1

❓ What makes this practical work experiment a self-supervised one?

*The fact that the data is not annotated. Instead, we create two models that "battle" against each other to force them to improve.*

## Questions 1.2

❓ Please look at the generator architecture.
How many time do we multiply by two the size of the input and what are the layers
responsible for this?

*We multiply twice and the layer responsible for this is this one :*
`layers.Conv2DTranspose(256, kernel_size=4, strides=2, padding='same', kernel_initializer=init)`

❓ What is the use of the Reshape layer in this code?

*The input is a vector of 7x7x256 elements. In order to use Convolutions on this data, we first need to reshape it to 7x7 images with 256 channels.*

## Questions 1.3

❓ Please look at the discriminator architecture, notices that it's a CNN classifier (between fake and real images).
If you where to classify RGB images of multiple animal classes (cats, dogs and ducks for example),
what would you need to change?

*We would need to change the output layer and have 3 output neurons (one for each class) with a softmax activation, instead of juste one neuron with a sigmoid activation. We would also need to change the input architecture to receive 3 channels 28x28 images instead of single channel 28x28 images.*

# DCGAN - outputs

## Questions 1.4

❓ Can you rely only on the loss of the generator and discriminator to choose the best model?
If no, provide a counter-example.

*No, the generator could learn to generate examples that happen to "fool" the discriminator really well without being a particularly good model.*

❓ In the third experiment we significatively reduced the number of parameters of the discriminator
compared to the other experiments. Did it helped the generator to produce better images? Why?

*The discriminator has similar results compared to the other experiments. However, the generator has a significantly lower loss compared to other experiments at around 0.75 (the loss is > 0.75 in all the other experiments).*

*Our hypothesis is that reducing the number of parameters of the discriminator made it simpler to "understand". Because of this, the generator was able to fool the discriminator more easily.*

❓ Compare experiments 1 and 6. Remember, They use the same number of filters
but have a different architecture.

*Experiment number 6 doesn't use the recommended architecture for GAN (batchnorm, strided convs, etc...). Therefore, the results are worse and much more unstable than those of the first experiment.*

❓ In experiment 5, we decrease the number of paramers of the generator. What was the impact?

*The generator starts with really bad results (loss of 6) and quickly goes down to a loss of ~1.5 but struggles to get any better. The loss is significantly higher than in the other experiments.*

# Pix2Pix colorization

## Questions 2.1

❓ We want to colorize grayscale images. Is there only one valid colorized output?

*No, there is no perfect answer. We can train the model by giving it greyed images and their "true" equivalent but the color of a grayscale image could be predicted in a number of different ways. For example, if we give a grayscale picture of the sky to the model, the "true" color could be blue, but it could also be orange if it's a sunset but the model has no way of knowing that, so predicting a blue sky is not necessarily right or wrong, it's one of the possible interpretations.*

## Questions 2.2

❓ Pix2Pix is a Conditional Adversarial Network, in the practical work with DCGAN we were using noise as input.
What is different in the input we have here?

*The goal of a pix2pix model is to produce variations of images. For example, we could give it a top view of the city and it could produce a map of the roads and streets, without the noise (color of the buildings, trees, etc...). Unlike an image generation model, the goal of pix2pix is not to produce random outputs. We want to obtain results specific to an image.*

*The way pix2pix works is by connecting the input layer directly to the output layer, in addition to the hidden layers (U-net architecture).*

❓ How does our colorization task relates to a problem where we would want to take photos as inputs
and make them look like paintings?
Please provide another task that would be related to these problems.

*It's similar in the sense that we want to augment a specific image. We don't want just any painting, we want the painting of one image in particular.*

*Another problem that could be resolved using pix2pix is if we want to generate a full image based on a simple drawing, for example. We can give a very simple sketch of the desired image as an input and the model will build an image based on that input.*

## Questions 2.3

❓ Why do you think the model predictions look like this?
In which way a Pix2Pix GAN would be useful to improve the results?

*All the predicted images have a "sepia" filter. This could be due to an overfitting of the model on those kind of pictures, or just not enough training data.*

*A Pix2pix GAN would probably solve the problem because GAN models consist of a generator and a discriminator. These images are easily "discriminable", so the generator would quickly have to find a way around it by producing better images.*

## Questions 2.4

❓ What is the advantage to use L*A*B* color space instead of RGB in our case?

*CIELAB was intended as a "perceptually uniform" color space. The goal is that small changes in the color space should result in small perceptual changes and vice versa (big changes -> big perceptual changes). Therefore, it is a better fit when it comes to producing images for humans.*

*With RGB, changes in the green channel are much more visible than changes in the red channel. This is problematic if we are training a model because the model will have to adapt the sensitivity to this color and could thus produce worse results.*

## Questions 2.5

❓ What does it mean to have an input shape of (None, None, 1)?

*A shape of None, None means that the images will have arbitrary size and a depth of 1 means that the image is in grayscale.*

❓ Look at the architecture plot.
What are the connections between some layers of the downsampling and upsampling parts?

*This is the standard architecture for U-Net models. This is what makes U-Net models so powerful. It allows the model to produce outputs highly related to the input.*

❓ Why do we have only two outputs channels? What is the model output?

*We are using CIELAB for coloring. One of the color channels in LAB is the luminosity, which is the same thing as greyscale. Therefore, and because the input layers are connected to the output, we only need to output the 2 other channels of LAB, since we already have the luminosity channel.*

## Questions 2.6

❓ In the training process, do the discriminator compare pairs of target and predicted images?

*Our hypothesis is that this would not be a good idea since it would introduce a risk of overfitting the model.*

❓ Let's consider that the generator model is better than the one trained here.
Is it probable for the generator to produce an image that is the same as one from the targets set
(with the real colors)? Why so?

*It's very unlikely that the model would produce the same exact image as the target samples. If it happened, it would mean the model is extremely overfit.*

❓ Look at the training code, what is the value we expect the discriminator to give us when the image is
fake and the one when the image is real.

*0.9 for real images, 0 for fake images.*

❓ Provide three colorized images with the model that you find interesting
(e.g. well colorized, artistic, disastrous result, ...).

TODO : plus que ces deux questions

❓ Provide an image you have in grayscale (convert one in graycale if you don't have any)
and apply the model on your image.