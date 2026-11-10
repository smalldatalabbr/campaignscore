"""
Funções para Modelagem de Propensão.

Objetivo:
- avaliar modelos no conjunto de validação
- selecionar um threshold por lucro (proxy) apenas para comparação de modelos
- manter PR-AUC como métrica secundária (sanity)

"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import average_precision_score, precision_recall_curve, confusion_matrix


def plot_pr_curve(y_true, proba, title=None, savepath=None):
    """
    Curva Precision–Recall (uso opcional).
    Retorna PR-AUC (Average Precision).
    """
    precisions, recalls, _ = precision_recall_curve(y_true, proba)
    pr_auc = average_precision_score(y_true, proba)

    plt.figure(figsize=(6, 4))
    plt.plot(recalls, precisions, label=f"PR-AUC = {pr_auc:.3f}")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title(title or "Precision–Recall Curve")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if savepath:
        plt.savefig(savepath, bbox_inches="tight")
  
    plt.show()

    return float(pr_auc)


def plot_confusion_matrix(
    cm,
    title=None,
    cmap="Blues",
    labels=("Não responde", "Responde"),
    savepath=None,
):
    """
    Plota matriz de confusão 2x2 de forma limpa e executiva.

    Parâmetros:
    - cm: array-like (2x2), matriz de confusão
    - title: título do gráfico
    - cmap: colormap do matplotlib
    - labels: rótulos das classes (negativa, positiva)

    Uso típico:
    - sanity check no threshold escolhido por lucro
    - visual único (baseline ou campeão)
    """
    cm = np.asarray(cm)

    fig, ax = plt.subplots(figsize=(6, 4))
    im = ax.imshow(cm, cmap=cmap)
    ax.set_title(title or "Matriz de Confusão")

    # Barra de cor discreta
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

    # Anotações numéricas
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(
                j,
                i,
                int(cm[i, j]),
                ha="center",
                va="center",
                fontsize=11,
                fontweight="bold",
            )

    ax.set_xlabel("Previsto")
    ax.set_ylabel("Real")

    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)

    # Limpeza visual
    ax.grid(False)
    ax.set_axisbelow(False)

    if savepath:
        plt.savefig(savepath, bbox_inches="tight")


    plt.tight_layout()
    plt.show()


def evaluate_on_valid_profit(model_name, y_valid, proba_valid, gain, cost, thresholds=None):
    """
    Avalia um modelo no VALID com critério orientado a lucro (proxy).

    Regras:
    - Seleção: proba >= threshold
    - Lucro total no VALID: (TP * gain) - (selecionados * cost)
    - Threshold escolhido: maximiza lucro total (empate -> threshold maior)

    Retorna um dicionário com:
    - PR-AUC (secundário)
    - melhor threshold por lucro (proxy)
    - lucro esperado no threshold escolhido
    - taxa de seleção e matriz de confusão (no threshold escolhido)
    """
    y_true = np.asarray(y_valid).astype(int)
    proba = np.asarray(proba_valid).astype(float)

    pr_auc = average_precision_score(y_true, proba)

    if thresholds is None:
        thresholds = np.linspace(0.01, 0.99, 99)

    best = {
        "profit_total": -np.inf,
        "threshold": None,
        "selected": None,
        "selected_rate": None,
        "cm": None,
    }

    n = len(y_true)
    positives = int(y_true.sum())

    for t in thresholds:
        sel = proba >= t
        n_sel = int(sel.sum())

        if n_sel == 0:
            profit_total = 0.0
            cm = np.array([[n - positives, 0], [positives, 0]])
        else:
            y_sel = y_true[sel]
            tp = int(y_sel.sum())
            profit_total = tp * gain - n_sel * cost

            y_pred = sel.astype(int)
            cm = confusion_matrix(y_true, y_pred)

        # maximiza lucro; empate -> threshold maior (seleciona menos)
        if (profit_total > best["profit_total"]) or (
            profit_total == best["profit_total"] and best["threshold"] is not None and t > best["threshold"]
        ):
            best.update({
                "profit_total": float(profit_total),
                "threshold": float(t),
                "selected": int(n_sel),
                "selected_rate": float(n_sel / n),
                "cm": cm,
            })

    return {
        "model": model_name,
        "gain": float(gain),
        "cost": float(cost),
        "pr_auc_valid": float(pr_auc),
        "best_threshold_valid": float(best["threshold"]),
        "expected_profit_valid": float(best["profit_total"]),
        "selected_valid": int(best["selected"]),
        "selected_rate_valid": float(best["selected_rate"]),
        "confusion_matrix_valid": best["cm"],
    }