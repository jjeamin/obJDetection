import torch.nn as nn
from utils.tester import model_test

# torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros')

class VGG(nn.Module):
    def __init__(self,classes=1000):
        super(VGG,self).__init__()
        '''
        layers = [2,2,3,3,3]
        chennels = [64,128,256,512,512]
        '''
        self.vgg16 = nn.Sequential(
            nn.Conv2d(3,64,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.Conv2d(64,64,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 128,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(256, 256,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.Conv2d(256, 256,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(512, 512,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.Conv2d(512, 512,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(512, 512,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.Conv2d(512, 512,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )

        self.F1 = nn.Linear(512*7*7,4096)
        self.F2 = nn.Linear(4096,4096)
        self.output = nn.Linear(4096,1000)

    def forward(self, x):
        x = self.vgg16(x)
        x = x.view(x.size(0), -1)
        x = self.F1(x)
        x = self.F2(x)
        out = self.output(x)

        return out

tester = model_test(VGG())
tester.summary((3,224,224))