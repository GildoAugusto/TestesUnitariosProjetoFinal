from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    # Melhoria, adicionar anotação dos atributos (Fixed)
    def __init__(self, restaurant_name: str, cuisine_type: str, flavors_list: list[str]):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
    # Melhoria, validação nos atributos da classe (fixed)
        if not isinstance(restaurant_name, str):
            raise TypeError("O atributo 'restaurant_name' deve ser uma string.")
        if not isinstance(cuisine_type, str):
            raise TypeError("O atributo 'cuisine_type' deve ser uma string.")
        if not isinstance(flavors_list, list):
            raise TypeError("O atributo 'flavors_list' deve ser uma lista de strings.")

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        # Melhoria, validar se o restaurante está aberto e possui estoque (FIXED)
        if self.flavors:
            result = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                result += f"\t-{flavor}"
            return result
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""

        # Melhoria, validar o tipo da váriavel 'flavor' (fixed)
        if not isinstance(flavor, str):
            return f"Parametro 'flavor' invalido!"

        # Bug, deveria mostrar qual sabor não tem e não todos os sabores (fixed)
        if self.flavors:
            if flavor in self.flavors:
                # Bug, deveria mostrar qual sabor  tem e não todos os sabores (fixed)
                return f"Temos no momento {flavor}!"
            else:
                # Bug, deveria mostrar qual sabor não tem e não todos os sabores (fixed)
                return f"Não temos no momento {flavor}!"
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor: str):
        """Add o sabor informado ao estoque."""

        # Melhoria, validar o tipo da váriavel 'flavor' (fixed)
        if not isinstance(flavor, str):
            return f"Parametro 'flavor' invalido!"

        if self.flavors:
            if flavor in self.flavors:
                # Melhoria, removendo o \n, não parece estar sendo utilizado
                return "Sabor já disponivel!"
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            # Bug - Quando não havia nenhum produto, não seria possível adicionar nada (FIXED)
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"
