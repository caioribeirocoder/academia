class Pagamento:
    def __init__(self, id, id_aluno, id_plano, valor, forma_pagamento, data_venc, status="pendente"):
        self.id = id
        self.id_aluno = id_aluno
        self.id_plano = id_plano
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.data_venc = data_venc
        self.status = status

    def confirmar_analise(self):
        if self.status == "pendente":
            self.status = "em_analise"
        else:
            print("Transição inválida!")

    def confirmar_pago(self):
        if self.status == "em_analise":
            self.status = "pago"
        else:
            print("Transição inválida!")

    def confirmar_inadimplente(self):
        if self.status == "pendente":
            self.status = "inadimplente"
        else:
            print("Transição inválida!")

    def confirmar_cancelamento(self):
        if self.status == "inadimplente":
            self.status = "cancelado"
        else:
            print("Transição inválida!")

    def confirmar_estorno(self):
        if self.status == "pago":
            self.status = "estornado"
        else:
            print("Transição inválida!")