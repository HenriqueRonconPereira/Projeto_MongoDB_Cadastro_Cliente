// Grupo
// Bruno Ramos da Costa - RM551942
// Guilherme Faria de Aguiar - RM551374
// Henrique Roncon Pereira - RM99161
// Lucas Carabolad Bob - RM550519
// Thiago Ulrych - RM9795

// Coleção: Produtos
db.Produtos.insertMany([
    {
        "_id": ObjectId("507f1f77bcf86cd799439011"),
        "nome": "Smartphone XYZ",
        "marca": "TechCorp",
        "categoria": "Celulares",
        "preco": 1999.99,
        "estoque": 20,
        "descricao": "Smartphone com tela AMOLED e câmera dupla",
        "especificacoes": {
            "memoria": "128GB",
            "bateria": "4000mAh",
            "cor": "Preto"
        }
    },
    {
        "_id": ObjectId("507f1f77bcf86cd799439012"),
        "nome": "Notebook Pro",
        "marca": "LaptopPlus",
        "categoria": "Computadores",
        "preco": 3499.99,
        "estoque": 15,
        "descricao": "Notebook de alta performance com 16GB de RAM",
        "especificacoes": {
            "memoria": "16GB",
            "processador": "Intel Core i7",
            "cor": "Prata"
        }
    },
    {
        "_id": ObjectId("507f1f77bcf86cd799439013"),
        "nome": "Fone Bluetooth",
        "marca": "SoundWave",
        "categoria": "Acessórios",
        "preco": 299.99,
        "estoque": 50,
        "descricao": "Fone de ouvido sem fio com cancelamento de ruído",
        "especificacoes": {
            "autonomia": "20h",
            "cor": "Branco"
        }
    },
    {
        "_id": ObjectId("507f1f77bcf86cd799439014"),
        "nome": "Smart TV 50 Polegadas",
        "marca": "ScreenMaster",
        "categoria": "TVs",
        "preco": 2799.99,
        "estoque": 10,
        "descricao": "Smart TV 4K com HDR e sistema operacional integrado",
        "especificacoes": {
            "resolucao": "4K",
            "sistema": "Android TV",
            "cor": "Preto"
        }
    }
]);

// Coleção: Clientes
db.Clientes.insertMany([
    {
        "_id": ObjectId("507f191e810c19729de860ea"),
        "nome": "João Silva",
        "email": "joao.silva@email.com",
        "telefone": "11987654321",
        "endereco": {
            "rua": "Rua das Flores",
            "numero": "123",
            "cidade": "São Paulo",
            "estado": "SP",
            "cep": "01234-567"
        }
    },
    {
        "_id": ObjectId("507f191e810c19729de860eb"),
        "nome": "Maria Oliveira",
        "email": "maria.oliveira@email.com",
        "telefone": "21976543210",
        "endereco": {
            "rua": "Avenida Central",
            "numero": "456",
            "cidade": "Rio de Janeiro",
            "estado": "RJ",
            "cep": "21000-123"
        }
    },
    {
        "_id": ObjectId("507f191e810c19729de860ec"),
        "nome": "Carlos Pereira",
        "email": "carlos.pereira@email.com",
        "telefone": "31965432109",
        "endereco": {
            "rua": "Rua dos Lírios",
            "numero": "789",
            "cidade": "Belo Horizonte",
            "estado": "MG",
            "cep": "30123-456"
        }
    },
    {
        "_id": ObjectId("507f191e810c19729de860ed"),
        "nome": "Ana Souza",
        "email": "ana.souza@email.com",
        "telefone": "41987654321",
        "endereco": {
            "rua": "Rua das Palmeiras",
            "numero": "101",
            "cidade": "Curitiba",
            "estado": "PR",
            "cep": "80000-789"
        }
    }
]);

