from src.models.restaurant import Restaurant
import pytest

class TestRestaurant:

    def test_describe_restaurant_success(self):
        # Setup
        restaurant =  Restaurant("Seu Alfredo", "Comida Italiana")
        resultado_esperado = (f"Esse restaurante chama {restaurant.restaurant_name} e serve {restaurant.cuisine_type}."
                              f"Esse restaurante está servindo {restaurant.number_served} consumidores desde que está aberto.")

        # Chamada
        resultado = restaurant.describe_restaurant()

        # Validação
        assert resultado == resultado_esperado, f"Esperado a mensagem: {resultado_esperado}, recebido: {resultado}"

    def test_open_restaurant(self):
        # Setup
        restaurant = Restaurant("Seu Alfredo", "Comida Italiana")
        resultado_esperado = f"{restaurant.restaurant_name} agora está aberto!"

        # Chamada
        resultado = restaurant.open_restaurant()

        # Validação
        assert resultado == resultado_esperado, f"Esperado a mensagem: {resultado_esperado}, recebido: {resultado}"
        assert restaurant.open is True, f"Esperado: {True}, recebido: {restaurant.open}"

    def test_open_restaurant_for_an_already_opened_restaurant(self):
        # Setup
        restaurant = Restaurant("Seu Alfredo", "Comida Italiana")
        restaurant.open_restaurant()
        resultado_esperado = f"{restaurant.restaurant_name} já está aberto!"

        # Chamada
        resultado = restaurant.open_restaurant()

        # Validação
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, recebido: {resultado}"
        assert restaurant.open is True, f"Esperado: {True}, recebido: {restaurant.open}"

    def test_close_restaurant(self):
        # Setup
        restaurant = Restaurant("Seu Alfredo", "Comida Italiana")
        restaurant.open_restaurant()
        resultado_esperado = f"{restaurant.restaurant_name} agora está fechado!"

        # Chamada
        resultado = restaurant.close_restaurant()

        # Validação
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, recebido: {resultado}"
        assert restaurant.open is False, f"Esperado: {False}, recebido: {restaurant.open}"

    def test_close_restaurant_for_an_already_closed_restaurant(self):
        # Setup
        restaurant = Restaurant("Seu Alfredo", "Comida Italiana")
        resultado_esperado = f"{restaurant.restaurant_name} já está fechado!"

        # Chamada
        resultado = restaurant.close_restaurant()

        # Validação
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, recebido: {resultado}"
        assert restaurant.open is False, f"Esperado: {False}, recebido: {restaurant.open}"

    def test_set_number_served_success(self):
        # Setup
        restaurant = Restaurant("Seu Alfredo", "Comida Italiana")
        restaurant.open_restaurant()
        resultado_esperado = 10

        # Chamada
        resultado = restaurant.set_number_served(10)

        # Validação
        assert restaurant.number_served == resultado_esperado, f"Esperado: {resultado_esperado}, recebido: {restaurant.number_served}"

    @pytest.mark.parametrize("test_data", ["HAHAHA", [], {}, 2.3, ""])
    def test_set_number_served_invalid_parameter(self, test_data):
        # Setup
        restaurant = Restaurant("Seu Alfredo", "Comida Italiana")
        restaurant.open_restaurant()
        resultado_esperado = "Parametro invalido"

        # Chamada
        resultado = restaurant.set_number_served(test_data)

        # Validação
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, recebido: {resultado}"

    def test_set_number_served_for_closed_restaurant(self):
        # Setup
        restaurant = Restaurant("Seu Alfredo", "Comida Italiana")
        resultado_esperado = f"{restaurant.restaurant_name} está fechado!"

        # Chamada
        resultado = restaurant.set_number_served(10)

        # Validação
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, recebido: {resultado}"

    def test_increment_number_served_success(self):
        # Setup
        restaurant = Restaurant("Seu Alfredo", "Comida Italiana")
        restaurant.open_restaurant()
        restaurant.set_number_served(10)
        restaurant.increment_number_served(10)
        resultado_esperado = 20

        # Chamada
        resultado = restaurant.number_served

        # Validação
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, recebido: {resultado}"

    def test_increment_number_served_closed_restaurant(self):
        # Setup
        restaurant = Restaurant("Seu Alfredo", "Comida Italiana")
        restaurant.open_restaurant()
        restaurant.set_number_served(10)
        restaurant.close_restaurant()
        resultado_esperado = f"{restaurant.restaurant_name} está fechado!"

        # Chamada
        resultado = restaurant.increment_number_served(10)

        # Validação
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, recebido: {resultado}"

    @pytest.mark.parametrize("test_data", ["HAHAHA", [], {}, 2.3, ""])
    def test_increment_number_served_invalid_parameter(self, test_data):
        # Setup
        restaurant = Restaurant("Seu Alfredo", "Comida Italiana")
        restaurant.open_restaurant()
        restaurant.set_number_served(10)
        resultado_esperado = "Parametro invalido"

        # Chamada
        resultado = restaurant.increment_number_served(test_data)

        # Validação
        assert resultado == resultado_esperado, f"Esperado: {resultado_esperado}, recebido: {resultado}"
