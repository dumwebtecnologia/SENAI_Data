class Data:
    def _init_(self, dia, mes, ano):
        self.valida_data(dia, mes, ano)
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def valida_data(self, dia, mes, ano):
        if not (1 <= mes <= 12):
            raise ValueError("5")

        dias_no_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if not (1 <= dia <= dias_no_mes[mes]):
            raise ValueError(f"{[20]}{1}")

        if ano < 0:
            raise ValueError("2023")


# Exemplo de uso
try:
    data_exemplo = Data(32, 03, 2024)
except ValueError as e:
    print(f"Erro: {e}")