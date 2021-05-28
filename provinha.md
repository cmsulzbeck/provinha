
# 1 Tratamento de dados (aprox. 30 min)

  

Crie uma função ou um notebook jupyter para realizar o processamento abaixo

  

- Importar o conjunto de dados presentes na pasta **"bases"**

	-  **airbnb_ny_2019.csv**

	-  **mapeamento_vizinhanca.csv**

- Remover linhas duplicadas

- Remover linhas com valores nulos

- Juntar as **bases airbnb_ny_2019** e **mapeamento_vizinhanca** através de um join (**neighbourhood** <-> **vizinhanca**)

- Remover a coluna **vizinhanca** após o join

- Trocar o nome da coluna de **vizinhanca_grupo** para **neighbourhood_group**

- Filtre a coluna neighbourhood_group e mantenha apenas os valores 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'

- Após todos os filtros mencionados acima, gere uma base chamada residencias.csv

- A partir da base **residencias.csv**, gere também uma base **media_preco.csv** com a média de preços por tipo de quarto (coluna room_type) e grupo do bairro (coluna neighbourhood_group)

  

As bases que esperamos obter ao final desta etapa estão na pasta **bases_tratadas**.

  

O que será avaliado nesse teste será o seu domínio das ferramentas e bibliotecas python para manipulação de dados (pandas, numpy, etc).

  
  
  
  

# 2 Web Api (aprox. 1h30)

  

Para persistir os dados utilize o sqlite e para construir a sua web api utilize os frameworks **flask-restplus** ou **flask-restx** e as duas bases geradas pela etapa anterior:

  

-  **residencias.csv**

-  **media_preco.csv**

  

Caso não tenha feito a etapa anterior, essas duas bases csv foram disponibilizadas na pasta **bases_tratada**.

  

A sua aplicação deve ter 3 endpoints, 2 get e 1 post, conforme abaixo:

  

##### 1. Lista de todas as residências com opção de filtros via query string

  

exemplo:

```json

get /residencias?neighbourhood_group=Manhattan

  
[


	{
  

		'id': 36411407,


		'name': 'Brand  new  1  bedroom  steps  from  Soho!',

		  
		'host_id': 33917435,


		'host_name': 'Mike',


		'neighbourhood_group': 'Manhattan',


		'neighbourhood': 'Lower  East  Side',


		'latitude': 40.71825,


		'longitude': -73.99019,


		'room_type': 'Entire  home/apt',
	  

		'price': 150,
	  

		'minimum_nights': 4,
		  

		'number_of_reviews': 1,

		  
		'last_review': '2019-07-06',
		  

		'reviews_per_month': 1.0,

		  
		'calculated_host_listings_count': 1,

		  
		'availability_365': 13
	  

	},
	  

	{

	  
		'id': 36425863,
		  

		'name': 'Lovely  Privet  Bedroom  with  Privet  Restroom',
		  

		'host_id': 83554966,
		  

		'host_name': 'Rusaa',
		  

		'neighbourhood_group': 'Manhattan',
		  

		'neighbourhood': 'Upper  East  Side',
		  

		'latitude': 40.78099,
		  

		'longitude': -73.95366,
		  

		'room_type': 'Private  room',
		  

		'price': 129,
		  

		'minimum_nights': 1,
		  

		'number_of_reviews': 1,
		  

		'last_review': '2019-07-07',

		  
		'reviews_per_month': 1.0,
		  

		'calculated_host_listings_count': 1,

		  
		'availability_365': 147
		  

	}
	  

]

```

  

##### 2. Média de preços por 'neighbourhood_group' e 'room_type'

exemplo:

  

```json

get /preco-medio?neighbourhood_group=Manhattan


[

	{

		'neighbourhood_group': 'Manhattan',

		'room_type': 'Entire  home/apt',

		'price': 230.20096366191527

	},

	{

		'neighbourhood_group': 'Manhattan',

		'room_type': 'Private  room',

		'price': 106.60748849754086

	},

	{

		'neighbourhood_group': 'Manhattan',

		'room_type': 'Shared  room',

		'price': 77.98033707865169

	}

]

```

  

##### 3. Salvar um "like" da propriedade

exemplo

  

```json

post /residencias

{
	'id'=36411407
	'like'=true
}

```

  
  

# 3 Frontend (aprox. 2h)

  

Para construção da sua aplicação utilize o framework **VueJs** e os json gerados pelos endpoints da etapa anterior.

Caso não tenha feito a etapa anterior, essas duas bases json foram disponibilizadas na pasta **bases_tratadas**.

  

Construa as seguintes páginas:

  

##### 1. Exibir uma lista/coleção de residências

  

##### 2. Página individual da residência selecionada pelo usuário na página anterior

  

##### 3. Página com média de preço

  
  

O que será avaliado nesse teste será o seu domínio do Framework Vue e design páginas web