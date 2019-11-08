from microesc import urbansound8k
import openl3
import soundfile as sf
import numpy as np
import os

def embedFiles(datasetPath, newDir):
    soundfiles = urbansound8k.load_dataset()

    model = openl3.models.load_embedding_model(input_repr="mel256", content_type="env",
                                           embedding_size=512)
    for index in range(len(soundfiles)):
        sample = soundfiles.iloc[index, :] #fetch each sample from the dataset
        path = urbansound8k.sample_path(sample,datasetPath) #find the path given the sample, and the directory the files lay in.
        fold = sample["fold"] #get the fold for the sound from the sample
        differentDir = newDir+str(fold) #assign directory to save file in by adding the respective fold to the path
        openl3.process_file(path, suffix='suffix', output_dir=differentDir,model=model, content_type="env", embedding_size=512, hop_size=0.5, verbose=True) #save the embedded file in its respective fold in the differentDir directory
    
def main():
    myDataPath = "/Users/giovannibirkelund/Documents/GitHub/ESC-CNN-microcontroller/data/datasets/UrbanSound8K/"
    differentDir = "/Users/giovannibirkelund/Documents/GitHub/ESC-CNN-microcontroller/data/embeddedSounds/fold"
    embedFiles(myDataPath,differentDir)
if __name__ == "__main__":
    main()
