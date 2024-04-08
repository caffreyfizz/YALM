def get_spn(toponym):
    delta1 = str(abs(float(toponym['lowerCorner'].split()[0]) - float(toponym['lowerCorner'].split()[1])))
    delta2 = str(abs(float(toponym['upperCorner'].split()[0]) - float(toponym['upperCorner'].split()[1])))
    spn = ",".join([delta1, delta2])
    return spn