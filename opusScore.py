# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 20:43:15 2017

@author: justinlboyer
"""
#from fixCategoricalValues import sht1
import numpy as np
from vectorSubsets import importanceOpus, opus
#from fixCategoricalValuesNoNan import fixValuesCategoricalNoNaN

# convert values to numerical
 # fix opus values   

# this script computes the OPUS Score and tacks it onto sht1
def opusScored(df):
    #df["opusScore"] = df.TieShoesWithDevice + df.AttachZipper + df.ButtonShirt + df.PutOnSocks + df.BrushCombHair + df.PlaceToothpasteToothbrush + df.BrushTeeth + df.Shave + df.UseMobilPhone + df.CarryLargeBox + df.OpenEnvelope + df.UseScissors + df.FoldBathTowel + df.UseHammerToDriveNail + df.StirFoodInBowl + df.PourDrinkFromBottle + df.UseForkAndSpoon + df.DrinkFromPaperPlastic + df.CutMeat + df.UseKeyboard
    df["opusScore"] = df[opus].sum(axis=1)
    return

def weightedOpusScore(df):
    dt = np.dot(df[opus],df[importanceOpus[0:20]].transpose())
    df["weightedOpusScore"] = np.diag(dt)
    return

 
# old code used if original names used   
#sht1["opusScore"] = sht1.TieShoesWithDevice + sht1.AttachZipper + sht1.ButtonShirt + sht1.PutOnSocks + sht1.BrushCombHair + sht1.PlaceToothpasteToothbrush + sht1.BrushTeeth + sht1.Shave + sht1.UseMobilPhone + sht1.CarryLargeBox + sht1.OpenEnvelope + sht1.UseScissors + sht1.FoldBathTowel + sht1.UseHammerToDriveNail + sht1.StirFoodInBowl + sht1.PourDrinkFromBottle + sht1.UseForkAndSpoon + sht1.DrinkFromPaperPlastic + sht1.CutMeat + sht1.UseKeyboard
#shtNoNan["opusScoreNoNan"] = shtNoNan.TieShoesWithDevice.dropna() + shtNoNan.AttachZipper.dropna() + shtNoNan.ButtonShirt.dropna() + shtNoNan.PutOnSocks.dropna() + shtNoNan.BrushCombHair.dropna() + shtNoNan.PlaceToothpasteToothbrush.dropna() + shtNoNan.BrushTeeth.dropna() + shtNoNan.Shave.dropna() + shtNoNan.UseMobilPhone.dropna() + shtNoNan.CarryLargeBox.dropna() + shtNoNan.OpenEnvelope.dropna() + shtNoNan.UseScissors.dropna() + shtNoNan.FoldBathTowel.dropna() + shtNoNan.UseHammerToDriveNail.dropna() + shtNoNan.StirFoodInBowl.dropna() + shtNoNan.PourDrinkFromBottle.dropna() + shtNoNan.UseForkAndSpoon.dropna() + shtNoNan.DrinkFromPaperPlastic.dropna() + shtNoNan.CutMeat.dropna() + shtNoNan.UseKeyboard.dropna()
