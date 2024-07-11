from configparser import ConfigParser
import atexit


class ConfigMgr():
    '''
    Singleton class that works on top of ConfigParser. It holds set of information for each particular test and section.
    It loads and saves the data from and to config.ini file.
    '''

    instr = {
        'scopeOnOff' : '0',
        'scopeModel' : 'MSO56',
        'scopeAddr' : 'USB0::0x0699::0x0522::B020140::INSTR',
        'scopeVertScaleCh1' : '2',
        'scopeVertScaleCh2' : '0.1',
        'scopeVertScaleCh3' : '5',
        'scopeVertScaleCh4' : '5',
        'scopeVertScaleCh5' : '1',
        'scopeVertScaleCh6' : '1',
        'scopeVertScaleCh7' : '1',
        'scopeVertScaleCh8' : '1',
        'scopeTermCh1' : '1.0e+6',
        'scopeTermCh2' : '1.0e+6',
        'scopeTermCh3' : '1.0e+6',
        'scopeTermCh4' : '1.0e+6',
        'scopeTermCh5' : '1.0e+6',
        'scopeTermCh6' : '1.0e+6',
        'scopeTermCh7' : '1.0e+6',
        'scopeTermCh8' : '1.0e+6',
        'scopeHorScale' : '200e-9',
        'scopeVertPosCh1' : '2',
        'scopeVertPosCh2' : '0',
        'scopeVertPosCh3' : '-3',
        'scopeVertPosCh4' : '-3',
        'scopeVertPosCh5' : '0',
        'scopeVertPosCh6' : '0',
        'scopeVertPosCh7' : '0',
        'scopeVertPosCh8' : '0',
        'scopeAttnCh1' : '1',
        'scopeAttnCh2' : '1',
        'scopeAttnCh3' : '1',
        'scopeAttnCh4' : '1',
        'scopeAttnCh5' : '1',
        'scopeAttnCh6' : '1',
        'scopeAttnCh7' : '1',
        'scopeAttnCh8' : '1',
        'loadOnOff' : '0',
        'loadModel' : 'Chroma 6312A',
        'loadChannel' : 'CH1',
        'loadAddr' : 'GPIB0::1::INSTR',
        'thermOnOff' : '0',
        'thermModel' : 'F4T',
        'thermAddr' : '10.46.92.10',
        'vinPSOnOff' : '0',
        'vinPSModel' : 'Xantrex XHR 33-33',
        'vinPSAddr' : 'GPIB0::2::INSTR',
        'vinPSCh' : '1',
        'vinCh' : '1',
        'fgenOnOff' : '0',
        'fgenModel' : 'Agilent 33250A',
        'fgenChannel' : 'CH1',
        'fgenAddr' : 'GPIB0::10::INSTR',
        'keithOnOff' : '0',
        'keithModel' : '2700',
        'keithAddr' : 'GPIB0::16::INSTR',
        'vccPSOnOff' : '0',
        'vccPSModel' : '',
        'vccPSAddr' : '',
        'vcc5VCh' : '1',
        'enPSOnOff' : '0',
        'enPSModel' : '',
        'enPSAddr' : '',
        'enPSCh' : '2',
        'customPSOnOff' : '0',
        'customPSModel' : '',
        'customPSAddr' : '',
        'customPSCh' : '2',
        'biasPSOnOff' : '0',
        'biasPSModel' : 'Xantrex XHR 33-33',
        'biasPSAddr' : 'GPIB0::2::INSTR',
        'biasPSCh' : '1',
        'camOnOff' : '0',
        'flirCam' : 'FLIR',
        'dongleOnOff' : '0',
        'dongleModel' : 'Acadia',
        'polBoardFamily' : 'Coronado',
        'polBoardModel' : 'TDA38825',
        'polBoardFamilyCustom' : '',
        'polBoardSilicRev' : '',
        'bom' : 'Insert comment here',
        'bodeOnOff' : '0',
        'bodeFreq1' : '1000',
        'bodeFreq2' : '',
        'bodeFreq3' : '',
        'bodeFreq4' : '',
        'bodeFreq5' : '',
        'bodeDbm1' : '-19',
        'bodeDbm2' : '',
        'bodeDbm3' : '',
        'bodeDbm4' : '',
        'bodeDbm5' : '',
    }

    tempSteps = {
        '1' : '-40',
        '2' : '25',
        '3' : '125',
        '4' : '',
        '5' : '',
        '6' : '',
    }

    testConditions101 = {
        'document' : '0',
        'test101' : '0',
        'test104' : '0',
        'demBoundary' : '3',
        'horScale1' : '200e-9',
        'horScale2' : '200e-9',
        'scopeVoutCh' : '2',
        'scopeSwCh' : '4',
        'currOpt' : 'fixed',
        'startCurr' : '0',
        'endCurr' : '60',
        'stepCurr' : '5',
        'curr1' : '0',
        'curr2' : '20',
        'curr3' : '40',
        'curr4' : '',
        'curr5' : '',
        'curr6' : '',
        'registerTemp' : '0',
        'vinOpt': 'PVin',
        'vinExt' : '',
        'pvinOpt' : 'incr',
        'startPVin' : '12',
        'endPVin' : '12',
        'stepPVin' : '12',
        'PVin1' : '12',
        'PVin2' : '',
        'PVin3' : '',
        'PVin4' : '',
        'PVin5' : '',
        'vout1' : '1.0',
        'vout2' : '3.3',
        'vout3' : '5.0',
        'fswOpt' : 'fixed',
        'startFsw' : '600',
        'endFsw' : '1500',
        'stepFsw' : '100',
        'fsw1' : '600',
        'fsw2' : '800',
        'fsw3' : '1000',
        'fsw4' : '',
        'fsw5' : '',
        'fsw6' : '',
        'fsw7' : '',
        'fsw8' : '',
        'fsw9' : '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'soak' : '12',
        'relax' : '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'biasOpt': '0',
        'bias1': '0.5',
        'bias2': '',
        'bias3': '',
        'enOpt': 'EN',
        'en1': '1.2',
        'en2': '',
        'en3': '',
        'enPvin': 'PVIN',
        'kiin' : '1',
        'kimon' : '2',
        'kvout' : '3',
        'ktmon' : '4',
        'kvin' : '5',
        'kiout' : '6',
        'kioutr' : '0.0001885',
        'kiinr' : '0.0001982',
        'kvcc' : '7',
        'kicc' : '8',
        'kiccr' : '0.001999',
        'kpgood' : '9',
    }

    testConditions102 = {
        'document' : '0',
        'currOpt' : 'fixed',
        'startCurr' : '0',
        'endCurr' : '60',
        'stepCurr' : '5',
        'curr1' : '0',
        'curr2' : '20',
        'curr3' : '40',
        'curr4' : '',
        'curr5' : '',
        'curr6' : '',
        'registerTemp' : '0',
        'vinOpt' : 'PVin',
        'vinExt' : '',
        'pvinOpt' : 'fixed',
        'PVin1' : '12',
        'PVin2' : '12',
        'vout1' : '1.0',
        'vout2' : '3.3',
        'vout3' : '5.0',
        'fswOpt' : 'fixed',
        'startFsw' : '600',
        'endFsw' : '1500',
        'stepFsw' : '100',
        'fsw1' : '600',
        'fsw2' : '800',
        'fsw3' : '1000',
        'fsw4' : '',
        'fsw5' : '',
        'fsw6' : '',
        'fsw7' : '',
        'fsw8' : '',
        'fsw9' : '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'soak' : '12',
        'relax' : '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc' : '3.0',
        'endVcc' : '3.3',
        'stepVcc' : '0.1',
        'biasOpt': '0',
        'bias1': '0.5',
        'bias2': '',
        'bias3': '',
        'enOpt': 'EN',
        'en1': '1.2',
        'en2': '',
        'en3': '',
        'enPvin': 'PVIN',
    }

    testConditions103 = {
        'document': '0',
        'test101': '0',
        'test104': '0',
        'demBoundary': '3',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'tipTemp': '85',
        'maxTemp': '105',
        'tLim': '115',
        'maxCurr': '20',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'pvinOpt': 'incr',
        'startPVin': '12',
        'endPVin': '12',
        'stepPVin': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'biasOpt': '0',
        'bias1': '0.5',
        'bias2': '',
        'bias3': '',
        'enOpt': 'EN',
        'en1': '1.2',
        'en2': '',
        'en3': '',
        'enPvin': 'PVIN',
        'kiin': '1',
        'kimon': '2',
        'kvout': '3',
        'ktmon': '4',
        'kvin': '5',
        'kiout': '6',
        'kioutr': '0.0001885',
        'kiinr': '0.0001982',
        'kvcc': '7',
        'kicc': '8',
        'kiccr': '0.001999',
        'kpgood': '9',
        'tCase': '',
        'tBoard': '',
        'tAmb1': '',
        'tAmb2': '',
        'tAC': '',
    }

    testConditions105 = {
        'document': '0',
        'fswMin' : '1',
        'fswMax' : '1000',
        'fswPerDeca' : '10',
        'ioutConv' : '50',
        'cooloff' : '10',
        'externLoad' : '0',
        'voutCh' : '3',
        'ioutCh' : '2',
        'extraCh1Opt' : '0',
        'extraCh1' : '1',
        'extraCh1Lbl' : '',
        'extraCh2Opt' : '0',
        'extraCh2' : '4',
        'extraCh2Lbl' : '',
        'numOfSlams' : '1',
        'currMax' : '25',
        'currMin' : '1',
        'slewRate' : '10',
        'dutyMax' : '90',
        'dutyMin' : '10',
        'fastAcqOpt' : '0',
    }

    testConditions106 = {
        'document': '0',
        'currOpt' : 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'pvinOpt' : 'incr',
        'startPVin': '12',
        'endPVin': '12',
        'stepPVin': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'vout4': '5.0',
        'vout5': '5.0',
        'fswOpt' : 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'biasOpt': '0',
        'bias1': '0.5',
        'bias2': '',
        'bias3': '',
        'enOpt': 'EN',
        'en1': '1.2',
        'en2': '',
        'en3': '',
        'enPvin': 'PVIN',
        'dbm' : '-25',
    }

    switchTempSteps = {
        '1': '-40',
        '2': '25',
        '3': '125',
        '4': '',
        '5': '',
        '6': '',
    }

    testConditions201 = {
        'document': '0',
        'test201' : '0',
        'test203' : '0',
        'test205' : '0',
        'scopeSwCh': '4',
        'scopeVdshCh': '3',
        'scopeVinCh': '2',
        'scopeVoutCh': '6',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'pvinOpt' : 'fixed',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'PVin4': '12',
        'PVin5': '',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0.5',
        'bias2': '',
        'bias3': '',
        'enOpt': 'EN',
        'en1': '1.2',
        'en2': '',
        'en3': '',
        'enPvin': 'PVIN',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'peakRise': '1',
        'dTeValley': '1',
        'fswTon': '1',
        'peakFall': '1',
        'dTFall': '1',
        'dTFallMan': '1',
        'jitter': '1',
        'jitterMan' : '1',
        'dTeValleyMan': '1',
        'acqNum' : '1',
    }

    testConditions202 = {
        'document': '0',
        'scopeSwCh': '4',
        'scopeVinCh': '1',
        'scopeVoutCh': '3',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'pvinOpt' : 'fixed',
        'PVin1': '12',
        'PVin2': '',
        'PVin3': '',
        'PVin4': '',
        'PVin5': '',
        'biasOpt': '0',
        'bias1': '0.5',
        'bias2': '',
        'bias3': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'enOpt': 'External',
        'en1': '1.2',
        'en2': '',
        'en3': '',
        'enPvin': 'PVIN',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
    }

    testConditions204 = {
        'document': '0',
        'scopeSwCh': '4',
        'scopeILCh': '1',
        'scopeVoutCh': '3',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '5',
        'curr2': '',
        'curr3': '',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'pvinOpt': 'fixed',
        'startPVin': '0',
        'endPVin': '20',
        'stepPVin': '2',
        'PVin1': '12',
        'PVin2': '',
        'PVin3': '',
        'PVin4': '',
        'PVin5': '',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'biasOpt': '0',
        'bias1': '0.5',
        'bias2': '',
        'bias3': '',
        'enOpt': 'EN',
        'en1': '1.2',
        'en2': '',
        'en3': '',
        'enPvin': 'PVIN',
    }

    testConditions205 = {
        'document': '0',
        'scopeSwCh': '1',
        'scopeVoutCh': '1',
        'scopeGateLCh': '1',
        'scopeBootCh': '5',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'pvinOpt': 'fixed',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'PVin4': '',
        'PVin5': '',
        'biasOpt': '0',
        'bias1': '0.5',
        'bias2': '',
        'bias3': '',
        'enOpt': 'EN',
        'en1': '1.2',
        'en2': '',
        'en3': '',
        'enPvin': 'PVIN',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    featuresTempSteps = {
        '1': '-40',
        '2': '25',
        '3': '125',
        '4': '',
        '5': '',
        '6': '',
    }

    testConditions301 = {
        'document': '0',
        'test301' : '0',
        'scopeVccCh' : '6',
        'scopePgoodCh' : '1',
        'scopeVoutCh' : '3',
        'scopeEnCh' : '5',
        'scopeCus1Ch' : '',
        'scopeCus1Lbl' : 'Custom 1',
        'scopeCus2Ch' : '',
        'scopeCus2Lbl' : 'Custom 2',
        'scopeCus3Ch' : '',
        'scopeCus3Lbl' : 'Custom 3',
        'scopeCus4Ch' : '',
        'scopeCus4Lbl' : 'Custom 4',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'pvinOpt': 'fixed',
        'PVin1': '12',
        'PVin2': '',
        'PVin3': '',
        'PVin4': '',
        'PVin5': '',
        'startPVin': '8',
        'endPVin': '16',
        'stepPVin': '4',
        'riseOpt': '0',
        'rise1' : '',
        'rise2' : '',
        'rise3' : '',
        'fall1' : '',
        'fall2' : '',
        'fall3' : '',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'vout4': '',
        'vout5': '',
        'enOpt': 'External',
        'en1': '',
        'en2': '',
        'en3': '',
        'enRiseOpt': '0',
        'enRise1': '',
        'enRise2': '',
        'enRise3': '',
        'enFall1': '',
        'enFall2': '',
        'enFall3': '',
        'enPvin': 'PVIN',
        'enFreq1': '1',
        'enFreq2': '',
        'enFreq3': '',
        'enFreq4': '',
        'enFreq5': '',
        'enFreq6': '',
        'startEnFreq': '1',
        'stepEnFreq': '1',
        'endEnFreq': '10',
        'enFreqOpt': 'incr',
        'enDC1': '10',
        'enDC2': '',
        'enDC3': '',
        'enDC4': '',
        'enDC5': '',
        'enDC6': '',
        'startEnDC': '10',
        'stepEnDC': '10',
        'endEnDC': '90',
        'enDCOpt': 'incr',
        'biasOpt': '0',
        'bias1': '',
        'bias2': '',
        'bias3': '',
        'delay1': '',
        'delay2': '',
        'delay3': '',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'sweepHorScale': '2e-3',
        'senHorScale': '200e-3',
        'sEnPeriod': '1000',
        'enFreq': '1',
        'slowEN': '0',
        'sweepEN': '0',
    }

    testConditions302 = {
        'document': '0',
        'test302': '0',
        'scopeSwCh': '4',
        'scopeVccCh': '6',
        'scopePgoodCh': '1',
        'scopeVoutCh': '3',
        'scopeEnCh': '5',
        'scopePvinCh': '',
        'scopeCus1Ch': '',
        'scopeCus1Lbl': 'Custom 1',
        'scopeCus2Ch': '',
        'scopeCus2Lbl': 'Custom 2',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'pvinOpt': 'fixed',
        'PVin1': '12',
        'PVin2': '',
        'PVin3': '',
        'PVin4': '',
        'PVin5': '',
        'startPVin': '8',
        'endPVin': '16',
        'stepPVin': '4',
        'riseOpt': '0',
        'rise1': '',
        'rise2': '',
        'rise3': '',
        'fall1': '',
        'fall2': '',
        'fall3': '',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'vout4': '',
        'vout5': '',
        'enOpt': 'External',
        'en1': '',
        'en2': '',
        'en3': '',
        'enPvin': 'PVIN',
        'biasOpt': '0',
        'bias1': '',
        'bias2': '',
        'bias3': '',
        'delay1': '',
        'delay2': '',
        'delay3': '',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM': '0',
        'modeFCCM': '0',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'pgoodRising': '92.5',
        'vccUvlo': '90',
        'enRising': '1.2',
        'enFalling': '1.0',
        'voutFalling': '10',
        'ssHorScale': '2e-3',
        'pdHorScale': '40e-3',
    }

    testConditions303 = {
        'document': '0',
        'test303': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions304 = {
        'document': '0',
        'test304': '0',
        'scopeSwCh': '4',
        'scopeVccCh': '6',
        'scopePgoodCh': '1',
        'scopeVoutCh': '3',
        'scopeEnCh': '5',
        'scopePvinCh': '',
        'scopeCus1Ch': '',
        'scopeCus1Lbl': 'Custom 1',
        'scopeCus2Ch': '',
        'scopeCus2Lbl': 'Custom 2',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'pvinOpt': 'fixed',
        'PVin1': '12',
        'PVin2': '',
        'PVin3': '',
        'PVin4': '',
        'PVin5': '',
        'startPVin': '8',
        'endPVin': '16',
        'stepPVin': '4',
        'riseOpt': '0',
        'rise1': '',
        'rise2': '',
        'rise3': '',
        'fall1': '',
        'fall2': '',
        'fall3': '',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'vout4': '',
        'vout5': '',
        'enOpt': 'External',
        'en1': '',
        'en2': '',
        'en3': '',
        'enPvin': 'PVIN',
        'biasOpt': '0',
        'bias1': '',
        'bias2': '',
        'bias3': '',
        'delay1': '',
        'delay2': '',
        'delay3': '',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM': '0',
        'modeFCCM': '0',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions305 = {
        'document': '0',
        'test305': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions306 = {
        'document': '0',
        'test306': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions307 = {
        'document': '0',
        'test307': '0',
        'scopeSwCh': '4',
        'scopeVoutCh': '2',
        'scopeILCh': '1',
        'scopeCSCh': '3',
        'scopeCus1Ch': '',
        'scopeCus1Lbl': 'custom 1',
        'scopeCus2Ch': '',
        'scopeCus2Lbl': 'custom 2',
        'kIoutCh': '0.10085',
        'ilTime1': '180',
        'ilTime2': '200',
        'ioutShunt': '',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'pvinOpt': 'fixed',
        'PVin1': '12',
        'PVin2': '',
        'PVin3': '',
        'PVin4': '',
        'PVin5': '',
        'startPVin': '0',
        'endPVin': '20',
        'stepPVin': '4',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'vout4': '',
        'vout5': '',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'csMin': '9',
        'csTyp': '10',
        'csMax': '11',
        'csRes': '1000',
        'enOpt': 'EN',
        'en1': '',
        'en2': '',
        'en3': '',
        'biasOpt': '0',
        'bias1': '',
        'bias2': '',
        'delay1': '',
        'delay2': '',
        'delay3': '',
        'modeDEM': '0',
        'modeFCCM': '0',
    }

    testConditions308 = {
        'document': '0',
        'test308': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions309 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions310 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions311 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions312 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    ldoVccTempSteps = {
        '1': '-40',
        '2': '25',
        '3': '125',
        '4': '',
        '5': '',
        '6': '',
    }

    testConditions401 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'startPVin': '0',
        'endPVin': '12',
        'stepPVin': '1',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions402 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '',
        'PVin3': '',
        'PVin4': '',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions403 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'riseOpt': '0',
        'rise1': '',
        'rise2': '',
        'rise3': '',
        'fall1': '',
        'fall2': '',
        'fall3': '',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    protectionTempSteps = {
        '1': '-40',
        '2': '25',
        '3': '125',
        '4': '',
        '5': '',
        '6': '',
    }

    testConditions501 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions502 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions503 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions504 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions505 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions506 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    testConditions507 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
    }

    powerSeqTempSteps = {
        '1': '-40',
        '2': '25',
        '3': '125',
        '4': '',
        '5': '',
        '6': '',
    }

    testConditions601 = {
        'document': '0',
        'test601': '0',
        'pvinScopeCh' : '1',
        'vccScopeCh' : '2',
        'enScopeCh' : '3',
        'voutScopeCh' : '4',
        'pgoodScopeCh' : '5',
        'customScopeCh' : '6',
        'customScopeLbl' : '',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'pvinOpt': 'fixed',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '',
        'PVin3': '',
        'riseOpt' : '0',
        'rise1' : '',
        'rise2' : '',
        'rise3' : '',
        'fall1' : '',
        'fall2' : '',
        'fall3' : '',
        'vccRiseOpt': '0',
        'vccRise1': '',
        'vccRise2': '',
        'vccRise3': '',
        'vccFall1': '',
        'vccFall2': '',
        'vccFall3': '',
        'enRiseOpt' : '0',
        'enRise1': '',
        'enRise2': '',
        'enRise3': '',
        'enFall1': '',
        'enFall2': '',
        'enFall3': '',
        'enOpt' : 'EN',
        'enPvin' : 'PVIN',
        'en1': '',
        'en2': '',
        'en3': '',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'biasOpt': '0',
        'bias1': '0.5',
        'bias2': '',
        'bias3': '',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'modeDEM' : '0',
        'modeFCCM' : '0',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccLdo': '0',
        'vccExt': '0',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'customVal': '',
        'scrambledOpt': '',
        'delay1': '5',
        'delay2': '50',
        'delay3': '500',
        'cusRiseOpt': '0',
        'cusRise1' : '',
        'cusRise2' : '',
        'cusRise3' : '',
        'cusFall1' : '',
        'cusFall2' : '',
        'cusFall3' : '',
    }

    ecTableParamTempSteps = {
        '1': '-40',
        '2': '25',
        '3': '125',
        '4': '',
        '5': '',
        '6': '',
    }

    testConditions701 = {
        'document': '0',
        'currOpt': 'fixed',
        'startCurr': '0',
        'endCurr': '60',
        'stepCurr': '5',
        'curr1': '0',
        'curr2': '20',
        'curr3': '40',
        'curr4': '',
        'curr5': '',
        'curr6': '',
        'registerTemp': '0',
        'vinOpt': 'PVin',
        'vinExt': '',
        'PVin1': '12',
        'PVin2': '12',
        'PVin3': '12',
        'vout1': '1.0',
        'vout2': '3.3',
        'vout3': '5.0',
        'bias1': '0',
        'bias2': '0',
        'bias3': '0',
        'fswOpt': 'fixed',
        'startFsw': '600',
        'endFsw': '1500',
        'stepFsw': '100',
        'fsw1': '600',
        'fsw2': '800',
        'fsw3': '1000',
        'fsw4': '',
        'fsw5': '',
        'fsw6': '',
        'fsw7': '',
        'fsw8': '',
        'fsw9': '',
        'mode': 'FCCM',
        'inductance': '150',
        'cout': '10',
        'soak': '12',
        'relax': '',
        'vccOpt': 'LDO',
        'startVcc': '3.0',
        'endVcc': '3.3',
        'stepVcc': '0.1',
        'biasOpt': '0'
    }

    runTest = {
        'test101' : '0',
        'test102' : '0',
        'test103' : '0',
        'test104' : '0',
        'test106' : '0',
        'test201' : '0',
        'test202' : '0',
        'test204' : '0',
        'test205' : '0',
        'test301' : '0',
        'test302' : '0',
        'test307' : '0',
        'test601' : '0',
    }

    polExcel = {
        'sectionSel' : 'Section 1 - Performance',
        'testSel' : 'Test 1.01 - Efficiency, Power Loss, Vout regulation',
    }

    snapshot = {
        'fileName' : '',
        'background' : 'white',
        'currOpt' : 'fixed',
        'curr1' : '0',
        'curr2' : '',
        'curr3' : '',
        'curr4' : '',
        'curr5' : '',
        'curr6' : '',
        'startCurr' : '0',
        'endCurr' : '12',
        'stepCurr' : '1',
        'delay' : '1',
        'delayVal' : '1',
        'image': '0',
        'signal': 'PVIN',
        'psVal1': '0',
        'psVal2': '',
        'psVal3': '',
        'psVal4': '',
        'psVal5': '',
        'psVal6': '',
        'startPsVal': '7',
        'endPsVal': '16',
        'stepPsVal': '1',
        'psOpt': 'fixed',
    }

    #region PS VARIABLES
    ini_Cond = {
        # [ini_Cond]
        'start_freq': 600,
        'end_freq': 1500,
        'step_freq': 100,
        'start_current': 0,
        'end_current': 60,
        'step_current': 5,
        'start_temp': -40,
        'end_temp': 75,
        'step_temp': 20,
        'temp': 25,
        'fsw': 1000,
        'vout': 1.8,
        'vin': 12.0,
        'vref': 1.202,
        'vdrv': 5.0,
        'vin_ilim': 20.0,
        'vdrv_ilim': 0.2,
        'hold_time': 5,
        'settle_time': 25,
        'notes': 'Katmai 7.6 with 2ohm Rboot',
    }

    pstestConditions12 = {
        'keithIoutCh': '15',
        'keithiout_r': '0.00010085',
        'keithImonCh' : '2',
        'keithToutCh' : '1',
    }

    pstestConditions31 = {
        'startVcc' : '2.5',
        'endVcc' : '6.0',
        'stepVcc' : '0.1',
        'pwmCh' : '1',
        'toutCh' : '2',
    }

    pstestConditions32 = {
        'pwmCh' : '1',
        'imonCh' : '2',
        'gateLCh' : '3',
        'swCh' : '4',
        'horScale' : '10e-9',
        'horPos' : '26',
    }

    Cond_1p4 = {
        'phase1ch': '1',
        'phase2ch': '2',
        'phase3ch': '3',
        'phase4ch': '4',
        'phase5ch': '5',
        'phase6ch': '6',
        'phase7ch': '7',
        'phase8ch': '8',
    }

    Cond_1p6 = {
        'tempStep1': '-40',
        'tempStep2': '-20',
        'tempStep3': '0',
        'tempStep4': '25',
        'tempStep5': '50',
        'tempStep6': '75',
        'keiththerm1' : '20',
        'keiththerm2' : '17',
    }

    excel = {
        'filepath': '',
        'partNumber': 'PMC41570',
        'description': 'Denali 4 Consumer',
        'nominalVin': '12',
        'maximumIout': '70',
        'nominalVID': '1.8',
        'nominalFsw': '1000',
        'nominalVCC': '5',
        'nominalInductanceValue': '100',
        'nominalImonRefVoltage': '1.2',
        'minfsw': '600',
        'maxfsw': '1500',
        'minvout': '0.85',
        'maxvout': '2.4',
        'minvcc': '4.5',
        'maxvcc': '5.5',
        'imonRefRange': [0.8, 1, 1.2, 1.5, 1.9],
        'fswRange': {
            'minFsw': '600',
            'maxFsw': '1500'
        },
        'voutRange': {
            'minVout': '0.85',
            'maxVout': '2.4'
        },
        'vccRange': {
            'minVcc': '4.5',
            'maxVcc': '5.5'
        },
    }
    #endregion

    _instance = None
    config = None
    filePath = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigMgr, cls).__new__(cls)
            cls.config = ConfigParser()
            cls.filePath = 'guiFiles/config.ini'
            cls.config.read(cls.filePath)
            # Put any initialization here.
        return cls._instance

    def __init__(self):
        atexit.register(self.cleanup)

    def update_dict(self, inst, temp1, temp2, temp3, temp4, temp5, temp6, snap, cond1, cond2, cond3, cond4, cond5, cond6, ini, pscond1):
        '''
        Recovers all data last saved into config.ini and updates the dictionaries of this class.
        :param inst: (bool) False will not update this section. True will update it.
        :param temp1: (bool) False will not update this section. True will update it.
        :param temp2: (bool) False will not update this section. True will update it.
        :param temp3: (bool) False will not update this section. True will update it.
        :param temp4: (bool) False will not update this section. True will update it.
        :param temp5: (bool) False will not update this section. True will update it.
        :param temp6: (bool) False will not update this section. True will update it.
        :param snap: (bool) False will not update this section. True will update it.
        :param cond1: (bool) False will not update this section. True will update it.
        :param cond2: (bool) False will not update this section. True will update it.
        :param cond3: (bool) False will not update this section. True will update it.
        :param cond4: (bool) False will not update this section. True will update it.
        :param cond5: (bool) False will not update this section. True will update it.
        :param cond6: (bool) False will not update this section. True will update it.
        :param ini: (bool) False will not update this section. True will update it.
        :param pscond1: (bool) False will not update this section. True will update it.
        :return: None
        '''
        #region instr
        if inst:
            self.instr['scopeOnOff'] = self.config.get('instr', 'scopeonoff')
            self.instr['scopeModel'] = self.config.get('instr', 'scopeModel')
            self.instr['scopeAddr'] = self.config.get('instr', 'scopeAddr')
            self.instr['scopeVertScaleCh1'] = self.config.get('instr', 'scopeVertScaleCh1')
            self.instr['scopeVertScaleCh2'] = self.config.get('instr', 'scopeVertScaleCh2')
            self.instr['scopeVertScaleCh3'] = self.config.get('instr', 'scopeVertScaleCh3')
            self.instr['scopeVertScaleCh4'] = self.config.get('instr', 'scopeVertScaleCh4')
            self.instr['scopeVertScaleCh5'] = self.config.get('instr', 'scopeVertScaleCh5')
            self.instr['scopeVertScaleCh6'] = self.config.get('instr', 'scopeVertScaleCh6')
            self.instr['scopeVertScaleCh7'] = self.config.get('instr', 'scopeVertScaleCh7')
            self.instr['scopeVertScaleCh8'] = self.config.get('instr', 'scopeVertScaleCh8')
            self.instr['scopeTermCh1'] = self.config.get('instr', 'scopeTermCh1')
            self.instr['scopeTermCh2'] = self.config.get('instr', 'scopeTermCh2')
            self.instr['scopeTermCh3'] = self.config.get('instr', 'scopeTermCh3')
            self.instr['scopeTermCh4'] = self.config.get('instr', 'scopeTermCh4')
            self.instr['scopeTermCh5'] = self.config.get('instr', 'scopeTermCh5')
            self.instr['scopeTermCh6'] = self.config.get('instr', 'scopeTermCh6')
            self.instr['scopeTermCh7'] = self.config.get('instr', 'scopeTermCh7')
            self.instr['scopeTermCh8'] = self.config.get('instr', 'scopeTermCh8')
            self.instr['scopeHorScale'] = self.config.get('instr', 'scopeHorScale')
            self.instr['scopeVertPosCh1'] = self.config.get('instr', 'scopeVertPosCh1')
            self.instr['scopeVertPosCh2'] = self.config.get('instr', 'scopeVertPosCh2')
            self.instr['scopeVertPosCh3'] = self.config.get('instr', 'scopeVertPosCh3')
            self.instr['scopeVertPosCh4'] = self.config.get('instr', 'scopeVertPosCh4')
            self.instr['scopeVertPosCh5'] = self.config.get('instr', 'scopeVertPosCh5')
            self.instr['scopeVertPosCh6'] = self.config.get('instr', 'scopeVertPosCh6')
            self.instr['scopeVertPosCh7'] = self.config.get('instr', 'scopeVertPosCh7')
            self.instr['scopeVertPosCh8'] = self.config.get('instr', 'scopeVertPosCh8')
            self.instr['scopeAttnCh1'] = self.config.get('instr', 'scopeAttnCh1')
            self.instr['scopeAttnCh2'] = self.config.get('instr', 'scopeAttnCh2')
            self.instr['scopeAttnCh3'] = self.config.get('instr', 'scopeAttnCh3')
            self.instr['scopeAttnCh4'] = self.config.get('instr', 'scopeAttnCh4')
            self.instr['scopeAttnCh5'] = self.config.get('instr', 'scopeAttnCh5')
            self.instr['scopeAttnCh6'] = self.config.get('instr', 'scopeAttnCh6')
            self.instr['scopeAttnCh7'] = self.config.get('instr', 'scopeAttnCh7')
            self.instr['scopeAttnCh8'] = self.config.get('instr', 'scopeAttnCh8')
            self.instr['loadOnOff'] = self.config.get('instr', 'loadOnOff')
            self.instr['loadModel'] = self.config.get('instr', 'loadModel')
            self.instr['loadChannel'] = self.config.get('instr', 'loadChannel')
            self.instr['loadAddr'] = self.config.get('instr', 'loadAddr')
            self.instr['thermOnOff'] = self.config.get('instr', 'thermOnOff')
            self.instr['thermModel'] = self.config.get('instr', 'thermModel')
            self.instr['thermAddr'] = self.config.get('instr', 'thermAddr')
            self.instr['vinPSOnOff'] = self.config.get('instr', 'vinPSOnOff')
            self.instr['vinPSModel'] = self.config.get('instr', 'vinPSModel')
            self.instr['vinPSAddr'] = self.config.get('instr', 'vinPSAddr')
            self.instr['vinPSCh'] = self.config.get('instr', 'vinPSCh')
            self.instr['fgenOnOff'] = self.config.get('instr', 'fgenOnOff')
            self.instr['fgenModel'] = self.config.get('instr', 'fgenModel')
            self.instr['fgenChannel'] = self.config.get('instr', 'fgenChannel')
            self.instr['fgenAddr'] = self.config.get('instr', 'fgenAddr')
            self.instr['keithOnOff'] = self.config.get('instr', 'keithOnOff')
            self.instr['keithModel'] = self.config.get('instr', 'keithModel')
            self.instr['keithAddr'] = self.config.get('instr', 'keithAddr')
            self.instr['vccPSOnOff'] = self.config.get('instr', 'vccPSOnOff')
            self.instr['vccPSModel'] = self.config.get('instr', 'vccPSModel')
            self.instr['vccPSAddr'] = self.config.get('instr', 'vccPSAddr')
            self.instr['vcc5VCh'] = self.config.get('instr', 'vcc5VCh')
            self.instr['enPSOnOff'] = self.config.get('instr', 'enPSOnOff')
            self.instr['enPSModel'] = self.config.get('instr', 'enPSModel')
            self.instr['enPSAddr'] = self.config.get('instr', 'enPSAddr')
            self.instr['enPSCh'] = self.config.get('instr', 'enPSCh')
            self.instr['customPSOnOff'] = self.config.get('instr', 'customPSOnOff')
            self.instr['customPSModel'] = self.config.get('instr', 'customPSModel')
            self.instr['customPSAddr'] = self.config.get('instr', 'customPSAddr')
            self.instr['customPSCh'] = self.config.get('instr', 'customPSCh')
            self.instr['biasPSOnOff'] = self.config.get('instr', 'biasPSOnOff')
            self.instr['biasPSModel'] = self.config.get('instr', 'biasPSModel')
            self.instr['biasPSAddr'] = self.config.get('instr', 'biasPSAddr')
            self.instr['biasPSCh'] = self.config.get('instr', 'biasPSCh')
            self.instr['camOnOff'] = self.config.get('instr', 'camOnOff')
            self.instr['flirCam'] = self.config.get('instr', 'flirCam')
            self.instr['dongleOnOff'] = self.config.get('instr', 'dongleOnOff')
            self.instr['dongleModel'] = self.config.get('instr', 'dongleModel')
            self.instr['bom'] = self.config.get('instr', 'bom')
            self.instr['bodeOnOff'] = self.config.get('instr', 'bodeOnOff')
        #endregion
        #region tempSteps
        if temp1:
            self.tempSteps['1'] = self.config.get('tempSteps', '1')
            self.tempSteps['2'] = self.config.get('tempSteps', '2')
            self.tempSteps['3'] = self.config.get('tempSteps', '3')
            self.tempSteps['4'] = self.config.get('tempSteps', '4')
            self.tempSteps['5'] = self.config.get('tempSteps', '5')
            self.tempSteps['6'] = self.config.get('tempSteps', '6')
        #endregion
        #region switchTempSteps
        if temp2:
            self.switchTempSteps['1'] = self.config.get('switchTempSteps', '1')
            self.switchTempSteps['2'] = self.config.get('switchTempSteps', '2')
            self.switchTempSteps['3'] = self.config.get('switchTempSteps', '3')
            self.switchTempSteps['4'] = self.config.get('switchTempSteps', '4')
            self.switchTempSteps['5'] = self.config.get('switchTempSteps', '5')
            self.switchTempSteps['6'] = self.config.get('switchTempSteps', '6')
        #endregion
        #region featuresTempSteps
        if temp3:
            self.featuresTempSteps['1'] = self.config.get('featuresTempSteps', '1')
            self.featuresTempSteps['2'] = self.config.get('featuresTempSteps', '2')
            self.featuresTempSteps['3'] = self.config.get('featuresTempSteps', '3')
            self.featuresTempSteps['4'] = self.config.get('featuresTempSteps', '4')
            self.featuresTempSteps['5'] = self.config.get('featuresTempSteps', '5')
            self.featuresTempSteps['6'] = self.config.get('featuresTempSteps', '6')
        #endregion
        #region ldoVccTempSteps
        if temp4:
            self.ldoVccTempSteps['1'] = self.config.get('ldoVccTempSteps', '1')
            self.ldoVccTempSteps['2'] = self.config.get('ldoVccTempSteps', '2')
            self.ldoVccTempSteps['3'] = self.config.get('ldoVccTempSteps', '3')
            self.ldoVccTempSteps['4'] = self.config.get('ldoVccTempSteps', '4')
            self.ldoVccTempSteps['5'] = self.config.get('ldoVccTempSteps', '5')
            self.ldoVccTempSteps['6'] = self.config.get('ldoVccTempSteps', '6')
        #endregion
        #region protectionTempSteps
        if temp5:
            self.protectionTempSteps['1'] = self.config.get('protectionTempSteps', '1')
            self.protectionTempSteps['2'] = self.config.get('protectionTempSteps', '2')
            self.protectionTempSteps['3'] = self.config.get('protectionTempSteps', '3')
            self.protectionTempSteps['4'] = self.config.get('protectionTempSteps', '4')
            self.protectionTempSteps['5'] = self.config.get('protectionTempSteps', '5')
            self.protectionTempSteps['6'] = self.config.get('protectionTempSteps', '6')
        #endregion
        #region powerSeqTempSteps
        if temp6:
            self.powerSeqTempSteps['1'] = self.config.get('powerSeqTempSteps', '1')
            self.powerSeqTempSteps['2'] = self.config.get('powerSeqTempSteps', '2')
            self.powerSeqTempSteps['3'] = self.config.get('powerSeqTempSteps', '3')
            self.powerSeqTempSteps['4'] = self.config.get('powerSeqTempSteps', '4')
            self.powerSeqTempSteps['5'] = self.config.get('powerSeqTempSteps', '5')
            self.powerSeqTempSteps['6'] = self.config.get('powerSeqTempSteps', '6')
        #endregion
        if cond1:
            #region testConditions101
            self.testConditions101['document'] = self.config.get('testConditions101', 'document')
            self.testConditions101['test101'] = self.config.get('testConditions101', 'test101')
            self.testConditions101['test104'] = self.config.get('testConditions101', 'test104')
            self.testConditions101['horScale1'] = self.config.get('testConditions101', 'horScale1')
            self.testConditions101['horScale2'] = self.config.get('testConditions101', 'horScale2')
            self.testConditions101['scopeVoutCh'] = self.config.get('testConditions101', 'scopeVoutCh')
            self.testConditions101['scopeSwCh'] = self.config.get('testConditions101', 'scopeSwCh')
            self.testConditions101['startCurr'] = self.config.get('testConditions101', 'startCurr')
            self.testConditions101['endCurr'] = self.config.get('testConditions101', 'endCurr')
            self.testConditions101['stepCurr'] = self.config.get('testConditions101', 'stepCurr')
            self.testConditions101['curr1'] = self.config.get('testConditions101', 'curr1')
            self.testConditions101['curr2'] = self.config.get('testConditions101', 'curr2')
            self.testConditions101['curr3'] = self.config.get('testConditions101', 'curr3')
            self.testConditions101['curr4'] = self.config.get('testConditions101', 'curr4')
            self.testConditions101['curr5'] = self.config.get('testConditions101', 'curr5')
            self.testConditions101['curr6'] = self.config.get('testConditions101', 'curr6')
            self.testConditions101['registerTemp'] = self.config.get('testConditions101', 'registerTemp')
            self.testConditions101['vinOpt'] = self.config.get('testConditions101', 'vinOpt')
            self.testConditions101['vinExt'] = self.config.get('testConditions101', 'vinExt')
            self.testConditions101['startPVin'] = self.config.get('testConditions101', 'startPVin')
            self.testConditions101['endPVin'] = self.config.get('testConditions101', 'endPVin')
            self.testConditions101['stepPVin'] = self.config.get('testConditions101', 'stepPVin')
            self.testConditions101['vout1'] = self.config.get('testConditions101', 'vout1')
            self.testConditions101['vout2'] = self.config.get('testConditions101', 'vout2')
            self.testConditions101['vout3'] = self.config.get('testConditions101', 'vout3')
            self.testConditions101['startFsw'] = self.config.get('testConditions101', 'startFsw')
            self.testConditions101['endFsw'] = self.config.get('testConditions101', 'endFsw')
            self.testConditions101['stepFsw'] = self.config.get('testConditions101', 'stepFsw')
            self.testConditions101['fsw1'] = self.config.get('testConditions101', 'fsw1')
            self.testConditions101['fsw2'] = self.config.get('testConditions101', 'fsw2')
            self.testConditions101['fsw3'] = self.config.get('testConditions101', 'fsw3')
            self.testConditions101['fsw4'] = self.config.get('testConditions101', 'fsw4')
            self.testConditions101['fsw5'] = self.config.get('testConditions101', 'fsw5')
            self.testConditions101['fsw6'] = self.config.get('testConditions101', 'fsw6')
            self.testConditions101['fsw7'] = self.config.get('testConditions101', 'fsw7')
            self.testConditions101['fsw8'] = self.config.get('testConditions101', 'fsw8')
            self.testConditions101['fsw9'] = self.config.get('testConditions101', 'fsw9')
            self.testConditions101['modeDEM'] = self.config.get('testConditions101', 'modeDEM')
            self.testConditions101['modeFCCM'] = self.config.get('testConditions101', 'modeFCCM')
            self.testConditions101['soak'] = self.config.get('testConditions101', 'soak')
            self.testConditions101['relax'] = self.config.get('testConditions101', 'relax')
            self.testConditions101['vccLdo'] = self.config.get('testConditions101', 'vccLdo')
            self.testConditions101['vccExt'] = self.config.get('testConditions101', 'vccExt')
            self.testConditions101['startVcc'] = self.config.get('testConditions101', 'startVcc')
            self.testConditions101['endVcc'] = self.config.get('testConditions101', 'endVcc')
            self.testConditions101['stepVcc'] = self.config.get('testConditions101', 'stepVcc')
            self.testConditions101['kiin'] = self.config.get('testConditions101', 'kiin')
            self.testConditions101['kimon'] = self.config.get('testConditions101', 'kimon')
            self.testConditions101['kvout'] = self.config.get('testConditions101', 'kvout')
            self.testConditions101['ktmon'] = self.config.get('testConditions101', 'ktmon')
            self.testConditions101['kvin'] = self.config.get('testConditions101', 'kvin')
            self.testConditions101['kiout'] = self.config.get('testConditions101', 'kiout')
            self.testConditions101['kioutr'] = self.config.get('testConditions101', 'kioutr')
            self.testConditions101['kiinr'] = self.config.get('testConditions101', 'kiinr')
            self.testConditions101['kvcc'] = self.config.get('testConditions101', 'kvcc')
            self.testConditions101['kicc'] = self.config.get('testConditions101', 'kicc')
            self.testConditions101['kiccr'] = self.config.get('testConditions101', 'kiccr')
            self.testConditions101['kpgood'] = self.config.get('testConditions101', 'kpgood')
            #endregion
            #region testConditions102
            self.testConditions102['document'] = self.config.get('testConditions102', 'document')
            self.testConditions102['startCurr'] = self.config.get('testConditions102', 'startCurr')
            self.testConditions102['endCurr'] = self.config.get('testConditions102', 'endCurr')
            self.testConditions102['stepCurr'] = self.config.get('testConditions102', 'stepCurr')
            self.testConditions102['curr1'] = self.config.get('testConditions102', 'curr1')
            self.testConditions102['curr2'] = self.config.get('testConditions102', 'curr2')
            self.testConditions102['curr3'] = self.config.get('testConditions102', 'curr3')
            self.testConditions102['curr4'] = self.config.get('testConditions102', 'curr4')
            self.testConditions102['curr5'] = self.config.get('testConditions102', 'curr5')
            self.testConditions102['curr6'] = self.config.get('testConditions102', 'curr6')
            self.testConditions102['registerTemp'] = self.config.get('testConditions102', 'registerTemp')
            self.testConditions102['PVin1'] = self.config.get('testConditions102', 'PVin1')
            self.testConditions102['PVin2'] = self.config.get('testConditions102', 'PVin2')
            self.testConditions102['vout1'] = self.config.get('testConditions102', 'vout1')
            self.testConditions102['vout2'] = self.config.get('testConditions102', 'vout2')
            self.testConditions102['vout3'] = self.config.get('testConditions102', 'vout3')
            self.testConditions102['fswOpt'] = self.config.get('testConditions102', 'fswOpt')
            self.testConditions102['startFsw'] = self.config.get('testConditions102', 'startFsw')
            self.testConditions102['endFsw'] = self.config.get('testConditions102', 'endFsw')
            self.testConditions102['stepFsw'] = self.config.get('testConditions102', 'stepFsw')
            self.testConditions102['fsw1'] = self.config.get('testConditions102', 'fsw1')
            self.testConditions102['fsw2'] = self.config.get('testConditions102', 'fsw2')
            self.testConditions102['fsw3'] = self.config.get('testConditions102', 'fsw3')
            self.testConditions102['fsw4'] = self.config.get('testConditions102', 'fsw4')
            self.testConditions102['fsw5'] = self.config.get('testConditions102', 'fsw5')
            self.testConditions102['fsw6'] = self.config.get('testConditions102', 'fsw6')
            self.testConditions102['fsw7'] = self.config.get('testConditions102', 'fsw7')
            self.testConditions102['fsw8'] = self.config.get('testConditions102', 'fsw8')
            self.testConditions102['fsw9'] = self.config.get('testConditions102', 'fsw9')
            self.testConditions102['modeDEM'] = self.config.get('testConditions102', 'modeDEM')
            self.testConditions102['modeFCCM'] = self.config.get('testConditions102', 'modeFCCM')
            self.testConditions102['soak'] = self.config.get('testConditions102', 'soak')
            self.testConditions102['relax'] = self.config.get('testConditions102', 'relax')
            self.testConditions102['vccLdo'] = self.config.get('testConditions102', 'vccLdo')
            self.testConditions102['vccExt'] = self.config.get('testConditions102', 'vccExt')
            self.testConditions102['startVcc'] = self.config.get('testConditions102', 'startVcc')
            self.testConditions102['endVcc'] = self.config.get('testConditions102', 'endVcc')
            self.testConditions102['stepVcc'] = self.config.get('testConditions102', 'stepVcc')
            #endregion
            #region testConditions103
            self.testConditions103['startCurr'] = self.config.get('testConditions103', 'startCurr')
            self.testConditions103['endCurr'] = self.config.get('testConditions103', 'endCurr')
            self.testConditions103['stepCurr'] = self.config.get('testConditions103', 'stepCurr')
            self.testConditions103['curr1'] = self.config.get('testConditions103', 'curr1')
            self.testConditions103['curr2'] = self.config.get('testConditions103', 'curr2')
            self.testConditions103['curr3'] = self.config.get('testConditions103', 'curr3')
            self.testConditions103['curr4'] = self.config.get('testConditions103', 'curr4')
            self.testConditions103['curr5'] = self.config.get('testConditions103', 'curr5')
            self.testConditions103['curr6'] = self.config.get('testConditions103', 'curr6')
            self.testConditions103['tipTemp'] = self.config.get('testConditions103', 'tipTemp')
            self.testConditions103['maxTemp'] = self.config.get('testConditions103', 'maxTemp')
            self.testConditions103['tLim'] = self.config.get('testConditions103', 'tLim')
            self.testConditions103['maxCurr'] = self.config.get('testConditions103', 'maxCurr')
            self.testConditions103['registerTemp'] = self.config.get('testConditions103', 'registerTemp')
            self.testConditions103['vinExt'] = self.config.get('testConditions103', 'vinExt')
            self.testConditions103['startPvin'] = self.config.get('testConditions103', 'startPvin')
            self.testConditions103['endPvin'] = self.config.get('testConditions103', 'endPvin')
            self.testConditions103['stepPvin'] = self.config.get('testConditions103', 'stepPvin')
            self.testConditions103['vout1'] = self.config.get('testConditions103', 'vout1')
            self.testConditions103['vout2'] = self.config.get('testConditions103', 'vout2')
            self.testConditions103['vout3'] = self.config.get('testConditions103', 'vout3')
            self.testConditions103['startFsw'] = self.config.get('testConditions103', 'startFsw')
            self.testConditions103['endFsw'] = self.config.get('testConditions103', 'endFsw')
            self.testConditions103['stepFsw'] = self.config.get('testConditions103', 'stepFsw')
            self.testConditions103['fsw1'] = self.config.get('testConditions103', 'fsw1')
            self.testConditions103['fsw2'] = self.config.get('testConditions103', 'fsw2')
            self.testConditions103['fsw3'] = self.config.get('testConditions103', 'fsw3')
            self.testConditions103['fsw4'] = self.config.get('testConditions103', 'fsw4')
            self.testConditions103['fsw5'] = self.config.get('testConditions103', 'fsw5')
            self.testConditions103['fsw6'] = self.config.get('testConditions103', 'fsw6')
            self.testConditions103['fsw7'] = self.config.get('testConditions103', 'fsw7')
            self.testConditions103['fsw8'] = self.config.get('testConditions103', 'fsw8')
            self.testConditions103['fsw9'] = self.config.get('testConditions103', 'fsw9')
            self.testConditions103['modeDEM'] = self.config.get('testConditions103', 'modeDEM')
            self.testConditions103['modeFCCM'] = self.config.get('testConditions103', 'modeFCCM')
            self.testConditions103['soak'] = self.config.get('testConditions103', 'soak')
            self.testConditions103['relax'] = self.config.get('testConditions103', 'relax')
            self.testConditions103['vccLdo'] = self.config.get('testConditions103', 'vccLdo')
            self.testConditions103['vccExt'] = self.config.get('testConditions103', 'vccExt')
            self.testConditions103['startVcc'] = self.config.get('testConditions103', 'startVcc')
            self.testConditions103['endVcc'] = self.config.get('testConditions103', 'endVcc')
            self.testConditions103['stepVcc'] = self.config.get('testConditions103', 'stepVcc')
            self.testConditions103['kiin'] = self.config.get('testConditions103', 'kiin')
            self.testConditions103['kimon'] = self.config.get('testConditions103', 'kimon')
            self.testConditions103['kvout'] = self.config.get('testConditions103', 'kvout')
            self.testConditions103['ktmon'] = self.config.get('testConditions103', 'ktmon')
            self.testConditions103['kvin'] = self.config.get('testConditions103', 'kvin')
            self.testConditions103['kiout'] = self.config.get('testConditions103', 'kiout')
            self.testConditions103['kioutr'] = self.config.get('testConditions103', 'kioutr')
            self.testConditions103['kiinr'] = self.config.get('testConditions103', 'kiinr')
            self.testConditions103['kvcc'] = self.config.get('testConditions103', 'kvcc')
            self.testConditions103['kicc'] = self.config.get('testConditions103', 'kicc')
            self.testConditions103['kiccr'] = self.config.get('testConditions103', 'kiccr')
            self.testConditions103['kpgood'] = self.config.get('testConditions103', 'kpgood')
            self.testConditions103['tCase'] = self.config.get('testConditions103', 'tCase')
            self.testConditions103['tBoard'] = self.config.get('testConditions103', 'tBoard')
            self.testConditions103['tAmb1'] = self.config.get('testConditions103', 'tAmb1')
            self.testConditions103['tAmb2'] = self.config.get('testConditions103', 'tAmb2')
            self.testConditions103['tAC'] = self.config.get('testConditions103', 'tAC')
            #endregion
            #region testConditions105
            self.testConditions105['fswMin'] = self.config.get('testConditions105', 'fswMin')
            self.testConditions105['fswMax'] = self.config.get('testConditions105', 'fswMax')
            self.testConditions105['fswPerDeca'] = self.config.get('testConditions105', 'fswPerDeca')
            self.testConditions105['ioutConv'] = self.config.get('testConditions105', 'ioutConv')
            self.testConditions105['cooloff'] = self.config.get('testConditions105', 'cooloff')
            self.testConditions105['externLoad'] = self.config.get('testConditions105', 'externLoad')
            self.testConditions105['voutCh'] = self.config.get('testConditions105', 'voutCh')
            self.testConditions105['ioutCh'] = self.config.get('testConditions105', 'ioutCh')
            self.testConditions105['extraCh1Opt'] = self.config.get('testConditions105', 'extraCh1Opt')
            self.testConditions105['extraCh1'] = self.config.get('testConditions105', 'extraCh1')
            self.testConditions105['extraCh1Lbl'] = self.config.get('testConditions105', 'extraCh1Lbl')
            self.testConditions105['extraCh2Opt'] = self.config.get('testConditions105', 'extraCh2Opt')
            self.testConditions105['extraCh2'] = self.config.get('testConditions105', 'extraCh2')
            self.testConditions105['extraCh2Lbl'] = self.config.get('testConditions105', 'extraCh2Lbl')
            self.testConditions105['numOfSlams'] = self.config.get('testConditions105', 'numOfSlams')
            self.testConditions105['currMax'] = self.config.get('testConditions105', 'currMax')
            self.testConditions105['currMin'] = self.config.get('testConditions105', 'currMin')
            self.testConditions105['slewRate'] = self.config.get('testConditions105', 'slewRate')
            self.testConditions105['dutyMax'] = self.config.get('testConditions105', 'dutyMax')
            self.testConditions105['dutyMin'] = self.config.get('testConditions105', 'dutyMin')
            #endregion
            #region testConditions106
            self.testConditions106['document'] = self.config.get('testConditions106', 'document')
            self.testConditions106['startCurr'] = self.config.get('testConditions106', 'startCurr')
            self.testConditions106['endCurr'] = self.config.get('testConditions106', 'endCurr')
            self.testConditions106['stepCurr'] = self.config.get('testConditions106', 'stepCurr')
            self.testConditions106['curr1'] = self.config.get('testConditions106', 'curr1')
            self.testConditions106['curr2'] = self.config.get('testConditions106', 'curr2')
            self.testConditions106['curr3'] = self.config.get('testConditions106', 'curr3')
            self.testConditions106['curr4'] = self.config.get('testConditions106', 'curr4')
            self.testConditions106['curr5'] = self.config.get('testConditions106', 'curr5')
            self.testConditions106['curr6'] = self.config.get('testConditions106', 'curr6')
            self.testConditions106['registerTemp'] = self.config.get('testConditions106', 'registerTemp')
            self.testConditions106['vinOpt'] = self.config.get('testConditions106', 'vinOpt')
            self.testConditions106['vinExt'] = self.config.get('testConditions106', 'vinExt')
            self.testConditions106['pvinOpt'] = self.config.get('testConditions106', 'pvinOpt')
            self.testConditions106['startPVin'] = self.config.get('testConditions106', 'startPVin')
            self.testConditions106['endPVin'] = self.config.get('testConditions106', 'endPVin')
            self.testConditions106['stepPVin'] = self.config.get('testConditions106', 'stepPVin')
            self.testConditions106['vout1'] = self.config.get('testConditions106', 'vout1')
            self.testConditions106['vout2'] = self.config.get('testConditions106', 'vout2')
            self.testConditions106['vout3'] = self.config.get('testConditions106', 'vout3')
            self.testConditions106['vout4'] = self.config.get('testConditions106', 'vout4')
            self.testConditions106['vout5'] = self.config.get('testConditions106', 'vout5')
            self.testConditions106['startFsw'] = self.config.get('testConditions106', 'startFsw')
            self.testConditions106['endFsw'] = self.config.get('testConditions106', 'endFsw')
            self.testConditions106['stepFsw'] = self.config.get('testConditions106', 'stepFsw')
            self.testConditions106['fsw1'] = self.config.get('testConditions106', 'fsw1')
            self.testConditions106['fsw2'] = self.config.get('testConditions106', 'fsw2')
            self.testConditions106['fsw3'] = self.config.get('testConditions106', 'fsw3')
            self.testConditions106['fsw4'] = self.config.get('testConditions106', 'fsw4')
            self.testConditions106['fsw5'] = self.config.get('testConditions106', 'fsw5')
            self.testConditions106['fsw6'] = self.config.get('testConditions106', 'fsw6')
            self.testConditions106['fsw7'] = self.config.get('testConditions106', 'fsw7')
            self.testConditions106['fsw8'] = self.config.get('testConditions106', 'fsw8')
            self.testConditions106['fsw9'] = self.config.get('testConditions106', 'fsw9')
            self.testConditions106['modeDEM'] = self.config.get('testConditions106', 'modeDEM')
            self.testConditions106['modeFCCM'] = self.config.get('testConditions106', 'modeFCCM')
            self.testConditions106['soak'] = self.config.get('testConditions106', 'soak')
            self.testConditions106['relax'] = self.config.get('testConditions106', 'relax')
            self.testConditions106['vccLdo'] = self.config.get('testConditions106', 'vccLdo')
            self.testConditions106['vccExt'] = self.config.get('testConditions106', 'vccExt')
            self.testConditions106['startVcc'] = self.config.get('testConditions106', 'startVcc')
            self.testConditions106['endVcc'] = self.config.get('testConditions106', 'endVcc')
            self.testConditions106['stepVcc'] = self.config.get('testConditions106', 'stepVcc')
            self.testConditions106['dbm'] = self.config.get('testConditions106', 'dbm')
            #endregion
        if cond2:
            #region testConditions201
            self.testConditions201['scopeSwCh'] = self.config.get('testConditions201', 'scopeSwCh')
            self.testConditions201['scopeVdshCh'] = self.config.get('testConditions201', 'scopeVdshCh')
            self.testConditions201['scopeVinCh'] = self.config.get('testConditions201', 'scopeVinCh')
            self.testConditions201['scopeVoutCh'] = self.config.get('testConditions201', 'scopeVoutCh')
            self.testConditions201['scopeGateLCh'] = self.config.get('testConditions201', 'scopeGateLCh')
            self.testConditions201['scopeBootCh'] = self.config.get('testConditions201', 'scopeBootCh')
            self.testConditions201['startCurr'] = self.config.get('testConditions201', 'startCurr')
            self.testConditions201['endCurr'] = self.config.get('testConditions201', 'endCurr')
            self.testConditions201['stepCurr'] = self.config.get('testConditions201', 'stepCurr')
            self.testConditions201['curr1'] = self.config.get('testConditions201', 'curr1')
            self.testConditions201['curr2'] = self.config.get('testConditions201', 'curr2')
            self.testConditions201['curr3'] = self.config.get('testConditions201', 'curr3')
            self.testConditions201['curr4'] = self.config.get('testConditions201', 'curr4')
            self.testConditions201['curr5'] = self.config.get('testConditions201', 'curr5')
            self.testConditions201['curr6'] = self.config.get('testConditions201', 'curr6')
            self.testConditions201['registerTemp'] = self.config.get('testConditions201', 'registerTemp')
            self.testConditions201['vinOpt'] = self.config.get('testConditions201', 'vinOpt')
            self.testConditions201['vinExt'] = self.config.get('testConditions201', 'vinExt')
            self.testConditions201['pvinOpt'] = self.config.get('testConditions201', 'pvinOpt')
            self.testConditions201['PVin1'] = self.config.get('testConditions201', 'PVin1')
            self.testConditions201['PVin2'] = self.config.get('testConditions201', 'PVin2')
            self.testConditions201['PVin3'] = self.config.get('testConditions201', 'PVin3')
            self.testConditions201['PVin4'] = self.config.get('testConditions201', 'PVin4')
            self.testConditions201['vout1'] = self.config.get('testConditions201', 'vout1')
            self.testConditions201['vout2'] = self.config.get('testConditions201', 'vout2')
            self.testConditions201['vout3'] = self.config.get('testConditions201', 'vout3')
            self.testConditions201['startFsw'] = self.config.get('testConditions201', 'startFsw')
            self.testConditions201['endFsw'] = self.config.get('testConditions201', 'endFsw')
            self.testConditions201['stepFsw'] = self.config.get('testConditions201', 'stepFsw')
            self.testConditions201['fsw1'] = self.config.get('testConditions201', 'fsw1')
            self.testConditions201['fsw2'] = self.config.get('testConditions201', 'fsw2')
            self.testConditions201['fsw3'] = self.config.get('testConditions201', 'fsw3')
            self.testConditions201['fsw4'] = self.config.get('testConditions201', 'fsw4')
            self.testConditions201['fsw5'] = self.config.get('testConditions201', 'fsw5')
            self.testConditions201['fsw6'] = self.config.get('testConditions201', 'fsw6')
            self.testConditions201['fsw7'] = self.config.get('testConditions201', 'fsw7')
            self.testConditions201['fsw8'] = self.config.get('testConditions201', 'fsw8')
            self.testConditions201['fsw9'] = self.config.get('testConditions201', 'fsw9')
            self.testConditions201['modeDEM'] = self.config.get('testConditions201', 'modeDEM')
            self.testConditions201['modeFCCM'] = self.config.get('testConditions201', 'modeFCCM')
            self.testConditions201['soak'] = self.config.get('testConditions201', 'soak')
            self.testConditions201['relax'] = self.config.get('testConditions201', 'relax')
            self.testConditions201['vccLdo'] = self.config.get('testConditions201', 'vccLdo')
            self.testConditions201['vccExt'] = self.config.get('testConditions201', 'vccExt')
            self.testConditions201['startVcc'] = self.config.get('testConditions201', 'startVcc')
            self.testConditions201['endVcc'] = self.config.get('testConditions201', 'endVcc')
            self.testConditions201['stepVcc'] = self.config.get('testConditions201', 'stepVcc')
            self.testConditions201['acqNum'] = self.config.get('testConditions201', 'acqNum')
            #endregion
            #region testConditions202
            self.testConditions202['scopeSwCh'] = self.config.get('testConditions202', 'scopeSwCh')
            self.testConditions202['scopeVinCh'] = self.config.get('testConditions202', 'scopeVinCh')
            self.testConditions202['scopeVoutCh'] = self.config.get('testConditions202', 'scopeVoutCh')
            self.testConditions202['startCurr'] = self.config.get('testConditions202', 'startCurr')
            self.testConditions202['endCurr'] = self.config.get('testConditions202', 'endCurr')
            self.testConditions202['stepCurr'] = self.config.get('testConditions202', 'stepCurr')
            self.testConditions202['curr1'] = self.config.get('testConditions202', 'curr1')
            self.testConditions202['curr2'] = self.config.get('testConditions202', 'curr2')
            self.testConditions202['curr3'] = self.config.get('testConditions202', 'curr3')
            self.testConditions202['curr4'] = self.config.get('testConditions202', 'curr4')
            self.testConditions202['curr5'] = self.config.get('testConditions202', 'curr5')
            self.testConditions202['curr6'] = self.config.get('testConditions202', 'curr6')
            self.testConditions202['registerTemp'] = self.config.get('testConditions202', 'registerTemp')
            self.testConditions202['vinOpt'] = self.config.get('testConditions202', 'vinOpt')
            self.testConditions202['vinExt'] = self.config.get('testConditions202', 'vinExt')
            self.testConditions202['PVin1'] = self.config.get('testConditions202', 'PVin1')
            self.testConditions202['PVin2'] = self.config.get('testConditions202', 'PVin2')
            self.testConditions202['PVin3'] = self.config.get('testConditions202', 'PVin3')
            self.testConditions202['PVin4'] = self.config.get('testConditions202', 'PVin4')
            self.testConditions202['PVin5'] = self.config.get('testConditions202', 'PVin5')
            self.testConditions202['bias1'] = self.config.get('testConditions202', 'bias1')
            self.testConditions202['bias2'] = self.config.get('testConditions202', 'bias2')
            self.testConditions202['bias3'] = self.config.get('testConditions202', 'bias3')
            self.testConditions202['vccLdo'] = self.config.get('testConditions202', 'vccLdo')
            self.testConditions202['vccExt'] = self.config.get('testConditions202', 'vccExt')
            self.testConditions202['startVcc'] = self.config.get('testConditions202', 'startVcc')
            self.testConditions202['endVcc'] = self.config.get('testConditions202', 'endVcc')
            self.testConditions202['stepVcc'] = self.config.get('testConditions202', 'stepVcc')
            self.testConditions202['en1'] = self.config.get('testConditions202', 'en1')
            self.testConditions202['en2'] = self.config.get('testConditions202', 'en2')
            self.testConditions202['en3'] = self.config.get('testConditions202', 'en3')
            self.testConditions202['enPvin'] = self.config.get('testConditions202', 'enPvin')
            self.testConditions202['vout1'] = self.config.get('testConditions202', 'vout1')
            self.testConditions202['vout2'] = self.config.get('testConditions202', 'vout2')
            self.testConditions202['vout3'] = self.config.get('testConditions202', 'vout3')
            self.testConditions202['startFsw'] = self.config.get('testConditions202', 'startFsw')
            self.testConditions202['endFsw'] = self.config.get('testConditions202', 'endFsw')
            self.testConditions202['stepFsw'] = self.config.get('testConditions202', 'stepFsw')
            self.testConditions202['fsw1'] = self.config.get('testConditions202', 'fsw1')
            self.testConditions202['fsw2'] = self.config.get('testConditions202', 'fsw2')
            self.testConditions202['fsw3'] = self.config.get('testConditions202', 'fsw3')
            self.testConditions202['fsw4'] = self.config.get('testConditions202', 'fsw4')
            self.testConditions202['fsw5'] = self.config.get('testConditions202', 'fsw5')
            self.testConditions202['fsw6'] = self.config.get('testConditions202', 'fsw6')
            self.testConditions202['fsw7'] = self.config.get('testConditions202', 'fsw7')
            self.testConditions202['fsw8'] = self.config.get('testConditions202', 'fsw8')
            self.testConditions202['fsw9'] = self.config.get('testConditions202', 'fsw9')
            self.testConditions202['modeDEM'] = self.config.get('testConditions202', 'modeDEM')
            self.testConditions202['modeFCCM'] = self.config.get('testConditions202', 'modeFCCM')
            self.testConditions202['soak'] = self.config.get('testConditions202', 'soak')
            self.testConditions202['relax'] = self.config.get('testConditions202', 'relax')
            #endregion
            #region testConditions204
            self.testConditions204['scopeSwCh'] = self.config.get('testConditions204', 'scopeSwCh')
            self.testConditions204['scopeILCh'] = self.config.get('testConditions204', 'scopeILCh')
            self.testConditions204['scopeVoutCh'] = self.config.get('testConditions204', 'scopeVoutCh')
            self.testConditions204['startCurr'] = self.config.get('testConditions204', 'startCurr')
            self.testConditions204['endCurr'] = self.config.get('testConditions204', 'endCurr')
            self.testConditions204['stepCurr'] = self.config.get('testConditions204', 'stepCurr')
            self.testConditions204['curr1'] = self.config.get('testConditions204', 'curr1')
            self.testConditions204['curr2'] = self.config.get('testConditions204', 'curr2')
            self.testConditions204['curr3'] = self.config.get('testConditions204', 'curr3')
            self.testConditions204['curr4'] = self.config.get('testConditions204', 'curr4')
            self.testConditions204['curr5'] = self.config.get('testConditions204', 'curr5')
            self.testConditions204['curr6'] = self.config.get('testConditions204', 'curr6')
            self.testConditions204['registerTemp'] = self.config.get('testConditions204', 'registerTemp')
            self.testConditions204['vinOpt'] = self.config.get('testConditions204', 'vinOpt')
            self.testConditions204['vinExt'] = self.config.get('testConditions204', 'vinExt')
            self.testConditions204['PVin1'] = self.config.get('testConditions204', 'PVin1')
            self.testConditions204['PVin2'] = self.config.get('testConditions204', 'PVin2')
            self.testConditions204['PVin3'] = self.config.get('testConditions204', 'PVin3')
            self.testConditions204['PVin4'] = self.config.get('testConditions204', 'PVin4')
            self.testConditions204['PVin5'] = self.config.get('testConditions204', 'PVin5')
            self.testConditions204['vout1'] = self.config.get('testConditions204', 'vout1')
            self.testConditions204['vout2'] = self.config.get('testConditions204', 'vout2')
            self.testConditions204['vout3'] = self.config.get('testConditions204', 'vout3')
            self.testConditions204['startFsw'] = self.config.get('testConditions204', 'startFsw')
            self.testConditions204['endFsw'] = self.config.get('testConditions204', 'endFsw')
            self.testConditions204['stepFsw'] = self.config.get('testConditions204', 'stepFsw')
            self.testConditions204['fsw1'] = self.config.get('testConditions204', 'fsw1')
            self.testConditions204['fsw2'] = self.config.get('testConditions204', 'fsw2')
            self.testConditions204['fsw3'] = self.config.get('testConditions204', 'fsw3')
            self.testConditions204['fsw4'] = self.config.get('testConditions204', 'fsw4')
            self.testConditions204['fsw5'] = self.config.get('testConditions204', 'fsw5')
            self.testConditions204['fsw6'] = self.config.get('testConditions204', 'fsw6')
            self.testConditions204['fsw7'] = self.config.get('testConditions204', 'fsw7')
            self.testConditions204['fsw8'] = self.config.get('testConditions204', 'fsw8')
            self.testConditions204['fsw9'] = self.config.get('testConditions204', 'fsw9')
            self.testConditions204['modeDEM'] = self.config.get('testConditions204', 'modeDEM')
            self.testConditions204['modeFCCM'] = self.config.get('testConditions204', 'modeFCCM')
            self.testConditions204['relax'] = self.config.get('testConditions204', 'relax')
            self.testConditions204['vccLdo'] = self.config.get('testConditions204', 'vccLdo')
            self.testConditions204['vccExt'] = self.config.get('testConditions204', 'vccExt')
            self.testConditions204['startVcc'] = self.config.get('testConditions204', 'startVcc')
            self.testConditions204['endVcc'] = self.config.get('testConditions204', 'endVcc')
            self.testConditions204['stepVcc'] = self.config.get('testConditions204', 'stepVcc')
            #endregion
            #region testConditions205
            self.testConditions205['scopeSwCh'] = self.config.get('testConditions205', 'scopeSwCh')
            self.testConditions205['scopeVoutCh'] = self.config.get('testConditions205', 'scopeVoutCh')
            self.testConditions205['scopeGateLCh'] = self.config.get('testConditions205', 'scopeGateLCh')
            self.testConditions205['scopeBootCh'] = self.config.get('testConditions205', 'scopeBootCh')
            self.testConditions205['startCurr'] = self.config.get('testConditions205', 'startCurr')
            self.testConditions205['endCurr'] = self.config.get('testConditions205', 'endCurr')
            self.testConditions205['stepCurr'] = self.config.get('testConditions205', 'stepCurr')
            self.testConditions205['curr1'] = self.config.get('testConditions205', 'curr1')
            self.testConditions205['curr2'] = self.config.get('testConditions205', 'curr2')
            self.testConditions205['curr3'] = self.config.get('testConditions205', 'curr3')
            self.testConditions205['curr4'] = self.config.get('testConditions205', 'curr4')
            self.testConditions205['curr5'] = self.config.get('testConditions205', 'curr5')
            self.testConditions205['curr6'] = self.config.get('testConditions205', 'curr6')
            self.testConditions205['registerTemp'] = self.config.get('testConditions205', 'registerTemp')
            self.testConditions205['vinOpt'] = self.config.get('testConditions205', 'vinOpt')
            self.testConditions205['vinExt'] = self.config.get('testConditions205', 'vinExt')
            self.testConditions205['PVin1'] = self.config.get('testConditions205', 'PVin1')
            self.testConditions205['PVin2'] = self.config.get('testConditions205', 'PVin2')
            self.testConditions205['PVin3'] = self.config.get('testConditions205', 'PVin3')
            self.testConditions205['PVin4'] = self.config.get('testConditions205', 'PVin4')
            self.testConditions205['PVin5'] = self.config.get('testConditions205', 'PVin5')
            self.testConditions205['vout1'] = self.config.get('testConditions205', 'vout1')
            self.testConditions205['vout2'] = self.config.get('testConditions205', 'vout2')
            self.testConditions205['vout3'] = self.config.get('testConditions205', 'vout3')
            self.testConditions205['fswOpt'] = self.config.get('testConditions205', 'fswOpt')
            self.testConditions205['startFsw'] = self.config.get('testConditions205', 'startFsw')
            self.testConditions205['endFsw'] = self.config.get('testConditions205', 'endFsw')
            self.testConditions205['stepFsw'] = self.config.get('testConditions205', 'stepFsw')
            self.testConditions205['fsw1'] = self.config.get('testConditions205', 'fsw1')
            self.testConditions205['fsw2'] = self.config.get('testConditions205', 'fsw2')
            self.testConditions205['fsw3'] = self.config.get('testConditions205', 'fsw3')
            self.testConditions205['fsw4'] = self.config.get('testConditions205', 'fsw4')
            self.testConditions205['fsw5'] = self.config.get('testConditions205', 'fsw5')
            self.testConditions205['fsw6'] = self.config.get('testConditions205', 'fsw6')
            self.testConditions205['fsw7'] = self.config.get('testConditions205', 'fsw7')
            self.testConditions205['fsw8'] = self.config.get('testConditions205', 'fsw8')
            self.testConditions205['fsw9'] = self.config.get('testConditions205', 'fsw9')
            self.testConditions205['modeDEM'] = self.config.get('testConditions205', 'modeDEM')
            self.testConditions205['modeFCCM'] = self.config.get('testConditions205', 'modeFCCM')
            self.testConditions205['soak'] = self.config.get('testConditions205', 'soak')
            self.testConditions205['relax'] = self.config.get('testConditions205', 'relax')
            self.testConditions205['vccLdo'] = self.config.get('testConditions205', 'vccLdo')
            self.testConditions205['vccExt'] = self.config.get('testConditions205', 'vccExt')
            self.testConditions205['startVcc'] = self.config.get('testConditions205', 'startVcc')
            self.testConditions205['endVcc'] = self.config.get('testConditions205', 'endVcc')
            self.testConditions205['stepVcc'] = self.config.get('testConditions205', 'stepVcc')
            #endregion
        if cond3:
            #region testConditions301
            self.testConditions301['scopeSwCh'] = self.config.get('testConditions301', 'scopeSwCh')
            self.testConditions301['scopeVccCh'] = self.config.get('testConditions301', 'scopeVccCh')
            self.testConditions301['scopePgoodCh'] = self.config.get('testConditions301', 'scopePgoodCh')
            self.testConditions301['scopeVoutCh'] = self.config.get('testConditions301', 'scopeVoutCh')
            self.testConditions301['scopeEnCh'] = self.config.get('testConditions301', 'scopeEnCh')
            self.testConditions301['scopePvinCh'] = self.config.get('testConditions301', 'scopePvinCh')
            self.testConditions301['scopeCus1Ch'] = self.config.get('testConditions301', 'scopeCus1Ch')
            self.testConditions301['scopeCus1Lbl'] = self.config.get('testConditions301', 'scopeCus1Lbl')
            self.testConditions301['startCurr'] = self.config.get('testConditions301', 'startCurr')
            self.testConditions301['endCurr'] = self.config.get('testConditions301', 'endCurr')
            self.testConditions301['stepCurr'] = self.config.get('testConditions301', 'stepCurr')
            self.testConditions301['curr1'] = self.config.get('testConditions301', 'curr1')
            self.testConditions301['curr2'] = self.config.get('testConditions301', 'curr2')
            self.testConditions301['curr3'] = self.config.get('testConditions301', 'curr3')
            self.testConditions301['curr4'] = self.config.get('testConditions301', 'curr4')
            self.testConditions301['curr5'] = self.config.get('testConditions301', 'curr5')
            self.testConditions301['curr6'] = self.config.get('testConditions301', 'curr6')
            self.testConditions301['registerTemp'] = self.config.get('testConditions301', 'registerTemp')
            self.testConditions301['vinOpt'] = self.config.get('testConditions301', 'vinOpt')
            self.testConditions301['vinExt'] = self.config.get('testConditions301', 'vinExt')
            self.testConditions301['Pvin1'] = self.config.get('testConditions301', 'Pvin1')
            self.testConditions301['Pvin2'] = self.config.get('testConditions301', 'Pvin2')
            self.testConditions301['Pvin3'] = self.config.get('testConditions301', 'Pvin3')
            self.testConditions301['Pvin4'] = self.config.get('testConditions301', 'Pvin4')
            self.testConditions301['Pvin5'] = self.config.get('testConditions301', 'Pvin5')
            self.testConditions301['riseOpt'] = self.config.get('testConditions301', 'riseOpt')
            self.testConditions301['rise1'] = self.config.get('testConditions301', 'rise1')
            self.testConditions301['rise2'] = self.config.get('testConditions301', 'rise2')
            self.testConditions301['rise3'] = self.config.get('testConditions301', 'rise3')
            self.testConditions301['fall1'] = self.config.get('testConditions301', 'fall1')
            self.testConditions301['fall2'] = self.config.get('testConditions301', 'fall2')
            self.testConditions301['fall3'] = self.config.get('testConditions301', 'fall3')
            self.testConditions301['vout1'] = self.config.get('testConditions301', 'vout1')
            self.testConditions301['vout2'] = self.config.get('testConditions301', 'vout2')
            self.testConditions301['vout3'] = self.config.get('testConditions301', 'vout3')
            self.testConditions301['en1'] = self.config.get('testConditions301', 'en1')
            self.testConditions301['en2'] = self.config.get('testConditions301', 'en2')
            self.testConditions301['en3'] = self.config.get('testConditions301', 'en3')
            self.testConditions301['biasOpt'] = self.config.get('testConditions301', 'biasOpt')
            self.testConditions301['bias1'] = self.config.get('testConditions301', 'bias1')
            self.testConditions301['bias2'] = self.config.get('testConditions301', 'bias2')
            self.testConditions301['bias3'] = self.config.get('testConditions301', 'bias3')
            self.testConditions301['startFsw'] = self.config.get('testConditions301', 'startFsw')
            self.testConditions301['endFsw'] = self.config.get('testConditions301', 'endFsw')
            self.testConditions301['stepFsw'] = self.config.get('testConditions301', 'stepFsw')
            self.testConditions301['fsw1'] = self.config.get('testConditions301', 'fsw1')
            self.testConditions301['fsw2'] = self.config.get('testConditions301', 'fsw2')
            self.testConditions301['fsw3'] = self.config.get('testConditions301', 'fsw3')
            self.testConditions301['fsw4'] = self.config.get('testConditions301', 'fsw4')
            self.testConditions301['fsw5'] = self.config.get('testConditions301', 'fsw5')
            self.testConditions301['fsw6'] = self.config.get('testConditions301', 'fsw6')
            self.testConditions301['fsw7'] = self.config.get('testConditions301', 'fsw7')
            self.testConditions301['fsw8'] = self.config.get('testConditions301', 'fsw8')
            self.testConditions301['fsw9'] = self.config.get('testConditions301', 'fsw9')
            self.testConditions301['modeDEM'] = self.config.get('testConditions301', 'modeDEM')
            self.testConditions301['modeFCCM'] = self.config.get('testConditions301', 'modeFCCM')
            self.testConditions301['soak'] = self.config.get('testConditions301', 'soak')
            self.testConditions301['relax'] = self.config.get('testConditions301', 'relax')
            self.testConditions301['vccLdo'] = self.config.get('testConditions301', 'vccLdo')
            self.testConditions301['vccExt'] = self.config.get('testConditions301', 'vccExt')
            self.testConditions301['startVcc'] = self.config.get('testConditions301', 'startVcc')
            self.testConditions301['endVcc'] = self.config.get('testConditions301', 'endVcc')
            self.testConditions301['stepVcc'] = self.config.get('testConditions301', 'stepVcc')
            #endregion
            # region testConditions302
            self.testConditions302['scopeSwCh'] = self.config.get('testConditions302', 'scopeSwCh')
            self.testConditions302['scopeVccCh'] = self.config.get('testConditions302', 'scopeVccCh')
            self.testConditions302['scopePgoodCh'] = self.config.get('testConditions302', 'scopePgoodCh')
            self.testConditions302['scopeVoutCh'] = self.config.get('testConditions302', 'scopeVoutCh')
            self.testConditions302['scopeEnCh'] = self.config.get('testConditions302', 'scopeEnCh')
            self.testConditions302['scopePvinCh'] = self.config.get('testConditions302', 'scopePvinCh')
            self.testConditions302['scopeCus1Ch'] = self.config.get('testConditions302', 'scopeCus1Ch')
            self.testConditions302['scopeCus1Lbl'] = self.config.get('testConditions302', 'scopeCus1Lbl')
            self.testConditions302['startCurr'] = self.config.get('testConditions302', 'startCurr')
            self.testConditions302['endCurr'] = self.config.get('testConditions302', 'endCurr')
            self.testConditions302['stepCurr'] = self.config.get('testConditions302', 'stepCurr')
            self.testConditions302['curr1'] = self.config.get('testConditions302', 'curr1')
            self.testConditions302['curr2'] = self.config.get('testConditions302', 'curr2')
            self.testConditions302['curr3'] = self.config.get('testConditions302', 'curr3')
            self.testConditions302['curr4'] = self.config.get('testConditions302', 'curr4')
            self.testConditions302['curr5'] = self.config.get('testConditions302', 'curr5')
            self.testConditions302['curr6'] = self.config.get('testConditions302', 'curr6')
            self.testConditions302['registerTemp'] = self.config.get('testConditions302', 'registerTemp')
            self.testConditions302['vinOpt'] = self.config.get('testConditions302', 'vinOpt')
            self.testConditions302['vinExt'] = self.config.get('testConditions302', 'vinExt')
            self.testConditions302['Pvin1'] = self.config.get('testConditions302', 'Pvin1')
            self.testConditions302['Pvin2'] = self.config.get('testConditions302', 'Pvin2')
            self.testConditions302['Pvin3'] = self.config.get('testConditions302', 'Pvin3')
            self.testConditions302['Pvin4'] = self.config.get('testConditions302', 'Pvin4')
            self.testConditions302['Pvin5'] = self.config.get('testConditions302', 'Pvin5')
            self.testConditions302['riseOpt'] = self.config.get('testConditions302', 'riseOpt')
            self.testConditions302['rise1'] = self.config.get('testConditions302', 'rise1')
            self.testConditions302['rise2'] = self.config.get('testConditions302', 'rise2')
            self.testConditions302['rise3'] = self.config.get('testConditions302', 'rise3')
            self.testConditions302['fall1'] = self.config.get('testConditions302', 'fall1')
            self.testConditions302['fall2'] = self.config.get('testConditions302', 'fall2')
            self.testConditions302['fall3'] = self.config.get('testConditions302', 'fall3')
            self.testConditions302['vout1'] = self.config.get('testConditions302', 'vout1')
            self.testConditions302['vout2'] = self.config.get('testConditions302', 'vout2')
            self.testConditions302['vout3'] = self.config.get('testConditions302', 'vout3')
            self.testConditions302['en1'] = self.config.get('testConditions302', 'en1')
            self.testConditions302['en2'] = self.config.get('testConditions302', 'en2')
            self.testConditions302['en3'] = self.config.get('testConditions302', 'en3')
            self.testConditions302['biasOpt'] = self.config.get('testConditions302', 'biasOpt')
            self.testConditions302['bias1'] = self.config.get('testConditions302', 'bias1')
            self.testConditions302['bias2'] = self.config.get('testConditions302', 'bias2')
            self.testConditions302['bias3'] = self.config.get('testConditions302', 'bias3')
            self.testConditions302['startFsw'] = self.config.get('testConditions302', 'startFsw')
            self.testConditions302['endFsw'] = self.config.get('testConditions302', 'endFsw')
            self.testConditions302['stepFsw'] = self.config.get('testConditions302', 'stepFsw')
            self.testConditions302['fsw1'] = self.config.get('testConditions302', 'fsw1')
            self.testConditions302['fsw2'] = self.config.get('testConditions302', 'fsw2')
            self.testConditions302['fsw3'] = self.config.get('testConditions302', 'fsw3')
            self.testConditions302['fsw4'] = self.config.get('testConditions302', 'fsw4')
            self.testConditions302['fsw5'] = self.config.get('testConditions302', 'fsw5')
            self.testConditions302['fsw6'] = self.config.get('testConditions302', 'fsw6')
            self.testConditions302['fsw7'] = self.config.get('testConditions302', 'fsw7')
            self.testConditions302['fsw8'] = self.config.get('testConditions302', 'fsw8')
            self.testConditions302['fsw9'] = self.config.get('testConditions302', 'fsw9')
            self.testConditions302['modeDEM'] = self.config.get('testConditions302', 'modeDEM')
            self.testConditions302['modeFCCM'] = self.config.get('testConditions302', 'modeFCCM')
            self.testConditions302['soak'] = self.config.get('testConditions302', 'soak')
            self.testConditions302['relax'] = self.config.get('testConditions302', 'relax')
            self.testConditions302['vccLdo'] = self.config.get('testConditions302', 'vccLdo')
            self.testConditions302['vccExt'] = self.config.get('testConditions302', 'vccExt')
            self.testConditions302['startVcc'] = self.config.get('testConditions302', 'startVcc')
            self.testConditions302['endVcc'] = self.config.get('testConditions302', 'endVcc')
            self.testConditions302['stepVcc'] = self.config.get('testConditions302', 'stepVcc')
            # endregion
            #region testConditions303
            # @TODO
            #endregion
            # region testConditions304
            self.testConditions304['scopeSwCh'] = self.config.get('testConditions304', 'scopeSwCh')
            self.testConditions304['scopeVccCh'] = self.config.get('testConditions304', 'scopeVccCh')
            self.testConditions304['scopePgoodCh'] = self.config.get('testConditions304', 'scopePgoodCh')
            self.testConditions304['scopeVoutCh'] = self.config.get('testConditions304', 'scopeVoutCh')
            self.testConditions304['scopeEnCh'] = self.config.get('testConditions304', 'scopeEnCh')
            self.testConditions304['scopePvinCh'] = self.config.get('testConditions304', 'scopePvinCh')
            self.testConditions304['scopeCus1Ch'] = self.config.get('testConditions304', 'scopeCus1Ch')
            self.testConditions304['scopeCus1Lbl'] = self.config.get('testConditions304', 'scopeCus1Lbl')
            self.testConditions304['startCurr'] = self.config.get('testConditions304', 'startCurr')
            self.testConditions304['endCurr'] = self.config.get('testConditions304', 'endCurr')
            self.testConditions304['stepCurr'] = self.config.get('testConditions304', 'stepCurr')
            self.testConditions304['curr1'] = self.config.get('testConditions304', 'curr1')
            self.testConditions304['curr2'] = self.config.get('testConditions304', 'curr2')
            self.testConditions304['curr3'] = self.config.get('testConditions304', 'curr3')
            self.testConditions304['curr4'] = self.config.get('testConditions304', 'curr4')
            self.testConditions304['curr5'] = self.config.get('testConditions304', 'curr5')
            self.testConditions304['curr6'] = self.config.get('testConditions304', 'curr6')
            self.testConditions304['registerTemp'] = self.config.get('testConditions304', 'registerTemp')
            self.testConditions304['vinOpt'] = self.config.get('testConditions304', 'vinOpt')
            self.testConditions304['vinExt'] = self.config.get('testConditions304', 'vinExt')
            self.testConditions304['Pvin1'] = self.config.get('testConditions304', 'Pvin1')
            self.testConditions304['Pvin2'] = self.config.get('testConditions304', 'Pvin2')
            self.testConditions304['Pvin3'] = self.config.get('testConditions304', 'Pvin3')
            self.testConditions304['Pvin4'] = self.config.get('testConditions304', 'Pvin4')
            self.testConditions304['Pvin5'] = self.config.get('testConditions304', 'Pvin5')
            self.testConditions304['riseOpt'] = self.config.get('testConditions304', 'riseOpt')
            self.testConditions304['rise1'] = self.config.get('testConditions304', 'rise1')
            self.testConditions304['rise2'] = self.config.get('testConditions304', 'rise2')
            self.testConditions304['rise3'] = self.config.get('testConditions304', 'rise3')
            self.testConditions304['fall1'] = self.config.get('testConditions304', 'fall1')
            self.testConditions304['fall2'] = self.config.get('testConditions304', 'fall2')
            self.testConditions304['fall3'] = self.config.get('testConditions304', 'fall3')
            self.testConditions304['vout1'] = self.config.get('testConditions304', 'vout1')
            self.testConditions304['vout2'] = self.config.get('testConditions304', 'vout2')
            self.testConditions304['vout3'] = self.config.get('testConditions304', 'vout3')
            self.testConditions304['en1'] = self.config.get('testConditions304', 'en1')
            self.testConditions304['en2'] = self.config.get('testConditions304', 'en2')
            self.testConditions304['en3'] = self.config.get('testConditions304', 'en3')
            self.testConditions304['biasOpt'] = self.config.get('testConditions304', 'biasOpt')
            self.testConditions304['bias1'] = self.config.get('testConditions304', 'bias1')
            self.testConditions304['bias2'] = self.config.get('testConditions304', 'bias2')
            self.testConditions304['bias3'] = self.config.get('testConditions304', 'bias3')
            self.testConditions304['startFsw'] = self.config.get('testConditions304', 'startFsw')
            self.testConditions304['endFsw'] = self.config.get('testConditions304', 'endFsw')
            self.testConditions304['stepFsw'] = self.config.get('testConditions304', 'stepFsw')
            self.testConditions304['fsw1'] = self.config.get('testConditions304', 'fsw1')
            self.testConditions304['fsw2'] = self.config.get('testConditions304', 'fsw2')
            self.testConditions304['fsw3'] = self.config.get('testConditions304', 'fsw3')
            self.testConditions304['fsw4'] = self.config.get('testConditions304', 'fsw4')
            self.testConditions304['fsw5'] = self.config.get('testConditions304', 'fsw5')
            self.testConditions304['fsw6'] = self.config.get('testConditions304', 'fsw6')
            self.testConditions304['fsw7'] = self.config.get('testConditions304', 'fsw7')
            self.testConditions304['fsw8'] = self.config.get('testConditions304', 'fsw8')
            self.testConditions304['fsw9'] = self.config.get('testConditions304', 'fsw9')
            self.testConditions304['modeDEM'] = self.config.get('testConditions304', 'modeDEM')
            self.testConditions304['modeFCCM'] = self.config.get('testConditions304', 'modeFCCM')
            self.testConditions304['soak'] = self.config.get('testConditions304', 'soak')
            self.testConditions304['relax'] = self.config.get('testConditions304', 'relax')
            self.testConditions304['vccLdo'] = self.config.get('testConditions304', 'vccLdo')
            self.testConditions304['vccExt'] = self.config.get('testConditions304', 'vccExt')
            self.testConditions304['startVcc'] = self.config.get('testConditions304', 'startVcc')
            self.testConditions304['endVcc'] = self.config.get('testConditions304', 'endVcc')
            self.testConditions304['stepVcc'] = self.config.get('testConditions304', 'stepVcc')
            # endregion
            #region testConditions305
            # @TODO
            #endregion
            #region testConditions306

            #endregion
            #region testConditions307
            self.testConditions307['scopeSwCh'] = self.config.get('testConditions307', 'scopeSwCh')
            self.testConditions307['scopeVoutCh'] = self.config.get('testConditions307', 'scopeVoutCh')
            self.testConditions307['scopeILCh'] = self.config.get('testConditions307', 'scopeILCh')
            self.testConditions307['scopeCSCh'] = self.config.get('testConditions307', 'scopeCSCh')
            self.testConditions307['kIoutCh'] = self.config.get('testConditions307', 'kIoutCh')
            self.testConditions307['ioutShunt'] = self.config['testConditions307']['ioutShunt']
            self.testConditions307['startCurr'] = self.config.get('testConditions307', 'startCurr')
            self.testConditions307['endCurr'] = self.config.get('testConditions307', 'endCurr')
            self.testConditions307['stepCurr'] = self.config.get('testConditions307', 'stepCurr')
            self.testConditions307['curr1'] = self.config.get('testConditions307', 'curr1')
            self.testConditions307['curr2'] = self.config.get('testConditions307', 'curr2')
            self.testConditions307['curr3'] = self.config.get('testConditions307', 'curr3')
            self.testConditions307['curr4'] = self.config.get('testConditions307', 'curr4')
            self.testConditions307['curr5'] = self.config.get('testConditions307', 'curr5')
            self.testConditions307['curr6'] = self.config.get('testConditions307', 'curr6')
            self.testConditions307['registerTemp'] = self.config.get('testConditions307', 'registerTemp')
            self.testConditions307['vinOpt'] = self.config.get('testConditions307', 'vinOpt')
            self.testConditions307['vinExt'] = self.config.get('testConditions307', 'vinExt')
            self.testConditions307['PVin1'] = self.config.get('testConditions307', 'PVin1')
            self.testConditions307['PVin2'] = self.config.get('testConditions307', 'PVin2')
            self.testConditions307['PVin3'] = self.config.get('testConditions307', 'PVin3')
            self.testConditions307['vout1'] = self.config.get('testConditions307', 'vout1')
            self.testConditions307['vout2'] = self.config.get('testConditions307', 'vout2')
            self.testConditions307['vout3'] = self.config.get('testConditions307', 'vout3')
            self.testConditions307['biasOpt'] = self.config.get('testConditions307', 'biasOpt')
            self.testConditions307['bias1'] = self.config.get('testConditions307', 'bias1')
            self.testConditions307['bias2'] = self.config.get('testConditions307', 'bias2')
            self.testConditions307['bias3'] = self.config.get('testConditions307', 'bias3')
            self.testConditions307['startFsw'] = self.config.get('testConditions307', 'startFsw')
            self.testConditions307['endFsw'] = self.config.get('testConditions307', 'endFsw')
            self.testConditions307['stepFsw'] = self.config.get('testConditions307', 'stepFsw')
            self.testConditions307['fsw1'] = self.config.get('testConditions307', 'fsw1')
            self.testConditions307['fsw2'] = self.config.get('testConditions307', 'fsw2')
            self.testConditions307['fsw3'] = self.config.get('testConditions307', 'fsw3')
            self.testConditions307['fsw4'] = self.config.get('testConditions307', 'fsw4')
            self.testConditions307['fsw5'] = self.config.get('testConditions307', 'fsw5')
            self.testConditions307['fsw6'] = self.config.get('testConditions307', 'fsw6')
            self.testConditions307['fsw7'] = self.config.get('testConditions307', 'fsw7')
            self.testConditions307['fsw8'] = self.config.get('testConditions307', 'fsw8')
            self.testConditions307['fsw9'] = self.config.get('testConditions307', 'fsw9')
            self.testConditions307['modeDEM'] = self.config.get('testConditions307', 'modeDEM')
            self.testConditions307['modeFCCM'] = self.config.get('testConditions307', 'modeFCCM')
            self.testConditions307['soak'] = self.config.get('testConditions307', 'soak')
            self.testConditions307['relax'] = self.config.get('testConditions307', 'relax')
            self.testConditions307['vccLdo'] = self.config.get('testConditions307', 'vccLdo')
            self.testConditions307['vccExt'] = self.config.get('testConditions307', 'vccExt')
            self.testConditions307['startVcc'] = self.config.get('testConditions307', 'startVcc')
            self.testConditions307['endVcc'] = self.config.get('testConditions307', 'endVcc')
            self.testConditions307['stepVcc'] = self.config.get('testConditions307', 'stepVcc')
            self.testConditions307['csMin'] = self.config.get('testConditions307', 'csMin')
            self.testConditions307['csTyp'] = self.config.get('testConditions307', 'csTyp')
            self.testConditions307['csMax'] = self.config.get('testConditions307', 'csMax')
            self.testConditions307['csRes'] = self.config.get('testConditions307', 'csRes')
            #endregion
            #region testConditions308

            #endregion
            # region testConditions309

            # endregion
            # region testConditions310

            # endregion
            # region testConditions311

            # endregion
            # region testConditions312

            # endregion
        if cond4:
            #region testConditions401
            # @TODO
            #endregion
            #region testConditions402
            # @TODO
            #endregion
            #region testConditions403
            # @TODO
            #endregion
            pass
        if cond5:
            #region testConditions501
            # @TODO
            #endregion
            #region testConditions502
            # @TODO
            #endregion
            #region testConditions503
            # @TODO
            #endregion
            #region testConditions504
            # @TODO
            #endregion
            #region testConditions505
            # @TODO
            #endregion
            #region testConditions506
            # @TODO
            #endregion
            #region testConditions507
            # @TODO
            #endregion
            pass
        if cond6:
            #region testConditions601
            self.testConditions601['document'] = self.config.get('testConditions601', 'document')
            self.testConditions601['pvinScopeCh'] = self.config.get('testConditions601', 'pvinScopeCh')
            self.testConditions601['vccScopeCh'] = self.config.get('testConditions601', 'vccScopeCh')
            self.testConditions601['enScopeCh'] = self.config.get('testConditions601', 'enScopeCh')
            self.testConditions601['voutScopeCh'] = self.config.get('testConditions601', 'voutScopeCh')
            self.testConditions601['pgoodScopeCh'] = self.config.get('testConditions601', 'pgoodScopeCh')
            self.testConditions601['customScopeCh'] = self.config.get('testConditions601', 'customScopeCh')
            self.testConditions601['customScopeLbl'] = self.config.get('testConditions601', 'customScopeLbl')
            self.testConditions601['startCurr'] = self.config.get('testConditions601', 'startCurr')
            self.testConditions601['endCurr'] = self.config.get('testConditions601', 'endCurr')
            self.testConditions601['stepCurr'] = self.config.get('testConditions601', 'stepCurr')
            self.testConditions601['curr1'] = self.config.get('testConditions601', 'curr1')
            self.testConditions601['curr2'] = self.config.get('testConditions601', 'curr2')
            self.testConditions601['curr3'] = self.config.get('testConditions601', 'curr3')
            self.testConditions601['curr4'] = self.config.get('testConditions601', 'curr4')
            self.testConditions601['curr5'] = self.config.get('testConditions601', 'curr5')
            self.testConditions601['curr6'] = self.config.get('testConditions601', 'curr6')
            self.testConditions601['registerTemp'] = self.config.get('testConditions601', 'registerTemp')
            self.testConditions601['vinExt'] = self.config.get('testConditions601', 'vinExt')
            self.testConditions601['Pvin1'] = self.config.get('testConditions601', 'Pvin1')
            self.testConditions601['Pvin2'] = self.config.get('testConditions601', 'Pvin2')
            self.testConditions601['Pvin3'] = self.config.get('testConditions601', 'Pvin3')
            self.testConditions601['rise1'] = self.config.get('testConditions601', 'rise1')
            self.testConditions601['rise2'] = self.config.get('testConditions601', 'rise2')
            self.testConditions601['rise3'] = self.config.get('testConditions601', 'rise3')
            self.testConditions601['fall1'] = self.config.get('testConditions601', 'fall1')
            self.testConditions601['fall2'] = self.config.get('testConditions601', 'fall2')
            self.testConditions601['fall3'] = self.config.get('testConditions601', 'fall3')
            self.testConditions601['vccRise1'] = self.config.get('testConditions601', 'vccRise1')
            self.testConditions601['vccRise2'] = self.config.get('testConditions601', 'vccRise2')
            self.testConditions601['vccRise3'] = self.config.get('testConditions601', 'vccRise3')
            self.testConditions601['vccFall1'] = self.config.get('testConditions601', 'vccFall1')
            self.testConditions601['vccFall2'] = self.config.get('testConditions601', 'vccFall2')
            self.testConditions601['vccFall3'] = self.config.get('testConditions601', 'vccFall3')
            self.testConditions601['enRise1'] = self.config.get('testConditions601', 'enRise1')
            self.testConditions601['enRise2'] = self.config.get('testConditions601', 'enRise2')
            self.testConditions601['enRise3'] = self.config.get('testConditions601', 'enRise3')
            self.testConditions601['enFall1'] = self.config.get('testConditions601', 'enFall1')
            self.testConditions601['enFall2'] = self.config.get('testConditions601', 'enFall2')
            self.testConditions601['enFall3'] = self.config.get('testConditions601', 'enFall3')
            self.testConditions601['en1'] = self.config.get('testConditions601', 'en1')
            self.testConditions601['en2'] = self.config.get('testConditions601', 'en2')
            self.testConditions601['en3'] = self.config.get('testConditions601', 'en3')
            self.testConditions601['vout1'] = self.config.get('testConditions601', 'vout1')
            self.testConditions601['vout2'] = self.config.get('testConditions601', 'vout2')
            self.testConditions601['vout3'] = self.config.get('testConditions601', 'vout3')
            self.testConditions601['bias1'] = self.config.get('testConditions601', 'bias1')
            self.testConditions601['bias2'] = self.config.get('testConditions601', 'bias2')
            self.testConditions601['bias3'] = self.config.get('testConditions601', 'bias3')
            self.testConditions601['startFsw'] = self.config.get('testConditions601', 'startFsw')
            self.testConditions601['endFsw'] = self.config.get('testConditions601', 'endFsw')
            self.testConditions601['stepFsw'] = self.config.get('testConditions601', 'stepFsw')
            self.testConditions601['fsw1'] = self.config.get('testConditions601', 'fsw1')
            self.testConditions601['fsw2'] = self.config.get('testConditions601', 'fsw2')
            self.testConditions601['fsw3'] = self.config.get('testConditions601', 'fsw3')
            self.testConditions601['fsw4'] = self.config.get('testConditions601', 'fsw4')
            self.testConditions601['fsw5'] = self.config.get('testConditions601', 'fsw5')
            self.testConditions601['fsw6'] = self.config.get('testConditions601', 'fsw6')
            self.testConditions601['fsw7'] = self.config.get('testConditions601', 'fsw7')
            self.testConditions601['fsw8'] = self.config.get('testConditions601', 'fsw8')
            self.testConditions601['fsw9'] = self.config.get('testConditions601', 'fsw9')
            self.testConditions601['modeDEM'] = self.config.get('testConditions601', 'modeDEM')
            self.testConditions601['modeFCCM'] = self.config.get('testConditions601', 'modeFCCM')
            self.testConditions601['soak'] = self.config.get('testConditions601', 'soak')
            self.testConditions601['relax'] = self.config.get('testConditions601', 'relax')
            self.testConditions601['startVcc'] = self.config.get('testConditions601', 'startVcc')
            self.testConditions601['endVcc'] = self.config.get('testConditions601', 'endVcc')
            self.testConditions601['stepVcc'] = self.config.get('testConditions601', 'stepVcc')
            #endregion
        if snap:
            #region SNAPSHOT
            self.snapshot['background'] = self.config.get('snapshot', 'background')
            self.snapshot['curr1'] = self.config.get('snapshot', 'curr1')
            self.snapshot['curr2'] = self.config.get('snapshot', 'curr2')
            self.snapshot['curr3'] = self.config.get('snapshot', 'curr3')
            self.snapshot['curr4'] = self.config.get('snapshot', 'curr4')
            self.snapshot['curr5'] = self.config.get('snapshot', 'curr5')
            self.snapshot['curr6'] = self.config.get('snapshot', 'curr6')
            self.snapshot['startCurr'] = self.config.get('snapshot', 'startCurr')
            self.snapshot['endCurr'] = self.config.get('snapshot', 'endCurr')
            self.snapshot['stepCurr'] = self.config.get('snapshot', 'stepCurr')
            self.snapshot['delay'] = self.config.get('snapshot', 'delay')
            self.snapshot['delayVal'] = self.config.get('snapshot', 'delayVal')
            self.snapshot['image'] = self.config.get('snapshot', 'image')
            #endregion
        # PS VARIABLES
        if ini:
            #region ini_Cond
            self.ini_Cond['start_freq'] = self.config.get('ini_Cond', 'start_freq')
            self.ini_Cond['end_freq'] = self.config.get('ini_Cond', 'end_freq')
            self.ini_Cond['step_freq'] = self.config.get('ini_Cond', 'step_freq')
            self.ini_Cond['start_current'] = self.config.get('ini_Cond', 'start_current')
            self.ini_Cond['end_current'] = self.config.get('ini_Cond', 'end_current')
            self.ini_Cond['step_current'] = self.config.get('ini_Cond', 'step_current')
            self.ini_Cond['start_temp'] = self.config.get('ini_Cond', 'start_temp')
            self.ini_Cond['end_temp'] = self.config.get('ini_Cond', 'end_temp')
            self.ini_Cond['step_temp'] = self.config.get('ini_Cond', 'step_temp')
            self.ini_Cond['temp'] = self.config.get('ini_Cond', 'temp')
            self.ini_Cond['fsw'] = self.config.get('ini_Cond', 'fsw')
            self.ini_Cond['vout'] = self.config.get('ini_Cond', 'vout')
            self.ini_Cond['vin'] = self.config.get('ini_Cond', 'vin')
            self.ini_Cond['vref'] = self.config.get('ini_Cond', 'vref')
            self.ini_Cond['vdrv'] = self.config.get('ini_Cond', 'vdrv')
            self.ini_Cond['vin_ilim'] = self.config.get('ini_Cond', 'vin_ilim')
            self.ini_Cond['vdrv_ilim'] = self.config.get('ini_Cond', 'vdrv_ilim')
            self.ini_Cond['hold_time'] = self.config.get('ini_Cond', 'hold_time')
            self.ini_Cond['settle_time'] = self.config.get('ini_Cond', 'settle_time')
            self.ini_Cond['notes'] = self.config.get('ini_Cond', 'notes')
            #endregion
        if pscond1:
            #region pstestConditions12
            self.pstestConditions12['keithIoutCh'] = self.config.get('pstestConditions12', 'keithIoutCh')
            self.pstestConditions12['keithiout_r'] = self.config.get('pstestConditions12', 'keithiout_r')
            self.pstestConditions12['keithImonCh'] = self.config.get('pstestConditions12', 'keithImonCh')
            self.pstestConditions12['keithToutCh'] = self.config.get('pstestConditions12', 'keithToutCh')
            #endregion
            #region Cond_1p4
            self.Cond_1p4['phase1ch'] = self.config.get('Cond_1p4', 'phase1ch')
            self.Cond_1p4['phase2ch'] = self.config.get('Cond_1p4', 'phase2ch')
            self.Cond_1p4['phase3ch'] = self.config.get('Cond_1p4', 'phase3ch')
            self.Cond_1p4['phase4ch'] = self.config.get('Cond_1p4', 'phase4ch')
            self.Cond_1p4['phase5ch'] = self.config.get('Cond_1p4', 'phase5ch')
            self.Cond_1p4['phase6ch'] = self.config.get('Cond_1p4', 'phase6ch')
            self.Cond_1p4['phase7ch'] = self.config.get('Cond_1p4', 'phase7ch')
            self.Cond_1p4['phase8ch'] = self.config.get('Cond_1p4', 'phase8ch')
            #endregion
            #region Cond_1p6
            self.Cond_1p6['tempStep1'] = self.config.get('Cond_1p6', 'tempStep1')
            self.Cond_1p6['tempStep2'] = self.config.get('Cond_1p6', 'tempStep2')
            self.Cond_1p6['tempStep3'] = self.config.get('Cond_1p6', 'tempStep3')
            self.Cond_1p6['tempStep4'] = self.config.get('Cond_1p6', 'tempStep4')
            self.Cond_1p6['tempStep5'] = self.config.get('Cond_1p6', 'tempStep5')
            self.Cond_1p6['tempStep6'] = self.config.get('Cond_1p6', 'tempStep6')
            self.Cond_1p6['keiththerm1'] = self.config.get('Cond_1p6', 'keiththerm1')
            self.Cond_1p6['keiththerm2'] = self.config.get('Cond_1p6', 'keiththerm2')
            #endregion
            #region excel
            self.excel['filepath'] = self.config.get('excel', 'filepath')
            #endregion

    def save_config(self, filePath):
        '''
        Saves current values of from dictionaries into .ini file
        :param filePath: The path to the .ini file
        :return: None
        '''
        for key in self.instr:
            self.config.set('instr', str(key), str(self.instr[key]))
        for key in self.tempSteps:
            self.config.set('tempSteps', str(key), str(self.tempSteps[key]))
        for key in self.switchTempSteps:
            self.config.set('switchTempSteps', str(key), str(self.switchTempSteps[key]))
        for key in self.featuresTempSteps:
            self.config.set('featuresTempSteps', str(key), str(self.featuresTempSteps[key]))
        for key in self.ldoVccTempSteps:
            self.config.set('ldoVccTempSteps', str(key), str(self.ldoVccTempSteps[key]))
        for key in self.protectionTempSteps:
            self.config.set('protectionTempSteps', str(key), str(self.protectionTempSteps[key]))
        for key in self.powerSeqTempSteps:
            self.config.set('powerSeqTempSteps', str(key), str(self.powerSeqTempSteps[key]))
        for key in self.ecTableParamTempSteps:
            self.config.set('ecTableParamTempSteps', str(key), str(self.ecTableParamTempSteps[key]))
        for key in self.testConditions101:
            self.config.set('testConditions101', str(key), str(self.testConditions101[key]))
        for key in self.testConditions102:
            self.config.set('testConditions102', str(key), str(self.testConditions102[key]))
        for key in self.testConditions103:
            self.config.set('testConditions103', str(key), str(self.testConditions103[key]))
        for key in self.testConditions105:
            self.config.set('testConditions105', str(key), str(self.testConditions105[key]))
        for key in self.testConditions106:
            self.config.set('testConditions106', str(key), str(self.testConditions106[key]))
        for key in self.testConditions201:
            self.config.set('testConditions201', str(key), str(self.testConditions201[key]))
        for key in self.testConditions202:
            self.config.set('testConditions202', str(key), str(self.testConditions202[key]))
        for key in self.testConditions204:
            self.config.set('testConditions204', str(key), str(self.testConditions204[key]))
        for key in self.testConditions205:
            self.config.set('testConditions205', str(key), str(self.testConditions205[key]))
        for key in self.testConditions301:
            self.config.set('testConditions301', str(key), str(self.testConditions301[key]))
        for key in self.testConditions302:
            self.config.set('testConditions302', str(key), str(self.testConditions302[key]))
        for key in self.testConditions303:
            self.config.set('testConditions303', str(key), str(self.testConditions303[key]))
        for key in self.testConditions304:
            self.config.set('testConditions304', str(key), str(self.testConditions304[key]))
        for key in self.testConditions305:
            self.config.set('testConditions305', str(key), str(self.testConditions305[key]))
        for key in self.testConditions306:
            self.config.set('testConditions306', str(key), str(self.testConditions306[key]))
        for key in self.testConditions307:
            self.config.set('testConditions307', str(key), str(self.testConditions307[key]))
        for key in self.testConditions308:
            self.config.set('testConditions308', str(key), str(self.testConditions308[key]))
        for key in self.testConditions309:
            self.config.set('testConditions309', str(key), str(self.testConditions309[key]))
        for key in self.testConditions310:
            self.config.set('testConditions310', str(key), str(self.testConditions310[key]))
        for key in self.testConditions311:
            self.config.set('testConditions311', str(key), str(self.testConditions311[key]))
        for key in self.testConditions312:
            self.config.set('testConditions312', str(key), str(self.testConditions312[key]))
        for key in self.testConditions401:
            self.config.set('testConditions401', str(key), str(self.testConditions401[key]))
        for key in self.testConditions402:
            self.config.set('testConditions402', str(key), str(self.testConditions402[key]))
        for key in self.testConditions403:
            self.config.set('testConditions403', str(key), str(self.testConditions403[key]))
        for key in self.testConditions501:
            self.config.set('testConditions501', str(key), str(self.testConditions501[key]))
        for key in self.testConditions502:
            self.config.set('testConditions502', str(key), str(self.testConditions502[key]))
        for key in self.testConditions503:
            self.config.set('testConditions503', str(key), str(self.testConditions503[key]))
        for key in self.testConditions504:
            self.config.set('testConditions504', str(key), str(self.testConditions504[key]))
        for key in self.testConditions505:
            self.config.set('testConditions505', str(key), str(self.testConditions505[key]))
        for key in self.testConditions506:
            self.config.set('testConditions506', str(key), str(self.testConditions506[key]))
        for key in self.testConditions507:
            self.config.set('testConditions507', str(key), str(self.testConditions507[key]))
        for key in self.testConditions601:
            self.config.set('testConditions601', str(key), str(self.testConditions601[key]))
        for key in self.testConditions701:
            self.config.set('testConditions701', str(key), str(self.testConditions701[key]))
        for key in self.polExcel:
            self.config.set('polExcel', str(key), str(self.polExcel[key]))
        for key in self.snapshot:
            self.config.set('snapshot', str(key), str(self.snapshot[key]))

        for key in self.ini_Cond:
            self.config.set('ini_Cond', str(key), str(self.ini_Cond[key]))
        for key in self.pstestConditions12:
            self.config.set('pstestConditions12', str(key), str(self.pstestConditions12[key]))
        for key in self.pstestConditions31:
            self.config.set('pstestConditions31', str(key), str(self.pstestConditions31[key]))
        for key in self.pstestConditions32:
            self.config.set('pstestConditions32', str(key), str(self.pstestConditions32[key]))
        for key in self.Cond_1p4:
            self.config.set('Cond_1p4', str(key), str(self.Cond_1p4[key]))
        for key in self.Cond_1p6:
            self.config.set('Cond_1p6', str(key), str(self.Cond_1p6[key]))
        for key in self.excel:
            self.config.set('excel', str(key), str(self.excel[key]))

        with open(filePath, 'w') as f:
            self.config.write(f)

    def cleanup(self):
        self.save_config('guiFiles/config.ini')


