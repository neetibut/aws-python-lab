{"filter":false,"title":"calc_weight_json.py","tooltip":"/files/calc_weight_json.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":22},"action":"insert","lines":["import jsonFileHandler"],"id":11}],[{"start":{"row":0,"column":22},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":22},"action":"insert","lines":["import jsonFileHandler"],"id":13}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":22},"action":"remove","lines":["import jsonFileHandler"],"id":14}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":57},"action":"insert","lines":["data = jsonFileHandler.readJsonFile('files/insulin.json')"],"id":15}],[{"start":{"row":2,"column":57},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":13,"column":35},"action":"insert","lines":["if data != \"\" :","    bInsulin = data['molecules']['bInsulin']","    aInsulin = data['molecules']['aInsulin']","    insulin = bInsulin + aInsulin","    molecularWeightInsulinActual = data['molecularWeightInsulinActual']","    print('bInsulin: ' + bInsulin)","    print('aInsulin: ' + aInsulin)","    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))","else:","    print(\"Error. Exiting program\")"],"id":17}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":18}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "],"id":19}],[{"start":{"row":12,"column":4},"end":{"row":22,"column":122},"action":"insert","lines":["# Calculating the molecular weight of insulin  ","# Getting a list of the amino acid (AA) weights  ","aaWeights = data['weights']","# Count the number of each amino acids  ","aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  ","# Multiply the count by the weights  ","molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in","['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  ","print(\"The rough molecular weight of insulin: \" +","str(molecularWeightInsulin))","print(\"Percent error: \" + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))"],"id":20}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "],"id":21},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":23,"column":5},"end":{"row":23,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1723724139515,"hash":"5cbcb8fd4c7c7e726dd79863f59b54f6142ceddc"}