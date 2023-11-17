#! /bin/env python3

# - Intenção A: Pergunta sobre como atualizar as informações de pagamento.
#   - Perguntas relacionadas: "Como posso atualizar meu cartão de crédito?", "Preciso mudar a forma de pagamento, o que fazer?", "Quero atualizar minhas informações de pagamento", "Método de pagamento desatualizado, como proceder para atualizar?"

# - Intenção B: Pergunta sobre como acompanhar o status do pedido.
#   - Perguntas relacionadas: "Onde vejo o status do meu pedido?", "Como faço para rastrear meu pedido?", "Quero saber onde está meu pedido, como faço?", "Status de entrega, como consultar?"

import re

intencoes = {
    "pagamento": [r"(?:(?:[Aa]tualizar)|(.*[Mm]udar*.)"],
    "status": [r"(?:(?:[Ss]tatus)|(.*[Oo]nde*.)|(.*pedido*.))"],
    "sair": [r"\b(?:[Ss]air)"]
}

acoes = {
    "pagamento": lambda _: f"Para atualizar/mudar...",
    "status": lambda _: f"Para acompanhar o status do seu pedido...",
    "sair": lambda _: exit()
}


def process_command(command:str):
    for intencao, patterns in intencoes.items():
        for pattern in patterns:
            match = re.match(pattern, command, re.IGNORECASE)
            if match:
                return acoes[intencao](match.group(len(match.groups())))


def main(args=None):
    
    while True:
        command = input("Como posso ajudar?! \n")
        print(process_command(command))

if __name__ == '__main__':
    main()
