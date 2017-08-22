''' Provides the order of the images in the excel sheets created by wind '''

def imageOrderScanner():
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

def imageOrderWifi():
    return [
            'RSSI',
            'RSSI Legend',
            'SNR',
            'SNR Legend',
            'LinkSpeed',
            'LinkSpeed Legend',
            ]
