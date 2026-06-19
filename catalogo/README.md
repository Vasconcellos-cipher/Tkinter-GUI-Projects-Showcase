# 🎬 Media Catalogue System

Um sistema de catálogo de mídia desenvolvido em **Python** com **Tkinter**, permitindo gerenciar filmes e séries através de uma interface gráfica simples e intuitiva.

## 📷 Interface:

<img width="647" height="626" alt="image" src="https://github.com/user-attachments/assets/d789576a-71e9-4c9d-b1e6-947d8715c015" />


---

## 🚀 Funcionalidades

✅ Adicionar filmes

✅ Adicionar séries de TV

✅ Buscar conteúdos por nome

✅ Filtrar buscas por tipo (Filme ou Série)

✅ Remover itens do catálogo

✅ Persistência de dados em JSON

✅ Interface gráfica desenvolvida com Tkinter

✅ Validação de dados de entrada

✅ Programação Orientada a Objetos (POO)

---

## 🏗️ Estrutura do Projeto

O projeto foi desenvolvido utilizando conceitos fundamentais de Programação Orientada a Objetos:

### Classes

### `Movie`

Representa um filme.

Atributos:

* Título
* Ano
* Diretor
* Duração

---

### `TVSeries`

Herda da classe `Movie`.

Atributos adicionais:

* Número de temporadas
* Número total de episódios

---

### `MediaCatalogue`

Responsável por:

* Armazenar mídias
* Adicionar itens
* Remover itens
* Salvar dados em JSON
* Carregar dados automaticamente

---

### `CatalogueApp`

Responsável pela interface gráfica utilizando Tkinter.

---

## 💾 Persistência de Dados

Os dados são armazenados automaticamente no arquivo:

```bash
catalogue.json
```

Ao abrir o programa novamente, todas as informações cadastradas são carregadas automaticamente.

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Tkinter
* JSON
* Programação Orientada a Objetos (POO)

---

## 📚 Conceitos Aplicados

Este projeto foi desenvolvido para praticar:

* Classes e Objetos
* Encapsulamento
* Herança
* Polimorfismo
* Tratamento de Exceções
* Manipulação de Arquivos JSON
* Interfaces Gráficas (GUI)
* Validação de Dados

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/media-catalogue-system.git
```

### 2. Entre na pasta

```bash
cd media-catalogue-system
```

### 3. Execute o programa

```bash
python main.py
```

---

## 📂 Estrutura de Arquivos

```bash
media-catalogue-system/
│
├── main.py
├── catalogue.json
├── README.md
└── assets/
    └── screenshot.png
```

---

## 🎯 Objetivo do Projeto

Este projeto foi criado com fins educacionais para praticar Programação Orientada a Objetos em Python e desenvolvimento de interfaces gráficas utilizando Tkinter.

Além disso, demonstra a aplicação de conceitos como herança, persistência de dados, tratamento de exceções e organização de código orientado a objetos. 

---

## 👨‍💻 Autor

Desenvolvido por **Ana Caroline Vasconcellos** durante os estudos de Python.

⭐ Se gostou do projeto, deixe uma estrela no repositório!
