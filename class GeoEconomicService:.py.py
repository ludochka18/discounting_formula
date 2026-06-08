class GeoEconomicService:
    """
    Сервис для геолого-экономической оценки месторождения.
    """

    @staticmethod
    def discount_cash_flow(
        cash_flow: float,
        discount_rate: float,
        year: int
    ) -> float:
        """
        Дисконтирует денежный поток за конкретный год.
        """

        return cash_flow / (1 + discount_rate) ** year

    @staticmethod
    def calculate_discounted_flows(
        cash_flows: list[float],
        discount_rate: float
    ) -> list[float]:
        """
        Возвращает список дисконтированных денежных потоков.
        """

        discounted_flows = []

        for year, cash_flow in enumerate(cash_flows, start=1):
            discounted_flow = GeoEconomicService.discount_cash_flow(
                cash_flow=cash_flow,
                discount_rate=discount_rate,
                year=year
            )
            discounted_flows.append(discounted_flow)

        return discounted_flows

    @staticmethod
    def calculate_npv(
        initial_investment: float,
        cash_flows: list[float],
        discount_rate: float
    ) -> float:
        """
        Считает NPV проекта.
        """

        discounted_flows = GeoEconomicService.calculate_discounted_flows(
            cash_flows=cash_flows,
            discount_rate=discount_rate
        )

        npv = sum(discounted_flows) - initial_investment

        return npv

    @staticmethod
    def calculate_payback_period(
        initial_investment: float,
        cash_flows: list[float]
    ) -> int | None:
        """
        Считает простой срок окупаемости проекта.

        Возвращает номер года, когда проект окупился.
        Если проект не окупился, возвращает None.
        """

        accumulated_cash_flow = 0

        for year, cash_flow in enumerate(cash_flows, start=1):
            accumulated_cash_flow += cash_flow

            if accumulated_cash_flow >= initial_investment:
                return year

        return None

    @staticmethod
    def calculate_irr(
        initial_investment: float,
        cash_flows: list[float],
        min_rate: float = 0.0,
        max_rate: float = 1.0,
        precision: float = 0.0001
    ) -> float | None:
        """
        Приближённо считает IRR методом бинарного поиска.
        """

        while max_rate - min_rate > precision:
            middle_rate = (min_rate + max_rate) / 2

            npv = GeoEconomicService.calculate_npv(
                initial_investment=initial_investment,
                cash_flows=cash_flows,
                discount_rate=middle_rate
            )

            if npv > 0:
                min_rate = middle_rate
            else:
                max_rate = middle_rate

        return (min_rate + max_rate) / 2
