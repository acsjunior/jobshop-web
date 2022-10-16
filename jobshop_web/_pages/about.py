import streamlit as st

from jobshop_web._pages.utils import get_title
from jobshop_web.config.paths import PATH_FORMULATIONS
from jobshop_web.config.params import PAGES


def about_page(session):
    st.header(get_title(session))

    about = """
    **Job Shop Web** é uma aplicação para fins didáticos que permite a resolução do problema do job shop com minimização do makespan por meio de quatro modelos de programação linear inteira mista:

    - [Modelo disjuntivo (Manne)](#modelo-disjuntivo-manne);
    - [Modelo disjuntivo (Liao)](#modelo-disjuntivo-liao);
    - [Modelo indexado no tempo](#modelo-indexado-no-tempo);
    - [Modelo baseado na ordem](#modelo-baseado-na-ordem).

    Os modelos utilizados são baseados nos trabalhos de [Manne (1960)](https://pubsonline.informs.org/doi/abs/10.1287/opre.8.2.219), [Liao e You (1992)](https://www.tandfonline.com/doi/abs/10.1057/jors.1992.162), [Kondili et al. (1988)](https://www.researchgate.net/profile/Roger-Sargent/publication/272294074_A_General_Algorithm_for_Scheduling_Batch_Operations/links/54e114140cf24d184b0fc476/A-General-Algorithm-for-Scheduling-Batch-Operations.pdf) e [Wagner (1959)](https://onlinelibrary.wiley.com/doi/abs/10.1002/nav.3800060205), respectivamente, e tiveram a implementação computacional facilitada graças aos trabalhos de [Ku e Beck (2016)](https://www.sciencedirect.com/science/article/abs/pii/S0305054816300764) e [Aguiar Júnior (2021)](https://repositorio.ufc.br/bitstream/riufc/59600/3/2021_dis_jcajunior.pdf).

    Este software pode ser utilizado gratuitamente. Para citá-lo: SILVA JÚNIOR, A. C. Job Shop Web (v.1.0). 2022.

    O código fonte está disponível no [GitHub](https://github.com/juniorssz/jobshop-web) sob a licença MPL 2.0 e você pode não só contribuir com melhorias, mas também modificar e redistribuir. Lembrando que versões modificadas deste software devem ser distribuídas sob a mesma licença.

    Para contatar o autor deste software, acesse [acsjunior.com](https://acsjunior.com).
    """

    st.markdown(about)

    for prefix in PAGES:
        if prefix != "about":
            with open(PATH_FORMULATIONS / f"{prefix}.md") as f:
                st.markdown("---")
                st.subheader(PAGES[prefix])
                st.markdown(f.read())
                st.text("")
                st.markdown("[Voltar ao topo](#sobre)")
