''' Provides the order of the images in the excel sheets created by wind '''

def imageOrderLTEScanner():
    return [
            'PCI',
            'PCI Legend',
            'RSRP',
            'RSRP Legend',
            'RSRQ',
            'RSRQ Legend',
            'CINR',
            'CINR Legend'
            ]

def imageOrderUMTSScanner():
    return [
            'PSC',
            'PSC Legend',
            'Ec',
            'Ec Legend',
            'Ec_Io',
            'Ec_Io Legend',
            'SIR',
            'SIR Legend'
            ]


def imageOrderWifi():
    return [
            'RSSI',
            'RSSI Legend',
            'SNR',
            'SNR Legend',
            'LinkSpeed',
            'LinkSpeed Legend',
            ]
