import FWCore.ParameterSet.Config as cms

from Validation.MtdValidation.btlSimHitsPostProcessor_cfi import btlSimHitsPostProcessor
from Validation.MtdValidation.btlRecoPostProcessor_cfi import btlRecoPostProcessor
from Validation.MtdValidation.etlRecoPostProcessor_cfi import etlRecoPostProcessor

mtdValidationPostProcessor = cms.Sequence(btlSimHitsPostProcessor + btlRecoPostProcessor + etlRecoPostProcessor)
