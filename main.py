from develop import utils


def main():
    filename = 'operations.json'
    amount_of_operations = int(input('Введите количество последних операций (не более 5): '))

    if amount_of_operations < 6:
        data = utils.get_data(filename)
        operations_executed = utils.get_operations_executed(data)
        last_num_operations = utils.get_last_five_operations(operations_executed, amount_of_operations)
        operations_formatted = utils.get_operations_formatted(last_num_operations)

        for string in operations_formatted:
            print(f'{string}\n')

    else:
        print("Запросите 5 или менее последних операций")
        return main()


if __name__ == "__main__":
    main()