// Coleção: Pedidos
db.Pedidos.insertMany([
    {
        "_id": ObjectId("507f1f77bcf86cd799439015"),
        "id_cliente": ObjectId("507f191e810c19729de860ea"),
        "data_pedido": "2024-10-28T10:30:00Z",
        "status": "Finalizado",
        "itens": [
            {"id_produto": ObjectId("507f1f77bcf86cd799439011"), "quantidade": 2, "preco": 1999.99},
            {"id_produto": ObjectId("507f1f77bcf86cd799439013"), "quantidade": 1, "preco": 299.99}
        ],
        "total": 4299.97
    },
    {
        "_id": ObjectId("507f1f77bcf86cd799439016"),
        "id_cliente": ObjectId("507f191e810c19729de860eb"),
        "data_pedido": "2024-10-28T15:45:00Z",
        "status": "Em Processamento",
        "itens": [
            {"id_produto": ObjectId("507f1f77bcf86cd799439012"), "quantidade": 1, "preco": 3499.99}
        ],
        "total": 3499.99
    },
    {
        "_id": ObjectId("507f1f77bcf86cd799439017"),
        "id_cliente": ObjectId("507f191e810c19729de860ec"),
        "data_pedido": "2024-10-29T09:00:00Z",
        "status": "Cancelado",
        "itens": [
            {"id_produto": ObjectId("507f1f77bcf86cd799439014"), "quantidade": 1, "preco": 2799.99}
        ],
        "total": 2799.99
    },
    {
        "_id": ObjectId("507f1f77bcf86cd799439018"),
        "id_cliente": ObjectId("507f191e810c19729de860ed"),
        "data_pedido": "2024-10-30T12:20:00Z",
        "status": "Finalizado",
        "itens": [
            {"id_produto": ObjectId("507f1f77bcf86cd799439011"), "quantidade": 1, "preco": 1999.99},
            {"id_produto": ObjectId("507f1f77bcf86cd799439013"), "quantidade": 2, "preco": 299.99}
        ],
        "total": 2599.97
    }
]);

// Consultas (find)

// 1. Listar todos os produtos de uma categoria específica
db.Produtos.find({ "categoria": "Celulares" });

// 2. Consultar pedidos de um cliente específico pelo nome
db.Pedidos.find({
    "id_cliente": db.Clientes.findOne({ "nome": "João Silva" })._id
});

// 3. Listar todos os clientes que realizaram pelo menos um pedido
db.Clientes.find({
    "_id": { $in: db.Pedidos.distinct("id_cliente") }
});

// 4. Consultar os produtos com estoque abaixo de um determinado nível
db.Produtos.find({ "estoque": { $lte: 10 } });

// 5. Listar pedidos com o valor total superior a um valor específico
db.Pedidos.find({ "total": { $gt: 3000 } });

// 6. Exibir o número total de pedidos realizados por cada cliente
db.Pedidos.aggregate([
    { $group: { _id: "$id_cliente", totalPedidos: { $sum: 1 } } },
    { $lookup: { from: "Clientes", localField: "_id", foreignField: "_id", as: "cliente" } },
    { $unwind: "$cliente" },
    { $project: { "cliente.nome": 1, totalPedidos: 1 } }
]);

// 7. Consultar detalhes dos produtos em um pedido específico
db.Pedidos.aggregate([
    { $match: { "_id": ObjectId("507f1f77bcf86cd799439015") } },
    { $unwind: "$itens" },
    {
        $lookup: {
            from: "Produtos",
            localField: "itens.id_produto",
            foreignField: "_id",
            as: "detalhes_produto"
        }
    },
    { $unwind: "$detalhes_produto" },
    {
        $project: {
            "detalhes_produto.nome": 1,
            "detalhes_produto.categoria": 1,
            "detalhes_produto.preco": 1,
            "itens.quantidade": 1
        }
    }
]);

// 8. Exibir o valor total das vendas por produto
db.Pedidos.aggregate([
    { $unwind: "$itens" },
    {
        $group: {
            _id: "$itens.id_produto",
            totalVendas: { $sum: { $multiply: ["$itens.quantidade", "$itens.preco"] } }
        }
    },
    {
        $lookup: {
            from: "Produtos",
            localField: "_id",
            foreignField: "_id",
            as: "produto"
        }
    },
    { $unwind: "$produto" },
    { $project: { "produto.nome": 1, "produto.categoria": 1, totalVendas: 1 } }
]);

// 9. Consultar um cliente específico pelo nome
db.Clientes.find({
    "nome": "Testinho"
});
