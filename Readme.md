# API de Viagens

```json
{
  "rotas": [
    {
      "endpoint": "/api/viagem/cadastro",
      "metodo": "POST",
      "descricao": "Cria uma nova viagem",
      "request_body": {
        "colaborador_id": 1,
        "origem": "São Paulo - SP",
        "destino": "Rio de Janeiro - RJ",
        "data_inicio": "2025-09-10",
        "data_fim": "2025-09-15",
        "motivo": "Reunião com cliente",
        "status": "Aprovada"
      },
      "response_exemplo": {
        "message": "Viagem criada com sucesso",
        "viagem_id": 1,
        "status_code": 201
      }
    },
    {
      "endpoint": "/api/viagem",
      "metodo": "GET",
      "descricao": "Lista todas as viagens",
      "response_exemplo": {
        "message": "Lista de viagens recuperada com sucesso",
        "viagens": [
          {
            "id": 1,
            "colaborador_id": 1,
            "origem": "São Paulo - SP",
            "destino": "Rio de Janeiro - RJ",
            "data_inicio": "2025-09-10",
            "data_fim": "2025-09-15",
            "motivo": "Reunião com cliente",
            "status": "Aprovada"
          }
        ],
        "status_code": 200
      }
    },
    {
      "endpoint": "/api/viagem/<id>",
      "metodo": "GET",
      "descricao": "Obtém detalhe de uma viagem",
      "response_exemplo": {
        "message": "Viagem encontrada com sucesso",
        "viagem": {
          "id": 1,
          "colaborador_id": 1,
          "origem": "São Paulo - SP",
          "destino": "Rio de Janeiro - RJ",
          "data_inicio": "2025-09-10",
          "data_fim": "2025-09-15",
          "motivo": "Reunião com cliente",
          "status": "Aprovada"
        },
        "status_code": 200
      }
    },
    {
      "endpoint": "/api/viagem/<id>",
      "metodo": "PUT",
      "descricao": "Edita uma viagem existente",
      "request_body": {
        "colaborador_id": 1,
        "origem": "São Paulo - SP",
        "destino": "Rio de Janeiro - RJ",
        "data_inicio": "2025-09-11",
        "data_fim": "2025-09-16",
        "motivo": "Reunião reagendada",
        "status": "Aprovada"
      },
      "response_exemplo": {
        "message": "Viagem editada com sucesso",
        "viagem_id": 1,
        "status_code": 200
      }
    },
    {
      "endpoint": "/api/viagem/<id>",
      "metodo": "DELETE",
      "descricao": "Remove uma viagem pelo ID",
      "response_exemplo": {
        "message": "Viagem removida com sucesso",
        "status_code": 200
      },
      {
  "endpoint": "/api/viagem/colaborador/<id_colaborador>",
  "metodo": "GET",
  "descricao": "Lista todas as viagens de um colaborador específico",
  "response_exemplo": {
    "message": "Lista de viagens recuperada com sucesso",
    "viagens": [
      {
        "id": 1,
        "colaborador_id": 1,
        "origem": "São Paulo - SP",
        "destino": "Rio de Janeiro - RJ",
        "data_inicio": "2025-09-10",
        "data_fim": "2025-09-15",
        "motivo": "Reunião com cliente",
        "status": "Aprovada"
      }
    ],
    "status_code": 200
        }
    }
    }
  ]
}
