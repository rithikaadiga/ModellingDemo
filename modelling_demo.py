import json

import pandas as pd

cgul_data = pd.read_parquet('demo_cguls.parquet')
with open('demo_portfolio.json') as file:
    portfolio_data = json.load(file)

retention_value = portfolio_data["Deals"][0]["Covers"][0]["Terms"][0]["OccurrenceRetention"]
limit_value = portfolio_data["Deals"][0]["Covers"][0]["Terms"][1]["OccurrenceLimit"]


event_counter = {event_id: 0 for event_id in cgul_data.event_id.unique()}
cashflows_counter = {event_id: 0 for event_id in cgul_data.event_id.unique()}

for obj in cgul_data:
    new_loss = event_counter.get(obj.event_id) + obj.cgul
    if new_loss <= retention_value:
        # No Losses, phew!
        event_counter[obj.event_id] = 0
        cashflows_counter[obj.event_id] = 0
    elif (new_loss >= retention_value & new_loss <= limit_value):
        # A loss
        event_counter[obj.event_id] = 0
        cashflows_counter[obj.event_id] = 0
    else:
        #maxed out loss
        event_counter[obj.event_id] = 0
        cashflows_counter[obj.event_id] = 0 

print(event_counter)
print(cashflows_counter)
    







