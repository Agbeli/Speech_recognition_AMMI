from matplotlib import pyplot as plt 
import numpy as np 
import warnings
warnings.filterwarnings("ignore")


##### train and validation loss 
train_loss = [20.205,5.955,4.935,4.685,4.567,4.509,4.463,4.426,4.401,4.376,4.360,4.341,4.325,4.315,4.301,4.291,4.286,4.280,4.277,4.253,4.249,4.242,
4.230,4.229,4.224,4.236,4.211,4.224,4.208,4.207,4.184,4.189,4.188,4.188,4.186,4.178,4.166,4.182,4.178,4.159,4.156,4.153,4.149,4.158,4.153,4.146,4.136,
4.132,4.129,4.126]
val_loss = [8.494,6.424,5.976,5.833,5.746,5.681,5.635,5.597,5.480,5.504,5.513,5.546,5.447,5.440,5.431,5.492,5.492,5.466,5.469,5.478,5.442,5.446,
5.409,5.444,5.445,5.554,5.523,5.457,5.461,5.390,5.561,5.582,5.587,5.511,5.569,5.472,5.375,5.395,5.464,5.505,5.435,5.534,5.435,5.491,5.4730,5.515,5.504,
5.523,5.473,5.431]

if __name__ == "__main__":
    # plt.figure(figsize=(8,6))
    # plt.plot(np.arange(len(train_loss)),train_loss,label="train loss curve")
    # plt.plot(np.arange(len(val_loss)),val_loss,label="val loss curve")
    # plt.xlabel("Training epoch")
    # plt.ylabel("loss level")
    # plt.legend(loc="best")
    # plt.title("train and validation loss curve")
    # plt.savefig("train_loss.jpg")
    print("Average training loss: ",np.mean(train_loss))
    print("Average validation loss: ",np.mean(val_loss))
    print("Size of train_epoch: ",len(train_loss))
    print("Size of train_epoch: ",len(val_loss))
