# Job Shop

## Orientações para deploy no Heroku

1 - Criar os arquivos [setup.sh](https://github.com/juniorssz/jobshop/blob/main/setup.sh), [Procfile](https://github.com/juniorssz/jobshop/blob/main/Procfile) e [Aptfile](https://github.com/juniorssz/jobshop/blob/main/Aptfile)

2 - No diretório do projeto, executar via Heroku CLI: `heroku create <nome da aplicação>`

3 - Adicionar via CLI os seguintes buildpacks:

-  `heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git`
-  `heroku buildpacks:add heroku/python`
-  `heroku buildpacks:add --index 1 heroku-community/apt`

    Referências: 
    - https://elements.heroku.com/buildpacks/moneymeets/python-poetry-buildpack
    - https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-apt

4 - Executar `git push heroku main`

<hr>

## Orientações para deploy no Streamlit

1 - Criar o arquivo [packages.txt](https://github.com/juniorssz/jobshop-sp/blob/streamlit/packages.txt)

2 - Acessar https://share.streamlit.io e seguir as orientações da plataforma