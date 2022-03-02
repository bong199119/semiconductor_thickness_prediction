![Python 3.7](https://img.shields.io/badge/python-3.7-b0071e.svg?style=plastic)
![PyTorch 1.8](https://img.shields.io/badge/pytorch-1.8-%239e008e.svg?style=plastic)
![Pytorch-Lightning 1.5.1](https://img.shields.io/badge/pytorch_lightning-1.5.1-%239e008e.svg?style=plastic)
![cuDNN 7.3.1](https://img.shields.io/badge/cuda-11.2-2545e6.svg?style=plastic)
![License CC BY-NC](https://img.shields.io/badge/license-MIT-108a00.svg?style=plastic)


<p align="center">
  <b><a href="https://github.com/choib/">BO CHOI</a></b>
</p>


# WGAN: Wasserstein GAN
Assuming that the loss function is a slowly changing value, it is a method to adjust the amount of updating the weight of the neural network using the clipping technique. It is a method in which gradient exploding and mode collapse, known as problems of vanilla GAN, occur less.


![22](https://user-images.githubusercontent.com/57978796/155951485-43db231f-dd3d-43ce-859e-6acb0237e069.png)


The repository includes:
* Source code of WGAN built on ResNet.
* Training code for stylegan dataset
* Pre-trained weights for stylegan dataset
* Example of training on stylegan dataset(cityscape)

# Testing Environment
* CPU = AMD® Ryzen threadripper 3960x 24-core processor × 48
* GPU = Nvidia Geforce 3090 RTX
* RAM = 128GB
* SSD = 512GB
* OS = Ubuntu 18.04

# Training
```bash
python waegan_pl.py --date "" --dataset "cityscape_data" --batch_size 15 --precision 16 --train_max 500
```
# Testing
```bash
python waegan_pl.py --date ""  --dataset "cityscape_data" --validate   --DDP --epoch 499
```
# Resutls
# License
