"""
Print desired dose stats of stated plan (for dose comparison using different structure sets).

vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['BrainStem'].GetRoiVolume()
relvol = 0.1/vol
This is needed to get clinical goals (i.e dose to 0.1cm3 volume)

If any of the structures listed are not present, 
script will crash. Comment them out and re-run.

To run type:
    from rmhTools.regTools import dose_stats
    dose_stats.main(PLAN_NAME)

"""

import connect as rsl
import os
import json


def main( planName ):

    
    patient = rsl.get_current("Patient")
    case = rsl.get_current("Case")
    plan = rsl.get_current("Plan")
    exam = rsl.get_current("Examination")
    
	# Read in desired plan from terminal
    plan = case.TreatmentPlans[planName]
    
	# The dose stats given per fraction. 
	#  (30 for manual plan but only 1 for imported dose cubes)
    fractions = plan.BeamSets[0].FractionationPattern.NumberOfFractions
     
    
    # PTV_65Gy_ed
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="PTV_65Gy_ed", RelativeVolumes=[0.5])[0] * fractions     # This is the D50%, i.e. median.
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="PTV_65Gy_ed", RelativeVolumes=[0.99])[0] * fractions
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="PTV_65Gy_ed", RelativeVolumes=[0.98])[0] * fractions
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="PTV_65Gy_ed", RelativeVolumes=[0.95])[0] * fractions            
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="PTV_65Gy_ed", RelativeVolumes=[0.02])[0] * fractions
            
    # PTV_54Gy_ed
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="PTV_54Gy_ed", RelativeVolumes=[0.5])[0] * fractions
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="PTV_54Gy_ed", RelativeVolumes=[0.02])[0] * fractions
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="PTV_54Gy_ed", RelativeVolumes=[0.99])[0] * fractions
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="PTV_54Gy_ed", RelativeVolumes=[0.98])[0] * fractions  
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="PTV_54Gy_ed", RelativeVolumes=[0.95])[0] * fractions            
            

    # Parotids
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="Parotid_L",DoseType="Average") * fractions    # Mean (min or max too)
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="Parotid_L", RelativeVolumes=[0.02])[0] * fractions    
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="Parotid_R",DoseType="Average") * fractions    
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
            RoiName="Parotid_R", RelativeVolumes=[0.02])[0] * fractions    

    #BrainStem
    vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['BrainStem'].GetRoiVolume()
    relvol = 0.1/vol
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="BrainStem",DoseType="Average") * fractions
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="BrainStem", RelativeVolumes=[relvol])[0] * fractions       
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="BrainStem", RelativeVolumes=[0.02])[0] * fractions  

    #BrainStem_03
    vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['BrainStem_03'].GetRoiVolume()
    relvol = 0.1/vol
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="BrainStem_03", RelativeVolumes=[relvol])[0] * fractions  


    #SpinalCord
    vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['SpinalCord'].GetRoiVolume()
    relvol = 0.1/vol
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="SpinalCord",DoseType="Average") * fractions
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="SpinalCord", RelativeVolumes=[0.02])[0] * fractions 
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="SpinalCord", RelativeVolumes=[relvol])[0] * fractions       
    #SpinalCord_03
    vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['SpinalCord_03'].GetRoiVolume()
    relvol = 0.1/vol
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="SpinalCord_03", RelativeVolumes=[relvol])[0] * fractions  
        
        
   
    #Chiasm
    vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['Chiasm'].GetRoiVolume()
    relvol = 0.1/vol
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="Chiasm", RelativeVolumes=[relvol])[0] * fractions   
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="Chiasm",DoseType="Average") * fractions
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="Chiasm", RelativeVolumes=[0.02])[0] * fractions   

    #Chiasm_01
    vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['Chiasm_01'].GetRoiVolume()
    relvol = 0.1/vol
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="Chiasm_01", RelativeVolumes=[relvol])[0] * fractions       
    
        
        
    #Globe_L
    vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['Globe_L'].GetRoiVolume()
    relvol = 0.1/vol
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="Globe_L", RelativeVolumes=[relvol])[0] * fractions   
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="Globe_L",DoseType="Average") * fractions
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="Globe_L", RelativeVolumes=[0.02])[0] * fractions 
    #Globe_R
    vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['Globe_R'].GetRoiVolume()
    relvol = 0.1/vol
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="Globe_R", RelativeVolumes=[relvol])[0] * fractions   
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="Globe_R",DoseType="Average") * fractions    
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="Globe_R", RelativeVolumes=[0.02])[0] * fractions 

    
    #Lenses
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="Lens_L",DoseType="Average") * fractions    
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="Lens_R",DoseType="Average") * fractions    
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="Lens_L", RelativeVolumes=[0.02])[0] * fractions   
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="Lens_R", RelativeVolumes=[0.02])[0] * fractions  
    
    

    
    #OpticNerve_L
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="OpticNerve_L", RelativeVolumes=[0.02])[0] * fractions 
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="OpticNerve_L",DoseType="Average") * fractions        
    #OpticNerve_R_
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="OpticNerve_R", RelativeVolumes=[0.02])[0] * fractions   
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="OpticNerve_R",DoseType="Average") * fractions        


    #OpticNerve_L_01
    vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['OpticNerve_L_01'].GetRoiVolume()
    relvol = 0.1/vol
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="OpticNerve_L_01", RelativeVolumes=[relvol])[0] * fractions   
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="OpticNerve_L_01",DoseType="Average") * fractions
    #OpticNerve_R_01
    vol = case.PatientModel.StructureSets[exam.Name].RoiGeometries['OpticNerve_R_01'].GetRoiVolume()
    relvol = 0.1/vol
    print plan.BeamSets[0].FractionDose.GetDoseAtRelativeVolumes( \
        RoiName="OpticNerve_R_01", RelativeVolumes=[relvol])[0] * fractions   
    print plan.BeamSets[0].FractionDose.GetDoseStatistic(RoiName="OpticNerve_R_01",DoseType="Average") * fractions        

