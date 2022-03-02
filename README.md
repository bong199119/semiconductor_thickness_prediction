![Python 3.7](https://img.shields.io/badge/python-3.7-b0071e.svg?style=plastic)
![PyTorch 1.8](https://img.shields.io/badge/pytorch-1.8-%239e008e.svg?style=plastic)
![Pytorch-Lightning 1.5.1](https://img.shields.io/badge/pytorch_lightning-1.5.1-%239e008e.svg?style=plastic)
![cuDNN 7.3.1](https://img.shields.io/badge/cuda-11.2-2545e6.svg?style=plastic)
![License CC BY-NC](https://img.shields.io/badge/license-MIT-108a00.svg?style=plastic)

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

# Testing Guidelines
The docker image is present in the docker_file folder. The required code, images and saved models are present in the code folder.
Inside code folder, the image data is preset inside the data folder. The images are already preprocessed to make the testing easier. The code for WGAN and the saved model is present in the folder WGAN. In order to test the trained model follow the following steps. 

* Step1: load docker image
docker load -i surgicaltool_wgan.tar
* Step2: start a container with the code, images and saved models
docker run --gpus 1 -v /home/mteg-vas/nisan/workspace/surgitool/code:/workspace --rm --shm-size=16g -ti surgicaltool_wgan
* Step3: change directory to the loaded code
cd WGAN/
* Step4: Run script for test
python waegan_pl.py --date ""  --dataset  "Graspers (curved) (KARL STORZ) (GRSL-CIKS)" --validate   --DDP --epoch 2



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
