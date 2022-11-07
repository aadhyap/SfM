import numpy as np
from scipy import linalg
from random import sample
import math


class PnPRANSAC:

    def __init__(self, new_matchings, imgtoX):

        PnP = LinearPnP(matching_2, imgToX, K)

        size_matchings = 0
        for pts in worldpointstoImage:
            x2 = pts[1][0:2]     
            if(x2 in new_matchings):
                size_matchings += 1

        self.size_matchings = size_matchings #number of coresspondance in dictionary




    def choose6(self, new_matchings, imgtoX):


        newimgpts = {}

        rangenums =  sample(range(0, self.size_matchings), 6) 
        print("length of list ", len(rangenums))
        

        for num in rangenums:
            count = 0
            for pts in worldpointstoImage:
                x2 = pts[1][0:2]
                if(x2 in new_matchings) and (count == num) :
                    #image2 match with new image pts
                    new_img = new_matchings[x2]
                    worldpt = worldpointstoImage[pts]
                    newimgpts[tuple(new_img)] = worldpt
                
                count +=  1

        #returns newimgpts with correct new image points correspondace with world points
        return newimgpts




