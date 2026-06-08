from geo_economic_service import GeoEconomicService


initial_investment = 50_000_000

cash_flows = [
    15_000_000,
    18_000_000,
    20_000_000,
    17_000_000,
    12_000_000
]

discount_rate = 0.12


discounted_flows = GeoEconomicService.calculate_discounted_flows(
    cash_flows=cash_flows,
    discount_rate=discount_rate
)

npv = GeoEconomicService.calculate_npv(
    initial_investment=initial_investment,
    cash_flows=cash_flows,
    discount_rate=discount_rate
)

payback_period = GeoEconomicService.calculate_payback_period(
    initial_investment=initial_investment,
    cash_flows=cash_flows
)

irr = GeoEconomicService.calculate_irr(
    initial_investment=initial_investment,
    cash_flows=cash_flows
)


print("Дисконтированные денежные потоки:")

for year, flow in enumerate(discounted_flows, start=1):
    print(f"{year} год: {flow:,.2f} руб.")

print()
print(f"NPV проекта: {npv:,.2f} руб.")

if npv > 0:
    print("Вывод: проект экономически целесообразен.")
else:
    print("Вывод: проект экономически нецелесообразен.")

if payback_period is not None:
    print(f"Срок окупаемости: {payback_period} год")
else:
    print("Проект не окупается за расчётный период.")

print(f"IRR проекта: {irr * 100:.2f}%")
