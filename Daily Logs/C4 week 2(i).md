# CLassic Networks
1. LeNet-5
2. AlexNet : Similar to LeNet but much larger, used ReLU, and was Trained on Multiple GPUs. 
3. VGG 16 : Very organised. Got its name bcause it used 16 kernels

As depth Increases, dimensions decrease and number of channels increases

## Residual Network (ResNets)
- Built out if Residual Blocks
- Introduces skip connections to maintain high level features.
- Effective for Training very deep Networks

Residual Networks (ResNets) are a type of deep neural network architecture that effectively mitigate the problem of vanishing and exploding gradients, which can hinder the training of very deep networks. They achieve this through the use of residual blocks, which introduce shortcut connections that bypass one or more layers.

## Why do ResNets Work?
ResNets introduce skip connections, or shortcuts, that bypass one or more layers. This helps in the easier flow of gradients during backpropagation, allowing the network to learn effectively even with many layers.

 By mitigating the vanishing gradient problem, ResNets enable the training of much deeper networks, which can capture more complex patterns and features from the data.

 
