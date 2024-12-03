class Restaurant:
    """Model de restaurante simples."""

    # Melhoria, adicionar anotação dos atributos (Fixed)
    def __init__(self, restaurant_name: str, cuisine_type: str):

        # Melhoria, validação nos atributos da classe (fixed)
        if not isinstance(restaurant_name, str):
            raise TypeError("O atributo 'restaurant_name' deve ser uma string.")
        if not isinstance(cuisine_type, str):
            raise TypeError("O atributo 'cuisine_type' deve ser uma string.")

        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        # Bug, está exibindo a mesma variável para ambas descrições, deveria ser restaurante_name e cuisine_type (Fixed)
        # Bug, Palavras em inglês misturadas com palavras em português (Fixed)
        # Bug, Palavra 'restaturante' ao invés de 'restaurante' (FIXED)
        result = f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}."

        # Bug, Palavra 'restaturante' ao invés de 'restaurante' (FIXED)
        result += f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto."
        return result

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            # Bug, deveria ser essa atribuição -> self.open = True (FIXED)
            self.open = True
            # Bug, não faz sentido colocar number_served negativo, apenas remover essa linha. (Fixed)
            #self.number_served = -2
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""

        # Melhoria, Validar o tipo recebido, para não receber valores inválidos (FIXED)
        if type(total_customers) is not int:
            return "Parametro invalido"

        if self.open:
            self.number_served = total_customers

        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers : int):
        """Aumenta número total de clientes atendidos por este restaurante."""

        # Melhoria Validar tipo de variável recebida (FIXED)
        if type(more_customers) is not int:
            return "Parametro invalido"

        if self.open:
            # Bug, deveria somar e não atribuir (FIXED)
            self.number_served += more_customers
        else:
            return f"{self.restaurant_name} está fechado!"
