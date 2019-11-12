from microesc import urbansound8k
import openl3
import soundfile as sf
import numpy as np
import os
def ifExists(fileName):
    if fileName in os.listdir(path):
        return True
    else: 
        return False
    
def embedFiles(datasetPath, newDir):
    soundfiles = urbansound8k.load_dataset()

    model = openl3.models.load_embedding_model(input_repr="mel256", content_type="env",
                                           embedding_size=512)
    for index in range(len(soundfiles)):
        sample = soundfiles.iloc[index, :] #fetch each sample from the dataset
        path = urbansound8k.sample_path(sample,datasetPath) #find the path given the sample, and the directory the files lay in.
        fold = sample["fold"] #get the fold for the sound from the sample
        differentDir = newDir+str(fold) #assign directory to save file in by adding the respective fold to the path
        openl3.process_file(path, suffix=None, output_dir=differentDir,model=model, content_type="env", embedding_size=512, hop_size=0.5, verbose=True) #save the embedded file in its respective fold in the differentDir directory
def embedding_path(sample, dataset_path = None):
    return os.path.join(dataset_path, 'fold'+str(sample.fold), sample.slice_file_name.replace('.wav', '.npz'))

def loadfiles():
    dataset = urbansound8k.load_dataset()
    dataset['embeddings'] = None
    # """print(dataset)
    for index, sample in dataset.iterrows():
        
        path = embedding_path(sample,"/Users/giovannibirkelund/Documents/GitHub/ESC-CNN-microcontroller/data/embeddedSounds")
        data = np.load(path)
        emb = data['embedding']
        dataset.at[index,'embeddings'] = emb

    return dataset

def main():
    myDataPath = "/Users/giovannibirkelund/Documents/GitHub/ESC-CNN-microcontroller/data/datasets/UrbanSound8K/"
    differentDir = "/Users/giovannibirkelund/Documents/GitHub/ESC-CNN-microcontroller/data/embeddedSounds/fold"
    
    
    
    # embedFiles(myDataPath,differentDir)
    dataFrame = loadfiles()
    print(dataFrame.loc[0,'embeddings'].shape)
    
    
    


    
if __name__ == "__main__":
    main()
