''' Provides the order of the images in the excel sheets created by wind '''

def ImageOrderScanner():
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

def ImageOrderWifi():
    return [
            'RSSI',
            'RSSI Legend',
            'SNR',
            'SNR Legend',
            'LinkSpeed',
            'LinkSpeed Legend',
            ]
