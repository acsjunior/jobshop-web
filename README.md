# Job Shop Web

**Job Shop Web** is an application for didactic purposes that allows solving the job shop problem with makespan minimization using four models of mixed integer linear programming:

- [Disjunctive model (Manne)](#modelo-disjuntivo-manne);
- [Disjunctive model (Liao)](#modelo-disjuntivo-liao);
- [Time-indexed model](#modelo-indexado-no-tempo);
- [Rank-based model](#modelo-baseado-na-ordem).

The models are based on the works of [Manne (1960)](https://pubsonline.informs.org/doi/abs/10.1287/opre.8.2.219), [Liao e You (1992)](https://www.tandfonline.com/doi/abs/10.1057/jors.1992.162), [Kondili et al. (1988)](https://www.researchgate.net/profile/Roger-Sargent/publication/272294074_A_General_Algorithm_for_Scheduling_Batch_Operations/links/54e114140cf24d184b0fc476/A-General-Algorithm-for-Scheduling-Batch-Operations.pdf), and [Wagner (1959)](https://onlinelibrary.wiley.com/doi/abs/10.1002/nav.3800060205), respectively. Their computational implementation was facilitated thanks to the works of [Ku e Beck (2016)](https://www.sciencedirect.com/science/article/abs/pii/S0305054816300764) and [Aguiar Júnior (2021)](https://repositorio.ufc.br/bitstream/riufc/59600/3/2021_dis_jcajunior.pdf) and to Professor [Cassiano Tavares](https://scholar.google.com.br/citations?user=v55iBgUAAAAJ&hl=en&oi=ao)' classes.

This software is available at this address and can be used free of charge.

This software is available at [this address](https://jobshop-web.herokuapp.com) and can be used free of charge. To cite: SILVA JÚNIOR, A. C. Job Shop Web (v.1.0). 2022.

The source code is available on [GitHub](https://github.com/juniorssz/jobshop-web), and you can contribute improvements and redistribute or modify it under the terms of GPL v3.0 or any later version.

To contact the author of this software, go to [acsjunior.com](https://acsjunior.com).

<hr>

## Deployment guidelines on Heroku

1 - Include the file **setup.sh** at the root of the project.

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

2 - Include the file **Procfile** at the root of the project.

```
web: sh setup.sh && streamlit run jobshop_web/app.py
```

3 - Include the file **Aptfile** at the root of the project.

```
libglpk-dev 
glpk-utils
locales-all
```

4 - In the project directory, run the command `heroku create <nome da aplicação>` via Heroku CLI.

5 - Add via CLI the following buildpacks:

-  `heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git`
-  `heroku buildpacks:add heroku/python`
-  `heroku buildpacks:add --index 1 heroku-community/apt`

    References: 
    - https://elements.heroku.com/buildpacks/moneymeets/python-poetry-buildpack
    - https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-apt

6 - Run the command `git push heroku main`.

<hr>

## Deployment guidelines on Streamlit

1 - Include the file **packages.txt** at the root of the project.

```
libglpk-dev 
glpk-utils
locales-all
```

2 - Access [https://share.streamlit.io](https://share.streamlit.io) and follow platform guidelines.