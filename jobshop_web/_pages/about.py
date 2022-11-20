"""
Job Shop Web: a didactic software to solve the job shop scheduling problem with makespan minimization.
Copyright (C) 2022  António C. da Silva Júnior <juniorssz@gmail.com>

This file is part of Job Shop Web.

Job Shop Web is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Job Shop Web is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Job Shop Web.  If not, see <https://www.gnu.org/licenses/>.
"""
import streamlit as st

from jobshop_web._pages.utils import get_title
from jobshop_web.config.params import PAGES
from jobshop_web.config.paths import PATH_FORMULATIONS


def about_page(session):
    st.header(get_title(session))

    about = """
    **Job Shop Web** is an application for didactic purposes that allows solving the job shop problem with makespan minimization using four models of mixed integer linear programming:

    - [Disjunctive model (Manne)](#modelo-disjuntivo-manne);
    - [Disjunctive model (Liao)](#modelo-disjuntivo-liao);
    - [Time-indexed model](#modelo-indexado-no-tempo);
    - [Rank-based model](#modelo-baseado-na-ordem).

    The models are based on the works of [Manne (1960)](https://pubsonline.informs.org/doi/abs/10.1287/opre.8.2.219), [Liao e You (1992)](https://www.tandfonline.com/doi/abs/10.1057/jors.1992.162), [Kondili et al. (1988)](https://www.researchgate.net/profile/Roger-Sargent/publication/272294074_A_General_Algorithm_for_Scheduling_Batch_Operations/links/54e114140cf24d184b0fc476/A-General-Algorithm-for-Scheduling-Batch-Operations.pdf), and [Wagner (1959)](https://onlinelibrary.wiley.com/doi/abs/10.1002/nav.3800060205), respectively. Their computational implementation was facilitated thanks to the works of [Ku e Beck (2016)](https://www.sciencedirect.com/science/article/abs/pii/S0305054816300764) and [Aguiar Júnior (2021)](https://repositorio.ufc.br/bitstream/riufc/59600/3/2021_dis_jcajunior.pdf) and to Professor [Cassiano Tavares](https://scholar.google.com.br/citations?user=v55iBgUAAAAJ&hl=en&oi=ao)' classes.

    This software can be used free of charge. To cite: SILVA JÚNIOR, A. C. Job Shop Web (v.1.0). 2022.

    The source code is available on [GitHub](https://github.com/juniorssz/jobshop-web), and you can contribute improvements and redistribute or modify it under the terms of GPL v3.0 or any later version.

    To contact the author of this software, go to [acsjunior.com](https://acsjunior.com).
    """

    st.markdown(about)

    for prefix in PAGES:
        if prefix != "about":
            with open(PATH_FORMULATIONS / f"{prefix}.md") as f:
                st.markdown("---")
                st.subheader(PAGES[prefix])
                st.markdown(f.read())
                st.text("")
                st.markdown("[Back to top](#sobre)")
