import json
from datetime import datetime

def get_dat(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        data: object = json.load(file)
        return data

def get_operations_executed(data):
    operations_executed = []
    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            operations_executed.append(operation)
    operations_with_from = []
    for operation in operations_executed:
        if 'from' in operation:
            operations_with_from.append(operation)
    return operations_with_from

def get_last_five_operations(operations_with_from, num_of_operations):
    operations_sort = sorted(operations_with_from, key=lambda operation: operation['date'], reverse=True)
    last_five_operations = operations_sort[0:num_of_operations]
    return last_five_operations

def get_operations_formatted(last_five_operations):
    operations_formatted_list = []
    for operation in last_five_operations:
        date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = operation['description']
        payer_info, payment_method = '', ''
        if 'from' in operation:
            payer = operation['from'].split()
            payment_method = payer.pop(-1)
            if payer[0] == 'Счет':
                payment_method_from = f'**{payment_method[-4:]}'
            else:
                payment_method_from = f'**{payment_method[4:]} {payment_method[4:6]}** ****{payment_method[-4:]}'
            payer_info = ' '.join(payer)
        recipient = f"{operation['to'].split()[0]} **{operation['to'][-4:]}"
        operation_amount = f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
        operations_formatted_list.append(
            f"""
         {date} {description}
         {payer_info} {payment_method_from}-> {recipient}
         {operation_amount}
         """)
    return operations_formatted_list