# Interpretable-ML-Thesis
This repo contains the necessary material to replicate the tool developed during my thesis work

## Getting Started

Once you have the projec you have to run the following commands from the project folder:

1. Create a virtual environment with Python, then activate the environment and install the dependencies reported in the requirements file.
2. The next step is to install the decompiler: *apktool* (you can find the instructions at its official page https://apktool.org/docs/install/).
3. Run *python apk_decompiler.py* to extract the smali files.
4. Run *python main\_cati.py* that will convert the smali files in OPCode and then convert them in images

Once here you can use the `main.py` this way:
```
python main.py --help
usage: main.py [-h] -m {DATA,BASIC_CNN,BASIC_LSTM,BASIC_MLP,NEDO,VINC,VGG16} -d DATASET [-o OUTPUT_MODEL] 
               [-l LOAD_MODEL] [-e EPOCHS] [-b BATCH_SIZE] [-i IMAGE_SIZE] 
               [-w WEIGHTS] [--mode {train-val,train-test,test,gradcam-cati,gradcam-only}]

Deep Learning Image-based Malware Classification

optional arguments:
  -h, --help            show this help message and exit

Arguments:
  -m {DATA,BASIC_CNN,BASIC_LSTM,BASIC_MLP,NEDO,VINC,VGG16}, --model {DATA,BASIC_CNN,BASIC_LSTM,BASIC_MLP,NEDO,VINC,VGG16}
                        Choose the model to use between the ones implemented
  -d DATASET, --dataset DATASET
                        the dataset path, must have the folder structure: training/train, training/val and test,
                        in each of this folders, one folder per class (see dataset_test)
  -o OUTPUT_MODEL, --output_model OUTPUT_MODEL
                        Name of model to store
  -l LOAD_MODEL, --load_model LOAD_MODEL
                        Name of model to load
  -e EPOCHS, --epochs EPOCHS
                        number of epochs
  -b BATCH_SIZE, --batch_size BATCH_SIZE
  -i IMAGE_SIZE, --image_size IMAGE_SIZE
                        FORMAT ACCEPTED = SxC , the Size (SIZExSIZE) and channel of the images in input 
                        (reshape will be applied)
  -w WEIGHTS, --weights WEIGHTS
                        If you do not want random initialization of the model weights (ex. 'imagenet' or path 
                        to weights to be loaded), not available for all models!
  --mode {train-val,train-test,test,gradcam-cati,gradcam-only}
                        Choose which mode run between 'train-val' (default), 'train-test', 'test' or 'gradcam'. 
                        The 'train-val' mode will run a phase of training and validation on the training and 
                        validation set, the 'train-test' mode will run a phase of training on the training+validation 
                        sets and then test on the test set, the 'test' mode will run only a phase of test on 
                        the test set. The 'gradcam-[cati|only]' will run the gradcam analysis on the model provided. 
                        'gradcam-only' will generate the heatmaps only, while 'gradcam-cati will also run 
                        the cati tool to reverse process and select the code from the heatmap to the decompiled 
                        smali (if provided, see cati README)

```
results are stored in `results` folder
