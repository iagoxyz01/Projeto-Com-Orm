async def test_get_produto_inexistente(client):

    response = await client.get("/produtos/9999")

    assert response.status_code == 404


async def test_atualizar_valor_produto(client):

    await client.post(
        "/produtos",
        json={
            "codigo": 1,
            "valor": 10.0,
            "tipo": 1
        }
    )

    response = await client.put(
        "/produtos/1/valor",
        json={
            "novo_valor": 25.0
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["alterou"] is True
