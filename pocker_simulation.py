import collections
from random import shuffle

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        shuffle(self._cards)


def evaluate_hand(hand: tuple) -> str:
    rank_order = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    ranks = [rank_order[card.rank] for card in hand]
    suits = [card.suit for card in hand]
    rank_count = collections.Counter(ranks)

    is_flush = len(set(suits)) == 1
    is_royal = sorted(ranks) == [10, 11, 12, 13, 14]
    is_straight = (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5
    is_kare = 4 in rank_count.values()
    is_pare = 2 in rank_count.values()
    is_three = 3 in rank_count.values()

    # Роял-флеш
    if is_flush and is_royal:
        return "Роял-флеш"
    # Стрит-флеш
    if is_straight and is_flush:
        return "Стрит-флеш"
    # Каре
    if is_kare:
        return "Каре"
    # Фулл-хаус
    if is_pare and is_three:
        return "Фулл-хаус"
    # Флеш
    if is_flush:
        return "Флеш"
    # Стрит
    if is_straight:
        return "Стрит"
    # Тройка
    if is_three:
        return "Тройка"
    # Две пары
    if list(rank_count.values()).count(2) == 2:
        return "Две пары"
    # Пара
    if is_pare:
        return "Пара"
    # Старшая карта
    return "Старшая карта"


def simulate_poker(num_simulations: int) -> dict:
    stats = collections.defaultdict(int)
    deck = FrenchDeck()
    for i in range(num_simulations):
        deck.shuffle()
        hand = (deck[0], deck[1], deck[2], deck[3], deck[4])
        stats[evaluate_hand(hand)] += 1
    return stats


def full_simulate_poker(num_simulations: int, num_player) -> dict:
    pass


if __name__ == "__main__":
    print("1. Симуляция покерных раздач в одну руку")
    print("2. Симуляция покерных раздач в несколько рук и картами на столе")
    answer = input()
    if answer == "1":
        print("Количество симуляций? ")
        sim_count = int(input())
        print(simulate_poker(num_simulations=sim_count))
    elif answer == "2":
        print("Количество симуляций? ")
        sim_count = int(input())
        print("Количество игроков? До 9 ")
        player_count = int(input())
        full_simulate_poker(num_simulations=sim_count, player_count=player_count)
    else:
        print("Ошибка")
