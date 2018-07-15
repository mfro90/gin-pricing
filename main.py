import data_collection.html_crawl2 as hc2
import pandas as pd

#last run: 15/07-2018
data = hc2.extract_data('https://www.hjhansen-vin.dk', 'https://www.hjhansen-vin.dk/gin.aspx?pageIndex=', 1, [])
df = pd.DataFrame(data)
df.to_csv('output_csv')
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'Ark1')
writer.save()