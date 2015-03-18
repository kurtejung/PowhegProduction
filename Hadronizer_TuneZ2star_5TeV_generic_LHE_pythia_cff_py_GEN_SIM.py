# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/Hadronizer_TuneZ2_5TeV_generic_LHE_pythia_cff.py --step GEN,SIM --filein file:powheg_Z_CT10nlo_1380_4000_100k.lhe --beamspot Realistic8TeVCollisionPPbBoost --conditions STARTHI53_V27::All --eventcontent RAWSIM --datatier GEN-SIM -n 1 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.VtxSmearedRealistic5TeVPPbBoost_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#additional loads for the analysis step...
process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("RecoJets.Configuration.GenJetParticles_cff")
process.load("RecoJets.Configuration.RecoGenJets_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

# Input source
process.source = cms.Source("LHESource",
        #fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/user/kjung/PowhegLHEs/5tev_kt75_bornsupp200_btag_100k.events')
        fileNames = cms.untracked.vstring('file:/home/jung68/MCProjects/powheg/CMSSW_5_3_24/src/powheg-hvq/POWHEG-BOX/hvq/testrun-b-lhc/hvq_kt5_bsupp200.lhe')
)

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.options = cms.untracked.PSet(
    #wantSummary = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('runs Z2 Pythia6'),
    name = cms.untracked.string('$Source:/afs/cern.ch/user/a/azsigmon/workspace/PowhegZ/CMSSW_5_3_13/src/Configuration/Generator/python/Hadronizer_TuneZ2star_8TeV_generic_LHE_pythia_cff.py $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('Powheg_Dijet_CT10nlo_5TeV_Pythia_TuneZ2star_kt40_bJet_GEN_SIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)
process.RAWSIMoutput.outputCommands.append('keep *_*pdfWeights*_*_*')

# Additional output definition
process.TFileService = cms.Service("TFileService",
            fileName = cms.string("testOutput.root")
            )


# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'STARTHI53_V27::All', '')

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

process.generator = cms.EDFilter("Pythia6HadronizerFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    comEnergy = cms.double(5020.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=0          ! User defined processes', 
            'PMAS(5,1)=4.4   ! b quark mass', 
            'PMAS(6,1)=172.4 ! t quark mass', 
            'MSTP(86)=1      ! requires MPIs to be softer than the main interaction'
	    ),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)


# Produce PDF weights (maximum is 3)
process.pdfWeights = cms.EDProducer("PdfWeightProducer",
    # Fix POWHEG if buggy (this PDF set will also appear on output,
    # so only two more PDF sets can be added in PdfSetNames if not "")
    #FixPOWHEG = cms.untracked.string("cteq66.LHgrid"),
    #GenTag = cms.untracked.InputTag("genParticles"),
    PdfInfoTag = cms.untracked.InputTag("generator"),
    PdfSetNames = cms.untracked.vstring(
       "CT10nlo.LHgrid"
    )
)

process.ak3GenJets = process.ak5GenJets.clone( rParam = 0.3 )
# ========== Flavor Matching ==========================

process.myPartons = cms.EDProducer("PartonSelector",
        withLeptons = cms.bool(False),
        src = cms.InputTag("genParticles")
        )

process.flavourByRef = cms.EDProducer("JetPartonMatcher",
        jets = cms.InputTag("ak3GenJets"),
        coneSizeToAssociate = cms.double(0.3),
        partons = cms.InputTag("myPartons")
        )

# =============== Analysis =============================

process.qcdAna = cms.EDAnalyzer('QCDAnalyzer',
        genJetSrc = cms.InputTag("ak3GenJets"),
        genParticleSrc = cms.InputTag("genParticles"),
        doFlavor = cms.bool(False),
        doSpecies = cms.bool(False),
        onlyDS = cms.bool(False),
        includePDFweight = cms.bool(False),
        useExternalWeight = cms.bool(False),
        externalWeight = cms.double(1),
        flavorSrc = cms.InputTag("flavourByRef"),
        flavorId = cms.vint32(21), # gluons
        speciesId = cms.vint32(11), # gamma
        useRapidity = cms.bool(False),
        jetEtaMin = cms.double(-0.5),
        jetEtaMax = cms.double(0.5),
        hEtaMin = cms.double(-1.0),
        hEtaMax = cms.double(1.0),
        jetRadius = cms.double(0.3),
        pthatMin = cms.double(0),
        pthatMax = cms.double(1000),
        jetPtBins = cms.vdouble(),
        hPtBins = cms.vdouble(),
        qScalePtBins = cms.vdouble(),
        etaBins = cms.vdouble()
        )

for x in range(0,201):
    process.qcdAna.hPtBins += [ float(x)*2.0 ]
    process.qcdAna.jetPtBins += [ float(x)*2.0 ]
    process.qcdAna.qScalePtBins += [ float(x)*2.0 ]

process.qcdAna_bJets = process.qcdAna.clone(
        doFlavor = cms.bool(True),
        flavorId = cms.vint32(5,-5)
        )

process.genjet_step = cms.Path(process.genJetParticles* process.ak3GenJets)
process.flavor_step = cms.Path( process.myPartons * process.flavourByRef )
process.ana_step = cms.Path(process.qcdAna_bJets)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.weight_step = cms.Path(process.pdfWeights)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.weight_step,process.genfiltersummary_step,
        process.endjob_step,process.RAWSIMoutput_step)
        #process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


def customise(process):
    process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')
    process.rivetAnalyzer.AnalysisNames = cms.vstring('CMS_TEST_ANALYSIS')      
    process.rivetAnalyzer.CrossSection = cms.double(1.319e+08) ##130600000) #cross-section in pb          
    process.rivetAnalyzer.OutputFile = cms.string('CMS_Dijet_Analysis_5tev_kt15_bsupp200.aida')
    process.generation_step+=process.rivetAnalyzer
    process.schedule.remove(process.RAWSIMoutput_step)
    return(process)

process = customise(process)
