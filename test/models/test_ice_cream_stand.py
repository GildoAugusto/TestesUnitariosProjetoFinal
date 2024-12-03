from src.models.ice_cream_stand import IceCreamStand
import pytest

class TestIceCreamStand:

    def test_flavors_available_success(self):
        # Setup
        test_flavors = ["Morango", "Chocolate", "Creme"]
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)
        icecream.open_restaurant()

        # Chamada
        resultado = icecream.flavors_available()

        # Validação
        resultado_esperado = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
        for flavor in test_flavors:
            resultado_esperado += f"\t-{flavor}"

        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    def test_flavors_out_of_stock(self):
        # Setup
        test_flavors = []
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)

        # Chamada
        resultado = icecream.flavors_available()

        # Validação
        resultado_esperado = "Estamos sem estoque atualmente!"
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    def test_find_flavor_success(self):
        # Setup
        test_flavors = ["Creme", "Morango", "Chocolate", "Baunilha", "Chocolate Amargo"]
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)

        # Chamada
        resultado = icecream.find_flavor("Morango")

        # Validação
        resultado_esperado = f"Temos no momento Morango!"
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    @pytest.mark.parametrize("test_data", [1234123,[], {}, 2.3])
    def test_find_flavor_invalid_parameter(self, test_data):
        # Setup
        test_flavors = ["Creme", "Morango", "Chocolate", "Baunilha", "Chocolate Amargo"]
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)

        # Chamada
        resultado = icecream.find_flavor(test_data)

        # Validação
        resultado_esperado = f"Parametro 'flavor' invalido!"
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    def test_find_flavor_that_not_exist(self):
        # Setup
        test_flavors = ["Creme", "Morango", "Chocolate", "Baunilha", "Chocolate Amargo"]
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)

        # Chamada
        resultado = icecream.find_flavor("Maracujá")

        # Validação
        resultado_esperado = f"Não temos no momento Maracujá!"
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    def test_find_flavor_there_is_no_flavors_registered(self):
        # Setup
        test_flavors = []
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)

        # Chamada
        resultado = icecream.find_flavor("Maracujá")

        # Validação
        resultado_esperado = f"Estamos sem estoque atualmente!"
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    def test_add_flavor_success(self):
        # Setup
        test_flavors = ["Creme", "Chocolate", "Morango", "Pistache"]
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)

        # Chamada
        resultado = icecream.add_flavor("Maracujá")

        # Validação
        resultado_esperado = f"Maracujá adicionado ao estoque!"
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    def test_add_flavor_out_of_stock(self):
        # Setup
        test_flavors = []
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)

        # Chamada
        resultado = icecream.add_flavor("Maracujá")

        # Validação
        resultado_esperado = f"Maracujá adicionado ao estoque!"
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    def test_add_flavor_that_already_exist(self):
        # Setup
        test_flavors = ["Maracujá"]
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)

        # Chamada
        resultado = icecream.add_flavor("Maracujá")

        # Validação
        resultado_esperado = f"Sabor já disponivel!"
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"

    @pytest.mark.parametrize("test_data", [1234123,[], {}, 2.3])
    def test_add_flavor_invalid_parameter(self, test_data):
        # Setup
        test_flavors = ["Maracujá"]
        icecream = IceCreamStand("Seu Romário", "Culinária Francesa", test_flavors)

        # Chamada
        resultado = icecream.add_flavor(test_data)

        # Validação
        resultado_esperado = f"Parametro 'flavor' invalido!"
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, Recebido: {resultado}"
