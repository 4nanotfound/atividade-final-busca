from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50

class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:

        pilha = [(initial, 0)]

        visitados = {initial}

        gerados = 1
        explorados = 0
        fronteira_maxima = len(pilha)

        while pilha:

            atual, profundidade = pilha.pop()
            explorados += 1

            if atual.is_goal:
                return SearchResult(
                    solution=atual,
                    nodes_expanded=explorados,
                    nodes_generated=gerados,
                    max_frontier_size=fronteira_maxima,
                    depth=atual.cost
                )

            if profundidade >= self.depth_limit:
                continue

            for filho in atual.neighbors():
                gerados += 1

                if filho not in visitados:
                    visitados.add(filho)

                    pilha.append((filho, profundidade + 1))
                    fronteira_maxima = max(fronteira_maxima, len(pilha))

        return SearchResult(
            solution=None,
            nodes_expanded=explorados,
            nodes_generated=gerados,
            max_frontier_size=fronteira_maxima
        )
