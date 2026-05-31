import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import quad

from ipywidgets import (
    interact,
    IntSlider,
    FloatSlider,
    Dropdown
)
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# =====================================================
# FUNÇÕES DISPONÍVEIS
# =====================================================

funcoes = {
    "x²": lambda x: x**2,
    "sen(x)": lambda x: np.sin(x),
    "√x": lambda x: np.sqrt(x),
    "1/x": lambda x: 1/x,
    "e^(-x²)": lambda x: np.exp(-x**2),
    "x³ - 4x": lambda x: x**3 - 4*x
}

equacoes = {
    "x²": r"x^2",
    "sen(x)": r"\sin(x)",
    "√x": r"\sqrt{x}",
    "1/x": r"\frac{1}{x}",
    "e^(-x²)": r"e^{-x^2}",
    "x³ - 4x": r"x^3-4x"
}
# =====================================================
# FUNÇÃO PRINCIPAL
# =====================================================

def comparar_riemann(funcao_nome, n, a, b):

    f = funcoes[funcao_nome]

    # =====================================================
    # INTERVALO
    # =====================================================

    if b <= a:
        print("Escolha b > a")
        return
    dx = (b - a) / n

    # =====================================================
    # PREPARAÇÃO
    # =====================================================

    x = np.linspace(a, b, 1000)
    y = f(x)

    fig, axs = plt.subplots(
        1,
        3,
        figsize=(18, 5)
    )

    tipos = [
        "Esquerda",
        "Direita",
        "Ponto Médio"
    ]

    # =====================================================
    # INTEGRAL REAL
    # =====================================================


    integral_real, _ = quad(f, a, b)
    fig.suptitle(
        rf"$\int_{{{a}}}^{{{b}}} "
        rf"{equacoes[funcao_nome]}"
        rf"\,dx"
        rf" = {integral_real:.6f}$",
        fontsize=18,
        y=1.4
    )

    # =====================================================
    # LOOP DOS MÉTODOS
    # =====================================================

    for ax, tipo in zip(axs, tipos):

        # =================================================
        # PONTOS DA SOMA
        # =================================================

        if tipo == "Esquerda":

            x_rect = np.linspace(
                a,
                b - dx,
                n
            )

        elif tipo == "Direita":

            x_rect = np.linspace(
                a + dx,
                b,
                n
            )

        else:

            x_rect = np.linspace(
                a + dx/2,
                b - dx/2,
                n
            )

        y_rect = f(x_rect)

        # =================================================
        # SOMA
        # =================================================

        area = np.sum(y_rect * dx)

        erro_assinado = area - integral_real

        erro = abs(erro_assinado)

        if erro_assinado > 0:
            texto = "Superestima"
        else:
            texto = "Subestima"


        # =================================================
        # CURVA
        # =================================================

        ax.plot(
            x,
            y,
            linewidth=3
        )

        ax.fill_between(
           x,
           y,
            alpha=0.15
        )

        ax.axhline(
            0,
            color='black',
            linewidth=1
        )

        # =================================================
        # RETÂNGULOS
        # =================================================

        for xi, yi in zip(x_rect, y_rect):

            if tipo == "Esquerda":

                x0 = xi

            elif tipo == "Direita":

                x0 = xi - dx

            else:

                x0 = xi - dx/2

            ax.add_patch(

                plt.Rectangle(
                    (x0, 0),
                    dx,
                    yi,
                    alpha=0.4
                )

            )

        # =================================================
        # LAYOUT PRINCIPAL
        # =================================================

        ax.set_title(

            f"{tipo}\n"
            f"Riemann ≈ {area:.5f}\n"
            f"Erro = {erro:.5f}\n"
            f"{texto}",
            loc='left'
        )
        ax.set_xlim(a, b)

        ymin = min(np.min(y), 0)
        ymax = max(np.max(y), 0)

        margem = (ymax - ymin) * 0.1

        ax.set_ylim(
            ymin - margem,
            ymax + margem
        )

        # eixo x
        ax.set_xlabel(
            "x",
            fontsize=12
        )

        # eixo y apenas no primeiro
        if tipo == "Esquerda":

            ax.set_ylabel(
                "f(x)",
                fontsize=12
            )

        ax.grid(False)

        # =================================================
        # INSET - CONVERGÊNCIA DO ERRO
        # =================================================
        inset = inset_axes(
            ax,
            width="32%",
            height="32%",
            loc='upper left',
            bbox_to_anchor=(0.65, 0.4, 1, 1),
            bbox_transform=ax.transAxes,
            borderpad=0
        )

        ns = np.arange(1, 51)

        erros = []

        # ---------------------------------------------
        # cálculo dos erros
        # ---------------------------------------------

        for nn in ns:

            dxx = (b - a) / nn

            if tipo == "Esquerda":

                xr = np.linspace(
                    a,
                    b - dxx,
                    nn
                )

            elif tipo == "Direita":

                xr = np.linspace(
                    a + dxx,
                    b,
                    nn
                )

            else:

                xr = np.linspace(
                    a + dxx/2,
                    b - dxx/2,
                    nn
                )

            yr = f(xr)

            area_temp = np.sum(
                yr * dxx
            )

            erro_temp = abs(
                integral_real - area_temp
            )

            erros.append(
                erro_temp
            )

        # ---------------------------------------------
        # gráfico do erro
        # ---------------------------------------------

        inset.plot(
            ns,
            erros,
            linewidth=2
        )

        # ponto atual
        inset.scatter(
            n,
            erro,
            s=35,
            zorder=5
        )

        inset.set_title(
            "Erro",
            fontsize=8
        )

        inset.tick_params(
            axis='both',
            labelsize=6
        )

        inset.grid(
            True,
            alpha=0.3
        )

        ax.text(
          0.03,
          0.95,
          rf"$f(x)={equacoes[funcao_nome]}$",
          transform=ax.transAxes,
          fontsize=13,
          verticalalignment="top",
          bbox=dict(alpha=0.8)
        )

    # =====================================================
    # AJUSTE FINAL
    # =====================================================
    plt.subplots_adjust(wspace=0.35)

    plt.show()

    # =====================================================
    # RESULTADOS
    # =====================================================



# =====================================================
# INTERATIVIDADE
# =====================================================

interact(

    comparar_riemann,

    funcao_nome=Dropdown(
        options=list(funcoes.keys()),
        value="x²",
        description="Função:"
    ),

    n=IntSlider(
        min=1,
        max=100,
        step=1,
        value=5,
        description="Retângulos:"
    ),

    a=FloatSlider(
        min=-5,
        max=5,
        step=0.5,
        value=1,
        description="a:"
    ),

    b=FloatSlider(
        min=-5,
        max=10,
        step=0.5,
        value=5,
        description="b:"
    )

);
