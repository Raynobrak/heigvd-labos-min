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

TODO continuer ici

❓ In the third experiment we significatively reduced the number of parameters of the discriminator
compared to the other experiments. Did it helped the generator to produce better images? Why?

❓ Compare experiments 1 and 6. Remember, They use the same number of filters
but have a different architecture.

❓ In experiment 5, we decrease the number of paramers of the generator. What was the impact?

# Pix2Pix colorization

## Questions 2.1

❓ We want to colorize grayscale images. Is there only one valid colorized output?

## Questions 2.2

❓ Pix2Pix is a Conditional Adversarial Network, in the practical work with DCGAN we were using noise as input.
What is different in the input we have here?

❓ How does our colorization task relates to a problem where we would want to take photos as inputs
and make them look like paintings?
Please provide another task that would be related to these problems.

## Questions 2.3

❓ Why do you think the model predictions look like this?
In which way a Pix2Pix GAN would be useful to improve the results?

## Questions 2.4

❓ What is the advantage to use L*A*B* color space instead of RGB in our case?

## Questions 2.5

❓ What does it mean to have an input shape of (None, None, 1)?

❓ Look at the architecture plot.
What are the connections between some layers of the downsampling and upsampling parts?

❓ Why do we have only two outputs channels? What is the model output?

## Questions 2.6

❓ In the training process, do the discriminator compare pairs of target and predicted images?

❓ Let's consider that the generator model is better than the one trained here.
Is it probable for the generator to produce an image that is the same as one from the targets set
(with the real colors)? Why so?

❓ Look at the training code, what is the value we expect the discriminator to give us when the image is
fake and the one when the image is real.

❓ Provide three colorized images with the model that you find interesting
(e.g. well colorized, artistic, disastrous result, ...).

❓ Provide an image you have in grayscale (convert one in graycale if you don't have any)
and apply the model on your image.