# Job Shop Web

**Job Shop Web** é uma aplicação para fins didáticos que permite a resolução do problema do job shop com minimização do makespan por meio de quatro modelos de programação linear inteira mista:

- Modelo disjuntivo (Manne);
- Modelo disjuntivo (Liao);
- Modelo indexado no tempo;
- Modelo baseado na ordem.

Os modelos utilizados são baseados nos trabalhos de [Manne (1960)](https://pubsonline.informs.org/doi/abs/10.1287/opre.8.2.219), [Liao e You (1992)](https://www.tandfonline.com/doi/abs/10.1057/jors.1992.162), [Kondili et al. (1988)](https://www.researchgate.net/profile/Roger-Sargent/publication/272294074_A_General_Algorithm_for_Scheduling_Batch_Operations/links/54e114140cf24d184b0fc476/A-General-Algorithm-for-Scheduling-Batch-Operations.pdf) e [Wagner (1959)](https://onlinelibrary.wiley.com/doi/abs/10.1002/nav.3800060205), respectivamente, e tiveram a implementação computacional facilitada graças aos trabalhos de [Ku e Beck (2016)](https://www.sciencedirect.com/science/article/abs/pii/S0305054816300764) e [Aguiar Júnior (2021)](https://repositorio.ufc.br/bitstream/riufc/59600/3/2021_dis_jcajunior.pdf).

Este software está disponível [neste endereço](https://jobshop-web.herokuapp.com) e pode ser utilizado gratuitamente. Para citá-lo: SILVA JÚNIOR, A. C. Job Shop Web (v.1.0). 2022.

O código fonte está totalmente disponível e você pode não só contribuir com melhorias, mas também redistribuí-lo e/ou modificá-lo, sob os termos da GPL v3.0 ou qualquer versão posterior.

Para contatar o autor deste software, acesse [acsjunior.com](https://acsjunior.com).

<hr>

## Orientações para deploy no Heroku

1 - Incluir na raíz do projeto o arquivo **setup.sh**:

```
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"seu-email@dominio.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

2 - Incluir na raíz do projeto o arquivo **Procfile**:

```
web: sh setup.sh && streamlit run jobshop_web/app.py
```

3 - Incluir na raíz do projeto o arquivo **Aptfile**:

```
libglpk-dev 
glpk-utils
locales-all
```

4 - No diretório do projeto, executar via Heroku CLI: `heroku create <nome da aplicação>`

5 - Adicionar via CLI os seguintes buildpacks:

-  `heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git`
-  `heroku buildpacks:add heroku/python`
-  `heroku buildpacks:add --index 1 heroku-community/apt`

    Referências: 
    - https://elements.heroku.com/buildpacks/moneymeets/python-poetry-buildpack
    - https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-apt

6 - Executar `git push heroku main`

<hr>

## Orientações para deploy no Streamlit

1 Incluir na raíz do projeto o arquivo **packages.txt**:

```
libglpk-dev 
glpk-utils
locales-all
```

2 - Acessar https://share.streamlit.io e seguir as orientações da plataforma