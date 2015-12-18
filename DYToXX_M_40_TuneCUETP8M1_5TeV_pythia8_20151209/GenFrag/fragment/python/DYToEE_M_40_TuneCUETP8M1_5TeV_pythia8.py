import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import * 
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import * 


generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    crossSection = cms.untracked.double(2423.9),
    comEnergy = cms.double(5020.0),

    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock, 
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring('WeakSingleBoson:ffbar2gmZ = on',
                                        'WeakZ0:gmZmode = 0',
                                        'PhaseSpace:mHatMin = 40.',
                                        '23:onMode = off',
                                        '23:onIfAny = 11', ),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythia8CommonSettings',
            'pythia8CUEP8M1Settings', 
            'processParameters')
    )
)
