import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import GOAL_STATE, State
from puzzle.result import SearchResult

class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:

        distancia = 0

        for posicao, valor in enumerate(state.tiles):

            if valor == 0:
                continue

            linha_atual = posicao // 3
            coluna_atual = posicao % 3
            posicao_objetivo = GOAL_STATE.index(valor)
            linha_objetivo = posicao_objetivo // 3
            coluna_objetivo = posicao_objetivo % 3

            distancia += (
                abs(linha_atual - linha_objetivo)
                + abs(coluna_atual - coluna_objetivo)
            )

        return distancia


    def search(self, initial: State) -> SearchResult:

        fila = []
        contador = 0

        heapq.heappush(
            fila,
            (self.heuristic(initial), contador, initial)
        )

        custos = {initial: 0}

        gerados = 1
        explorados = 0
        fronteira_maxima = len(fila)

        while fila:

            _, _, atual = heapq.heappop(fila)

            if atual.cost != custos.get(atual):
                continue

            explorados += 1

            if atual.is_goal:
                return SearchResult(
                    solution=atual,
                    nodes_expanded=explorados,
                    nodes_generated=gerados,
                    max_frontier_size=fronteira_maxima,
                    depth=atual.cost
                )

            for filho in atual.neighbors():
                gerados += 1

                novo_custo = atual.cost + 1

                if novo_custo < custos.get(filho, float("inf")):

                    filho.cost = novo_custo
                    custos[filho] = novo_custo

                    contador += 1

                    prioridade = (
                        novo_custo + self.heuristic(filho)
                    )

                    heapq.heappush(
                        fila,
                        (prioridade, contador, filho)
                    )
                    fronteira_maxima = max(fronteira_maxima, len(fila))

        return SearchResult(
            solution=None,
            nodes_expanded=explorados,
            nodes_generated=gerados,
            max_frontier_size=fronteira_maxima
        )
