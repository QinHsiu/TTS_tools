import pydub
import os
from pydub import AudioSegment
from pydub.silence import detect_silence
from os import listdir
from os.path import isfile, join,exists
import json
import time


class SilenceProcessing():
    def __init__(self,args):
        self.args=args
        self.threshold=args.threshold
        self.interval=args.interval
        

    def get_silence(self,audio_path_relative):
        sound = AudioSegment.from_wav(audio_path_relative)
        res=detect_silence(sound, 100, self.threshold, self.interval)
        return res
        # sound.export("{0}/wav_ori_s/{1}".format("moyuqingcopyf",f_name),format="wav")


    def add_silence(self,audio,mode):
        # mode:{beging,end,both}
        cmd=""
        os.system()
        
    
        


    def add_data(self,data,res_dict,f_name):
        if data <= 200:
            key_temp="(0,200]"
        elif data>200 and data <=250:
            key_temp="(200,250]"
        elif data>250 and data<=300:
            key_temp="(250,300]"
        else:
            key_temp="(300,1000]"
        res_dict[key_temp].append(f_name)


        

        





if __name__=="__main__":
    # get files in a directory
    audio_path = 'moyuqingcopyf/wav_ori_t'
    audio_files = [i for i in listdir(audio_path) if isfile(join(audio_path, i))]
    print("total data length: {}".format(len(audio_files)))

    threshold = -65.2 # tweak based on signal-to-noise ratio

    interval = 1 # ms, increase to speed up
    