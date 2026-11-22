from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:

        fila = deque([initial])

        visitados = {initial}

        gerados = 1
        explorados = 0
        fronteira_maxima = len(fila)

        while fila:

            atual = fila.popleft()
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

                if filho not in visitados:
                    visitados.add(filho)
                    fila.append(filho)
                    fronteira_maxima = max(fronteira_maxima, len(fila))

        return SearchResult(
            solution=None,
            nodes_expanded=explorados,
            nodes_generated=gerados,
            max_frontier_size=fronteira_maxima
        )
