from finglish import f2p
import csv
import json
import pandas as pd
#
i = 1
final_result = {}
while i > 0:
    m = input("Your text: ")
    l=(f2p(m))
    print(l)
    final_result.update({str(m): str(l)})
    with open("test1.json", "w")as jsfile:
        json.dump(final_result, jsfile, indent=2, ensure_ascii=False)

