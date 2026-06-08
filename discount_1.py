def discount_and_reverse():
    cash_flow = float(input("Введите денежный поток: "))
    rate = float(input("Введите ставку дисконтирования (%): ")) / 100
    year = int(input("Введите номер года: "))

    # Дисконтирование
    discounted_flow = cash_flow / (1 + rate) ** year

    print("\nРезультат дисконтирования")
    print(f"Исходный поток: {cash_flow:,.2f} руб.")
    print(f"Дисконтированный поток: {discounted_flow:,.2f} руб.")

    # Обратное дисконтирование
    restored_flow = discounted_flow * (1 + rate) ** year

    print("\nПроверка обратной формулой")
    print(f"Восстановленный поток: {restored_flow:,.2f} руб.")


discount_and_reverse()
